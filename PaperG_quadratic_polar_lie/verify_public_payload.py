from pathlib import Path
from hashlib import sha256
import json
root = Path(__file__).resolve().parent
manifest = json.loads((root / 'source_manifest.json').read_text(encoding='utf-8'))
for row in manifest['files']:
    data = (root / row['path']).read_bytes()
    assert len(data) == row['bytes'] and sha256(data).hexdigest() == row['sha256'], row['path']
pdf = root / manifest['manuscript_pdf']['name']
if pdf.exists():
    assert sha256(pdf.read_bytes()).hexdigest() == manifest['manuscript_pdf']['sha256']
print('PASS: all original public source and verification payload hashes match.')
