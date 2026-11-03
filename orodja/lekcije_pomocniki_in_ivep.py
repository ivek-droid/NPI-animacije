U = 'https://npi.splet.arnes.si/files/'
GH = 'https://ivek-droid.github.io/NPI-animacije/'
TXT = '_builder_version="4.27.9" text_font_size="19px" text_line_height="1.6em" text_text_color="#1b1e28"'
def sec(inner, bg='#ffffff'):
    return f'[et_pb_section fb_built="1" _builder_version="4.27.9" background_color="{bg}" custom_padding="20px||28px||false|false"]{inner}[/et_pb_section]'
def row(cols, structure=None):
    cs = f' column_structure="{structure}"' if structure else ''
    return f'[et_pb_row{cs} _builder_version="4.27.9" width="90%" max_width="1080px" custom_padding="10px||10px||false|false" column_gap="3"]{cols}[/et_pb_row]'
def col(t, inner): return f'[et_pb_column type="{t}" _builder_version="4.27.9"]{inner}[/et_pb_column]'
def text(html): return f'[et_pb_text {TXT}]{html}[/et_pb_text]'
def img(src, alt, extra='', lightbox=True):
    lb = ' show_in_lightbox="on"' if lightbox else ''
    return f'[et_pb_image src="{U}{src}" alt="{alt}" title_text="{alt}"{lb} _builder_version="4.27.9" border_radii="on|14px|14px|14px|14px"{extra}][/et_pb_image]'
def video(src, alt, url):
    return img(src, alt, f' url="{url}" url_new_window="on" max_width="420px"', lightbox=False)
CAP = '<p style="font-size:16px;color:#4a4f5c;margin-top:6px;line-height:1.4">'
def cap(t): return text(CAP + t + '</p>')
H2 = '<h2 style="margin-top:0">'
DET = '<details style="margin:0 0 10px;padding:10px 16px;border:2px solid #c9c4bb;border-radius:14px"><summary style="cursor:pointer;font-weight:700;min-height:32px">'
def q(v, a): return f'{DET}{v}</summary><p style="margin-top:12px">{a}</p></details>'
def box(kind, label, body, margin='0'):
    return f'<div class="pg-okvir pg-okvir--{kind}" style="margin:{margin}">\n<p class="pg-okvir__oznaka">{label}</p>\n{body}\n</div>'
def cilj(h1, items):
    return f'<h1 style="margin-bottom:16px">{h1}</h1>\n' + box('cilj', 'Po tej lekciji znaš', '<ul>\n' + ''.join(f'<li>{i}</li>\n' for i in items) + '</ul>')
def ul(items): return '<ul>\n' + ''.join(f'<li>{i}</li>\n' for i in items) + '</ul>'
def ol(items): return '<ol>\n' + ''.join(f'<li>{i}</li>\n' for i in items) + '</ol>'
def anim(file, title, intro, h):
    return (text(H2 + 'Preizkusi sam</h2>\n<p>' + intro + ' Uporabiš lahko tudi tipko Tab in Enter.</p>\n'
                 f'[iframe src="{GH}{file}?kompakt" width="100%" height="{h}" title="Animacija: {title}"]')
            + f'[et_pb_button button_url="{GH}{file}" url_new_window="on" button_text="Odpri animacijo v celem oknu" module_class="pg-btn" _builder_version="4.27.9"][/et_pb_button]')
VID = H2 + 'Poglej video</h2>\n<p>Klikni sliko. Video se odpre v novem oknu.</p>'
ELBI = '»Ničelni vodnik« je starejše ime za nevtralni vodnik (N). Vir: trgovina-elbi.si'

import sys as _sys; _sys.path.insert(0, '/home/claude/npi-animacije/orodja')
from koraki_nbsp import nb_koraki
def write(name, out):
    out = nb_koraki(out)
    open(f'/home/claude/npi-animacije/slog/osnutki/{name}.txt', 'w').write(out)
    print(name, len(out))

# ======================================================== SERIJSKA
kaj = H2 + '''Kaj je serijska vezava</h2>
<p>Pomisli na lestenec s petimi žarnicami. Z eno tipko prižgeš dve žarnici, z drugo tri, z obema vseh pet.</p>
<p>Pri tej vezavi imamo dve svetilki oziroma dve skupini svetilk. Serijsko vezavo uporabljamo predvsem pri lestencih in v prostorih z večjim številom svetilk. Ta vezava s prihodom modularnih sistemov počasi izgublja svoj pomen.</p>
''' + box('pozor', 'Ne zamenjaj', '<p><strong>Serijska vezava</strong> je vezava s serijskim stikalom – stikalom z dvema tipkama v enem ohišju.</p>\n<p>Svetilke so tudi tu vezane <strong>vzporedno</strong>. Vsaka ima 230 V. Ne zamenjaj z zaporedno vezavo porabnikov.</p>', '16px 0 0')
stikalo = H2 + '''Serijsko stikalo</h2>
<p>Serijsko stikalo ima tri priključke:</p>
''' + ul(['en <strong>skupni</strong> priključek za fazni vodnik L,', "dva <strong>izhodna</strong> priključka za stikalna vodnika L1' in L2'."]) + '''
<p>Tipka 1 vklaplja L1', tipka 2 vklaplja L2'. Tipki delujeta neodvisno.</p>'''
pravilo = H2 + 'Pravilo vezave</h2>\n' + ol([
    'Fazni vodnik L pripelješ na skupni priključek serijskega stikala (označen s puščico ali L).',
    "S prvega izhoda vodiš stikalni vodnik L1' do prve skupine svetilk, na centralne kontakte.",
    "Z drugega izhoda vodiš stikalni vodnik L2' do druge skupine svetilk, na centralne kontakte.",
    'Nevtralni vodnik N vodiš do vseh svetilk, na navojni kontakt.',
    'Zaščitni vodnik PE vodiš do ohišij svetilk.']) + "\n<p>Do serijskega stikala vodiš 3 vodnike: L, L1' in L2'.</p>"
napaka = box('pozor', 'Pogosta napaka', '<p>Fazni vodnik priključiš na izhodni priključek namesto na skupnega.</p>\n<p>Potem tipka 1 deluje, skupina 2 pa sveti samo, ko sta vklopljeni obe tipki.</p>')
preveri = H2 + 'Preveri se</h2>' + q('1. Koliko priključkov ima serijsko stikalo?', "Tri: skupnega za L in dva izhodna za L1' in L2'.") \
    + q('2. Na lestencu 2 + 3 sta vklopljeni obe tipki. Koliko žarnic sveti?', 'Vseh pet.') \
    + q('3. Ali so svetilke pri serijski vezavi vezane zaporedno?', 'Ne. Vsaka svetilka je vezana vzporedno med svoj stikalni vodnik in N. Vsaka ima 230 V.')
kratko = box('cilj', 'Na kratko', ul(['Serijsko stikalo = dve tipki v enem ohišju.', 'L → skupni priključek stikala.', "Tipka 1 → L1' → skupina 1, tipka 2 → L2' → skupina 2.", 'N → navojni kontakti vseh svetilk.', 'Svetilke so vezane vzporedno, vsaka ima 230 V.']))
out = sec(
    row(col('4_4', text(cilj('Serijska vezava za razsvetljavo', ['povedati, kje uporabimo serijsko vezavo,', 'priključiti serijsko stikalo in dve skupini svetilk,', 'ločiti serijsko vezavo od zaporedne vezave.']))))
  + row(col('1_2', text(kaj)) + col('1_2', img('2024/03/vezave_serijsko-splet.jpg', 'Vezava serijskega stikala v prostoru: dovod iz električne omarice, serijsko stikalo pri vratih in dve svetilki na stropu. Barve: fazni vodnik črn, nevtralni moder, zaščitni rumeno-zelen.') + cap('Vezava serijskega stikala. ' + ELBI)), '1_2,1_2')
  + row(col('1_3', text(stikalo)) + col('1_3', img('2024/03/enopolna-serijska.png', 'Enopolna shema serijske vezave: dovod, serijsko stikalo s tremi vodniki in lestenec 2 + 3.') + cap('Enopolna shema'))
        + col('1_3', img('2024/03/dvopolna-serijsko.png', 'Dvopolna shema serijske vezave: L na serijsko stikalo, dva stikalna vodnika do dveh skupin svetilk (2 in 3), N do vseh svetilk.') + cap('Dvopolna shema')), '1_3,1_3,1_3')
  + row(col('1_2', text(pravilo)) + col('1_2', text(napaka)), '1_2,1_2'))
out += sec(row(col('4_4', anim('serijska-vezava.html', 'serijska vezava', 'Vklapljaj tipki in opazuj, katera skupina svetilk sveti.', 720))), '#f5f3ef')
out += sec(row(col('1_2', text(preveri)) + col('1_2', text(kratko) + text(VID) + video('2024/03/serijska-vezava.png', 'Video: serijska vezava (odpre se v novem oknu)', 'https://video.arnes.si/watch/9611l8fqxj1j')), '1_2,1_2'))
write('serijska-vezava', out)

# ======================================================== KRIŽNA
kaj = H2 + '''Kaj je križna vezava</h2>
<p>Pomisli na dolg hodnik z vrati na štirih mestih. Luč želiš prižgati in ugasniti pri vsakih vratih.</p>
<p>Križno vezje izvedemo z dvema menjalnima stikaloma in enim ali več križnimi stikali. Menjalni stikali običajno namestimo na začetku in na koncu križnega vezja. Omogoča nam izklop ali vklop ene ali skupine žarnic s poljubnega števila mest. Uporabljamo jo pri razsvetljavi dolgih hodnikov in večnadstropnih stopnišč.</p>'''
stikalo = H2 + '''Križno stikalo</h2>
<p>Križno stikalo ima štiri priključke: dva vhodna in dva izhodna.</p>
''' + ul(['V enem položaju poveže vodnika <strong>naravnost</strong>.', 'V drugem položaju ju poveže <strong>navzkriž</strong>.']) + '''
<p>Križno stikalo toka ne prekine. Samo zamenja stikalna vodnika med sabo.</p>'''
pravilo = H2 + 'Pravilo vezave</h2>\n' + ol([
    'Fazni vodnik L pripelješ na skupni priključek prvega menjalnega stikala.',
    'Prosta priključka prvega menjalnega stikala povežeš z obema vhodoma prvega križnega stikala.',
    'Izhoda križnega stikala povežeš z vhodoma naslednjega križnega stikala ali z drugim menjalnim stikalom.',
    "S skupnega priključka drugega menjalnega stikala vodiš stikalni vodnik do svetilk, na centralni kontakt.",
    'N vodiš do svetilk na navojni kontakt, PE do ohišij svetilk.']) + '\n<p>Do križnega stikala vodiš 4 vodnike: dva prideta, dva gresta naprej.</p>'
napaka = box('pozor', 'Pogosta napaka', '<p>Vodnika iz prejšnjega stikala priključiš na en vhod in en izhod križnega stikala.</p>\n<p>Potem vezava deluje samo pri nekaterih položajih stikal. Preveri oznake vhodov in izhodov na stikalu.</p>')
primer = box('primer', 'Rešen primer', '''<p style="margin-top:0">Hodnik ima 5 mest, kjer želimo prižigati luč. Koliko križnih stikal potrebujemo?</p>
<ol class="pg-koraki">
<li><span><span class="pg-koraki__oznaka">Podatki</span>število mest = 5, menjalni stikali = 2</span></li>
<li><span><span class="pg-koraki__oznaka">Iskano</span>število križnih stikal k = ?</span></li>
<li><span><span class="pg-koraki__oznaka">Formula</span>k = število mest − 2</span></li>
<li><span><span class="pg-koraki__oznaka">Vstavim</span>k = 5 − 2</span></li>
<li><span><span class="pg-koraki__oznaka">Rezultat</span><span class="pg-rezultat">k = 3 križna stikala</span></span></li>
<li><span><span class="pg-koraki__oznaka">Preverim</span>2 menjalni + 3 križna = 5 stikal = 5 mest.</span></li>
</ol>''') + box('pozor', 'Pogosta napaka', '<p>Pozabiš na menjalni stikali in vzameš 5 križnih stikal. Menjalni stikali sta tudi mesti vklopa.</p>', '16px 0 0')
preveri = H2 + 'Preveri se</h2>' + q('1. Koliko priključkov ima križno stikalo?', 'Štiri: dva vhodna in dva izhodna.') \
    + q('2. S koliko mest prižigaš luč, če imaš dve menjalni in dve križni stikali?', 'S štirih mest.') \
    + q('3. Kaj naredi križno stikalo, ko ga preklopiš?', 'Zamenja stikalna vodnika: iz »naravnost« v »navzkriž« ali obratno. Zato se stanje svetilke spremeni.')
kratko = box('cilj', 'Na kratko', ul(['Na začetku in koncu je menjalno stikalo, vmes so križna.', 'Število križnih stikal = število mest − 2.', 'Križno stikalo ima 4 priključke: 2 vhoda, 2 izhoda.', 'Vsak preklop kateregakoli stikala spremeni stanje svetilke.']))
out = sec(
    row(col('4_4', text(cilj('Križna vezava za razsvetljavo', ['povedati, kje uporabimo križno vezavo,', 'vezati križno stikalo med dve menjalni stikali,', 'izračunati, koliko križnih stikal potrebuješ.']))))
  + row(col('1_2', text(kaj)) + col('1_2', img('2024/03/krizna-vezava-splet.jpg', 'Vezava križnega stikala v prostoru: dve menjalni stikali na stenah, križno stikalo pri vratih in svetilka na stropu. Barve: fazni vodnik črn, nevtralni moder, zaščitni rumeno-zelen.') + cap('Vezava križnega stikala. ' + ELBI)), '1_2,1_2')
  + row(col('1_3', text(stikalo)) + col('1_3', img('2024/03/enopolna-krizna.png', 'Enopolna shema križne vezave: dve menjalni in dve križni stikali ter dve svetilki; do križnih stikal vodijo štirje vodniki.') + cap('Enopolna shema'))
        + col('1_3', img('2024/03/dvopolna-krizna.png', 'Dvopolna shema križne vezave: menjalno stikalo, dve križni stikali, menjalno stikalo in dve svetilki, vsak vodnik narisan posebej.') + cap('Dvopolna shema')), '1_3,1_3,1_3')
  + row(col('1_2', text(pravilo)) + col('1_2', text(napaka)), '1_2,1_2')
  + row(col('1_2', text(H2 + 'Koliko križnih stikal?</h2>\n<p>Vsako stikalo je eno mesto vklopa. Menjalni stikali sta vedno dve, vsa ostala so križna.</p>')) + col('1_2', text(primer)), '1_2,1_2'))
out += sec(row(col('4_4', anim('krizna-vezava.html', 'križna vezava', 'Izberi eno ali dve križni stikali in preklapljaj stikala. Opazuj, po katerem vodniku teče tok.', 700))), '#f5f3ef')
out += sec(row(col('1_2', text(preveri)) + col('1_2', text(kratko) + text(VID) + video('2024/03/krizna-video.png', 'Video: križna vezava (odpre se v novem oknu)', 'https://video.arnes.si/watch/xr38s3cyxrz7')), '1_2,1_2'))
write('krizna-vezava', out)

# ======================================================== IMPULZNI RELE
kaj = H2 + '''Kaj je vezava z impulznim relejem</h2>
<p>Pomisli na dolg hodnik s tipkali pri vseh vratih. Pritisneš katerokoli tipkalo in luč se prižge. Pritisneš znova in luč ugasne.</p>
<p>Križno vezavo lahko nadomestimo z vezavo bistabilnega impulznega releja. Najprej usvojimo pojem elektromagneta, da bomo lažje razumeli delovanje releja.</p>'''
magnet = H2 + '''Elektromagnet</h2>
<p>Ko skozi tuljavo teče tok, nastane magnetno polje. Tuljava z železnim jedrom privlači železni del – kotvo.</p>
<p>Ko tok preneha, magnetno polje izgine.</p>'''
rele = H2 + '''Bistabilni impulzni rele</h2>
<p>Bistabilni impulzni releji so namenjeni za izmenično in enosmerno impulzno napajanje. S tokovnim impulzom vzbudimo elektromagnet releja. Magnetna sila prevrže kotvo, ki ostane v novem položaju do ponovnega impulza.</p>
<p>Impulzni bistabilni rele po krmilnem impulzu (pritisk na tipkalo) spremeni in ohranja stanje stikala porabnika do naslednjega impulza (ponovni pritisk na tipkalo).</p>
<p>Rele lahko uporabljamo tudi kot ločilni člen med nizkonapetostnim krmilnim tokokrogom in porabniki, ki so priključeni neposredno na omrežje.</p>
''' + box('cilj', 'Bistabilni', '<p>pomeni, da ima rele dve stalni stanji: kontakt je sklenjen ali odprt. Vsak impulz ga preklopi v drugo stanje.</p>', '16px 0 0')
pravilo = H2 + 'Pravilo vezave</h2>\n<p><strong>Krmilni krog</strong> (tipkala in tuljava):</p>\n' + ol([
    'Fazni vodnik L pripelješ do vseh tipkal.',
    'Tipkala vežeš vzporedno. Z izhodov tipkal greš na priključek tuljave A1.',
    'Priključek tuljave A2 povežeš z nevtralnim vodnikom N.']) + '\n<p><strong>Krmiljeni krog</strong> (kontakt in svetilke):</p>\n' + ol([
    'Fazni vodnik L pripelješ na kontakt releja.',
    "Z drugega priključka kontakta vodiš stikalni vodnik L' do svetilk, na centralni kontakt.",
    'N vodiš do svetilk na navojni kontakt, PE do ohišij.']) + '\n<p>Tipkalo se po pritisku samo vrne v izhodni položaj. Zato dobi tuljava samo kratek impulz. Oznake priključkov kontakta se med proizvajalci razlikujejo – poglej na rele.</p>'
napaka = box('pozor', 'Pogosta napaka', '<p>Tipkala vežeš zaporedno namesto vzporedno.</p>\n<p>Potem rele preklopi samo, če pritisneš vsa tipkala hkrati.</p>') \
    + box('pozor', 'Pozor', '<p>Namesto tipkala ne vgradi navadnega stikala. Tuljava bi bila ves čas pod napetostjo: rele preklopi samo enkrat, tuljava se lahko pregreje.</p>', '16px 0 0')
preveri = H2 + 'Preveri se</h2>' + q('1. Kaj pomeni »bistabilni«?', 'Rele ima dve stalni stanji. Kontakt ostane sklenjen ali odprt do naslednjega impulza.') \
    + q('2. Kako vežemo tipkala?', 'Vzporedno. Vsako tipkalo lahko samo pošlje impulz tuljavi.') \
    + q('3. Kateri krog vklaplja svetilke: krmilni ali krmiljeni?', 'Krmiljeni krog. Krmilni krog s tipkali samo preklaplja rele.')
kratko = box('cilj', 'Na kratko', ul(['Tipkalo da kratek impulz, rele si stanje zapomni.', 'Tipkala so vezana vzporedno na tuljavo (A1–A2).', 'Kontakt releja vklaplja svetilke.', 'Tipkal je lahko poljubno veliko.', 'Nadomesti križno vezavo pri dolgih hodnikih.']))
out = sec(
    row(col('4_4', text(cilj('Vezava bistabilnega impulznega releja', ['razložiti, kako deluje bistabilni impulzni rele,', 'vezati tipkala in rele,', 'ločiti krmilni in krmiljeni krog.']))))
  + row(col('1_2', text(kaj) + text(magnet)) + col('1_2', img('2024/02/elektromagnet.png', 'Elektromagnet: tok skozi tuljavo ustvari magnetno polje; primeri uporabe elektromagneta.')), '1_2,1_2')
  + row(col('1_2', text(rele)) + col('1_2', img('2024/02/impulzni-rele.jpg', 'Bistabilni impulzni rele: prozorno ohišje s priključnimi sponkami, oznaki tuljave A1 in A2.', ' max_width="360px"') + img('2024/02/impulzni-rele-shema.jpg', 'Simbol impulznega releja: tuljava in kontakt, povezana z mehansko povezavo.', ' max_width="360px"')), '1_2,1_2')
  + row(col('1_2', text(pravilo)) + col('1_2', text(napaka) + img('2024/02/vezalna-shema-z-impulznim-relejem.png', 'Vezalna shema z impulznim relejem: pet tipkal S1 do S5 vzporedno v krmilnem krogu, kontakt releja v krmiljenem krogu vklaplja svetilko.') + cap('Vezalna shema z impulznim relejem. Vir: Zdravko Žalar, Elektrotehnika.')), '1_2,1_2')
  + row(col('4_4', img('2024/02/vezava-imulznega-releja.jpg', 'Dvopolna shema vezave impulznega releja z več tipkali in svetilkami.'))))
out += sec(row(col('4_4', anim('impulzni-rele.html', 'bistabilni impulzni rele', 'Pritiskaj tipkala. Opazuj impulz v tuljavi in kontakt releja.', 680))), '#f5f3ef')
out += sec(row(col('1_2', text(preveri)) + col('1_2', text(kratko) + text(VID) + video('2024/04/IMPULZNI-RELE-DELOVANJE.png', 'Video: delovanje impulznega releja (odpre se v novem oknu)', 'https://video.arnes.si/watch/cv1zn1bwhqhk')), '1_2,1_2'))
write('impulzni-rele', out)
