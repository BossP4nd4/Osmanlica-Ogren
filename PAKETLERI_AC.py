from pathlib import Path
import hashlib, zipfile, sys

CHECKS = {'01-kaynak-kod-ve-kilavuzlar.zip': 'd826695efc737f977a166c2064e66b0fdf43faa49612602fa0ad8b11a127ac5a', '02-sozluk-paketi.zip': '7532073d7eaa1bcbf16f7f565a1439a6071d8f0cf842e7a5914d7f57002b4bbd', '03-hazir-ipa.zip': '41286d75488d07def6c5f65fc6565c5951cf1bf4488fa94c6235061f397c7356'}
base = Path(__file__).resolve().parent
target = base / "Osmanlica-Kurulum"
if target.exists():
    sys.exit("Osmanlica-Kurulum zaten var. Mevcut klasoru koruyun; araci bos bir klasorde calistirin.")
for name, expected in CHECKS.items():
    p = base / name
    if not p.is_file(): sys.exit("Eksik paket: " + name)
    h = hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda: f.read(8 * 1024 * 1024), b""): h.update(b)
    if h.hexdigest() != expected: sys.exit("Dogrulama basarisiz: " + name + ". Paketi yeniden indirin.")
    print("Dogrulandi:", name, flush=True)
for name in CHECKS:
    with zipfile.ZipFile(base / name) as z:
        for entry in z.infolist():
            resolved = (target / entry.filename).resolve()
            if target.resolve() not in resolved.parents: sys.exit("Gecersiz arsiv yolu")
        z.extractall(target)
    print("Acildi:", name, flush=True)
print("Tamamlandi:", target)
