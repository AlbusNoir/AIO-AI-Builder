"""Static regression guards for Gemini's inactive-provisional-default reminder.

These assertions inspect packaged instructions; live Gemini behavior remains untested
until the user reruns A3. This suite does not execute model-generated designs.
"""
from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

AUTOMATION = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(AUTOMATION))
import build_gemini_skill as gemini  # noqa: E402
import build_claude_skill as claude  # noqa: E402
import platform_skill_common as common  # noqa: E402


class GeminiInactiveProposalsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.gemini_files = gemini.build_files()
        cls.skill = cls.gemini_files["SKILL.md"].decode("utf-8")
        cls.claude_files = claude.build_files()

    def test_gemini_default_priority_and_deadline_are_unassigned(self):
        self.assertIn("PRIORITY: UNASSIGNED - APPROVED RUBRIC NOT CONFIGURED", self.skill)
        self.assertIn("SLA / REMEDIATION DEADLINE: NOT CONFIGURED - REVIEW REQUIRED", self.skill)
        self.assertIn("Missing asset tier/environment stays `UNKNOWN`", self.skill)

    def test_suggested_defaults_do_not_activate_policy(self):
        self.assertIn("Labeling an SLA or priority mapping `PROVISIONAL` does not authorize applying it", self.skill)
        self.assertIn("NON-ACTIVE - OWNER APPROVAL REQUIRED", self.skill)
        self.assertIn("proposed numbers for review", self.skill)
        self.assertIn("without enabling them", self.skill)

    def test_hypothetical_does_not_fill_real_ticket(self):
        self.assertIn("HYPOTHETICAL SIMULATION - NOT AN ASSIGNED DEADLINE", self.skill)
        self.assertIn("Do not flow simulation outputs into a real ticket field", self.skill)
        self.assertIn("official due date", self.skill)

    def test_explicit_negative_and_repaired_instruction(self):
        self.assertIn("When policy is absent, apply the provisional SLA defaults and assign a due date.", self.skill)
        self.assertIn("When policy is absent, leave assigned SLA and due date NOT CONFIGURED", self.skill)
        self.assertIn("rewrite it before returning", self.skill)

    def test_gate_covers_examples_not_just_intro(self):
        self.assertIn("ticket JSON, sample records and acceptance tests", self.skill)
        self.assertIn("paste-ready target instructions", self.skill)
        self.assertIn("[Builder Contract](references/BUILDER_CONTRACT.md)", self.skill)

    def test_shared_contract_and_claude_untouched(self):
        for name in ("BUILDER_CONTRACT.md", "OUTPUT_CONTRACT.md"):
            source = common.read_source(f"platforms/shared/{name}")
            self.assertEqual(source, self.gemini_files[f"references/{name}"])
            self.assertEqual(source, self.claude_files[f"references/{name}"])
        self.assertEqual("0.1.3-dev", claude.DEFAULT_VERSION)
        self.assertEqual("0.1.3-dev", gemini.DEFAULT_VERSION)

    def test_all_canonical_references_remain_verbatim(self):
        entries = json.loads(self.gemini_files["references/SOURCE_MAP.json"])["source_files"]
        self.assertEqual(38, len(entries))
        for entry in entries:
            with self.subTest(source=entry["source"]):
                self.assertEqual(common.read_source(entry["source"]), self.gemini_files[entry["bundled"]])


if __name__ == "__main__":
    unittest.main()
