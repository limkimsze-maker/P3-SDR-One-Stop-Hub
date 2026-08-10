from pathlib import Path

path = Path('index.html')
raw = path.read_bytes()
had_crlf = b'\r\n' in raw
text = raw.decode('utf-8').replace('\r\n', '\n')

url = 'https://limkimsze-maker.github.io/Phonograms-Toy-Castle-Game/'
if url in text:
    print('Toy Castle link already exists in hub; no change needed.')
    raise SystemExit(0)

# Keep the fixed-screen page, but allow the resource area itself to scroll if an extra row is needed.
needle = '''    .resource-grid {\n      min-height: 0;\n      display: grid;'''
replacement = '''    .resource-grid {\n      min-height: 0;\n      overflow-y: auto;\n      padding-right: 4px;\n      display: grid;'''
if needle in text:
    text = text.replace(needle, replacement, 1)

section_start = text.find('<section class="resource-grid"')
if section_start == -1:
    raise SystemExit('Could not find resource grid section.')
section_end = text.find('</section>', section_start)
if section_end == -1:
    raise SystemExit('Could not find end of resource grid section.')

card = '''\n\n      <a class="resource-card card-4"\n         href="https://limkimsze-maker.github.io/Phonograms-Toy-Castle-Game/"\n         target="_blank" rel="noopener">\n        <div class="icon" aria-hidden="true">🏰</div>\n        <h2>Phonograms Toy Castle Game</h2>\n        <p>Practise phonograms through a colourful one- or two-player castle game.</p>\n        <span class="open-button">Play Game →</span>\n      </a>\n'''

text = text[:section_end] + card + text[section_end:]
if had_crlf:
    text = text.replace('\n', '\r\n')
path.write_bytes(text.encode('utf-8'))
print('Added Phonograms Toy Castle Game to P3 SDR One Stop Hub.')
