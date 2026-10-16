"""Static guardrail tests for the cross-platform generated-artifact consistency rule.

These verify packaging and explicit review criteria, not live model behavior or
an exhaustive validation of arbitrary generated code or operational workflows.
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

AUTOMATION = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(AUTOMATION))
import build_claude_skill as claude  # noqa: E402
import build_gemini_skill as gemini  # noqa: E402
import platform_skill_common as common  # noqa: E402


class GeneratedArtifactConsistencyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.c = claude.build_files()
        cls.g = gemini.build_files()
        cls.contract = cls.c['references/BUILDER_CONTRACT.md'].decode()
        cls.output = cls.c['references/OUTPUT_CONTRACT.md'].decode()
        cls.gemini_skill = cls.g['SKILL.md'].decode()

    def test_bundles_share_exact_canonical_builder_contract(self):
        source = common.read_source('platforms/shared/BUILDER_CONTRACT.md')
        self.assertEqual(source, self.c['references/BUILDER_CONTRACT.md'])
        self.assertEqual(source, self.g['references/BUILDER_CONTRACT.md'])

    def test_bundles_share_exact_output_contract(self):
        source = common.read_source('platforms/shared/OUTPUT_CONTRACT.md')
        self.assertEqual(source, self.c['references/OUTPUT_CONTRACT.md'])
        self.assertEqual(source, self.g['references/OUTPUT_CONTRACT.md'])

    def test_quality_gate_explicitly_checks_complete_artifact(self):
        for phrase in ('Generated-artifact consistency gate', 'paste-ready instructions',
                       'API/JSON examples', 'scripts, commands, playbooks',
                       'Reconcile before output'):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.contract)
        self.assertIn('after drafting', self.gemini_skill)

    def test_unknown_asset_tier_stays_unknown(self):
        for phrase in ('Tier 2 - Internal Production', 'UNKNOWN',
                       'must not populate a real target record',
                       'Required unknown inputs leave derived priorities'):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.contract + '\n' + self.output)

    def test_proposed_slas_remain_inactive_without_approval(self):
        for phrase in ('illustrative / configurable / not-active',
                       'UNASSIGNED', 'REVIEW REQUIRED',
                       'clearly labeled hypothetical result',
                       'replaces inapplicable proposed defaults'):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.contract)

    def test_missing_organizational_sla_not_autocalculated(self):
        self.assertIn('SLA: NOT CONFIGURED', self.contract)
        self.assertIn('not** `Required due date = today + 14 days`', self.contract)
        self.assertIn('unassigned', self.output)

    def test_no_live_write_or_deploy_in_draft_only_example(self):
        for phrase in ('curl -X POST', 'ansible-playbook', 'externally consequential actions',
                       'including ServiceNow ticket creation/updates',
                       'copy-pasteable workarounds', 'non-executable pending verification'):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.contract)
        self.assertIn('omit runnable mutating commands', self.output)

    def test_self_attested_approval_not_enough(self):
        for phrase in ('verified_by=$(whoami)', 'approved: true',
                       'approved-looking', 'not actually verified and enforced',
                       'system of record'):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.contract)

    def test_dry_run_not_assumed_harmless(self):
        self.assertIn('Dry-run is not assumed harmless', self.contract)
        self.assertIn('--check --diff', self.contract)
        self.assertIn('not as universal safety guarantees', self.output)
        self.assertIn('Check-mode is not guaranteed safe', self.gemini_skill)

    def test_gemini_reminder_enforces_same_rule_not_second_owner(self):
        self.assertIn('[Builder Contract](references/BUILDER_CONTRACT.md)', self.gemini_skill)
        self.assertIn('[Output Contract](references/OUTPUT_CONTRACT.md)', self.gemini_skill)
        self.assertIn('An unknown asset tier remains **UNKNOWN**', self.gemini_skill)
        self.assertIn('"assume Tier 2"', self.gemini_skill)
        self.assertIn('revise contradictions', self.gemini_skill.lower())

    def test_output_contract_has_contradiction_stop(self):
        for phrase in ('Final artifact consistency review', 'Contradiction stop',
                       'If the introduction says `draft-only`',
                       'no later copy-paste block'):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.output)

    def test_adapter_version_separation_preserved(self):
        self.assertEqual('0.1.3-dev', claude.DEFAULT_VERSION)
        self.assertEqual('0.1.3-dev', gemini.DEFAULT_VERSION)
        self.assertEqual('0.1.3-dev', __import__('json').loads(self.c['references/SOURCE_MAP.json'])['adapter_version'])
        self.assertEqual('0.1.3-dev', __import__('json').loads(self.g['references/SOURCE_MAP.json'])['adapter_version'])


if __name__ == '__main__':
    unittest.main()
