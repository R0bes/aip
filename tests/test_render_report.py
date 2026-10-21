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
