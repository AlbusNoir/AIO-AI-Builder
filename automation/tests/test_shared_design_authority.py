"""Static design-authority checks in both distributable Builder skills.

These checks assert packaged wording and cross-adapter consistency; they are
not model behavioral executions or proof of live host authorization.
"""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

AUTOMATION = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(AUTOMATION))
import build_claude_skill as claude  # noqa: E402
import build_gemini_skill as gemini  # noqa: E402
import platform_skill_common as common  # noqa: E402


class SharedDesignAuthorityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.claude_files = claude.build_files()
        cls.gemini_files = gemini.build_files()
        cls.contract = cls.claude_files["references/BUILDER_CONTRACT.md"].decode()
        cls.output = cls.claude_files["references/OUTPUT_CONTRACT.md"].decode()

    def test_both_host_bundles_include_byte_identical_shared_contracts(self):
        for file in ("BUILDER_CONTRACT.md", "OUTPUT_CONTRACT.md"):
            with self.subTest(contract=file):
                source = common.read_source(f"platforms/shared/{file}")
                self.assertEqual(source, self.claude_files[f"references/{file}"])
                self.assertEqual(source, self.gemini_files[f"references/{file}"])

    def test_requirement_provenance_covers_all_four_statuses(self):
        for phrase in ("User-specified requirement", "Verified source requirement",
                       "Proposed design default", "Unresolved organizational decision"):
            with self.subTest(status=phrase):
                self.assertIn(phrase, self.contract)
        self.assertIn("both analysis **and the paste-ready target instructions**", self.contract)

    def test_no_invented_organization_slas_or_workflows(self):
        for phrase in ("severity bands", "remediation SLAs", "change types",
                       "24-hour bake windows", "approval hierarchies",
                       "regulatory reporting triggers"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.contract)
        self.assertIn("do not assert an invented precedence", self.contract)

    def test_auto_mode_does_not_invent_authority(self):
        self.assertIn("Auto request permits a provisional design", self.contract)
        self.assertIn("not** invented organizational policy or execution authorization", self.contract)

    def test_connected_tool_vs_action_authorization_separated(self):
        for phrase in ("Capability is not authorization", "confirmed available/connected tool",
                       "organizational authorization for a particular action and scope",
                       "verified outcome", "non-production environment alone"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.contract)

    def test_approval_cannot_be_inferred_from_boolean_or_chat(self):
        self.assertIn("`deployment_approved: true`", self.contract)
        self.assertIn("a message in Slack is not independently sufficient proof", self.contract)
        self.assertIn("trusted verification mechanism", self.contract)

    def test_missing_authorization_is_draft_only(self):
        for phrase in ("proposal / draft-only mode", "not describe them as validated",
                       "Do not substitute ready-to-run destructive commands"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.contract)

    def test_output_contract_requires_requirement_and_authority_trace(self):
        for phrase in ("Requirement and authority trace", "user-requested", "verified from reviewed source",
                       "proposed provisional default", "confirmation required", "authorization boundary",
                       "illustrative templates"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.output)

    def test_claude_skill_surface_prompts_new_guardrails(self):
        skill = self.claude_files["SKILL.md"].decode()
        self.assertIn("provisional defaults", skill)
        self.assertIn("Tool connection is not action authorization", skill)
        self.assertIn("draft-only", skill)

    def test_gemini_skill_surface_prompts_new_guardrails(self):
        skill = self.gemini_files["SKILL.md"].decode()
        self.assertIn("organizational decisions pending confirmation", skill)
        self.assertIn("non-production target does not establish organizational authorization", skill)
        self.assertIn("draft-only / human-reviewed", skill)

    def test_adapter_versions_and_canonical_inventory_unchanged(self):
        self.assertEqual("0.1.3-dev", claude.DEFAULT_VERSION)
        self.assertEqual("0.1.3-dev", gemini.DEFAULT_VERSION)
        for files in (self.claude_files, self.gemini_files):
            source_map = json.loads(files["references/SOURCE_MAP.json"])
            self.assertEqual(38, len(source_map["source_files"]))
            for entry in source_map["source_files"]:
                self.assertEqual(common.read_source(entry["source"]), files[entry["bundled"]])


if __name__ == "__main__":
    unittest.main()
