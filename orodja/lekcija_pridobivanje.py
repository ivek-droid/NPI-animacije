src = open('/home/claude/npi-animacije/orodja/lekcije_pomocniki_in_ivep.py').read().split('# ======================================================== SERIJSKA')[0]
exec(src)
# Vir: Električne inštalacije za IEK (tehnik), pogl. 19.2.3 Hidroelektrarne (str. 342–344).

def anim2(file, title, h2, intro, h):
    return (text(H2 + h2 + '</h2>\n<p>' + intro + ' Uporabiš lahko tudi tipko Tab in Enter.</p>\n'
                 f'[iframe src="{GH}{file}?kompakt" width="100%" height="{h}" title="Animacija: {title}"]')
            + f'[et_pb_button button_url="{GH}{file}" url_new_window="on" button_text="Odpri animacijo v celem oknu" module_class="pg-btn" _builder_version="4.27.9"][/et_pb_button]')

kaj = H2 + '''Od vode do elektrike</h2>
<p>Pomisli na mlinsko kolo. Voda pada nanj in ga vrti. Več vode in višje kot pade, močneje ga vrti.</p>
<p>Hidroelektrarna (HE) dela enako. Namesto mlinskega kolesa ima turbino. Turbina vrti generator, ta proizvaja električno energijo.</p>'''

pot = box('cilj', 'Pot energije', ol([
    '<strong>Voda v jezeru</strong> ima potencialno energijo, ker je visoko.',
    '<strong>Voda v cevovodu</strong> pada in dobi hitrost – kinetično energijo.',
    '<strong>Turbina</strong> pretvori energijo vode v mehansko energijo vrtenja.',
    '<strong>Generator</strong> pretvori mehansko energijo v električno.']) + '<p>Pri vsaki pretvorbi se del energije izgubi (trenje, segrevanje). To opisuje izkoristek η.</p>')

TD = 'style="padding:8px 10px;border-bottom:1px solid #c9c4bb;text-align:left;vertical-align:top"'
def tr(c, th=False):
    t = 'th' if th else 'td'
    return '<tr>' + ''.join(f'<{t} {TD}>{x}</{t}>' for x in c) + '</tr>'
tabela = H2 + 'Katero turbino izbrati?</h2>\n<p>Turbino izberemo po <strong>padcu</strong> Δh (višinska razlika vode) in <strong>pretoku</strong> Q (koliko vode steče v eni sekundi).</p>\n' + \
    '<table style="width:100%;border-collapse:collapse;font-size:18px">' + \
    tr(['Turbina', 'Padec Δh', 'Pretok Q', 'Kje'], True) + \
    tr(['<strong>Peltonova</strong>', 'največji (več sto do čez 1000 m)', 'majhen', 'akumulacijske HE v gorah, mini in mikro HE']) + \
    tr(['<strong>Francisova</strong>', 'srednji in veliki (nekaj deset do več sto m)', 'srednji', 'akumulacijske in črpalne HE, male HE']) + \
    tr(['<strong>Kaplanova</strong>', 'majhen (do 70 m)', 'velik', 'pretočne HE na rekah']) + \
    '</table>\n<p style="font-size:16px;color:#4a4f5c">Meje se prekrivajo. Vir: učbenik Električne inštalacije, pogl. 19.2.3.</p>'

vrste = H2 + 'Vrste hidroelektrarn</h2>\n' + ul([
    '<strong>Pretočna HE</strong> stoji na nižinski reki. Reko zajezimo toliko, da je razlika gladin vsaj 7 do 8 m. Večjih zalog vode nima. Uporablja Kaplanovo turbino.',
    '<strong>Akumulacijska HE</strong> dobiva vodo iz velikega umetnega jezera v gorah. Jez je lahko visok več kot 100 m. Brez dotoka lahko deluje tudi več mesecev. Uporablja Francisovo ali Peltonovo turbino.',
    '<strong>Črpalna HE (ČHE)</strong> ima zgornji in spodnji hranilnik vode. Ko je elektrike preveč, črpa vodo navzgor. Ko je elektrike premalo, vodo spušča skozi turbino. Najpogosteje ima Francisovo turbino, ki deluje tudi kot črpalka.',
    '<strong>Male HE</strong> izkoriščajo manjše potoke in reke. Delimo jih na male (1 do 10 MW), mini (100 kW do 1 MW), mikro (pod 100 kW) in piko (do 5 kW).'])

vrtljaji = box('cilj', 'Zakaj ima generator v HE veliko polov', '''<p>Frekvenca v omrežju mora biti vedno 50 Hz. Zato se mora generator vrteti s stalnimi vrtljaji.</p>
<p>Vodna turbina se vrti počasi – le nekaj sto vrtljajev na minuto. Zato ima generator veliko parov magnetnih polov p.</p>
<p style="font-weight:700">n = 60 · f / p</p>
<p>Primer iz učbenika: p = 20, f = 50 Hz → n = 60 · 50 / 20 = 150 min⁻¹.</p>''')

pelton = H2 + 'Peltonova turbina</h2>\n<p><strong>Za največje padce in majhne pretoke.</strong></p>\n' + \
'''<p>Voda brizga iz šobe z veliko hitrostjo. Curek vode je usmerjen tangencialno na lopate gonilnika. Voda udarja ob lopate in oddaja gonilniku svojo kinetično energijo. Vodni curek brizga samo na nekaj lopat, zato je gonilnik samo delno oblit z vodo. Druge lopate gonilnika ne sprejemajo vodne energije.</p>
<p>Pretok vode in s tem moč Peltonove turbine se uravnava s premikanjem igle v šobi; poleg igle v šobi imajo turbine še nož. Ta naprava pri razbremenitvi turbine takoj odreže curek, medtem ko igla počasi pripira šobe tako, da pri nepričakovani razbremenitvi ne pride do prekomernega povišanja tlaka v tlačnem cevovodu.</p>'''

francis = H2 + 'Francisova turbina</h2>\n<p><strong>Za srednje in velike padce.</strong></p>\n' + \
'''<p>Francisova vodna turbina je nadtlačna turbina radialno-aksialnega tipa in je najpogosteje uporabljena vodna turbina, saj je primerna za srednje pretoke in srednje padce, kakršne ima večina virov vodne energije.</p>
<p>Moč turbine je odvisna od pretoka vode in smeri toka vode glede na lopate gonilnika, kar uravnavajo vodilne lopate, ki so premične in se jih da poljubno odpreti ali zapreti.</p>
<p>Sodobne Francisove turbine imajo spiralno ohišje, ki se uporablja pri tlačnih višinah od 15 do 500 m. Pri padcih do 15 m doteka voda do turbine po odprtih kanalih – jaških. Izkoristek dobre Francisove turbine je okoli 0,9 (90 %).</p>
<p>Francisova turbina je lahko horizontalna ali vertikalna. Njeni gradniki:</p>
''' + ul(['spiralno ohišje,', 'vodilne lopate,', 'gonilnik,', 'sesalna cev (difuzor ali aspirator).'])

kaplan = H2 + 'Kaplanova turbina</h2>\n<p><strong>Za majhne padce in velike pretoke.</strong></p>\n' + \
'''<p>Kaplanova vodna turbina je aksialna nadtlačna vodna turbina, ki ima vtok radialen, iztok pa aksialen. Uporablja se za velike pretoke in manjše padce (do 70 m).</p>
''' + ul([
    'Gonilnik je podoben ladijskemu vijaku: ima široko pesto in 4 do 8 lopat. Prerez lopate je podoben letalskemu krilu (vzgon).',
    'Vodilne lopate imajo isto obliko kot pri Francisovi turbini, število lopat je med 8 in 24.',
    'Dvojna regulacija: nastavljati se dajo lopate gonilnika (naklon lopat rotorja) in vodilne lopate. Zato voda vstopa brez udarca pri zelo različnih pretokih.',
    'Dober izkoristek dosežemo že pri 25 % nazivne obremenitve.',
    'Kaplanove turbine se vrtijo hitro, zato so manjše in cenejše.'])

moc = H2 + '''Moč hidroelektrarne</h2>
<p>Več vode in višji padec pomenita večjo moč.</p>
<p>Najprej izračunaš moč vodnega toka:</p>
<p style="font-size:22px;font-weight:700">P<sub>vode</sub> = 9,81 · Q · Δh</p>
''' + ul(['P<sub>vode</sub> – moč vodnega toka v kW,', 'Q – pretok v m³/s,', 'Δh – padec (višinska razlika vode) v m,', '9,81 – teža 1 m³ vode v kN.']) + '''
<p>Turbina in generator imata izgube. Moč generatorja je zato manjša:</p>
<p style="font-size:22px;font-weight:700">P = η · P<sub>vode</sub></p>
<p>η je izkoristek elektrarne. Je brez enote in vedno manjši od 1.</p>'''

primer = box('primer', 'Rešen primer', '''<p style="margin-top:0">Pretočna hidroelektrarna na reki ima padec 8 m. Pretok vode skozi turbine je 500 m³/s. Izkoristek elektrarne je 0,85. Kolikšna je moč generatorjev? Katero turbino uporablja?</p>
<ol class="pg-koraki">
<li><span><span class="pg-koraki__oznaka">Podatki</span>Δh = 8 m, Q = 500 m³/s, η = 0,85</span></li>
<li><span><span class="pg-koraki__oznaka">Iskano</span>P<sub>vode</sub> = ?, P = ?, vrsta turbine</span></li>
<li><span><span class="pg-koraki__oznaka">Formula</span>P<sub>vode</sub> = 9,81 · Q · Δh</span></li>
<li><span><span class="pg-koraki__oznaka">Vstavim</span>P<sub>vode</sub> = 9,81 · 500 · 8</span></li>
<li><span><span class="pg-koraki__oznaka">Izračunam</span>P<sub>vode</sub> = 39 240 kW</span></li>
<li><span><span class="pg-koraki__oznaka">Formula</span>P = η · P<sub>vode</sub></span></li>
<li><span><span class="pg-koraki__oznaka">Izračunam</span>P = 0,85 · 39 240 kW = 33 354 kW</span></li>
<li><span><span class="pg-koraki__oznaka">Rezultat</span><span class="pg-rezultat">P ≈ 33,4 MW</span></span></li>
<li><span><span class="pg-koraki__oznaka">Turbina</span>Majhen padec, velik pretok, pretočna HE → Kaplanova turbina.</span></li>
<li><span><span class="pg-koraki__oznaka">Preverim</span>P je manjša od P<sub>vode</sub>, ker je η manjši od 1. Enote: kN/m³ · m³/s · m = kN · m/s = kW.</span></li>
</ol>''') + box('pozor', 'Pogosta napaka', '<p>Pozabiš na izkoristek. 39,2 MW je moč vode, ne moč generatorja.</p>\n<p>Druga napaka: pretok vstaviš v l/s namesto v m³/s (1 m³/s = 1000 l/s).</p>', '16px 0 0')

preveri = H2 + 'Preveri se</h2>' \
    + q('1. Padec je 600 m, pretok je majhen. Katero turbino izbereš?', 'Peltonovo turbino.') \
    + q('2. Katero turbino ima pretočna HE na nižinski reki?', 'Kaplanovo turbino: padec je majhen, pretok velik.') \
    + q('3. Pretok se podvoji, padec ostane enak. Kaj se zgodi z močjo?', 'Moč se podvoji. Moč je premo sorazmerna s pretokom Q.') \
    + q('4. Zakaj ima Kaplanova turbina dober izkoristek pri različnih pretokih?', 'Ker ima dvojno regulacijo: nastavljajo se vodilne lopate in naklon lopat rotorja.')
kratko = box('cilj', 'Na kratko', ul(['Pot energije: potencialna → kinetična → mehanska → električna.', 'Turbina vrti generator.', 'Pelton: največji padci, majhen pretok.', 'Francis: srednji in veliki padci.', 'Kaplan: majhen padec, velik pretok (pretočne HE).', 'P<sub>vode</sub> = 9,81 · Q · Δh (kW), P = η · P<sub>vode</sub>.']))

out = sec(
    row(col('4_4', text(cilj('Pridobivanje električne energije – hidroelektrarne', ['razložiti, kako hidroelektrarna pretvori energijo vode v električno,', 'našteti vrste hidroelektrarn,', 'izbrati turbino glede na padec in pretok,', 'izračunati moč hidroelektrarne.']))))
  + row(col('1_2', text(kaj) + text(pot)) + col('1_2', text(tabela)), '1_2,1_2')
  + row(col('1_2', text(vrste)) + col('1_2', text(vrtljaji)), '1_2,1_2'))
out += sec(row(col('1_3', text(pelton)) + col('1_3', text(francis)) + col('1_3', text(kaplan)), '1_3,1_3,1_3'))
out += sec(row(col('4_4', anim2('vodne-turbine.html', 'vodne turbine', 'Preizkusi sam: vodne turbine', 'Izberi turbino. Z gumbi odpiraš in zapiraš pretok vode in opazuješ moč.', 620))), '#f5f3ef')
out += sec(row(col('1_2', text(moc)) + col('1_2', text(primer)), '1_2,1_2'))
out += sec(row(col('4_4', anim2('hidroelektrarna.html', 'hidroelektrarna', 'Preizkusi sam: moč hidroelektrarne', 'Spreminjaj padec in pretok. Opazuj moč in točko na grafu turbin.', 730))), '#f5f3ef')
out += sec(row(col('1_2', text(preveri)) + col('1_2', text(kratko)), '1_2,1_2'))
write('pridobivanje-elektricne-energije', out)
