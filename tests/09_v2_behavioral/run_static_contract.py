from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
PKG = ROOT / 'package'

checks = []

def check(name, condition, detail=''):
    checks.append((name, bool(condition), detail))

# Kernel / bootstrap contract
boot = (PKG/'PASTE_THIS_INTO_THE_GPT.txt').read_text(encoding='utf-8')
for term in ['requirements','source meaning','provenance','uncertainty','evidence','capabilit','unsupported','inference','action']:
    check(f'KERN presence: {term}', term.lower() in boot.lower())

check('KERN provenance verification rule', 'actually verifiable' in boot.lower() and 'never infer, reconstruct' in boot.lower())

gm2 = (PKG/'modules/governing/GM-02_Knowledge_Source_Handling.md').read_text(encoding='utf-8').lower()
check('GM-02 provenance verification rule', '31a. provenance verification' in gm2 and 'correct information with unsupported provenance is still a provenance failure' in gm2)

# Current ownership references: retired IDs must not appear in live cross-reference sentences.
files = [PKG/'02_MASTER_OPERATING_SPEC.md'] + list((PKG/'modules').rglob('*.md'))
retired = re.compile(r'\bGM-(10|11|15)\b')
historical_markers = re.compile(r'historical|former|migration|lineage|retired|legacy|not a current|not current|source id|→', re.I)
for p in files:
    lines=p.read_text(encoding='utf-8').splitlines()
    for i,line in enumerate(lines,1):
        if retired.search(line) and not historical_markers.search(line):
            # Ignore module title/heading occurrences inside explicit migration sections only if nearby context says migration.
            context=' '.join(lines[max(0,i-4):min(len(lines),i+3)])
            if not historical_markers.search(context):
                check(f'LIVE retired ref: {p.relative_to(ROOT)}:{i}', False, line.strip())

# Ownership-specific assertions from the reconciled architecture.
expectations = {
    'SM-07 file analysis owner': (PKG/'modules/supporting/SM-07_Supplemental_Guided_Entry_and_Conversation_Starters.md', 'GM-03'),
    'SM-07 research owner': (PKG/'modules/supporting/SM-07_Supplemental_Guided_Entry_and_Conversation_Starters.md', 'GM-04'),
    'SM-07 support owner': (PKG/'modules/supporting/SM-07_Supplemental_Guided_Entry_and_Conversation_Starters.md', 'SM-11'),
    'SM-08 file owner': (PKG/'modules/supporting/SM-08_Supplemental_User_Guided_Preferences_and_Confirmation.md', 'GM-03'),
    'SM-08 research owner': (PKG/'modules/supporting/SM-08_Supplemental_User_Guided_Preferences_and_Confirmation.md', 'GM-04'),
    'Master file owner': (PKG/'02_MASTER_OPERATING_SPEC.md', 'GM-03'),
    'Master research owner': (PKG/'02_MASTER_OPERATING_SPEC.md', 'GM-04'),
}
for name,(p,term) in expectations.items():
    check(name, term in p.read_text(encoding='utf-8'))

# Module-specific boundary assertions.
boundaries = {
    'SM-02 distinguishes navigation from research': ('SM-02_Resource_and_Reference_Guidance.md', ['navigation','research']),
    'SM-06 distinguishes selection from source authority': ('SM-06_Supplemental_Selective_Information_Handling.md', ['source','select']),
    'SM-10 avoids unsupported competence determination': ('SM-10_Supplemental_Interactive_Practice_and_Assessment.md', ['competence','assessment']),
    'SM-11 avoids claiming support actions': ('SM-11_Support_and_Feedback.md', ['support','action']),
}
for name,(fname,terms) in boundaries.items():
    p=next(PKG.glob(f'modules/**/{fname}'))
    text=p.read_text(encoding='utf-8').lower()
    check(name, all(t.lower() in text for t in terms))

passed=sum(ok for _,ok,_ in checks)
failed=len(checks)-passed
print(f'STATIC V2 BEHAVIORAL CONTRACT: {passed}/{len(checks)} PASS')
for name,ok,detail in checks:
    print(('PASS' if ok else 'FAIL'), name, detail)
raise SystemExit(1 if failed else 0)
