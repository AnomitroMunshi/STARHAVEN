// Starhaven layer on top of graphify's graph.html: focus mode, portrait panel, kind filter.
// Loaded by a <script src> that enhance_graph.py adds; uses graph.html's globals
// (network, nodesDS, edgesDS, RAW_NODES, RAW_EDGES, hiddenCommunities, esc, showInfo).
(function () {
  document.title = 'Starhaven Character Map';
  const css = document.createElement('style');
  css.textContent = `
    #kind-wrap { display:flex; gap:4px; padding:8px 12px; border-bottom:1px solid var(--border); }
    #kind-wrap button { flex:1; background:var(--bg); color:var(--text-2); border:1px solid var(--input-border); border-radius:4px; padding:4px 0; font-size:11px; cursor:pointer; }
    #kind-wrap button[aria-pressed="true"] { background:#C84030; border-color:#C84030; color:#fff; }
    #info-panel { max-height:55vh; overflow-y:auto; }
    .sh-portrait { width:100%; max-height:220px; object-fit:cover; object-position:top; border-radius:8px; margin-bottom:10px; }
    .sh-name { font-size:16px; font-weight:600; color:var(--text); }
    .sh-meta { font-size:11px; color:var(--text-2); text-transform:uppercase; letter-spacing:.05em; margin:2px 0 8px; }
    .sh-desc { font-size:12.5px; line-height:1.55; margin-bottom:10px; }
    .sh-rel { font-size:11px; color:var(--text-2); margin-right:4px; }
    .sh-hint { font-size:11px; color:var(--muted); margin-top:8px; }`;
  document.head.appendChild(css);

  const KINDS = { char_: 'character', fac_: 'faction', place_: 'place' };
  const kindOf = id => { for (const p in KINDS) if (id.startsWith(p)) return KINDS[p]; return 'other'; };
  const DATA = new Map(RAW_NODES.map(n => [n.id, n]));
  const REL = RAW_EDGES.map(e => (e.label || '').replace(/_/g, ' '));
  const LABEL_MIN_DEGREE = 6;  // smaller nodes show their name on hover / in focus only
  const pretty = s => s.replace(/_/g, ' ');

  // Calm default look: quiet edges, labels only on well-connected nodes.
  network.setOptions({ edges: { font: { size: 10, color: '#bbb', strokeWidth: 0, align: 'middle' } } });
  function resetView() {
    focused = null;
    nodesDS.update(nodesDS.get().map(n => ({
      id: n.id, opacity: 1,
      font: Object.assign({}, n.font, { size: (DATA.get(n.id).degree || 0) >= LABEL_MIN_DEGREE ? 14 : 0 }),
    })));
    edgesDS.update(edgesDS.get().map(e => ({ id: e.id, hidden: false, label: '', color: { opacity: 0.18 } })));
  }

  // Focus: keep the node and its neighbours, fade the rest, name the relationships.
  let focused = null;
  function focusOn(id) {
    focused = id;
    const keep = new Set(network.getConnectedNodes(id)); keep.add(id);
    const edges = new Set(network.getConnectedEdges(id));
    nodesDS.update(nodesDS.get().map(n => ({
      id: n.id, opacity: keep.has(n.id) ? 1 : 0.08,
      font: Object.assign({}, n.font, { size: keep.has(n.id) ? (n.id === id ? 18 : 13) : 0 }),
    })));
    edgesDS.update(edgesDS.get().map(e => ({
      id: e.id, hidden: !edges.has(e.id),
      label: edges.has(e.id) ? REL[e.id] : '', color: { opacity: 0.8 },
    })));
  }

  // Richer info panel (replaces graphify's showInfo; its listeners call it by name).
  showInfo = function (id) {
    const n = DATA.get(id);
    if (!n) return;
    focusOn(id);
    const rels = network.getConnectedEdges(id).map(eid => {
      const e = RAW_EDGES[eid];
      const other = e.from === id ? e.to : e.from;
      const o = DATA.get(other);
      const arrow = e.from === id ? '→' : '←';
      return `<span class="neighbor-link" data-nid="${esc(other)}" style="border-left-color:${esc(o ? o.color.background : '#555')}"><span class="sh-rel">${esc(REL[eid])} ${arrow}</span>${esc(o ? o.label : other)}</span>`;
    }).join('');
    let html = '';
    if (n.image) html += `<img class="sh-portrait" src="${esc(n.image)}" alt="${esc(n.label)}">`;
    html += `<div class="sh-name">${esc(n.label)}</div>`;
    html += `<div class="sh-meta">${esc(kindOf(id))} · ${esc(n.community_name || '')}</div>`;
    if (n.description) html += `<div class="sh-desc">${esc(n.description)}</div>`;
    html += `<div class="field" style="color:var(--text-2);font-size:11px">Connections (${n.degree || 0})</div>`;
    html += `<div id="neighbors-list" style="max-height:none">${rels}</div>`;
    html += `<div class="sh-hint">Click empty space to see everyone again.</div>`;
    document.getElementById('info-content').innerHTML = html;
    document.querySelector('#info-panel h3').textContent = 'Who is who';
  };
  network.on('click', p => { if (!p.nodes.length && focused) resetView(); });
  network.on('doubleClick', p => { if (p.nodes.length) network.focus(p.nodes[0], { scale: 1.3, animation: true }); });

  // Kind filter: All / Characters / Factions / Places (respects community checkboxes).
  const wrap = document.createElement('div');
  wrap.id = 'kind-wrap';
  [['all', 'All'], ['character', 'Characters'], ['faction', 'Factions'], ['place', 'Places']].forEach(([k, label]) => {
    const b = document.createElement('button');
    b.type = 'button'; b.textContent = label; b.dataset.kind = k;
    b.setAttribute('aria-pressed', String(k === 'all'));
    b.onclick = () => {
      wrap.querySelectorAll('button').forEach(x => x.setAttribute('aria-pressed', String(x === b)));
      nodesDS.update(RAW_NODES.map(n => ({
        id: n.id,
        hidden: hiddenCommunities.has(n.community) || (k !== 'all' && kindOf(n.id) !== k),
      })));
    };
    wrap.appendChild(b);
  });
  document.getElementById('search-wrap').after(wrap);
  document.getElementById('search').placeholder = 'Search characters, factions, places…';
  document.querySelector('#info-panel h3').textContent = 'Who is who';
  document.getElementById('info-content').innerHTML = '<span class="empty">Click anyone to see their portrait and relationships</span>';

  resetView();
})();
