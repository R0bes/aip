"""Contract tests for the standalone AIP HTML renderer."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from render_report import render


class ReportRendererTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / "examples/report.json").read_text())

    def test_example_renders(self):
        html = render(self.report)
        self.assertIn("AIP 0.3.0", html)
        self.assertIn("Report specification updated", html)
        self.assertIn("Verify report schema", html)
        self.assertIn('placeholder="⧉"', html)
        self.assertIn('class="card action"', html)
        self.assertIn("aip:invoke", html)

    def test_next_run_prompt_contract(self):
        output = render(self.report)
        self.assertIn("payload.prompt=promptParts.filter(Boolean).join", output)
        self.assertIn("Task: ${action.instruction}", output)
        self.assertIn("Action: ${action.id} (key ${action.key})", output)
        self.assertIn("Supplemental text (verbatim):", output)
        self.assertIn("${supplemental_text}", output)
        self.assertIn("[aip: ${report.protocol_version}; repo: ${repoName}; profile: ${profile}]", output)
        self.assertIn("If AIP instructions are missing, uncertain, or inconsistent", output)
        self.assertNotIn("fetch(", output)
        self.assertNotIn("window.location.reload", output)

    def test_compact_borderless_supplemental_and_neon_cards(self):
        output = render(self.report)
        self.assertIn(".header,.card{border:2px solid", output)
        self.assertIn("background:transparent", output)
        self.assertIn(".action{border-color:#3c6670}", output)
        self.assertIn("textarea{box-sizing:border-box;width:100%;background:transparent", output)
        self.assertIn("border:0;outline:0;box-shadow:none", output)
        self.assertIn("e.target.closest('textarea,button')", output)

    def test_escapes_user_supplied_html(self):
        report = json.loads(json.dumps(self.report))
        report["blocks"][0]["text"] = '<script>alert("bad")</script>'
        html = render(report)
        self.assertIn("&lt;script&gt;", html)
        self.assertNotIn('<script>alert("bad")</script>', html)

    def test_optional_selector(self):
        report = json.loads(json.dumps(self.report))
        report.pop("next_run")
        self.assertNotIn('class="card action"', render(report))

    def test_invalid_report_rejected(self):
        report = json.loads(json.dumps(self.report))
        report["blocks"][0]["type"] = "unknown"
        with self.assertRaises(Exception):
            render(report)


if __name__ == "__main__":
    unittest.main()
