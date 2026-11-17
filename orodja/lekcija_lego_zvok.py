# Generator: LEGO programiranje, vaja 5 »Zvok, zaslon in lučka« (osnutek, ni objavljeno)
exec(open('/home/claude/npi-animacije/orodja/lekcije_pomocniki_in_ivep.py').read())
# --- preverjanje števil (ustavi se ob neskladju)
O = 17.6
N40 = 40 / O
assert round(N40, 2) == 2.27 and round(2.27 * O, 1) == 40.0      # vožnja 40 cm (vaja 3)
def dec(x, d=2): return f'{x:.{d}f}'.replace('.', ',')
IMG = '2026/11/'

kaj = H2 + 'Kako robot »govori«</h2>\n' + '''<p>Tovornjak, ki vzvratno vozi, <strong>piska</strong>. Semafor <strong>sveti</strong> rdeče ali zeleno. Na tabli piše <strong>STOP</strong>. Vsak od njih ti na svoj način pove, kaj se dogaja.</p>
<p>Tudi robot ti lahko sporoča, kaj dela. Za to ima tri načine: zvok, napis na zaslonu in barvo lučke.</p>'''
pravilo = box('cilj', 'Pravilo', '<p style="margin-top:0">Robot sporoča s tremi bloki. Vsak je v svoji paleti:</p>' + ul([
    '<strong>zvok</strong>: paleta SOUND (svetlo vijolična),',
    '<strong>napis na zaslonu</strong>: paleta DISPLAY (temno vijolična),',
    '<strong>lučka</strong>: tudi paleta DISPLAY, blok »set status light to«.']) + '<p>Zvok ni dovolj. V hrupu ga ne slišiš. Zato mu dodamo še napis in lučko.</p>')

zvok = H2 + 'Zvok: pisk</h2>\n' + ol([
    'Odpri nov projekt. Odpri paleto <strong>SOUND</strong>.',
    'Povleci blok <strong>»play beep 60 for 0.2 seconds«</strong> tik pod rumeni blok.',
    'Klikni ▶ (desni gumb). Slišiš kratek pisk.',
    'Klikni na številko <strong>60</strong>. Odpre se klaviatura. Vsaka tipka je ena številka: <strong>C (60)</strong> je levo, <strong>C (72)</strong> desno. Klikni na tipko in zaženi.',
    'Poskusi tipko bolj levo in tipko bolj desno. <strong>Večja številka je višji ton.</strong> Poslušaj, ali drži.',
    'Številka 0.2 je dolžina pisanja v sekundah. Vpiši <strong>1</strong> in zaženi.'])
sl_beep = img(IMG + 'lego-play-beep.png', 'Blok »play beep 60 for 0.2 seconds« iz palete SOUND.', ' max_width="260px"') + cap('Blok za pisk. Prva številka je višina tona, druga je dolžina v sekundah.') \
    + img(IMG + 'lego-beep-klaviatura.png', 'Klaviatura, ki se odpre ob kliku na številko pri bloku play beep. Izbrana je tipka E (64). Levo je C (60), desno C (72).', ' max_width="340px"') + cap('Klaviatura: vsaka tipka je ena številka. Desno so višji toni.')
glasnost = H2 + 'Glasnost</h2>\n' + '''<p>Blok <strong>»set volume to 100 %«</strong> nastavi glasnost. Vstavi ga na začetek programa, pred prvi zvok.</p>
<p>Poskusi s 100 in z 30. V razredu je dovolj tudi 50.</p>'''
sl_vol = img(IMG + 'lego-set-volume.png', 'Blok »set volume to 100 %« iz palete SOUND.', ' max_width="200px"') + cap('Blok za glasnost.')

dva = H2 + 'Dva načina predvajanja zvoka</h2>\n' + '''<p>V paleti SOUND sta dva podobna bloka:</p>''' + ul([
    '<strong>play sound … until done</strong>: program <strong>počaka</strong>, da se zvok konča, šele nato izvede naslednji blok.',
    '<strong>start sound</strong>: zvok se <strong>zažene</strong>, program pa gre takoj naprej.']) + '<p>Razlika se sliši, kadar sledi še kak blok.</p>'
sl_until = img(IMG + 'lego-play-sound-until-done.png', 'Blok »play sound Communication / Hello until done« iz palete SOUND.', ' max_width="340px"') + cap('Program počaka, da se zvok konča.')
sl_start = img(IMG + 'lego-start-sound.png', 'Blok »start sound Communication / Hello« iz palete SOUND.', ' max_width="290px"') + cap('Program gre takoj naprej.')
poskus = H2 + 'Poskus: počakaj ali ne?</h2>\n' + ol([
    'Pod rumeni blok povleci <strong>»play sound Communication / Hello until done«</strong>.',
    'Pod njega povleci <strong>»play beep 60 for 0.2 seconds«</strong>. Zaženi in poslušaj.',
    'Zamenjaj prvi blok z <strong>»start sound Communication / Hello«</strong>. Zaženi in poslušaj.',
    'Kaj slišiš drugače? Kaj se zgodi s piskom?']) 
napaka_zaslon = box('pozor', 'Stari napis ostane', '<p>Nov napis <strong>ne pobriše</strong> starega. Pokrije samo toliko znakov, kolikor jih ima sam. Ostali znaki starega napisa ostanejo.</p>\n<p>Primer: najprej napišeš »avtomobilcek«, nato na isti vrstici »formentor«. Na zaslonu piše <strong>formentorcek</strong>: zadnje tri črke so ostale od prvega napisa.</p>\n<p>Zato pred novim napisom vedno uporabi <strong>»clear display«</strong>.</p>', '16px 0 0')
napaka1 = box('pozor', 'Pogosta napaka', '<p>Izbereš <strong>»start sound«</strong>, robot pa že vozi, preden se zvok konča. Če želiš zvok slišati do konca, izberi <strong>»play sound … until done«</strong>.</p>\n<p>Če zvoka ne slišiš, preveri glasnost: blok <strong>set volume</strong>.</p>', '16px 0 0')

zaslon = H2 + 'Zaslon: napis</h2>\n' + ol([
    'Odpri paleto <strong>DISPLAY</strong>.',
    'Povleci blok <strong>»write EV3 at line 1«</strong> pod rumeni blok.',
    'Klikni na besedo <strong>EV3</strong> in vpiši <strong>Vozim</strong>.',
    'Zaženi. Poglej zaslon na robotu.',
    'Številka pri »line« je vrstica na zaslonu. Vpiši <strong>3</strong> in zaženi. Kje je zdaj napis?',
    'Blok <strong>»clear display«</strong> pobriše zaslon. Povleci ga pod blok »write« in zaženi.']) + '<p>Zaslon robota črke <strong>č</strong> ne zna prikazati. Namesto č napiše c. Zato piši brez strešic: namesto č, š in ž piši c, s in z.</p>'
sl_write = img(IMG + 'lego-write-line.png', 'Blok »write EV3 at line 1« iz palete DISPLAY.', ' max_width="260px"') + cap('Blok za napis na zaslonu. Prvo polje je besedilo, drugo je vrstica.') \
    + img(IMG + 'lego-clear-display.png', 'Blok »clear display« iz palete DISPLAY.', ' max_width="180px"') + cap('Blok, ki pobriše zaslon.')
lucka = H2 + 'Lučka</h2>\n' + ol([
    'V paleti <strong>DISPLAY</strong> poišči blok <strong>»set status light to green«</strong>.',
    'Povleci ga pod rumeni blok in zaženi. Poglej lučko okoli gumbov na robotu.',
    'Klikni na puščico ob besedi <strong>green</strong>. Odpre se seznam: off, green, red, orange in še tri z besedo <strong>pulse</strong>.',
    'Izberi <strong>red</strong> in zaženi. Poskusi tudi <strong>red pulse</strong>. Kaj je drugače?']) 
sl_light = img(IMG + 'lego-status-light.png', 'Blok »set status light to green« iz palete DISPLAY.', ' max_width="260px"') + cap('Blok za lučko. Barvo izbereš s puščico.') \
    + img(IMG + 'lego-lucka-barve.png', 'Seznam barv lučke: off, green, red, orange, green pulse, red pulse, orange pulse.', ' max_width="240px"') + cap('Seznam barv. Rdečo uporabimo za ustavitev.')
radovedni = H2 + 'Za radovedne</h2>\n<p>V paleti DISPLAY je tudi blok <strong>»display Eyes / Neutral for 2 seconds«</strong>. Namesto besedila pokaže sliko. Poskusi različne slike s seznama.</p>'

primer = box('primer', 'Rešen primer', f'''<p style="margin-top:0">Robot naj prevozi 40 cm naprej in pri tem sporoča: med vožnjo sveti zeleno in piše »Vozim«, ob ustavitvi sveti rdeče in piše »Stop«.</p>
<ol class="pg-koraki">
<li><span><span class="pg-koraki__oznaka">Podatki</span>pot 40 cm, obseg kolesa o = 17,6 cm</span></li>
<li><span><span class="pg-koraki__oznaka">Iskano</span>program z bloki za lučko, napis, pisk in vožnjo</span></li>
<li><span><span class="pg-koraki__oznaka">Formula</span>vrtljaji = pot / obseg kolesa</span></li>
<li><span><span class="pg-koraki__oznaka">Vstavim</span>n = 40 cm / 17,6 cm = {dec(N40)} vrtljaja</span></li>
<li><span><span class="pg-koraki__oznaka">Blok 1</span>set status light to <strong>green</strong></span></li>
<li><span><span class="pg-koraki__oznaka">Blok 2</span>write <strong>Vozim</strong> at line 1</span></li>
<li><span><span class="pg-koraki__oznaka">Blok 3</span>play beep 60 for 0.2 seconds</span></li>
<li><span><span class="pg-koraki__oznaka">Blok 4</span>move forward for <strong>2.27</strong> rotations</span></li>
<li><span><span class="pg-koraki__oznaka">Blok 5</span>clear display</span></li>
<li><span><span class="pg-koraki__oznaka">Blok 6</span>write <strong>Stop</strong> at line 1</span></li>
<li><span><span class="pg-koraki__oznaka">Blok 7</span>set status light to <strong>red</strong></span></li>
<li><span><span class="pg-koraki__oznaka">Rezultat</span><span class="pg-rezultat">7 blokov, vožnja {dec(N40)} vrtljaja</span></span></li>
<li><span><span class="pg-koraki__oznaka">Preverim</span>2,27 · 17,6 cm = 39,95 cm, kar je 40 cm. Ujema se.</span></li>
</ol>''') + box('pozor', 'Pogosta napaka', '<p>Blok za barvo lučke je v paleti <strong>DISPLAY</strong>, ne v paleti za zvok. Če ga ne najdeš, poglej tam.</p>', '16px 0 0')

izziv = H2 + 'Izziv: semafor</h2>\n<p>Robot stoji in čaka. Ko pritisneš senzor dotika, zapelje.</p>\n' + ol([
    'Na začetku naj lučka sveti <strong>rdeče</strong> in na zaslonu naj piše <strong>Stop</strong>.',
    'Nato robot čaka na pritisk. Blok <strong>»1 wait until pressed«</strong> je v paleti SENSORS (modra). Številka 1 je vrata senzorja dotika.',
    'Ko pritisneš senzor, naj lučka postane <strong>zelena</strong>, na zaslonu naj piše <strong>Vozim</strong> in robot naj <strong>enkrat pisne</strong>.',
    'Robot prevozi 40 cm (2,27 vrtljaja).',
    'Ob ustavitvi naj lučka spet sveti rdeče in na zaslonu naj piše Stop.',
    'Namig: pred novim napisom uporabi »clear display«.'])

preveri = H2 + 'Preveri se</h2>' \
    + q('1. Kakšna je razlika med »play sound … until done« in »start sound«?', 'Pri »play sound … until done« program počaka, da se zvok konča. Pri »start sound« se zvok zažene, program pa gre takoj naprej.') \
    + q('2. V kateri paleti je blok »set status light to«?', 'V paleti DISPLAY.') \
    + q('3. Koliko vrtljajev vpišeš pri »move forward«, da robot prevozi 40 cm?', '2,27 vrtljaja (40 cm / 17,6 cm).') \
    + q('4. Zakaj robotu poleg zvoka dodamo še napis in lučko?', 'Zvoka ne slišiš v hrupu ali kadar ga ne moreš slišati. Napis in lučko pa vidiš.')
kratko = box('cilj', 'Na kratko', ul([
    'Zvok: paleta SOUND. Pisk: »play beep«, glasnost: »set volume«.',
    '»play sound … until done« počaka, »start sound« ne.',
    'Napis: »write … at line …« (paleta DISPLAY), brisanje: »clear display«.',
    'Lučka: »set status light to« (paleta DISPLAY).',
    'Robot lahko sporoča, kaj dela, z zvokom, napisom in lučko.']))

out = sec(
    row(col('4_4', text(cilj('Zvok, zaslon in lučka', [
        'predvajati pisk in zvok ter nastaviti glasnost,',
        'razlikovati »play sound … until done« in »start sound«,',
        'izpisati napis na zaslon robota,',
        'nastaviti barvo lučke,',
        'sestaviti program, ki s sporočili pove, kaj robot dela.']))))
  + row(col('1_2', text(kaj)) + col('1_2', text(pravilo)), '1_2,1_2')
  + row(col('1_2', text(zvok) + sl_beep) + col('1_2', text(glasnost) + sl_vol), '1_2,1_2')
  + row(col('1_2', text(dva) + sl_until + sl_start) + col('1_2', text(poskus + napaka1)), '1_2,1_2')
  + row(col('1_2', text(zaslon) + sl_write + text(napaka_zaslon)) + col('1_2', text(lucka) + sl_light + text(radovedni)), '1_2,1_2')
  + row(col('1_2', text(primer)) + col('1_2', text(izziv)), '1_2,1_2'))
out += sec(row(col('1_2', text(preveri)) + col('1_2', text(kratko)), '1_2,1_2'), '#f5f3ef')
write('lego-zvok-zaslon-lucka', out)
