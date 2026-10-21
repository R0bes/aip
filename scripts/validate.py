#!/usr/bin/env python3
"""Validate AIP example shape and semantic invariants.

Requires: pip install jsonschema
"""
import json
from pathlib import Path

from jsonschema import Draft202012Validator, ValidationError

ROOT = Path(__file__).resolve().parents[1]


def validate_semantics(data: dict) -> None:
    actions = data["actions"]
    ids = [a["id"] for a in actions]
    keys = [a["key"] for a in actions]
    assert len(ids) == len(set(ids)), "duplicate action id"
    assert len(keys) == len(set(keys)), "duplicate action key"
    assert sum(a.get("recommended", False) for a in actions) <= 1, "multiple recommendations"
    for action in actions:
        assert (action["key"] == "0") == (action["id"] == "continue"), "key 0 reserved for continue"
        params = action.get("parameters", [])
        names = [p["id"] for p in params]
        assert len(names) == len(set(names)), "duplicate parameter id"
        for p in params:
            if p["type"] == "integer":
                assert p["min"] <= p["default"] <= p["max"], "integer default out of bounds"
            if p["type"] == "enum":
                assert p["default"] in p["choices"], "enum default not among choices"
                assert len(p["choices"]) == len(set(p["choices"])), "duplicate enum choice"


def main() -> None:
    schema = json.loads((ROOT / "run-ui.schema.json").read_text())
    example = json.loads((ROOT / "examples/development-run.json").read_text())
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema).validate(example)
    validate_semantics(example)
    empty = json.loads(json.dumps(example))
    empty["actions"] = []
    Draft202012Validator(schema).validate(empty)
    validate_semantics(empty)
    print("PASS: zero-action selector")

    report_schema = json.loads((ROOT / "report.schema.json").read_text())
    report_example = json.loads((ROOT / "examples/report.json").read_text())
    Draft202012Validator.check_schema(report_schema)
    from referencing import Registry, Resource
    registry = Registry().with_resource(schema["$id"], Resource.from_contents(schema))
    report_validator = Draft202012Validator(report_schema, registry=registry)
    report_validator.validate(report_example)
    validate_semantics(report_example["next_run"])
    print("PASS: report schema and example")

    def reject_report(name, change):
        candidate = json.loads(json.dumps(report_example))
        change(candidate)
        try:
            report_validator.validate(candidate)
            if "next_run" in candidate:
                validate_semantics(candidate["next_run"])
        except (AssertionError, ValueError, ValidationError):
            print("PASS:", name)
        else:
            raise AssertionError("accepted invalid report: " + name)

    reject_report("unknown report block", lambda x: x["blocks"].append({"type":"mystery"}))
    reject_report("empty command", lambda x: x["blocks"][2].update(content=""))
    reject_report("missing GitHub operation", lambda x: x["blocks"][1].pop("operation"))
    reject_report("invalid action in report", lambda x: x["next_run"]["actions"][0].update(key="1"))

    def must_reject(name, change):
        candidate = json.loads(json.dumps(example))
        change(candidate)
        try:
            Draft202012Validator(schema).validate(candidate)
            validate_semantics(candidate)
        except (AssertionError, ValueError, ValidationError):
            print("PASS:", name)
        else:
            raise AssertionError("accepted invalid example: " + name)

    must_reject("duplicate key", lambda x: x["actions"][1].update(key="0"))
    must_reject("duplicate action id", lambda x: x["actions"][1].update(id="continue"))
    must_reject("multiple recommendations", lambda x: [a.update(recommended=True) for a in x["actions"]])
    must_reject("invalid integer default", lambda x: x["actions"][1]["parameters"][0].update(default=99))
    must_reject("invalid enum default", lambda x: x["actions"][1]["parameters"].append({"id":"mode","type":"enum","choices":["a"],"default":"b"}))
    must_reject("duplicate parameter", lambda x: x["actions"][1]["parameters"].append(dict(x["actions"][1]["parameters"][0])))
    must_reject("key zero used by non-continue", lambda x: x["actions"][0].update(id="other"))
    must_reject("continue with nonzero key", lambda x: x["actions"][0].update(key="2"))
    must_reject("inverted integer bounds", lambda x: x["actions"][1]["parameters"][0].update(min=6, max=1))
    must_reject("duplicate enum choices", lambda x: x["actions"][1]["parameters"].append({"id":"mode","type":"enum","choices":["a","a"],"default":"a"}))
    must_reject("missing action instruction", lambda x: x["actions"][0].pop("instruction"))
    print("PASS: schema, example, semantic checks")


if __name__ == "__main__":
    main()
