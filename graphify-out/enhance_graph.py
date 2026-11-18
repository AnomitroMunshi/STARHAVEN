# Starhaven polish for graph.html: wiki portraits, descriptions, and starhaven.js
# (focus mode, portrait panel, kind filter). Re-run after every `graphify export html`.
import json, os, re
from pathlib import Path

os.chdir(Path(__file__).resolve().parent.parent)  # repo root
wiki = Path('starhaven_wiki.html').read_text(encoding='utf-8')

# Characters: each wiki entry has name:'X' ... image:'path' before the next name:'
import unicodedata
def key(name):  # 'Vael "Nightwind" Noss', 'Tomás Rael' -> 'vaelnightwindnoss', 'tomasrael'
    name = re.sub(r'\s*\([^)]*\)', '', name)  # 'Sora Ashe (née Keld)' -> 'Sora Ashe'
    name = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]', '', name.lower())

images = {}
for m in re.finditer(r"name:'((?:[^'\\]|\\.)*)'", wiki):
    seg = re.split(r"[{}]|name:'", wiki[m.end():m.end() + 1500])[0]  # stay inside this entry
    img = re.search(r"image:'([^']+)'", seg)
    if img and os.path.exists(img.group(1)):
        images.setdefault(key(m.group(1).replace("\\'", "'")), img.group(1))
# Partner cards put the image first: {image:'...', name:'X'}
for m in re.finditer(r"image:'([^']+)',\s*name:'((?:[^'\\]|\\.)*)'", wiki):
    if os.path.exists(m.group(1)):
        images.setdefault(key(m.group(2).replace("\\'", "'")), m.group(1))

# Chapter nodes that are the same person as a wiki entry under another name
SAME_AS = {'char_bram': 'Bram Seawall', 'char_vera': 'Vera Holt','char_brek': 'Brek Stonefall', 'char_ashen_scholar': 'Velkan Drake'}

# Mounts: graph node -> unitImages picture (see the MOUNTS sections of character_portrait_prompts.txt)
MOUNTS = json.loads(Path('graphify-out/mount_images.json').read_text(encoding='utf-8'))

# Places: the wiki builds starhaven_places_image/<slug>.jpg from the name
def slug(name):
    return re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')

html_path = Path('graphify-out/graph.html')
html = html_path.read_text(encoding='utf-8')
m = re.search(r'^const RAW_NODES = (.*);$', html, re.M)
nodes = json.loads(m.group(1))
desc = {n['id']: n.get('description') for n in json.loads(Path('graphify-out/graph.json').read_text(encoding='utf-8'))['nodes']}
hit = 0
for n in nodes:
    if desc.get(n['id']):
        n['description'] = desc[n['id']]
    label = n['label'].split(' (')[0]
    alias = re.search(r'\(([^)]+)\)', n['label'])  # 'Caelum Vey (Kai)' -> also try 'Kai'
    p = images.get(key(n['label'])) or images.get(key(label)) or (alias and images.get(key(alias.group(1))))
    if not p:  # titles: 'Admiral-Scholar Pren Vane' in the wiki vs 'Pren Vane' here
        p = next((v for k, v in images.items() if k.endswith(key(label)) and len(key(label)) > 6), None)
    if not p and os.path.exists(MOUNTS.get(n['id'], '')):
        p = MOUNTS[n['id']]
    if not p and n['id'] in SAME_AS:
        p = images.get(key(SAME_AS[n['id']]))
    if not p and n['id'].startswith('char_'):  # new portraits saved as <name>.jpg (see character_portrait_prompts.txt)
        cand = f'starhaven_chars_image/{key(label)}.jpg'
        p = cand if os.path.exists(cand) else None
    if not p and n['id'].startswith('place_'):
        cand = f'starhaven_places_image/{slug(label.lower())}.jpg'
        p = cand if os.path.exists(cand) else None
    n.pop('image', None)
    if p:
        n['image'] = '../' + p
        hit += 1
html = html[:m.start(1)] + json.dumps(nodes, ensure_ascii=False) + html[m.end(1):]

# Render nodes with an image as round portraits (patch once)
old = '  font: n.font, title: n.title,\n'
new = old + "  ...(n.image ? { shape: 'circularImage', image: n.image, size: Math.max(n.size, 18) } : {}),\n"
if new not in html:
    assert old in html, 'graph.html layout changed; update add_images.py'
    html = html.replace(old, new, 1)
tag = '<script src="starhaven.js"></script>\n'
if tag not in html:
    html = html.replace('</body>', tag + '</body>', 1)
html_path.write_text(html, encoding='utf-8')
print(f'{hit} of {len(nodes)} nodes got an image ({len(images)} wiki portraits found)')
