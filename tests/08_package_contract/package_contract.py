from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PACKAGE = ROOT / "package"
MANIFEST = PACKAGE / "01_MANIFEST.json"

EXPECTED_GM = {
    "GM-02","GM-03","GM-04","GM-05","GM-06","GM-07","GM-08","GM-09","GM-12","GM-13","GM-14"
}
EXPECTED_SM = {f"SM-{i:02d}" for i in range(1, 12)}
EXPECTED_REFS = {"REF-CN-001","REF-CN-002","REF-CN-003","REF-CN-004"}


def load_manifest():
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def test_manifest_paths_exist():
    m = load_manifest()
    paths = [m["bootstrap"]["path"], m["master_spec"]["path"]]
    paths += [x["path"] for x in m["modules"]["governing"]]
    paths += [x["path"] for x in m["modules"]["supporting"]]
    paths += [x["path"] for x in m["references"]["canonical"]]
    missing = [p for p in paths if not (PACKAGE / p).is_file()]
    assert not missing, f"Manifest paths missing: {missing}"


def test_module_inventory():
    m = load_manifest()
    gm = {x["id"] for x in m["modules"]["governing"]}
    sm = {x["id"] for x in m["modules"]["supporting"]}
    assert gm == EXPECTED_GM, (gm ^ EXPECTED_GM)
    assert sm == EXPECTED_SM, (sm ^ EXPECTED_SM)
    assert not (gm & sm)


def test_reference_inventory():
    m = load_manifest()
    refs = {x["id"] for x in m["references"]["canonical"]}
    assert refs == EXPECTED_REFS, (refs ^ EXPECTED_REFS)


def test_no_retired_active_modules():
    m = load_manifest()
    ids = {x["id"] for group in m["modules"].values() for x in group}
    assert not ({"GM-10", "GM-11", "GM-15"} & ids)


def test_bootstrap_kernel_invariants():
    text = (PACKAGE / "PASTE_THIS_INTO_THE_GPT.txt").read_text(encoding="utf-8").lower()
    required = [
        "you are", "purpose", "defined requirements", "constraints",
        "source meaning", "provenance", "uncertainty", "evidence",
        "calibrate claims", "capabilities actually available", "unsupported",
    ]
    missing = [x for x in required if x not in text]
    assert not missing, f"Bootstrap missing Kernel concepts: {missing}"


def test_no_leaked_citation_artifacts():
    bad = []
    for path in PACKAGE.rglob("*.md"):
        text = path.read_text(encoding="utf-8", errors="replace")
        if "oaicite" in text or "contentReference[" in text:
            bad.append(str(path.relative_to(PACKAGE)))
    assert not bad, f"Leaked citation artifacts: {bad}"


def test_markdown_fences_balanced():
    bad = []
    for path in PACKAGE.rglob("*.md"):
        text = path.read_text(encoding="utf-8", errors="replace")
        fences = re.findall(r"^\s*```", text, flags=re.MULTILINE)
        if len(fences) % 2:
            bad.append(str(path.relative_to(PACKAGE)))
    assert not bad, f"Unbalanced Markdown fences: {bad}"


if __name__ == "__main__":
    tests = [v for k, v in globals().items() if k.startswith("test_")]
    for test in tests:
        test()
        print(f"PASS {test.__name__}")
