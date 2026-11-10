# Generator: LEGO programiranje, vaja 2 »Vožnja naravnost« (osnutek, ni objavljeno)
exec(open('/home/claude/npi-animacije/orodja/lekcije_pomocniki_in_ivep.py').read())
import math
# --- preverjanje števil (ustavi se ob neskladju)
D = 5.6                                   # premer kolesa v cm (napis na kolesu 25x28 in uporabnik)
O = math.pi * D
assert round(O, 1) == 17.6
assert round(3.14 * D, 1) == 17.6         # z π = 3,14
assert 60 / 20 == 3 and 3 * 20 == 60      # rešen primer (obseg 20 cm)
assert 4 * 15 == 60 and 90 / 15 == 6       # preveri se
N1M = 100 / 17.6
assert round(N1M, 2) == 5.68
IMG = '2026/11/'
def blk(name, alt, w='420px'): return img(IMG + name, alt, f' max_width="{w}"')

kaj = H2 + '''Kaj se zgodi pri enem vrtljaju</h2>
<p>Pomisli na kolo. Kolo se zavrti enkrat in kolo kolesa prevozi pot, ki je dolga toliko kot obod kolesa.</p>
<p>Tako je tudi pri robotu. Kolo robota se zavrti enkrat, robot pa se premakne naprej za en <strong>obseg kolesa</strong>. Obseg je dolžina črte okoli kolesa.</p>
<p>Zato lahko pot izračunaš. Vpišeš število vrtljajev, robot pa pelje naprej.</p>'''
pravilo = box('cilj', 'Pravilo', '''<p style="margin-top:0">Pot robota: <strong>s = n · o</strong></p>
<ul>
<li>s = pot v centimetrih (cm)</li>
<li>n = število vrtljajev kolesa</li>
<li>o = obseg kolesa v centimetrih (cm)</li>
</ul>
<p>Obseg izračunaš iz premera kolesa: <strong>o = π · d</strong>. Pri nas je π ≈ 3,14.</p>''')
program = H2 + 'Sestavi program</h2>\n' + ol([
    'Robot je povezan z računalnikom (vaja 1). Postavi ga na tla. Pred njim naj bo prosta pot vsaj 1 m.',
    'V EV3 Classroom odpri nov projekt. Na delovni površini je že rumeni blok »when program starts«.',
    'Klikni paleto MOVEMENT (roza).',
    'Povleci blok »move forward for 1 rotations« tik pod rumeni blok. Bloka se zaskočita.',
    'Zaženi program. Klikni rumeni blok.']) + '\n<p>Program ima samo dva bloka. Število <strong>1</strong> v bloku pomeni 1 vrtljaj kolesa.</p>'
meritev = H2 + 'Izmeri, koliko pelje en vrtljaj</h2>\n' + ol([
    'Na tla prilepi trak za začetek. Robota postavi tako, da se sprednji rob dotika traku.',
    'Zaženi program. Robot se ustavi.',
    'Izmeri pot od traku do sprednjega roba robota. Zapiši: <strong>1 vrtljaj = ___ cm</strong>.',
    'Ponovi meritev še dvakrat. Izračunaj povprečje treh meritev. To je obseg tvojega kolesa o.',
    'Izračunaj obseg še iz premera kolesa: d = 5,6 cm.']) + '''
<p>o = π · d = 3,14 · 5,6 cm ≈ <strong>17,6 cm</strong></p>
<p>Izmerjena in izračunana vrednost se morata približno ujemati.</p>'''
napaka1 = box('pozor', 'Pogosta napaka', '<p>Pot izmeriš od enega dela robota, na koncu pa do drugega. Merjenje začneš in končaš na isti točki robota.</p>') \
    + box('pozor', 'Robot se ne premakne ali se vrti', '<p>Motorja morata biti priključena na vrati B (levo kolo) in C (desno kolo). Preveri kabla. V paleti MOVEMENT je tudi blok »set movement motors to B and C«.</p>', '16px 0 0')
primer = box('primer', 'Rešen primer', '''<p style="margin-top:0">Drug robot ima obseg kolesa 20 cm. Pelje naj 60 cm. Koliko vrtljajev vpišeš v blok?</p>
<ol class="pg-koraki">
<li><span><span class="pg-koraki__oznaka">Podatki</span>o = 20 cm, s = 60 cm</span></li>
<li><span><span class="pg-koraki__oznaka">Iskano</span>število vrtljajev n = ?</span></li>
<li><span><span class="pg-koraki__oznaka">Formula</span>s = n · o, torej n = s / o</span></li>
<li><span><span class="pg-koraki__oznaka">Vstavim</span>n = 60 cm / 20 cm</span></li>
<li><span><span class="pg-koraki__oznaka">Rezultat</span><span class="pg-rezultat">n = 3 vrtljaji</span></span></li>
<li><span><span class="pg-koraki__oznaka">Preverim</span>3 · 20 cm = 60 cm. Ujema se.</span></li>
</ol>''') + box('pozor', 'Pogosta napaka', '<p>Deliš obratno: n = o / s. Rezultat bi bil 0,33 vrtljaja, kar je očitno premalo. Če računaš v metrih, pretvori vse v isto enoto.</p>', '16px 0 0')
izziv = H2 + 'Izziv: 1 meter</h2>\n<p>Tvoj robot naj pelje natanko 1 m (100 cm).</p>\n' + ol([
    f'Izračunaj število vrtljajev: n = s / o = 100 cm / 17,6 cm ≈ <strong>{str(round(N1M, 2)).replace(".", ",")}</strong>.',
    'V blok vpiši to število z decimalno piko: 5.68. Vejica ni dovoljena.',
    'Zaženi program in izmeri pot. Za koliko cm si zgrešil?',
    'Popravi število vrtljajev in poskusi znova.'])
anim_sec = anim('robot-vozi-naravnost.html', 'koliko pelje robot', 'Nastavi število vrtljajev in obseg kolesa. Pritisni Zaženi in opazuj, kam pride robot.', 660)
preveri = H2 + 'Preveri se</h2>' + q('1. Obseg kolesa je 15 cm. Koliko pelje robot pri 4 vrtljajih?', '4 · 15 cm = 60 cm.') \
    + q('2. Obseg kolesa je 15 cm. Koliko vrtljajev potrebuje za 90 cm?', '90 cm / 15 cm = 6 vrtljajev.') \
    + q('3. V blok namesto 1 vpišeš 2. Kaj se zgodi?', 'Robot pelje dvakrat dlje, ker se kolo zavrti dvakrat.')
kratko = box('cilj', 'Na kratko', ul(['Program: »when program starts« in »move forward for … rotations«.', 'En vrtljaj kolesa = en obseg kolesa.', 's = n · o, n = s / o.', 'Obseg kolesa: o = π · d ≈ 17,6 cm (d = 5,6 cm).', 'Vedno izmeri in popravi.']))
out = sec(
    row(col('4_4', text(cilj('Vožnja naravnost', ['sestaviti program z blokoma »when program starts« in »move forward«,', 'spremeniti število vrtljajev koles,', 'izmeriti, koliko pelje robot pri enem vrtljaju,', 'izračunati, koliko vrtljajev potrebuje za izbrano pot.']))))
  + row(col('1_2', text(kaj)) + col('1_2', text(pravilo)), '1_2,1_2')
  + row(col('1_2', text(program)) + col('1_2', blk('lego-when-program-starts.png', 'Blok »when program starts« (rumen): začetek programa.', '300px') + cap('Blok iz palete EVENTS.') + blk('lego-move-forward.png', 'Blok »move forward for 1 rotations« (roza): vožnja naprej za 1 vrtljaj.', '420px') + cap('Blok iz palete MOVEMENT.')), '1_2,1_2')
  + row(col('1_2', text(meritev)) + col('1_2', text(napaka1)), '1_2,1_2')
  + row(col('1_2', text(H2 + 'Koliko vrtljajev za dano pot?</h2>\n<p>Če poznaš obseg kolesa, lahko vrtljaje izračunaš. Ne rabiš ugibati.</p>')) + col('1_2', text(primer)), '1_2,1_2')
  + row(col('4_4', text(izziv))))
out += sec(row(col('4_4', anim_sec)), '#f5f3ef')
out += sec(row(col('1_2', text(preveri)) + col('1_2', text(kratko)), '1_2,1_2'))
write('lego-vozi-naravnost', out)
