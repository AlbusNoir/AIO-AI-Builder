from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent

# Remove stale Python caches before testing.
CACHE_DIRS = [
    ROOT / "automation" / "__pycache__",
    ROOT / "automation" / "tests" / "__pycache__",
]

for cache in CACHE_DIRS:
    if cache.is_dir():
        print(f"Removing: {cache}", flush=True)
        shutil.rmtree(cache)

print("Running AIO test suite...\n", flush=True)

# Run tests without generating new .pyc files.
result = subprocess.run(
    [
        sys.executable,
        "-B",
        "-m",
        "unittest",
        "discover",
        "-s",
        "automation/tests",
        "-p",
        "test_*.py",
    ],
    cwd=ROOT,
)

sys.exit(result.returncode)