#!/usr/bin/env python3
"""Check public-source file hashes after checkout (not a signature)."""
import hashlib
import json
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
try:
    manifest = json.loads((root / 'PUBLIC_SOURCE_MANIFEST.json').read_text(encoding='utf-8'))
    assert manifest['product'] == 'AIO AI Builder - public source distribution'
    files = manifest['files']
    assert len(files) == manifest['file_count']
    expected = set(files) | {'PUBLIC_SOURCE_MANIFEST.json'}
    actual = {p.relative_to(root).as_posix() for p in root.rglob('*')
              if p.is_file() and not set(p.relative_to(root).parts).intersection(
                  {'.git', 'dist', '__pycache__', '.venv', '.pytest_cache'})}
    assert actual == expected, 'unexpected/missing public source files'
    for name, sha in files.items():
        file = root / name
        assert '..' not in Path(name).parts and not Path(name).is_absolute()
        assert not file.is_symlink() and file.is_file()
        assert hashlib.sha256(file.read_bytes()).hexdigest() == sha, name
except (OSError, ValueError, KeyError, AssertionError, TypeError) as error:
    sys.exit(f'Public manifest verification FAILED: {error}')
print(f'PUBLIC SOURCE INTEGRITY VERIFIED: {len(files)} files')
