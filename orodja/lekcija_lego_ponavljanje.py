# Generator: LEGO programiranje, vaja 4 »Ponavljanje« (osnutek, ni objavljeno)
exec(open('/home/claude/npi-animacije/orodja/lekcije_pomocniki_in_ivep.py').read())
# --- preverjanje števil (ustavi se ob neskladju)
T = 12.0; O = 17.6; PI = 3.14
NSQ = 40 / O; NTURN = PI * T / 4 / O
assert round(NSQ, 2) == 2.27 and round(NTURN, 2) == 0.54          # iz vaje 3
assert round(2.27 * O, 1) == 40.0
assert 4 * 90 == 360 and 8 == 4 + 4                              # kvadrat: 4 ponovitve; brez zanke 8 blokov
# šestkotnik, stranica 20 cm (rešen primer)
SIX = 20; REP6 = 360 // 60; assert REP6 == 6
n_vozi6 = SIX / O; assert round(n_vozi6, 2) == 1.14
s60 = PI * T * 60 / 360; assert round(s60, 2) == 6.28
n_zavoj6 = s60 / O; assert round(n_zavoj6, 2) == 0.36 and round(0.36 * O, 1) == 6.3
assert round(0.36 * O / (PI * T) * 360, 1) == 60.5   # kontrola: 0,36 → 60,5°
# trikotnik, stranica 30 cm (izziv)
TRI = 30; REP3 = 360 // 120; assert REP3 == 3
assert round(TRI / O, 2) == 1.70
s120 = PI * T * 120 / 360; assert round(s120, 2) == 12.56
assert round(s120 / O, 2) == 0.71
def dec(x, d=2): return f'{x:.{d}f}'.replace('.', ',')

kaj = H2 + 'Kaj je ponavljanje</h2>' + '''
<p>Pomisli na skakanje s kolebnico. Trener ti ne reče: »skoči, skoči, skoči …« desetkrat. Reče: »<strong>10-krat skoči</strong>.«</p>
<p>Tudi robotu lahko rečeš, naj nekaj ponovi. Napišeš eno navodilo in številko, kolikokrat naj ga izvede. Program je krajši in lažje ga popraviš.</p>'''
pravilo = box('cilj', 'Pravilo', '''<p style="margin-top:0">Blok <strong>repeat</strong> ima v sredini prostor za druge bloke. Robot jih izvede večkrat, kolikor je napisano na bloku.</p>
<ul>
<li>Številka pri »repeat« pove, <strong>kolikokrat</strong> se ponovi vsebina.</li>
<li>Ponovi se samo tisto, kar je <strong>znotraj</strong> bloka.</li>
<li>Bloki pod repeat se izvedejo šele, ko so vse ponovitve končane.</li>
</ul>''')

kvadrat0 = H2 + 'Kvadrat iz vaje 3</h2>\n' + '''<p>V vaji 3 si za kvadrat sestavil <strong>8 blokov</strong>: štirikrat vožnjo in štirikrat zavoj. Vsak par je enak.</p>
<p>Zdaj ga sestaviš z <strong>enim blokom repeat</strong> in dvema blokoma znotraj njega.</p>'''
sestavi = H2 + 'Sestavi program</h2>\n' + ol([
    'Odpri nov projekt. Na ploščadi je rumeni blok »when program starts«.',
    'Odpri paleto <strong>CONTROL</strong> (oranžna). Poišči blok <strong>»repeat 10«</strong> in ga povleci tik pod rumeni blok.',
    'Klikni na številko 10 in vpiši <strong>4</strong>.',
    'Iz palete MOVEMENT povleci blok <strong>»move forward for 1 rotations«</strong> v notranjost bloka repeat. Vpiši <strong>2.27</strong> (s piko).',
    'Pod njega, še vedno znotraj bloka repeat, povleci blok <strong>»move straight: 0 for 1 rotations«</strong>. Pri »straight« vpiši <strong>100</strong>, pri vrtljajih vrednost, ki si jo našel pri zavojih (okoli <strong>0.54</strong>).',
    'Preveri: oba bloka morata biti <strong>znotraj</strong> bloka repeat.'])
IMG = '2026/11/'
sl_rep = img(IMG + 'lego-repeat-10.png', 'Blok »repeat 10« iz palete CONTROL: oranžen blok z odprtim prostorom v sredini.', ' max_width="240px"') + cap('Blok repeat iz palete CONTROL. Bloke povleci v odprti prostor.')
zazeni = H2 + 'Preizkusi na robotu</h2>\n' + ol([
    'Robota postavi na tla. Označi začetno mesto s trakom. Okoli naj bo prosto vsaj 50 cm.',
    'Klikni desni gumb ▶ (prenos in zagon).',
    'Opazuj: robot prevozi štiri stranice in štirikrat zavije. Kje se ustavi? V katero smer gleda?',
    'Zamenjaj 4 z <strong>8</strong>. Zaženi. Robot naredi dva kroga. Ali je drugi krog natanko na prvem?',
    'Zamenjaj 4 z <strong>2</strong>. Kaj nariše robot?'])
napaka1 = box('pozor', 'Pogosta napaka', '<p>Bloka vožnje in zavoja sta <strong>pod</strong> blokom repeat, ne <strong>znotraj</strong> njega. Robot potem naredi eno stranico in en zavoj, ponovi pa ničesar.</p>\n<p>Blok repeat ima odprt prostor. Bloka povleci vanj, da ju obda.</p>') \
    + box('pozor', 'Robot ne pride natanko nazaj', '<p>Vsak zavoj ima majhno napako (vaja 3). Pri štirih ponovitvah se napake seštejejo, pri osmih še bolj. Zato je drugi krog malo zamaknjen.</p>', '16px 0 0')

primer = box('primer', 'Rešen primer', f'''<p style="margin-top:0">Robot naj prevozi pravilni šestkotnik s stranico 20 cm. Kolikokrat ponovimo vožnjo in zavoj, kolikšna sta vrtljaja vožnje in zavoja? T = 12 cm, o = 17,6 cm.</p>
<ol class="pg-koraki">
<li><span><span class="pg-koraki__oznaka">Podatki</span>stranica 20 cm, šest stranic, T = 12 cm, o = 17,6 cm</span></li>
<li><span><span class="pg-koraki__oznaka">Iskano</span>število ponovitev, vrtljaji vožnje, vrtljaji zavoja</span></li>
<li><span><span class="pg-koraki__oznaka">Formula</span>skupni zasuk je 360°, zato je ponovitev = 360° / kot zavoja</span></li>
<li><span><span class="pg-koraki__oznaka">Vstavim</span>kot zavoja = 360° / 6 = 60°, ponovitev = 6</span></li>
<li><span><span class="pg-koraki__oznaka">Vstavim</span>vožnja: n = 20 cm / 17,6 cm = {dec(n_vozi6)}</span></li>
<li><span><span class="pg-koraki__oznaka">Vstavim</span>pot kolesa pri zavoju 60°: s = π · T · 60° / 360° = 3,14 · 12 cm / 6 = {dec(s60)} cm</span></li>
<li><span><span class="pg-koraki__oznaka">Vstavim</span>zavoj: n = {dec(s60)} cm / 17,6 cm = {dec(n_zavoj6)}</span></li>
<li><span><span class="pg-koraki__oznaka">Rezultat</span><span class="pg-rezultat">repeat 6: vožnja 1,14 vrtljaja, zavoj 0,36 vrtljaja</span></span></li>
<li><span><span class="pg-koraki__oznaka">Preverim</span>6 · 60° = 360°. 0,36 · 17,6 cm = 6,3 cm, kar je blizu 6,28 cm. Ujema se.</span></li>
</ol>''') + box('pozor', 'Pogosta napaka', '<p>Robot zavije za <strong>zunanji kot</strong>, ne za notranji kot lika. Pri šestkotniku je notranji kot 120°, robot pa zavije za 60°. Če vstaviš 120°, naredi preveč zavit lik.</p>', '16px 0 0')
zakaj = H2 + 'Koliko ponovitev za zaprt lik?</h2>\n' \
    + '<p>Ko robot naredi poln krog in se vrne na začetek, se je skupaj zasukal za <strong>360°</strong>.</p>\n' \
    + '<p>Zato velja: <strong>število ponovitev = 360° / kot zavoja</strong>.</p>\n' \
    + '<p>Kvadrat: 360° / 90° = 4. Šestkotnik: 360° / 60° = 6. Trikotnik: 360° / 120° = 3.</p>\n' \
    + '<p>Pri zavoju na mestu je število vrtljajev za zavoj sorazmerno s kotom. Za 90° je 0,54 vrtljaja, za 60° je tretjino manj, za 120° pa tretjino več.</p>'

izziv = H2 + 'Izziv: enakostranični trikotnik</h2>\n<p>Robot naj prevozi trikotnik s stranico 30 cm.</p>\n' + ol([
    f'Število ponovitev: 360° / 120° = <strong>{REP3}</strong>. Robot zavije za <strong>120°</strong>, ne za 60°.',
    f'Vožnja: n = 30 cm / 17,6 cm ≈ <strong>{dec(TRI / O)}</strong>.',
    f'Zavoj za 120°: s = 3,14 · 12 cm · 120° / 360° = {dec(s120)} cm. n = {dec(s120)} cm / 17,6 cm ≈ <strong>{dec(s120 / O)}</strong>.',
    'Sestavi program: repeat 3, vožnja naprej, zavoj v desno. Zaženi.',
    'Izmeri, kje se robot ustavi, in popravi vrtljaje zavoja, dokler ni trikotnik zaprt.'])

anim_sec = anim('robot-ponavlja.html', 'ponavljanje', 'Nastavi število ponovitev in pritisni Zaženi. Poglej, kaj nariše robot in kateri blok se izvaja.', 780)

preveri = H2 + 'Preveri se</h2>' + q('1. Kaj naredi blok »repeat 5«?', 'Ponovi bloke, ki so znotraj njega, petkrat.') \
    + q('2. Robot naredi kvadrat z blokom »repeat 4«. Koliko ponovitev potrebuješ za dva kroga?', '8 ponovitev.') \
    + q('3. Koliko ponovitev za zaprt osemkotnik? Za kolikšen kot zavije robot?', '8 ponovitev. Kot zavoja je 360° / 8 = 45°.') \
    + q('4. Blok »move forward« je pod blokom repeat, ne znotraj. Kolikokrat ga robot izvede?', 'Enkrat, ko so vse ponovitve končane.')
kratko = box('cilj', 'Na kratko', ul([
    'Blok repeat ponovi bloke, ki so znotraj njega.',
    'Kvadrat: repeat 4, vožnja naprej 2,27 vrtljaja, zavoj v desno 0,54 vrtljaja.',
    'Število ponovitev za zaprt lik: 360° / kot zavoja.',
    'Robot zavije za zunanji kot lika.',
    'Pri več ponovitvah se majhne napake seštevajo.']))

out = sec(
    row(col('4_4', text(cilj('Ponavljanje', ['uporabiti blok repeat,', 'iz osmih blokov narediti tri,', 'izračunati število ponovitev za zaprt lik,', 'sestaviti program za šestkotnik in trikotnik.']))))
  + row(col('1_2', text(kaj)) + col('1_2', text(pravilo)), '1_2,1_2')
  + row(col('1_2', text(kvadrat0 + sestavi) + sl_rep) + col('1_2', text(zazeni)), '1_2,1_2')
  + row(col('1_2', text(zakaj)) + col('1_2', text(napaka1)), '1_2,1_2')
  + row(col('1_2', text(primer)) + col('1_2', text(izziv)), '1_2,1_2'))
out += sec(row(col('4_4', anim_sec)), '#f5f3ef')
out += sec(row(col('1_2', text(preveri)) + col('1_2', text(kratko)), '1_2,1_2'))
write('lego-ponavljanje', out)
