# Generator: LEGO programiranje, vaja 3 »Zavoji« (osnutek, ni objavljeno)
exec(open('/home/claude/npi-animacije/orodja/lekcije_pomocniki_in_ivep.py').read())
import math
# --- preverjanje števil (ustavi se ob neskladju)
T = 12.0                      # razmak koles v cm (uporabnik, 11. 11. 2026: sredina do sredine, kolesa razmaknjena na 12 cm)
D = 5.6; O = 17.6             # premer kolesa in obseg (kot v vaji 2: 3,14 · 5,6 = 17,6)
PI = 3.14
assert round(PI * D, 1) == O
S90 = PI * T / 4              # pot vsakega kolesa pri zasuku za 90° na mestu = četrtina kroga s premerom T
assert round(S90, 2) == 9.42
N90 = S90 / O
assert round(N90, 2) == 0.54 and round(N90, 3) == 0.535
assert round(0.54 * O, 1) == 9.5                 # preverjanje: 0,54 · 17,6 = 9,5 cm
assert round(0.54 * O / (PI * T) * 360) == 91     # izračunani zasuk pri 0,54 (animacija: 91°)
assert round(0.5 * O / (PI * T) * 360) == 84      # pri 0,5 vrtljaja (animacija: 84°)
assert round(0.54 * 360) == 194                   # stopinje kolesa pri 0,54 vrtljaja (meritev uporabnika: B 194°/195°)
assert round(0.5 * 360) == 180                    # meritev: B +180°, C −180°
SQ = 40.0
NSQ = SQ / O
assert round(NSQ, 2) == 2.27                      # kvadrat, stranica 40 cm
assert round(2.27 * O, 1) == 40.0
assert round(2 * PI * (T / 2), 2) == round(PI * T, 2) == 37.68   # 2 · π · r z r = T/2 je π · T
assert 4 * 90 == 360 and 4 * 3 == 12              # preveri se / izziv
IMG = '2026/11/'
def blk(name, alt, w='420px'): return img(IMG + name, alt, f' max_width="{w}"')
def dec(x, d=2): return f'{x:.{d}f}'.replace('.', ',')

kaj = H2 + 'Kaj je zavoj na mestu</h2>' + '''
<p>Pomisli na bager na gosenicah. Ko se obrne na mestu, se ena goseniča vrti naprej, druga nazaj. Bager se zasuče okoli svoje sredine.</p>
<p>Tako zavije tudi tvoj robot. Eno kolo se vrti naprej, drugo nazaj. Robot ostane na istem mestu, spremeni pa smer.</p>'''
pravilo = box('cilj', 'Pravilo', '''<p style="margin-top:0">Zavoj nastaviš v bloku <strong>move straight … for … rotations</strong> s številko pri »straight«:</p>
<ul>
<li><strong>100</strong>: zavoj v desno (right: 100),</li>
<li><strong>−100</strong>: zavoj v levo (left: −100),</li>
<li><strong>0</strong>: vožnja naravnost (straight: 0).</li>
</ul>
<p>Število vrtljajev pove, koliko se zavrti vsako kolo. Več vrtljajev pomeni večji zasuk.</p>''')

blok = H2 + 'Blok za zavijanje</h2>\n' + ol([
    'Odpri paleto MOVEMENT (roza).',
    'Poišči blok <strong>»move straight: 0 for 1 rotations«</strong>. To je drugi blok v paleti. Prvi blok (»move forward«) je za vožnjo naravnost iz vaje 2.',
    'Povleci ga tik pod rumeni blok »when program starts«.',
    'Klikni na polje <strong>»straight: 0«</strong>. Odpre se kolo smeri.',
    'Vpiši <strong>100</strong>. V polju piše »right: 100«. Puščica na kolesu se premakne.',
    'V polje za vrtljaje vpiši <strong>0.5</strong>. Uporabi piko, ne vejice.'])
sl_blok = blk('lego-move-steering.png', 'Blok »move straight: 0 for 1 rotations« iz palete MOVEMENT.', '420px') + cap('Blok za vožnjo s smerjo. Pri »straight: 0« robot vozi naravnost.') \
    + blk('lego-kolo-smeri.png', 'Kolo smeri: puščica kaže, v katero smer zavije robot. Na sliki je nastavljeno »right: 100«.', '240px') + cap('Kolo smeri pri vrednosti 100.')

prog = H2 + 'Prvi zavoj</h2>\n' + ol([
    'Robota postavi na tla. Okoli njega naj bo prosto vsaj 20 cm na vse strani.',
    'Program naj ima dva bloka: »when program starts« in »move right: 100 for 0.5 rotations«.',
    'Klikni desni gumb ▶ (prenos in zagon). Robot se zasuče na mestu v desno.',
    'Poglej vrata B in C. Pri vratih B piše okoli +180°, pri vratih C okoli −180°. Kolesi sta se vrteli v nasprotnih smereh.',
    'Poglej še vrata 2 (žiroskop). Ob vsakem zagonu programa se postavi na 0. Po zavoju kaže zasuk robota v stopinjah: pri zavoju v desno plus, pri zavoju v levo minus. Pri 0.5 vrtljaja kaže okoli 84°.',
    'Zamenjaj 100 z −100. Robot zavije v levo. Števci B in C imata zdaj obratna predznaka, žiroskop kaže minus.'])
sl_prog = blk('lego-move-right-100.png', 'Blok »move right: 100 for 0.54 rotations«.', '420px') + cap('Primer bloka za zavoj v desno.')

poskus = H2 + 'Poskusi: koliko vrtljajev za pravi kot?</h2>\n' + ol([
    'Na tla prilepi dva trakova pod pravim kotom. Uporabi list A4 kot šablono: oba trakova naj tečeta ob dveh sosednjih robovih lista.',
    'Robota postavi tako, da stoji ob prvem traku in gleda vzdolž njega.',
    'Zaženi program z <strong>0.5</strong> vrtljaja. Poglej: ali se robot zasuče manj ali več kot za pravi kot?',
    'Poskusi z <strong>0.54</strong> vrtljaja. Poglej, ali stoji robot zdaj vzdolž drugega traku. Žiroskop pri vratih 2 kaže okoli 90°.',
    'Po potrebi popravljaj število: 0.5, 0.52, 0.54, 0.56, 0.6. Izberi vrednost, pri kateri je zasuk najbolj podoben pravemu kotu.',
    'Zapiši: <strong>moj robot za pravi kot: ___ vrtljaja</strong>.',
    'Isto preveri še za zavoj v levo (−100).'])
napaka1 = box('pozor', 'Pogosta napaka', '<p>V blok vpišeš 90, ker želiš 90 stopinj. Blok pa pričakuje <strong>vrtljaje kolesa</strong>, ne stopinj robota. Robot bi se vrtel 90 vrtljajev. Pravi kot dobiš pri približno 0,54 vrtljaja.</p>') \
    + box('pozor', 'Robot ne zavije natanko', '<p>Zasuk se lahko od poskusa do poskusa malo razlikuje, na primer zaradi podlage. Zato vedno izmeri in popravi, tako kot pri vožnji naravnost.</p>', '16px 0 0')

primer = box('primer', 'Rešen primer', f'''<p style="margin-top:0">Razmak med kolesoma je T = 12 cm, obseg kolesa o = 17,6 cm. Koliko vrtljajev potrebuje vsako kolo za zasuk robota za 90°?</p>
<ol class="pg-koraki">
<li><span><span class="pg-koraki__oznaka">Podatki</span>T = 12 cm, o = 17,6 cm, zasuk 90° (četrtina kroga)</span></li>
<li><span><span class="pg-koraki__oznaka">Iskano</span>število vrtljajev n = ?</span></li>
<li><span><span class="pg-koraki__oznaka">Formula</span>pot kolesa s = π · T / 4, n = s / o</span></li>
<li><span><span class="pg-koraki__oznaka">Vstavim</span>s = 3,14 · 12 cm / 4 = {dec(S90)} cm</span></li>
<li><span><span class="pg-koraki__oznaka">Vstavim</span>n = {dec(S90)} cm / 17,6 cm = {dec(N90, 3)}</span></li>
<li><span><span class="pg-koraki__oznaka">Rezultat</span><span class="pg-rezultat">n ≈ 0,54 vrtljaja</span></span></li>
<li><span><span class="pg-koraki__oznaka">Preverim</span>0,54 · 17,6 cm = 9,5 cm. To je približno {dec(S90, 1)} cm. Ujema se.</span></li>
</ol>''') + box('pozor', 'Pogosta napaka', '<p>Za T vstaviš premer kolesa (5,6 cm) namesto razmaka med kolesoma (12 cm). Razmak izmeriš od sredine enega do sredine drugega kolesa.</p>', '16px 0 0')
zakaj = H2 + 'Zakaj ravno četrtina kroga?</h2>\n' \
    + '<p>Obseg kroga že poznaš: o = 2 · π · r. Pazi, kaj je tukaj r.</p>\n' \
    + '<p>Robot se zasuče okoli točke na sredini med kolesoma. Vsako kolo je od te točke oddaljeno T / 2. To je polmer: <strong>r = T / 2</strong>, ne T.</p>\n' \
    + '<p>Vstavi v obrazec: 2 · π · T / 2 = π · T. Dvojki se pokrajšata. Vsako kolo opiše krog s premerom T in obsegom <strong>π · T</strong>.</p>\n' \
    + '<p>Zasuk za 90° je četrtina obrata. Pot kolesa je zato četrtina kroga: <strong>s = π · T / 4</strong>.</p>\n' \
    + '<p>Račun ti da začetno vrednost. Pravi robot se lahko malo razlikuje, zato jo vedno preveri s poskusom.</p>' \
    + blk('lego-zavoj-krog.png', 'Pogled od zgoraj: robot z dvema kolesoma na razmaku T = 12 cm. Okoli središča med kolesoma je krog s premerom T in polmerom r = T / 2. Obe kolesi pri zasuku za 90° prepotujeta četrtino tega kroga.', '460px') \
    + cap('Robot od zgoraj. Debela črta je pot vsakega kolesa pri zasuku za 90°: četrtina kroga s premerom T.')

izziv = H2 + 'Izziv: kvadrat s stranico 40 cm</h2>\n<p>Robot naj prevozi kvadrat in se vrne na začetek.</p>\n' + ol([
    f'Stranica: 40 cm. Število vrtljajev za vožnjo: n = 40 cm / 17,6 cm ≈ <strong>{dec(NSQ)}</strong>. Vpiši ga v blok »move forward« s piko (2.27).',
    'Zavoj: uporabi vrednost, ki si jo našel pri poskusu (okoli 0.54) z blokom »move right: 100«.',
    'Sestavi program: štirikrat zapored vožnja naravnost in zavoj. Skupaj je 8 blokov pod rumenim blokom.',
    'Robota postavi na začetek. Označi mesto s trakom. Zaženi program.',
    'Poglej, kje se robot ustavi. Za koliko cm je zgrešil začetek? V katero smer gleda?'])
napaka2 = box('pozor', 'Zakaj robot ne pride natančno nazaj?', '<p>Vsak zavoj se zasuče malo preveč ali malo premalo. Pri štirih zavojih se napake seštejejo. Če je vsak zavoj zgrešil za 3°, je po štirih zavojih napaka že 12°.</p>')

anim_sec = anim('robot-zavija.html', 'zasuk robota', 'Nastavi število vrtljajev in smer. Pritisni Zaženi in opazuj, za koliko stopinj se zasuče robot.', 740)

preveri = H2 + 'Preveri se</h2>' + q('1. Kaj naredi blok »move right: 100 for 0.5 rotations«?', 'Robot se zasuče na mestu v desno. Eno kolo se vrti naprej, drugo nazaj. Vsako kolo se zavrti pol vrtljaja.') \
    + q('2. Kolikšen del kroga je zasuk za 90°?', 'Četrtina kroga.') \
    + q('3. Robot štirikrat zavije za 90° in vmes vozi naravnost. Za koliko stopinj se zasuče na koncu, če zavija natančno?', 'Za 4 · 90° = 360°. To je poln obrat, robot gleda v isto smer kot na začetku.') \
    + q('4. Zakaj robot po štirih zavojih ni natančno na začetku?', 'Vsak zavoj ima majhno napako. Napake se seštejejo.')
kratko = box('cilj', 'Na kratko', ul([
    'Blok: »move straight: 100 for … rotations« (desno), −100 (levo).',
    'Pri zavoju na mestu se kolesi vrtita v nasprotnih smereh.',
    'Za 90° je pot vsakega kolesa četrtina kroga: s = π · T / 4.',
    'n = s / o ≈ 0,54 vrtljaja (T = 12 cm, o = 17,6 cm).',
    'Žiroskop (vrata 2) se ob zagonu programa postavi na 0 in po zavoju kaže zasuk v stopinjah.',
    'Vedno izmeri in popravi.']))

out = sec(
    row(col('4_4', text(cilj('Zavoji', ['zasukati robota na mestu v levo in desno,', 'nastaviti smer zavoja v bloku,', 'izračunati število vrtljajev za zasuk 90°,', 'sestaviti program za kvadrat.']))))
  + row(col('1_2', text(kaj)) + col('1_2', text(pravilo)), '1_2,1_2')
  + row(col('1_2', text(blok)) + col('1_2', sl_blok), '1_2,1_2')
  + row(col('1_2', text(prog)) + col('1_2', sl_prog), '1_2,1_2')
  + row(col('1_2', text(poskus)) + col('1_2', text(napaka1)), '1_2,1_2')
  + row(col('1_2', text(zakaj)) + col('1_2', text(primer)), '1_2,1_2')
  + row(col('1_2', text(izziv)) + col('1_2', text(napaka2)), '1_2,1_2'))
out += sec(row(col('4_4', anim_sec)), '#f5f3ef')
out += sec(row(col('1_2', text(preveri)) + col('1_2', text(kratko)), '1_2,1_2'))
write('lego-zavoji', out)
