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

# Units / factions: the unit wiki's top-level "name" and "image" sit at the same indent in one entry
units = {}
uw = Path('starhaven-unit-wiki.html').read_text(encoding='utf-8')
for m in re.finditer(r'(?m)^( +)"name": "([^"]+)",\n(?:\1"[^\n]*\n)*?\1"image": "([^"]+)"', uw):
    if os.path.exists(m.group(3)):
        units.setdefault(key(m.group(2)), m.group(3))

# Chapter nodes that are the same person as a wiki entry under another name
SAME_AS = {'char_black_silence': 'Nyx Ravel', 'char_bram': 'Bram Seawall', 'char_vera': 'Vera Holt','char_brek': 'Brek Stonefall', 'char_ashen_scholar': 'Velkan Drake'}

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
    if not p and n['id'].startswith('fac_'):  # 'The Warbreakers' or 'Warbreakers' -> unitImages/warbreakers.png
        p = units.get(key(label)) or units.get(key(re.sub(r'^the ', '', label, flags=re.I)))
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
# Structured links the chapter extraction never saw: army/unit commanders and wiki relationships.
em = re.search(r'^const RAW_EDGES = (.*);$', html, re.M)
edges = json.loads(em.group(1))
# Links extracted from wiki text that has since been corrected (Brynhild Voss is at Sancthaven, not Frosthold)
STALE = {frozenset(('char_brynhild_voss', 'place_frosthold_bastion')), frozenset(('char_varg_ironfrost', 'char_brynhild_voss'))}
edges = [e for e in edges if frozenset((e['from'], e['to'])) not in STALE]
have = {frozenset((e['from'], e['to'])) for e in edges}
idx = {}
for n in nodes:
    for lab in (n['label'], n['label'].split(' (')[0], re.sub(r'^the ', '', n['label'], flags=re.I)):
        idx.setdefault(key(lab), n['id'])
def find(name, prefix):
    k = key(re.sub(r'\s*·.*|\s*\(.*', '', name).strip())
    hit_ = idx.get(k)
    if hit_ and hit_.startswith(prefix): return hit_
    c = [v for kk, v in idx.items() if v.startswith(prefix) and len(k) > 6 and (kk.endswith(k) or k.endswith(kk) and len(kk) > 6)]
    return c[0] if len(set(c)) == 1 else None
added = 0
def link(a, b, rel):
    global added
    if a and b and a != b and frozenset((a, b)) not in have:
        have.add(frozenset((a, b))); added += 1
        edges.append({'from': a, 'to': b, 'label': rel, 'title': rel + ' [WIKI]', 'dashes': False, 'width': 2,
                      'color': {'opacity': 0.7}, 'confidence': 'EXTRACTED'})
def people(s):  # 'Lyria Valen · Sub: Cass Thorn, Fenris Grey' -> ['Lyria Valen', 'Cass Thorn', 'Fenris Grey']
    s = re.sub(r'\([^)]*\)', '', s)
    out = []
    for part in re.split(r'\s*·\s*', s):
        if part.lower().startswith(('mount', 'hq')): continue
        part = re.sub(r'^Sub:\s*', '', part)
        out += [re.sub(r'^(Captain|Commander|Director|Spear-Marshal|General|Admiral|Lord|Lady|Commodore|Marshal|Warden)\s+', '', p).strip()
                for p in re.split(r',\s*', part) if p.strip()]
    return out
armies = wiki[wiki.index('const ARMIES = ['):wiki.index('const BALLADS')]
for m2 in re.finditer(r"name:'((?:[^'\\]|\\.)*)',[\s\S]*?commander:'((?:[^'\\]|\\.)*)'", armies):
    fac = find(m2.group(1).replace("\\'", "'"), 'fac_')
    for p_ in people(m2.group(2).replace("\\'", "'")):
        link(find(p_, 'char_'), fac, 'commands')
for m2 in re.finditer(r'(?m)^( +)"name": "([^"]+)",\n(?:\1"[^\n]*\n)*?\1"army": "([^"]+)"', uw):
    fac = find(m2.group(2), 'fac_')
    who = m2.group(3).split(' — ')[-1]
    for p_ in people(who):
        link(find(p_, 'char_'), fac, 'commands')
chars = wiki[wiki.index('const CHARACTERS = ['):wiki.index('const ARMIES = [')]
for card in re.split(r"\n  \{\n", chars):
    nm = re.search(r"name:'((?:[^'\\]|\\.)*)'", card)
    if not nm: continue
    me = find(nm.group(1).replace("\\'", "'"), 'char_')
    rels = re.search(r"relationships:\[(.*?)\],\n", card, re.S)
    for r_ in re.finditer(r"\{name:'((?:[^'\\]|\\.)*)',\s*type:'([^']*)'", rels.group(1) if rels else ''):
        link(me, find(r_.group(1).replace("\\'", "'"), 'char_'), r_.group(2).replace(' ', '_') + '_of')
    cm = re.search(r"commands:\[([^\]]*)\]", card)
    for c_ in re.findall(r"'((?:[^'\\]|\\.)*)'", cm.group(1) if cm else ''):
        link(me, find(c_.replace("\\'", "'"), 'fac_'), 'commands')
# Musicians: link every bard/singer/musician card to Dren Solm, the kingdom's first titled bard
dren = find('Dren Solm', 'char_')
MUSIC = re.compile(r'bard|musician|singer|soprano|tenor|composer|lutenist|drummer|fiddler|harpist|piper|choir|minstrel|songwright', re.I)
musicians = []
for card in re.split(r"\n  \{\n", chars):
    nm = re.search(r"name:'((?:[^'\\]|\\.)*)'", card)
    who = ' '.join(x.group(1) for x in (re.search(r"role:'((?:[^'\\]|\\.)*)'", card), re.search(r"title:'((?:[^'\\]|\\.)*)'", card)) if x)
    band = 'The Starborn' in (re.search(r"tags:\[([^\]]*)\]", card) or [None, ''])[1]  # Dren Solm's band in the wiki
    if nm and (band or MUSIC.search(who)):
        me = find(nm.group(1).replace("\\'", "'"), 'char_')
        if me and me != dren:
            link(me, dren, 'band_member_of' if band else 'fellow_musician'); musicians.append(nm.group(1))
print(f'{len(musicians)} musicians linked to Dren Solm: {", ".join(musicians)}')
deg = {}
for e in edges:
    for x in (e['from'], e['to']): deg[x] = deg.get(x, 0) + 1
for n in nodes: n['degree'] = deg.get(n['id'], 0)
html = html[:em.start(1)] + json.dumps(edges, ensure_ascii=False) + html[em.end(1):]
m = re.search(r'^const RAW_NODES = (.*);$', html, re.M)
html = html[:m.start(1)] + json.dumps(nodes, ensure_ascii=False) + html[m.end(1):]
print(f'{added} wiki links added')

# Render nodes with an image as round portraits (patch once)
old = '  font: n.font, title: n.title,\n'
new = old + "  ...(n.image ? { shape: 'circularImage', image: n.image, size: Math.max(n.size, 18) } : {}),\n"
if new not in html:
    assert old in html, 'graph.html layout changed; update add_images.py'
    html = html.replace(old, new, 1)
# Group outlines only for the clicked node's groups (starhaven.js sets window.shFocus)
old = '    hyperedges.forEach(h => {\n'
new = old + '        if (!window.shFocus || !h.nodes.includes(window.shFocus)) return;\n'
if new not in html:
    assert old in html, 'graph.html hyperedge drawing changed; update enhance_graph.py'
    html = html.replace(old, new, 1)
tag = '<script src="starhaven.js"></script>\n'
if tag not in html:
    html = html.replace('</body>', tag + '</body>', 1)
html_path.write_text(html, encoding='utf-8')
print(f'{hit} of {len(nodes)} nodes got an image ({len(images)} wiki portraits found)')
