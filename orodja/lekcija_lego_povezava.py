# Generator: LEGO programiranje, vaja 1 »Spoznaj robota in program« (osnutek, ni objavljeno)
exec(open('/home/claude/npi-animacije/orodja/lekcije_pomocniki_in_ivep.py').read())
IMG = '2026/11/'
def blk(name, alt, w='420px'): return img(IMG + name, alt, f' max_width="{w}"')

# --- preverjeno z uporabnikom (10. 11. 2026): B levi motor, C desni; Windows kaže »EV3C – Povezava je vzpostavljena«;
# --- levi gumb = samo prenos, desni (▶) = prenos in zagon; pri seznanjanju je treba vpisati PIN; kolesa se z roko težko vrtijo
PIN = '1234'   # potrjeno (uporabnik, 10. 11. 2026): privzeta koda

poveži = H2 + 'Poveži robota z Bluetooth</h2>\n' + ol([
    'Vklopi robota. Pritisni srednji gumb na robotu in počakaj, da se na zaslonu pokaže meni.',
    'Na robotu vklopi Bluetooth.',
    'Na računalniku odpri nastavitve Bluetooth in dodaj napravo <strong>EV3C</strong>.',
    f'Ko računalnik vpraša po kodi PIN, vpiši <strong>{PIN}</strong>. Kodo potrdi tudi na robotu.',
    'Počakaj, da pod napravo EV3C piše »Povezava je vzpostavljena«.',
    'Odpri EV3 Classroom. Program te vodi skozi povezavo. Izberi robota <strong>EV3C</strong>.',
    'Ko je robot povezan, ima ikona robota zeleno piko.'])
slika_win = blk('lego-windows-povezano.png', 'Windows: naprava EV3C s sporočilom »Povezava je vzpostavljena«.', '360px') + cap('Tako izgleda, ko je robot seznanjen z računalnikom.')
usb = box('cilj', 'Povezava z USB kablom', '<p style="margin-top:0">Če Bluetooth ne dela, uporabi USB kabel. Kabel priključi v robota (vrata PC) in v računalnik. Nato v programu EV3 Classroom izberi robota.</p>')
napaka = box('pozor', 'Robot se ne poveže', ul([
    'Preveri, ali je robot vklopljen in ali je Bluetooth vklopljen na robotu in na računalniku.',
    'Preveri kodo PIN.',
    'Robota izklopi in ga ponovno vklopi.',
    'Poskusi še z USB kablom.']))

vrata = H2 + 'Preberi vrednosti na vratih</h2>\n<p>Klikni ikono robota z zeleno piko (»open brick connection«). Odpre se pogled na robota. Vsak senzor in motor je priključen na svoja vrata. Ob vratih vidiš njegovo vrednost.</p>\n' + ul([
    'vrata <strong>1</strong>: senzor dotika,',
    'vrata <strong>2</strong>: žiroskop (stopinje),',
    'vrata <strong>3</strong>: barvni senzor (odstotki),',
    'vrata <strong>4</strong>: ultrazvočni senzor (cm),',
    'vrata <strong>B</strong>: levi motor, vrata <strong>C</strong>: desni motor (stopinje).'])
poskus = H2 + 'Poskusi</h2>\n' + ol([
    'Pritisni senzor dotika. Poglej, kaj se zgodi z vrednostjo pri vratih 1.',
    'Dlan postavi pred ultrazvočni senzor in jo odmikaj. Poglej, kako se spreminja razdalja pri vratih 4.',
    'Zavrti levo kolo z roko za en polni obrat. Poglej število stopinj pri vratih B. Spremenilo se je za 360°.']) + '\n<p>Isto lahko narediš z desnim kolesom in vrati C.</p>'
slika_vrata = blk('lego-vrata-robot.png', 'Pogled na robota EV3C: motorja na vratih B in C ter senzorji na vratih 1, 2, 3 in 4 z njihovimi vrednostmi.', '560px') + cap('Pogled na robota. Ob vsakih vratih je vrednost.')

program = H2 + 'Prvi program</h2>\n' + ol([
    'Robota postavi na tla. Pred njim naj bo prosta pot vsaj 30 cm. Na mizi bi robot padel.',
    'V programu EV3 Classroom odpri nov projekt. Na delovni površini je že rumeni blok »when program starts«.',
    'Klikni paleto MOVEMENT (roza).',
    'Povleci blok »move forward for 1 rotations« tik pod rumeni blok. Bloka se zaskočita.',
    'Klikni desni gumb ▶ (prenos in zagon). Robot odpelje naprej.',
    'V pogledu na robota poglej vrata B in C. Število stopinj se je povečalo za 360°. To je en vrtljaj kolesa.'])
gumba = blk('lego-gumba-prenos-zagon.png', 'Spodaj desno v programu: levi gumb s puščico navzdol (prenos) in desni modri gumb ▶ (prenos in zagon).', '300px') + cap('Levi gumb samo prenese program na robota. Desni gumb ga prenese in zažene.') \
    + text(box('pozor', 'Roke stran', '<p style="margin-top:0">Robot odpelje takoj po kliku. Roke umakni z njegove poti in poskrbi, da je pred njim prosto.</p>'))

preveri = H2 + 'Preveri se</h2>' + q('1. Na katerih vratih je levi motor in na katerih desni?', 'Levi motor je na vratih B, desni na vratih C.') \
    + q('2. Kateri gumb program samo prenese na robota in kateri ga prenese in zažene?', 'Levi gumb (puščica navzdol) samo prenese. Desni gumb (▶) prenese in zažene.') \
    + q('3. Za koliko stopinj se zavrti kolo pri enem vrtljaju?', 'Za 360°.')
kratko = box('cilj', 'Na kratko', ul(['Robota povežeš z Bluetooth (ime EV3C) ali z USB kablom.', 'Vrata: 1 dotik, 2 žiroskop, 3 barvni, 4 ultrazvočni, B levi motor, C desni motor.', 'Levi gumb = prenos, desni gumb ▶ = prenos in zagon.', 'En vrtljaj kolesa = 360°.']))

out = sec(
    row(col('4_4', text(cilj('Spoznaj robota in program', ['povezati robota z računalnikom,', 'prebrati vrednosti na vratih,', 'prenesti program na robota in ga zagnati.']))))
  + row(col('1_2', text(poveži)) + col('1_2', slika_win + text(usb) + text(napaka)), '1_2,1_2')
  + row(col('1_2', text(vrata)) + col('1_2', slika_vrata), '1_2,1_2')
  + row(col('4_4', text(poskus)))
  + row(col('1_2', text(program)) + col('1_2', gumba), '1_2,1_2'))
out += sec(row(col('1_2', text(preveri)) + col('1_2', text(kratko)), '1_2,1_2'))
write('lego-povezava', out)
