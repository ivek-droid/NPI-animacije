import importlib.util, sys
spec = importlib.util.spec_from_file_location('l3', '/home/claude/npi-animacije/orodja/lekcije_pomocniki_in_ivep.py')
src = open('/home/claude/npi-animacije/orodja/lekcije_pomocniki_in_ivep.py').read().split('# ======================================================== SERIJSKA')[0]
exec(src)

def btn(url, label):
    return f'[et_pb_button button_url="{url}" url_new_window="on" button_text="{label}" module_class="pg-btn" _builder_version="4.27.9" custom_margin="0||12px||false|false"][/et_pb_button]'

kaj = H2 + '''Kaj je trifazni sistem</h2>
<p>Doma imaš v razdelilni omarici navadno tri varovalke – za vsako fazo eno. Zmogljivejše naprave, na primer električni štedilnik, so lahko priključene na vse tri faze.</p>
<p>Elektrarna ima trifazni generator. V njem se vrti magnet, okrog njega so tri navitja. Navitja so na obodu zamaknjena za 120°.</p>
<p>V vsakem navitju nastane izmenična napetost. Tri napetosti so med seboj zamaknjene za tretjino obrata – za 120°.</p>'''

vodniki = H2 + '''Vodniki in napetosti</h2>
<p>Vodnike, ki povezujejo začetke navitij trifaznega generatorja s porabniki, imenujemo linijski vodniki, označujemo pa jih z L1, L2 in L3.</p>
<p>Vodnik, ki povezuje zvezdišče trifaznega generatorja z zvezdiščem porabnikov, imenujemo nevtralni vodnik (starejše ime: ničelni vodnik), označujemo pa ga z N. Zvezdišče generatorjev elektrarn je ozemljeno in na potencialu 0 V, zato mu pravimo tudi ničlišče.</p>
<p>Napetosti med linijskimi vodniki in nevtralnim vodnikom imenujemo fazne napetosti, označujemo pa jih s parom indeksov, ki določata vodnika, med katerima deluje napetost (U1N, U2N in U3N).</p>
<p>Napetosti med linijskimi vodniki imenujemo medfazne napetosti, označujemo pa jih s parom indeksov, ki določata linijska vodnika, med katerima deluje medfazna napetost (U12, U23 in U31).</p>'''

vrednosti = box('cilj', 'V hišni napeljavi', '''<ul>
<li>fazna napetost U<sub>f</sub> = 230 V (med L in N),</li>
<li>medfazna napetost U = 400 V (med dvema L).</li>
</ul>
<p>Povezava: U = √3 · U<sub>f</sub> = 1,73 · 230 V ≈ 398 V ≈ 400 V.</p>''', '16px 0 0') + box('pozor', 'Ne zamenjaj', '<p>Fazna napetost (230 V) je med linijskim vodnikom in N. Medfazna napetost (400 V) je med dvema linijskima vodnikoma.</p>', '16px 0 0')

zvezda = H2 + '''Vezava v zvezdo in trikot</h2>
<p>Z medsebojno povezavo priključkov navitij generatorja U2, V2 in W2 v skupno točko (slika generatorja) dobimo zvezdno vezavo trifaznega generatorja. Taka vezava generatorja ali transformatorja je osnova elektroenergetskega sistema, ki je dostopen uporabnikom. Stično točko zvezdne vezave U2, V2 in W2 imenujemo zvezdišče. (Trikotno vezavo navitij generatorjev in transformatorjev uporabljamo v visokonapetostnih prenosnih sistemih.)</p>
<p>Podobno velja za vezavo trifaznega porabnika, s tem da pri porabnikih poleg zvezdne uporabljamo še trikotno vezavo, ki jo dobimo s povezavo priključkov W2 - U1, U2 - V1 ter V2 - W1</p>'''

porabniki = H2 + '''Priključitev porabnikov</h2>
<p><strong>Enofazne</strong> porabnike priključimo med en linijski vodnik in N. Imajo 230 V.</p>
<p><strong>Trifazne</strong> porabnike priključimo na L1, L2 in L3 – v zvezdo ali v trikot. Primera: trifazna peč (zvezda) in elektromotor (zvezda ali trikot).</p>'''

moc = H2 + '''Moč trifaznega porabnika</h2>
<p>Za zvezdo in trikot velja ista formula za navidezno moč:</p>
<p style="font-size:22px;font-weight:700">S = √3 · U · I</p>
<ul>
<li>U je medfazna napetost (400 V),</li>
<li>I je linijski tok (tok v vodniku L1, L2 ali L3).</li>
</ul>
<p>Delovna moč: P = S · cos φ. Jalova moč: Q = S · sin φ.</p>'''

primer = box('primer', 'Rešen primer', '''<p style="margin-top:0">Trifazna peč je vezana v zvezdo na 400 V. Linijski tok je 10 A. Grelniki so ohmski, zato je cos φ = 1. Kolikšna je moč peči? Kolikšna je napetost na enem grelniku?</p>
<ol class="pg-koraki">
<li><span><span class="pg-koraki__oznaka">Podatki</span>U = 400 V, I = 10 A, cos φ = 1, zvezda</span></li>
<li><span><span class="pg-koraki__oznaka">Iskano</span>S = ?, P = ?, U<sub>b</sub> = ?</span></li>
<li><span><span class="pg-koraki__oznaka">Formula</span>S = √3 · U · I</span></li>
<li><span><span class="pg-koraki__oznaka">Vstavim</span>S = √3 · 400 V · 10 A</span></li>
<li><span><span class="pg-koraki__oznaka">Izračunam</span>S ≈ 6928 VA ≈ 6,93 kVA</span></li>
<li><span><span class="pg-koraki__oznaka">Formula</span>P = S · cos φ</span></li>
<li><span><span class="pg-koraki__oznaka">Izračunam</span>P = 6,93 kVA · 1 = 6,93 kW</span></li>
<li><span><span class="pg-koraki__oznaka">Formula</span>U<sub>b</sub> = U / √3</span></li>
<li><span><span class="pg-koraki__oznaka">Izračunam</span>U<sub>b</sub> = 400 V / √3 ≈ 231 V</span></li>
<li><span><span class="pg-koraki__oznaka">Rezultat</span><span class="pg-rezultat">P ≈ 6,93 kW, U<sub>b</sub> ≈ 231 V</span></span></li>
<li><span><span class="pg-koraki__oznaka">Preverim</span>V · A = VA. Na grelniku v zvezdi je fazna napetost, približno 230 V.</span></li>
</ol>''') + box('pozor', 'Pogosta napaka', '<p>V formulo vstaviš fazno napetost 230 V namesto medfazne 400 V. Ali pa pozabiš na √3.</p>', '16px 0 0')

matura = box('matura', 'Vaje in matura', '<p>Reši nalogi in maturitetno nalogo. Vsaka se odpre v novem oknu.</p>')
matura_btns = (btn('https://npi.splet.arnes.si/files/2025/10/20251006_122920-scaled.jpg', 'Primer s table (1/237)')
             + btn('https://npi.splet.arnes.si/files/2023/12/1-in-2-237.pdf', 'Nalogi 1 in 2 (237)')
             + btn('https://npi.splet.arnes.si/files/2023/12/jesenski-2021-10-prvi-del.jpg', 'Matura, jesenski rok 2021 – 10 (1. del)'))

preveri = H2 + 'Preveri se</h2>' \
    + q('1. Za koliko stopinj so fazne napetosti med seboj zamaknjene?', 'Za 120°.') \
    + q('2. Kolikšni sta fazna in medfazna napetost v hišni napeljavi?', 'Fazna 230 V, medfazna 400 V (√3 · 230 V ≈ 400 V).') \
    + q('3. Kateri priključki navitij so povezani v zvezdišču?', 'U2, V2 in W2.') \
    + q('4. Kako povežeš navitja v trikot?', 'W2 z U1, U2 z V1 in V2 z W1.')
kratko = box('cilj', 'Na kratko', ul(['Tri napetosti, zamaknjene za 120°.', 'L1, L2, L3 = linijski vodniki, N = nevtralni vodnik.', 'Fazna napetost 230 V, medfazna 400 V.', 'U = √3 · U<sub>f</sub>.', 'S = √3 · U · I (zvezda in trikot).']))

out = sec(
    row(col('4_4', text(cilj('Trifazni izmenični sistem', ['povedati, kako nastanejo tri fazne napetosti in zakaj so zamaknjene za 120°,', 'ločiti fazno in medfazno napetost (230 V in 400 V),', 'povezati navitja v zvezdo ali trikot,', 'izračunati moč trifaznega porabnika.']))))
  + row(col('1_2', text(kaj)) + col('1_2', img('2023/12/3f-G.png', 'Trifazni generator: vrteči se magnet in tri navitja U1–U2, V1–V2, W1–W2, zamaknjena za 120°. Linijski vodniki L1, L2, L3, nevtralni vodnik N in fazne napetosti U1N, U2N, U3N.', ' max_width="460px"')), '1_2,1_2')
  + row(col('1_2', text(vodniki)) + col('1_2', img('2023/12/graf-trih-faz.png', 'Graf treh faznih napetosti: tri sinusne krivulje, zamaknjene za 120°, od 0° do 360°.') + cap('Trifazna električna napeljava, faze so med seboj zamaknjene za 120°. Napetosti se določajo glede na skupni nevtralni vodnik.') + text(vrednosti)), '1_2,1_2')
  + row(col('1_2', text(zvezda)) + col('1_2', img('2023/12/3f-AM.png', 'Trifazni motor in priključna plošča: vezava v zvezdo (W2, U2, V2 povezani) in v trikot (W2–U1, U2–V1, V2–W1).', ' max_width="360px"')), '1_2,1_2')
  + row(col('1_2', text(porabniki)) + col('1_2', img('2023/12/trifazni-porabniki.png', 'Priključitev porabnikov: enofazni porabniki med L in N, trifazna peč v zvezdi in elektromotor v trikotu na L1, L2, L3.')), '1_2,1_2'))
out += sec(row(col('4_4', anim('trifazni-sistem.html', 'trifazni izmenični sistem', 'Ustavi vrtenje in s koraki po 15° opazuj trenutne vrednosti. Vklopi še medfazno napetost U12.', 780))), '#f5f3ef')
out += sec(
    row(col('1_2', text(moc) + img('2024/12/Posnetek-zaslona-2024-12-13-122039.png', 'Preglednica formul za vezavo v zvezdo in trikot: povezave med linijskimi in faznimi napetostmi ter tokovi in formula S = √3 · U · I.')) + col('1_2', text(primer)), '1_2,1_2')
  + row(col('4_4', text(matura) + matura_btns))
  + row(col('1_2', text(preveri)) + col('1_2', text(kratko)), '1_2,1_2'))
write('trifazni-sistem', out)
