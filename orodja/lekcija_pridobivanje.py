src = open('/home/claude/npi-animacije/orodja/lekcije_pomocniki_in_ivep.py').read().split('# ======================================================== SERIJSKA')[0]
exec(src)

def vid(src):
    return f'[et_pb_video src="{U}{src}" _builder_version="4.27.9" border_radii="on|14px|14px|14px|14px"][/et_pb_video]'

kaj = H2 + '''Od vode do elektrike</h2>
<p>Pomisli na mlinsko kolo. Voda pada nanj in ga vrti. Več vode in višje kot pade, močneje ga vrti.</p>
<p>Hidroelektrarna dela enako. Namesto mlinskega kolesa ima turbino. Turbina vrti generator, ta proizvaja električno energijo.</p>'''

pot = box('cilj', 'Pot energije', ol([
    '<strong>Voda v jezeru</strong> ima potencialno energijo, ker je visoko.',
    '<strong>Voda v cevovodu</strong> pada in dobi hitrost – kinetično energijo.',
    '<strong>Turbina</strong> pretvori energijo vode v mehansko energijo vrtenja.',
    '<strong>Generator</strong> pretvori mehansko energijo v električno.']) + '<p>Pri vsaki pretvorbi se del energije izgubi (trenje, segrevanje). To opisuje izkoristek η.</p>')

TD = 'style="padding:8px 10px;border-bottom:1px solid #c9c4bb;text-align:left"'
def tr(c, th=False):
    t = 'th' if th else 'td'
    return '<tr>' + ''.join(f'<{t} {TD}>{x}</{t}>' for x in c) + '</tr>'
tabela = H2 + 'Katero turbino izbrati?</h2>\n<p>Turbino izberemo po <strong>padcu</strong> (H – višina, s katere pade voda) in <strong>pretoku</strong> (Q – koliko vode steče v eni sekundi).</p>\n' + \
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:18px">' + \
    tr(['Turbina', 'Padec', 'Pretok', 'Vrsta'], True) + \
    tr(['<strong>Peltonova</strong>', 'velik (več sto metrov)', 'majhen', 'enakotlačna']) + \
    tr(['<strong>Francisova</strong>', 'srednji (15–500 m)', 'srednji', 'nadtlačna']) + \
    tr(['<strong>Kaplanova</strong>', 'majhen (do 70 m)', 'velik', 'nadtlačna']) + \
    '</table></div>\n<p style="font-size:16px;color:#4a4f5c">Meje se med turbinami prekrivajo. Številke so iz besedila spodaj.</p>'

pelton = H2 + 'Peltonova turbina</h2>\n<p><strong>Za velike padce in majhne pretoke.</strong></p>\n' + \
'''<p>Voda brizga iz šobe z veliko hitrostjo. Curek vode je usmerjen tangencialno na lopatice gonilnika. Voda udarja ob lopatice in oddaja gonilniku svojo kinetično energijo. Vodni curek brizga samo na nekaj lopatic, zato je gonilnik samo delno oblit z vodo. Druge lopatice gonilnika ne sprejemajo vodne energije.</p>
<p>Pretok vode in s tem moč Peltonove turbine se uravnava s premikanjem igle v šobi; poleg igle v šobi imajo turbine še nož. Ta naprava pri razbremenitvi turbine takoj odreže curek, medtem ko igla počasi pripira šobe tako, da pri nepričakovani razbremenitvi ne pride do prekomernega povišanja tlaka v tlačnem cevovodu.</p>'''

francis = H2 + 'Francisova turbina</h2>\n<p><strong>Za srednje padce in srednje pretoke.</strong></p>\n' + \
'''<p>Francisova vodna turbina je nadtlačna turbina radialno-aksialnega tipa in je najpogosteje uporabljena vodna turbina, saj je primerna za srednje pretoke in srednje padce, kakršne ima večina virov vodne energije.</p>
<p>Moč turbine je odvisna od pretoka vode in smeri toka vode glede na lopatice gonilnika, kar uravnavajo vodilne lopatice, ki so premične in se jih da poljubno odpreti ali zapreti.</p>
<p>Sodobne Francisove turbine imajo spiralno ohišje, ki se uporablja pri tlačnih višinah od 15 do 500 m. Pri padcih do 15 m doteka voda do turbine po odprtih kanalih – jaških. Izkoristek dobre Francisove turbine je okoli 0,9 (90 %).</p>
<p>Francisova turbina je lahko horizontalna ali vertikalna. Njeni gradniki:</p>
''' + ul(['spiralno ohišje,', 'vodilne lopatice,', 'gonilnik,', 'sesalna cev (difuzor ali aspirator).'])

kaplan = H2 + 'Kaplanova turbina</h2>\n<p><strong>Za majhne padce in velike pretoke.</strong></p>\n' + \
'''<p>Kaplanova vodna turbina je aksialna nadtlačna vodna turbina, ki ima vtok radialen, iztok pa aksialen. Uporablja se za velike pretoke in manjše padce (do 70 m).</p>
''' + ul([
    'Gonilnik je podoben ladijskemu vijaku: ima široko pesto in 4 do 8 lopatic. Prerez lopatice je podoben letalskemu krilu (vzgon).',
    'Vodilne lopatice imajo isto obliko kot pri Francisovi turbini, število lopatic je med 8 in 24.',
    'Dvojna regulacija: nastavljati se dajo lopatice gonilnika in vodilne lopatice. Zato voda vstopa brez udarca pri zelo različnih pretokih.',
    'Dober izkoristek dosežemo že pri 25 % nazivne obremenitve.',
    'Kaplanove turbine se vrtijo hitro, zato so manjše in cenejše.'])

moc = H2 + '''Moč hidroelektrarne</h2>
<p>Več vode in višji padec pomenita večjo moč.</p>
<p style="font-size:22px;font-weight:700">P = ρ · g · Q · H · η</p>
''' + ul(['P – moč v vatih (W),', 'ρ – gostota vode: 1000 kg/m³,', 'g – težni pospešek: 9,81 m/s²,', 'Q – pretok v m³/s,', 'H – padec v metrih (m),', 'η – izkoristek (brez enote, vedno manjši od 1).']) + \
'<p>Pretok vedno pretvori v m³/s: 1 m³/s = 1000 l/s.</p>'

primer = box('primer', 'Rešen primer', '''<p style="margin-top:0">Mala hidroelektrarna ima padec 10 m. Pretok vode je 3 m³/s. Izkoristek elektrarne je 0,85. Kolikšna je moč? Katero turbino izberemo?</p>
<ol class="pg-koraki">
<li><span><span class="pg-koraki__oznaka">Podatki</span>H = 10 m, Q = 3 m³/s, η = 0,85, ρ = 1000 kg/m³, g = 9,81 m/s²</span></li>
<li><span><span class="pg-koraki__oznaka">Iskano</span>P = ?, vrsta turbine</span></li>
<li><span><span class="pg-koraki__oznaka">Formula</span>P = ρ · g · Q · H · η</span></li>
<li><span><span class="pg-koraki__oznaka">Vstavim</span>P = 1000 kg/m³ · 9,81 m/s² · 3 m³/s · 10 m · 0,85</span></li>
<li><span><span class="pg-koraki__oznaka">Izračunam</span>P = 250 155 W</span></li>
<li><span><span class="pg-koraki__oznaka">Rezultat</span><span class="pg-rezultat">P ≈ 250 kW</span></span></li>
<li><span><span class="pg-koraki__oznaka">Turbina</span>Padec 10 m je majhen (manj kot 15 m), pretok je velik → Kaplanova turbina.</span></li>
<li><span><span class="pg-koraki__oznaka">Preverim</span>kg/m³ · m/s² · m³/s · m = kg · m²/s³ = W. Ocena: 8,3 · 3 · 10 ≈ 250 kW.</span></li>
</ol>''') + box('pozor', 'Pogosta napaka', '<p>Pretok vstaviš v litrih na sekundo (3000 l/s) namesto v m³/s. Dobiš 250 MW – 1000-krat preveč.</p>', '16px 0 0')

preveri = H2 + 'Preveri se</h2>' \
    + q('1. Padec je 600 m, pretok je majhen. Katero turbino izbereš?', 'Peltonovo turbino.') \
    + q('2. Kateri del hidroelektrarne pretvori mehansko energijo v električno?', 'Generator. Turbina samo vrti generator.') \
    + q('3. Pretok se podvoji, padec ostane enak. Kaj se zgodi z močjo?', 'Moč se podvoji. P je premo sorazmerna s Q.') \
    + q('4. Zakaj ima Kaplanova turbina dober izkoristek pri različnih pretokih?', 'Ker ima dvojno regulacijo: nastavljajo se lopatice gonilnika in vodilne lopatice.')
kratko = box('cilj', 'Na kratko', ul(['Pot energije: potencialna → kinetična → mehanska → električna.', 'Turbina vrti generator.', 'Pelton: velik padec, majhen pretok.', 'Francis: srednji padec in pretok.', 'Kaplan: majhen padec, velik pretok.', 'P = ρ · g · Q · H · η; hitra ocena: P (kW) ≈ 8,3 · Q · H (pri η = 0,85).']))

out = sec(
    row(col('4_4', text(cilj('Pridobivanje električne energije – vodne turbine', ['razložiti, kako hidroelektrarna pretvori energijo vode v električno,', 'izbrati turbino glede na padec in pretok,', 'izračunati moč hidroelektrarne.']))))
  + row(col('1_2', text(kaj) + text(tabela)) + col('1_2', text(pot)), '1_2,1_2'))
out += sec(
    row(col('1_2', text(pelton)) + col('1_2', vid('2023/11/Voith-Functioning-of-Pelton-turbines-EN-1-1.mp4') + cap('Video: delovanje Peltonove turbine. Opazuj curek vode in lopatice.')), '1_2,1_2')
  + row(col('1_2', text(francis)) + col('1_2', vid('2023/11/Working-of-Francis-Turbine.mp4') + cap('Video: delovanje Francisove turbine. Opazuj, kod voda priteče do gonilnika.')), '1_2,1_2')
  + row(col('1_2', text(kaplan)) + col('1_2', vid('2023/11/WORKING-OF-KAPLAN-TURBINE.mp4') + cap('Video: delovanje Kaplanove turbine. Opazuj obliko gonilnika.')), '1_2,1_2'))
out += sec(row(col('1_2', text(moc)) + col('1_2', text(primer)), '1_2,1_2'))
out += sec(row(col('4_4', anim('hidroelektrarna.html', 'hidroelektrarna', 'Spreminjaj padec in pretok. Opazuj moč in točko na grafu turbin.', 700))), '#f5f3ef')
out += sec(row(col('1_2', text(preveri)) + col('1_2', text(kratko)), '1_2,1_2'))
write('pridobivanje-elektricne-energije', out)
