CSS = open('/home/claude/npi-animacije/orodja/common.css.html').read()
CSS = CSS.replace('</style>', '''
.ct-sym { fill: var(--panel); stroke: var(--ink); stroke-width: 2.5; }
.ct-box { fill: none; stroke: var(--muted); stroke-width: 2; stroke-dasharray: 6 5; }
.ct-coil { stroke: var(--ink); stroke-width: 3; }
.ct-tag { font: 600 17px var(--font); fill: var(--muted); }
</style>''')

HELP = r'''
  var $ = function (id) { return document.getElementById(id); };
  var svg = $('svg');
  function P(d, cls) { return '<path class="ct-w ' + cls + '" d="' + d + '"/>'; }
  function F(d) { return '<path class="ct-flow" d="' + d + '"/>'; }
  function T(x, y, s, cls, anchor) { return '<text class="' + (cls || 'ct-t') + '" x="' + x + '" y="' + y + '"' + (anchor ? ' text-anchor="' + anchor + '"' : '') + '>' + s + '</text>'; }
  function dot(x, y) { return '<circle cx="' + x + '" cy="' + y + '" r="5" fill="var(--ink)"/>'; }
  function term(x, y) { return '<circle class="ct-term" cx="' + x + '" cy="' + y + '" r="6"/>'; }
  function lamp(cx, cy, on, label, lx, ly) {
    var s = '';
    if (on) s += '<circle cx="' + cx + '" cy="' + cy + '" r="46" fill="var(--glow)" opacity=".45"/>';
    s += '<circle class="ct-bulb" cx="' + cx + '" cy="' + cy + '" r="26" fill="' + (on ? 'var(--lamp)' : 'var(--panel)') + '"/>';
    s += '<line class="ct-fil" x1="' + (cx - 13) + '" y1="' + (cy - 13) + '" x2="' + (cx + 13) + '" y2="' + (cy + 13) + '"/>';
    s += '<line class="ct-fil" x1="' + (cx + 13) + '" y1="' + (cy - 13) + '" x2="' + (cx - 13) + '" y2="' + (cy + 13) + '"/>';
    if (label) s += T(lx, ly, label);
    return s;
  }
  function source() {
    return '<circle class="ct-term" cx="40" cy="180" r="24"/>' + T(40, 187, '~', 'ct-t', 'middle') + T(74, 187, '230 V', 'ct-tm');
  }
  function pauseBtn() {
    $('pause').addEventListener('click', function () {
      var p = !svg.classList.contains('ct-paused');
      svg.classList.toggle('ct-paused', p);
      this.setAttribute('aria-pressed', p ? 'true' : 'false');
      this.textContent = p ? 'Nadaljuj gibanje toka' : 'Ustavi gibanje toka';
    });
  }
'''

def page(fname, title, h1, lead, viewbox, svglabel, controls, bottom_right, legend, script):
    html = f'''<!DOCTYPE html>
<html lang="sl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<script>if (/[?&]kompakt\\b/.test(location.search)) document.documentElement.classList.add('ct-kompakt');</script>
{CSS}
</head>
<body>
<div class="ct-wrap">
  <header>
    <h1>{h1}</h1>
    <p class="ct-lead">{lead}</p>
  </header>
  <section class="ct-panel" aria-label="Animacija: {h1}">
    <div class="ct-status">
      <span class="ct-chip" id="chip"></span>
      <p id="status" aria-live="polite"></p>
    </div>
    <p class="ct-scrollhint">Shema je širša od zaslona – povleci jo levo in desno.</p>
    <div class="ct-stage" tabindex="0" aria-label="Shema – s puščicami jo premikaš levo in desno">
      <svg class="ct-circuit" id="svg" viewBox="{viewbox}" role="img" aria-label="{svglabel}"></svg>
    </div>
    <div class="ct-legend">{legend}</div>
    <div class="ct-bottom">
      <div class="ct-controls">{controls}
        <button class="ct-btn" type="button" id="pause" aria-pressed="false">Ustavi gibanje toka</button>
      </div>
      <div class="ct-tablewrap">{bottom_right}</div>
    </div>
    <p class="ct-note" id="note"></p>
  </section>
</div>
<script>
(function () {{
  'use strict';
{HELP}
{script}
}})();
</script>
</body>
</html>
'''
    open('/home/claude/npi-animacije/' + fname, 'w').write(html)

LEG = ('<span><b style="background:var(--live)"></b>fazni ali stikalni vodnik pod napetostjo</span>'
       '<span><b style="background:var(--neutral)"></b>nevtralni vodnik s tokom</span>'
       '<span><b style="background:var(--off)"></b>brez napetosti</span>')

# ---------------------------------------------------------------- SERIJSKA
page('serijska-vezava.html', 'Serijska vezava – animacija', 'Serijska vezava',
 'Serijsko stikalo ima dve tipki. Vsaka prižge svojo skupino svetilk.',
 '0 30 910 300', 'Dvopolna shema serijske vezave: serijsko stikalo z dvema tipkama, skupina 1 z dvema svetilkama in skupina 2 s tremi svetilkami',
 '''
        <button class="ct-btn" type="button" id="b1">Tipka 1: vklopi</button>
        <button class="ct-btn" type="button" id="b2">Tipka 2: vklopi</button>''',
 '''<table><thead><tr><th>Tipka 1</th><th>Tipka 2</th><th>Sveti</th></tr></thead><tbody id="tbody">
  <tr data-a="0" data-b="0"><td>izklop</td><td>izklop</td><td>nič</td></tr>
  <tr data-a="1" data-b="0"><td>vklop</td><td>izklop</td><td>skupina 1 (2 svetilki)</td></tr>
  <tr data-a="0" data-b="1"><td>izklop</td><td>vklop</td><td>skupina 2 (3 svetilke)</td></tr>
  <tr data-a="1" data-b="1"><td>vklop</td><td>vklop</td><td>vseh 5 svetilk</td></tr>
</tbody></table>''', LEG, r'''
  var a = 0, b = 0;
  var G1 = [360, 460], G2 = [600, 700, 800];
  function render() {
    var s = '';
    // dovod (zunaj zamika)
    var o = P('M40 60 V155', 'ct-w-live') + P('M40 205 V300', (a || b) ? 'ct-w-n' : 'ct-w-offn') + P('M40 60 H70', 'ct-w-live') + P('M40 300 H70', (a || b) ? 'ct-w-n' : 'ct-w-offn') + source();
    o += T(40, 52, 'L', 'ct-t', 'middle') + T(40, 326, 'N', 'ct-t', 'middle');
    s += P('M40 60 H110 V140 H150', 'ct-w-live');
    if (a || b) s += F('M10 155 V60 H110 V140 H150');
    // serijsko stikalo
    s += '<rect class="ct-box" x="130" y="72" width="150" height="132" rx="8"/>' + T(205, 230, 'serijsko stikalo', 'ct-tag', 'middle');
    var e2 = b ? [260, 100] : [150 + 72 * Math.cos(-1.05), 140 + 72 * Math.sin(-1.05)];
    var e1 = a ? [260, 180] : [150 + 72 * Math.cos(1.05), 140 + 72 * Math.sin(1.05)];
    s += '<line class="ct-blade" stroke="var(--live)" x1="150" y1="140" x2="' + e2[0].toFixed(1) + '" y2="' + e2[1].toFixed(1) + '"/>';
    s += '<line class="ct-blade" stroke="var(--live)" x1="150" y1="140" x2="' + e1[0].toFixed(1) + '" y2="' + e1[1].toFixed(1) + '"/>';
    s += term(150, 140) + term(260, 100) + term(260, 180);
    s += T(232, 96, '2', 'ct-tm', 'end') + T(232, 196, '1', 'ct-tm', 'end');
    // L2' zgoraj do skupine 2
    s += P('M260 100 H800', b ? 'ct-w-live' : 'ct-w-off') + T(300, 90, "L2'", 'ct-tm');
    // L1' spodaj do skupine 1
    s += P('M260 180 H460', a ? 'ct-w-live' : 'ct-w-off') + T(300, 172, "L1'", 'ct-tm');
    // N
    s += P('M40 300 H800', (a || b) ? 'ct-w-n' : 'ct-w-offn');
    G1.forEach(function (x, i) {
      s += P('M' + x + ' 180 V214', a ? 'ct-w-live' : 'ct-w-off') + P('M' + x + ' 266 V300', a ? 'ct-w-n' : 'ct-w-offn');
      s += dot(x, 180) + dot(x, 300) + lamp(x, 240, !!a, null);
      if (a) s += F('M260 180 H' + x + ' V214') + F('M' + x + ' 266 V300 H10 V205');
    });
    G2.forEach(function (x, i) {
      s += P('M' + x + ' 100 V174', b ? 'ct-w-live' : 'ct-w-off') + P('M' + x + ' 226 V300', b ? 'ct-w-n' : 'ct-w-offn');
      s += dot(x, 100) + dot(x, 300) + lamp(x, 200, !!b, null);
      if (b) s += F('M260 100 H' + x + ' V174') + F('M' + x + ' 226 V300 H10 V205');
    });
    if (a) s += F('M150 140 L260 180');
    if (b) s += F('M150 140 L260 100');
    s += T(410, 166, 'skupina 1', 'ct-tag', 'middle') + T(700, 86, 'skupina 2', 'ct-tag', 'middle');
    svg.innerHTML = o + '<g transform="translate(30 0)">' + s + '</g>';

    $('b1').textContent = 'Tipka 1: ' + (a ? 'izklopi' : 'vklopi');
    $('b2').textContent = 'Tipka 2: ' + (b ? 'izklopi' : 'vklopi');
    $('b1').setAttribute('aria-pressed', a ? 'true' : 'false');
    $('b2').setAttribute('aria-pressed', b ? 'true' : 'false');
    var n = 2 * a + 3 * b;
    $('chip').textContent = n === 0 ? 'Nič ne sveti' : 'Sveti ' + n + ' od 5';
    $('status').textContent = n === 0 ? 'Obe tipki sta izklopljeni. Stikalna vodnika L1\' in L2\' sta brez napetosti.'
      : (a && b ? 'Obe tipki sta vklopljeni. Svetijo vse svetilke.'
      : 'Tipka ' + (a ? '1' : '2') + ' je vklopljena. Napetost je na stikalnem vodniku L' + (a ? '1' : '2') + '\' in sveti skupina ' + (a ? '1' : '2') + '.');
    document.querySelectorAll('#tbody tr').forEach(function (r) {
      var cur = +r.dataset.a === a && +r.dataset.b === b;
      r.style.background = cur ? 'var(--row)' : '';
      r.style.fontWeight = cur ? '700' : '';
      if (cur) r.setAttribute('aria-current', 'true'); else r.removeAttribute('aria-current');
    });
    $('note').textContent = 'Vse svetilke so vezane vzporedno: vsaka ima 230 V. »Serijsko« je samo ime stikala. Zaščitni vodnik PE ni narisan.';
  }
  $('b1').addEventListener('click', function () { a = 1 - a; render(); });
  $('b2').addEventListener('click', function () { b = 1 - b; render(); });
  pauseBtn();
  render();
''')

# ---------------------------------------------------------------- KRIŽNA
page('krizna-vezava.html', 'Križna vezava – animacija', 'Križna vezava',
 'Dve menjalni stikali in eno ali dve križni stikali. Svetilko prižgeš in ugasneš s katerega koli mesta.',
 '0 40 1000 290', 'Dvopolna shema križne vezave: menjalno stikalo S1, križni stikali K1 in K2, menjalno stikalo S2 in svetilka',
 '''
        <div class="ct-group" role="group" aria-label="Število križnih stikal"><span>Križna stikala:</span>
          <button class="ct-btn" type="button" data-k="1">1</button>
          <button class="ct-btn" type="button" data-k="2">2</button>
        </div>
        <button class="ct-btn" type="button" id="bs1">Preklopi S1</button>
        <button class="ct-btn" type="button" id="bk1">Preklopi K1</button>
        <button class="ct-btn" type="button" id="bk2">Preklopi K2</button>
        <button class="ct-btn" type="button" id="bs2">Preklopi S2</button>''',
 '''<table><thead><tr><th>Stikalo</th><th>Položaj</th></tr></thead><tbody id="tbody"></tbody></table>''', LEG, r'''
  // položaj menjalnega stikala: 0 = vodnik 1 (zgoraj), 1 = vodnik 2 (spodaj); križno: 0 = naravnost, 1 = navzkriž
  var st = { s1: 0, s2: 0, k1: 0, k2: 0, nk: 1 };
  var Y = [120, 200];
  function on() { var t = st.s1 ^ st.k1 ^ (st.nk === 2 ? st.k2 : 0); return t === st.s2; }
  function cross(x0, k, liveIn, lit) {
    // križno stikalo med x0 in x0+100; vhoda levo, izhoda desno
    var s = '<rect class="ct-box" x="' + (x0 - 10) + '" y="96" width="120" height="128" rx="8"/>';
    var pairs = k ? [[0, 1], [1, 0]] : [[0, 0], [1, 1]];
    pairs.forEach(function (p) {
      var live = p[0] === liveIn;
      s += '<line class="ct-blade" stroke="' + (live ? 'var(--live)' : 'var(--off)') + '" x1="' + x0 + '" y1="' + Y[p[0]] + '" x2="' + (x0 + 100) + '" y2="' + Y[p[1]] + '"/>';
      if (live && lit) s += F('M' + x0 + ' ' + Y[p[0]] + ' L' + (x0 + 100) + ' ' + Y[p[1]]);
    });
    s += term(x0, 120) + term(x0, 200) + term(x0 + 100, 120) + term(x0 + 100, 200);
    return s;
  }
  function trav(x1, x2, liveIdx, lit) {
    var s = '';
    [0, 1].forEach(function (i) {
      s += P('M' + x1 + ' ' + Y[i] + ' H' + x2, i === liveIdx ? 'ct-w-live' : 'ct-w-off');
      if (i === liveIdx && lit) s += F('M' + x1 + ' ' + Y[i] + ' H' + x2);
    });
    return s;
  }
  function render() {
    var lit = on(), s = '';
    var o = P('M40 70 V155', 'ct-w-live') + P('M40 205 V300', lit ? 'ct-w-n' : 'ct-w-offn') + P('M40 70 H80', 'ct-w-live') + P('M40 300 H80', lit ? 'ct-w-n' : 'ct-w-offn') + source();
    o += T(40, 62, 'L', 'ct-t', 'middle') + T(40, 326, 'N', 'ct-t', 'middle');
    s += P('M40 70 H100 V160 H120', 'ct-w-live');
    if (lit) s += F('M0 155 V70 H100 V160 H120');
    // S1
    s += '<rect class="ct-box" x="110" y="96" width="110" height="128" rx="8"/>' + T(165, 88, 'S1', 'ct-t', 'middle');
    s += '<line class="ct-blade" stroke="var(--live)" x1="120" y1="160" x2="205" y2="' + Y[st.s1] + '"/>' + term(120, 160) + term(210, 120) + term(210, 200);
    if (lit) s += F('M120 160 L205 ' + Y[st.s1]);
    // K1
    var t1 = st.s1;
    s += trav(210, 320, t1, lit) + cross(320, st.k1, t1, lit) + T(370, 88, 'K1', 'ct-t', 'middle');
    var t2 = t1 ^ st.k1, xS2;
    if (st.nk === 2) {
      s += trav(420, 520, t2, lit) + cross(520, st.k2, t2, lit) + T(570, 88, 'K2', 'ct-t', 'middle');
      t2 = t2 ^ st.k2; s += trav(620, 720, t2, lit); xS2 = 720;
    } else {
      s += trav(420, 720, t2, lit); xS2 = 720;
    }
    // S2
    s += '<rect class="ct-box" x="710" y="96" width="110" height="128" rx="8"/>' + T(765, 88, 'S2', 'ct-t', 'middle');
    s += '<line class="ct-blade" stroke="' + (lit ? 'var(--live)' : 'var(--off)') + '" x1="810" y1="160" x2="725" y2="' + Y[st.s2] + '"/>' + term(810, 160) + term(720, 120) + term(720, 200);
    if (lit) s += F('M725 ' + Y[st.s2] + ' L810 160');
    // svetilka
    s += P('M810 160 H862', lit ? 'ct-w-live' : 'ct-w-off') + lamp(888, 160, lit, null) + P('M914 160 H935 V300 H40', lit ? 'ct-w-n' : 'ct-w-offn');
    if (lit) s += F('M810 160 H862') + F('M914 160 H935 V300 H0 V205');
    s += T(888, 124, 'E1', 'ct-t', 'middle');
    s += T(165, 250, 'menjalno', 'ct-tag', 'middle') + T(370, 250, 'križno', 'ct-tag', 'middle') + (st.nk === 2 ? T(570, 250, 'križno', 'ct-tag', 'middle') : '') + T(765, 250, 'menjalno', 'ct-tag', 'middle');
    svg.innerHTML = o + '<g transform="translate(40 0)">' + s + '</g>';

    document.querySelectorAll('[data-k]').forEach(function (b) { b.setAttribute('aria-pressed', +b.dataset.k === st.nk ? 'true' : 'false'); });
    $('bk2').hidden = st.nk !== 2;
    $('chip').textContent = lit ? 'Svetilka sveti' : 'Svetilka ne sveti';
    var mest = 2 + st.nk;
    $('status').textContent = (lit ? 'Pot od L do svetilke je sklenjena. ' : 'Pot je prekinjena na stikalu S2. ')
      + 'Svetilko lahko prižgeš ali ugasneš s ' + mest + ' mest – vsak preklop kateregakoli stikala spremeni stanje svetilke.';
    var rows = '<tr><td>S1 (menjalno)</td><td>vodnik ' + (st.s1 + 1) + '</td></tr>'
      + '<tr><td>K1 (križno)</td><td>' + (st.k1 ? 'navzkriž' : 'naravnost') + '</td></tr>'
      + (st.nk === 2 ? '<tr><td>K2 (križno)</td><td>' + (st.k2 ? 'navzkriž' : 'naravnost') + '</td></tr>' : '')
      + '<tr><td>S2 (menjalno)</td><td>vodnik ' + (st.s2 + 1) + '</td></tr>';
    $('tbody').innerHTML = rows;
    $('note').textContent = 'Križno stikalo vodnika, ki prideta, poveže naravnost ali navzkriž. Zaščitni vodnik PE ni narisan.';
  }
  document.querySelectorAll('[data-k]').forEach(function (b) { b.addEventListener('click', function () { st.nk = +b.dataset.k; render(); }); });
  $('bs1').addEventListener('click', function () { st.s1 ^= 1; render(); });
  $('bs2').addEventListener('click', function () { st.s2 ^= 1; render(); });
  $('bk1').addEventListener('click', function () { st.k1 ^= 1; render(); });
  $('bk2').addEventListener('click', function () { st.k2 ^= 1; render(); });
  pauseBtn();
  render();
''')

# ---------------------------------------------------------------- IMPULZNI RELE
page('impulzni-rele.html', 'Bistabilni impulzni rele – animacija', 'Bistabilni impulzni rele',
 'Kratek pritisk na katerokoli tipkalo pošlje impulz tuljavi. Rele preklopi kontakt in ga obdrži do naslednjega impulza.',
 '0 20 940 320', 'Shema z bistabilnim impulznim relejem: tri tipkala vezana vzporedno na tuljavo releja, kontakt releja vklaplja svetilko',
 '''
        <button class="ct-btn" type="button" data-t="0">Pritisni tipkalo 1</button>
        <button class="ct-btn" type="button" data-t="1">Pritisni tipkalo 2</button>
        <button class="ct-btn" type="button" data-t="2">Pritisni tipkalo 3</button>''',
 '''<table><thead><tr><th>Kaj</th><th>Stanje</th></tr></thead><tbody id="tbody"></tbody></table>''', LEG, r'''
  var st = { contact: 0, pressed: -1, count: 0 };
  var TX = [150, 270, 390];
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function tipkalo(x, closed) {
    var s = term(x, 100) + term(x, 150);
    s += '<line class="ct-blade" stroke="' + (closed ? 'var(--live)' : 'var(--off)') + '" x1="' + (x + (closed ? 0 : 14)) + '" y1="' + (closed ? 100 : 104) + '" x2="' + (x + (closed ? 0 : 14)) + '" y2="' + (closed ? 150 : 146) + '"/>';
    s += '<line stroke="var(--ink)" stroke-width="3" x1="' + (x + (closed ? 0 : 14)) + '" y1="125" x2="' + (x + 34) + '" y2="125"/>';
    s += '<line stroke="var(--ink)" stroke-width="4" stroke-linecap="round" x1="' + (x + 34) + '" y1="114" x2="' + (x + 34) + '" y2="136"/>';
    return s;
  }
  function render() {
    var imp = st.pressed >= 0, lit = st.contact === 1, s = '';
    var o = T(40, 42, 'L', 'ct-t', 'middle') + T(40, 330, 'N', 'ct-t', 'middle') + P('M40 50 V155', 'ct-w-live') + source() + P('M40 205 V300', (imp || lit) ? 'ct-w-n' : 'ct-w-offn') + P('M40 50 H90', 'ct-w-live') + P('M40 300 H90', (imp || lit) ? 'ct-w-n' : 'ct-w-offn');
    s += P('M40 50 H700', 'ct-w-live') + P('M40 300 H700', (imp || lit) ? 'ct-w-n' : 'ct-w-offn');
    // krmilni krog
    s += '<rect class="ct-box" x="110" y="64" width="470" height="224" rx="10"/>' + T(345, 282, 'krmilni krog', 'ct-tag', 'middle');
    TX.forEach(function (x, i) {
      var c = st.pressed === i;
      s += P('M' + x + ' 50 V100', 'ct-w-live') + dot(x, 50) + tipkalo(x, c) + T(x + 44, 130, 'T' + (i + 1), 'ct-tm');
      s += P('M' + x + ' 150 V190', c ? 'ct-w-live' : 'ct-w-off');
      if (c) s += F('M' + x + ' 50 V190 H500');
    });
    s += P('M150 190 H500', imp ? 'ct-w-live' : 'ct-w-off');
    s += dot(270, 190) + dot(390, 190);
    // tuljava
    s += P('M500 190 V205', imp ? 'ct-w-live' : 'ct-w-off');
    s += '<rect class="ct-coil" x="480" y="205" width="40" height="44" fill="' + (imp ? 'var(--glow)' : 'var(--panel)') + '"/>';
    s += T(530, 212, 'A1', 'ct-tm') + T(530, 258, 'A2', 'ct-tm');
    s += P('M500 249 V300', imp ? 'ct-w-n' : 'ct-w-offn');
    if (imp) s += F('M500 190 V205') + F('M500 249 V300 H-10 V205');
    // mehanska povezava
    // mehanska povezava: od tuljave do kontakta (elektromagnet premakne kontakt)
    var cx = lit ? 700 : 714;
    s += '<path d="M520 227 H655 V122 H' + (cx - 3) + '" stroke="var(--accent)" stroke-width="3" stroke-dasharray="8 6" fill="none"/>';
    s += '<circle cx="' + cx + '" cy="122" r="5" fill="var(--accent)"/>';
    s += T(468, 234, 'elektromagnet', 'ct-tag', 'end');
    // krmiljeni krog
    s += '<rect class="ct-box" x="600" y="64" width="230" height="224" rx="10"/>' + T(735, 256, 'krmiljeni', 'ct-tag') + T(735, 276, 'krog', 'ct-tag');
    s += P('M700 50 V95', 'ct-w-live') + dot(700, 50) + term(700, 95) + term(700, 150);
    var ex = lit ? 700 : 728, ey = lit ? 150 : 140;
    s += '<line class="ct-blade" stroke="var(--live)" x1="700" y1="95" x2="' + ex + '" y2="' + ey + '"/>';
    s += T(722, 108, 'kontakt', 'ct-tag');
    s += P('M700 150 V184', lit ? 'ct-w-live' : 'ct-w-off') + lamp(700, 210, lit, null) + P('M700 236 V300', lit ? 'ct-w-n' : 'ct-w-offn');
    s += T(740, 218, 'E1', 'ct-t');
    if (lit) s += F('M700 50 V184') + F('M700 236 V300 H-10 V205');
    svg.innerHTML = o + '<g transform="translate(50 0)">' + s + '</g>';

    $('chip').textContent = lit ? 'Svetilka sveti' : 'Svetilka ne sveti';
    $('status').textContent = imp
      ? 'Tipkalo T' + (st.pressed + 1) + ' je pritisnjeno: skozi tuljavo teče kratek impulz in rele preklopi kontakt.'
      : (st.count === 0 ? 'Pritisni katerokoli tipkalo.'
         : 'Tipkalo je spuščeno, tuljava je brez toka. Kontakt ostane ' + (lit ? 'sklenjen – svetilka sveti' : 'odprt – svetilka ne sveti') + ' do naslednjega impulza.');
    $('tbody').innerHTML = '<tr><td>Tuljava (A1–A2)</td><td>' + (imp ? 'impulz' : 'brez toka') + '</td></tr>'
      + '<tr><td>Kontakt releja</td><td>' + (lit ? 'sklenjen' : 'odprt') + '</td></tr>'
      + '<tr><td>Število impulzov</td><td class="ct-num">' + st.count + '</td></tr>';
    $('note').textContent = 'Tipkala so vezana vzporedno. Zaščitni vodnik PE ni narisan. Oznake priključkov se med proizvajalci lahko razlikujejo.';
    document.querySelectorAll('[data-t]').forEach(function (b) { b.disabled = imp; });
  }
  document.querySelectorAll('[data-t]').forEach(function (b) {
    b.addEventListener('click', function () {
      if (st.pressed >= 0) return;
      st.pressed = +b.dataset.t; st.count++; st.contact ^= 1; render();
      setTimeout(function () { st.pressed = -1; render(); b.focus(); }, reduce ? 900 : 900);
    });
  });
  pauseBtn();
  render();
''')
k=open('/home/claude/npi-animacije/krizna-vezava.html').read().replace('min-width: 600px','min-width: 700px')
open('/home/claude/npi-animacije/krizna-vezava.html','w').write(k)
print('ok')

# ---------------------------------------------------------------- TRIFAZNI SISTEM
LEG3 = ('<span><b style="background:#7a4a1e"></b>L1 (rjav, polna črta)</span>'
        '<span><b style="background:repeating-linear-gradient(90deg,#1b1e28 0 8px,transparent 8px 12px)"></b>L2 (črn, črtkano)</span>'
        '<span><b style="background:repeating-linear-gradient(90deg,#6b6b6b 0 3px,transparent 3px 7px)"></b>L3 (siv, pikčasto)</span>'
        '<span><b style="background:var(--accent)"></b>medfazna U12</span>')
page('trifazni-sistem.html', 'Trifazni izmenični sistem – animacija', 'Trifazni izmenični sistem',
 'Trije kazalci se vrtijo skupaj, zamaknjeni za 120°. Desno vidiš, kako se iz njih rišejo tri sinusne napetosti.',
 '0 0 900 380', 'Levo trije vrteči se kazalci faznih napetosti, zamaknjeni za 120 stopinj; desno časovni potek treh sinusnih napetosti s kazalcem trenutnega kota',
 '''
        <button class="ct-btn" type="button" id="back">− 15°</button>
        <button class="ct-btn" type="button" id="fwd">+ 15°</button>
        <button class="ct-btn" type="button" id="u12" aria-pressed="false">Pokaži medfazno U12</button>''',
 '''<table><thead><tr><th>Napetost</th><th>Trenutna vrednost</th></tr></thead><tbody id="tbody"></tbody></table>''', LEG3, r'''
  var UF = 230, UH = UF * Math.SQRT2;            // fazna efektivna 230 V, temenska ≈ 325 V
  var ang = 90, show12 = false;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var playing = !reduce, last = null;
  var CX = 170, CY = 190, R = 95;                // kazalci in graf v enakem merilu: 325 V -> 95 px
  var GX = 360, GW = 510, GY = 190, GS = R / UH;  // zato vodoravne projekcije zadenejo krivulje
  var COL = ['#7a4a1e', '#1b1e28', '#6b6b6b'], DASH = ['', '10 6', '3 5'];
  function u(k, a) { return UH * Math.sin((a - 120 * k) * Math.PI / 180); }
  function curve(fn, col, dash, w) {
    var d = '';
    for (var x = 0; x <= 360; x += 4) d += (x ? 'L' : 'M') + (GX + x / 360 * GW).toFixed(1) + ' ' + (GY - fn(x) * GS).toFixed(1);
    return '<path d="' + d + '" fill="none" stroke="' + col + '" stroke-width="' + (w || 3.5) + '"' + (dash ? ' stroke-dasharray="' + dash + '"' : '') + '/>';
  }
  function arrow(x1, y1, x2, y2, col, dash, w) {
    var a = Math.atan2(y2 - y1, x2 - x1), h = 14;
    var p1 = [x2 - h * Math.cos(a - 0.4), y2 - h * Math.sin(a - 0.4)], p2 = [x2 - h * Math.cos(a + 0.4), y2 - h * Math.sin(a + 0.4)];
    return '<line x1="' + x1 + '" y1="' + y1 + '" x2="' + x2.toFixed(1) + '" y2="' + y2.toFixed(1) + '" stroke="' + col + '" stroke-width="' + (w || 4) + '"' + (dash ? ' stroke-dasharray="' + dash + '"' : '') + '/>'
      + '<path d="M' + x2.toFixed(1) + ' ' + y2.toFixed(1) + ' L' + p1[0].toFixed(1) + ' ' + p1[1].toFixed(1) + ' L' + p2[0].toFixed(1) + ' ' + p2[1].toFixed(1) + 'Z" fill="' + col + '"/>';
  }
  function fmtV(v) { var r = Math.round(v); return (r > 0 ? '+' : (r < 0 ? '−' : '')) + Math.abs(r) + ' V'; }
  function render() {
    var a = ((ang % 360) + 360) % 360, s = '';
    // kazalci
    s += '<circle cx="' + CX + '" cy="' + CY + '" r="' + R + '" fill="none" stroke="var(--border)" stroke-width="2"/>';
    s += '<line x1="' + (CX - R - 12) + '" y1="' + CY + '" x2="' + (CX + R + 12) + '" y2="' + CY + '" stroke="var(--border)" stroke-width="1.5"/>';
    var tips = [];
    for (var k = 0; k < 3; k++) {
      var t = (a - 120 * k) * Math.PI / 180, x = CX + R * Math.cos(t), y = CY - R * Math.sin(t);
      tips.push([x, y]);
      s += '<line x1="' + x.toFixed(1) + '" y1="' + y.toFixed(1) + '" x2="' + GX + '" y2="' + y.toFixed(1) + '" stroke="' + COL[k] + '" stroke-width="1.2" stroke-dasharray="2 5" opacity=".6"/>';
      s += arrow(CX, CY, x, y, COL[k], DASH[k] ? '' : '', 4.5);
      var lx = CX + (R + 24) * Math.cos(t), ly = CY - (R + 24) * Math.sin(t) + 7;
      s += T(lx.toFixed(1), ly.toFixed(1), 'U' + (k + 1) + 'N', 'ct-tm', 'middle');
    }
    if (show12) s += arrow(tips[1][0], tips[1][1], tips[0][0], tips[0][1], 'var(--accent)', '', 4);
    s += '<circle cx="' + CX + '" cy="' + CY + '" r="5" fill="var(--ink)"/>';
    // 120° lok med U1N in U2N
    var t0 = a * Math.PI / 180, t1 = (a - 120) * Math.PI / 180, rr = 42;
    s += '<path d="M' + (CX + rr * Math.cos(t0)).toFixed(1) + ' ' + (CY - rr * Math.sin(t0)).toFixed(1) + ' A' + rr + ' ' + rr + ' 0 0 1 ' + (CX + rr * Math.cos(t1)).toFixed(1) + ' ' + (CY - rr * Math.sin(t1)).toFixed(1) + '" fill="none" stroke="var(--muted)" stroke-width="2"/>';
    var tm = (a - 60) * Math.PI / 180;
    s += T((CX + 66 * Math.cos(tm)).toFixed(1), (CY - 66 * Math.sin(tm) + 6).toFixed(1), '120°', 'ct-tag', 'middle');
    // graf
    s += '<line x1="' + GX + '" y1="' + GY + '" x2="' + (GX + GW) + '" y2="' + GY + '" stroke="var(--muted)" stroke-width="1.5"/>';
    [0, 90, 180, 270, 360].forEach(function (d) {
      var x = GX + d / 360 * GW;
      s += '<line x1="' + x + '" y1="' + (GY - 4) + '" x2="' + x + '" y2="' + (GY + 4) + '" stroke="var(--muted)" stroke-width="1.5"/>';
      s += T(x, 372, d + '°', 'ct-tag', 'middle');
    });
    for (k = 0; k < 3; k++) s += curve(function (x) { return u(k, x); }, COL[k], DASH[k]);
    if (show12) s += curve(function (x) { return u(0, x) - u(1, x); }, 'var(--accent)', '', 3);
    var cx = GX + a / 360 * GW;
    s += '<line x1="' + cx.toFixed(1) + '" y1="20" x2="' + cx.toFixed(1) + '" y2="355" stroke="var(--accent)" stroke-width="2"/>';
    for (k = 0; k < 3; k++) s += '<circle cx="' + cx.toFixed(1) + '" cy="' + (GY - u(k, a) * GS).toFixed(1) + '" r="6" fill="' + COL[k] + '" stroke="#fff" stroke-width="2"/>';
    s += T(GX + 4, 34, 'u', 'ct-tm') + T(GX + GW - 4, GY - 10, 'α', 'ct-tm', 'end');
    svg.innerHTML = s;

    var v = [u(0, a), u(1, a), u(2, a)], sum = v[0] + v[1] + v[2];
    var rows = '';
    for (k = 0; k < 3; k++) rows += '<tr><td>u' + (k + 1) + 'N (L' + (k + 1) + ')</td><td class="ct-num">' + fmtV(v[k]) + '</td></tr>';
    rows += '<tr class="ct-sum"><td>Vsota u1N + u2N + u3N</td><td class="ct-num">' + fmtV(Math.abs(sum) < 0.5 ? 0 : sum) + '</td></tr>';
    if (show12) rows += '<tr><td>u12 = u1N − u2N</td><td class="ct-num">' + fmtV(v[0] - v[1]) + '</td></tr>';
    $('tbody').innerHTML = rows;
    $('chip').textContent = 'α = ' + Math.round(a) + '°';
    $('status').textContent = show12
      ? 'Medfazna napetost U12 je razlika napetosti L1 in L2. Njena efektivna vrednost je √3 · 230 V ≈ 400 V.'
      : 'Fazne napetosti so zamaknjene za 120°. Vsota vseh treh je v vsakem trenutku 0 V.';
  }
  function frame(t) {
    if (!playing) { last = null; return; }
    if (last !== null) ang += (t - last) / 1000 * 45;   // 45° na sekundo (en obrat v 8 s)
    last = t; render(); requestAnimationFrame(frame);
  }
  function setPlay(p) {
    playing = p;
    $('pause').setAttribute('aria-pressed', p ? 'false' : 'true');
    $('pause').textContent = p ? 'Ustavi vrtenje' : 'Zaženi vrtenje';
    if (p) requestAnimationFrame(frame);
  }
  $('pause').addEventListener('click', function () { setPlay(!playing); });
  $('back').addEventListener('click', function () { setPlay(false); ang = Math.round((ang - 15) / 15) * 15; render(); });
  $('fwd').addEventListener('click', function () { setPlay(false); ang = Math.round((ang + 15) / 15) * 15; render(); });
  $('u12').addEventListener('click', function () { show12 = !show12; this.setAttribute('aria-pressed', show12 ? 'true' : 'false'); this.textContent = show12 ? 'Skrij medfazno U12' : 'Pokaži medfazno U12'; render(); });
  $('note').textContent = 'Fazna napetost 230 V (temenska ≈ 325 V). V resnici se kazalci zavrtijo 50-krat na sekundo – tu zelo počasi.';
  render(); setPlay(playing);
''')
t=open('/home/claude/npi-animacije/trifazni-sistem.html').read().replace('min-width: 600px','min-width: 720px')
open('/home/claude/npi-animacije/trifazni-sistem.html','w').write(t)
print('trifazni ok')
