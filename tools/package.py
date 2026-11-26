import hashlib
import json
from pathlib import Path
import sys
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

root = Path(__file__).resolve().parent.parent
output = Path(sys.argv[1]) if len(sys.argv) > 1 else root / "dist"
output.mkdir(parents=True, exist_ok=True)
manifest = json.loads((root / "plugin.json").read_text(encoding="utf-8"))
assert manifest["schema"] == 3
assert manifest["id"] == "character"
assert manifest["kind"] == "character_profiles"
assert manifest["skill"] == "SKILL.md"
archive = output / f"onesdm-plugin-character-{manifest['version']}.zip"
with ZipFile(archive, "w") as package:
    for name in ["plugin.json", manifest["skill"], "LICENSE"]:
        package.writestr(ZipInfo(name), (root / name).read_bytes(), compress_type=ZIP_DEFLATED)
with ZipFile(archive) as package:
    assert package.testzip() is None
digest = hashlib.sha256(archive.read_bytes()).hexdigest()
archive.with_suffix(".zip.sha256").write_text(f"{digest}  {archive.name}\n", encoding="ascii")
print(archive)
