src = open('/home/claude/npi-animacije/orodja/lekcije_pomocniki_in_ivep.py').read().split('# ======================================================== SERIJSKA')[0]
exec(src)

import sys
SLIKA = sys.argv[1] if len(sys.argv) > 1 else '2026/11/iskra-mi7043.jpg'
def f(x, n=1): return f'{x:.{n}f}'.replace('.', ',')

# ---- preračun vseh števil (skale iz odcitavanje-instrumenta.html) ----
# primer 1: 15 V =, črna 0-15 (75 razdelkov), kazalec na 45. razdelku
k1 = 15 / 75; U1 = 45 * k1
assert f(k1) == '0,2' and f(U1) == '9,0'
assert f(10 - 5 * k1) == '9,0'                  # 5 razdelkov pred številko 10
assert f(45 / 75 * 100, 0) == '60'
assert f(45 / 75 * 5) == '3,0'                  # napaka: odčitek na skali 0-5
# primer 2: 300 V ~, rdeča 0-30 (30 razdelkov), kazalec na 23. razdelku
k2 = 300 / 30; U2 = 23 * k2
assert f(k2, 0) == '10' and f(U2, 0) == '230'
assert f(200 + 3 * k2, 0) == '230'              # 3 razdelki za številko 20 (200 V)
assert f(23 / 30 * 100, 0) == '77'
# preveri se
assert f(5 / 50) == '0,1' and f(32 * 5 / 50) == '3,2'
assert f(100 / 50, 0) == '2' and f(37 * 100 / 50, 0) == '74'

def korak(oznaka, vsebina, rez=False):
    v = f'<span class="pg-rezultat">{vsebina}</span>' if rez else vsebina
    return f'<li><span><span class="pg-koraki__oznaka">{oznaka}</span>{v}</span></li>'
def koraki(items): return '<ol class="pg-koraki">\n' + '\n'.join(items) + '\n</ol>'

TD = 'style="padding:8px 10px;border-bottom:1px solid #c9c4bb;text-align:left;vertical-align:top"'
def tr(c, th=False):
    t = 'th' if th else 'td'
    return '<tr>' + ''.join(f'<{t} {TD}>{x}</{t}>' for x in c) + '</tr>'
def tab(rows, head):
    return '<table style="width:100%;border-collapse:collapse;font-size:18px">' + tr(head, True) + ''.join(tr(r) for r in rows) + '</table>'

kaj = H2 + '''Kaj kaže kazalec</h2>
<p>Pomisli na kuhinjsko tehtnico s kazalcem. Na njej piše 0–5 kg. Kazalec ti pove samo, kje je. Koliko to je, ti pove skala.</p>
<p>Univerzalni merilnik je enak. S stikalom izbereš <strong>merilno območje</strong>. To je vrednost, ki jo kaže kazalec na koncu skale. Ko območje spremeniš, se spremeni tudi vrednost vsakega razdelka.</p>
<p>Merilnik meri napetost (V), tok (A), enosmerno (=) in izmenično (~).</p>'''

skale = H2 + '''Skale na merilniku</h2>
<p>Enosmerne vrednosti (=) odčitavaš na <strong>črni</strong> skali, izmenične (~) na <strong>rdeči</strong>.</p>
''' + tab([['črna 0–5', '50', '10'], ['črna 0–15', '75', '25'], ['rdeča 0–10', '50', '10'], ['rdeča 0–30', '30', '10']],
          ['Skala', 'Razdelkov (N)', 'Med številkama'])

navodila = H2 + 'Kako izmeriš</h2>\n' + ol([
    'Ugotovi, kaj meriš: <strong>napetost</strong> ali <strong>tok</strong>, <strong>enosmerno</strong> (=) ali <strong>izmenično</strong> (~). Drsnik nad stikalom postavi na ~ ali =.',
    'Z vrtljivim stikalom izberi območje. Beli napisi so za enosmerno, rdeči za izmenično. Če vrednosti ne poznaš, izberi <strong>največje</strong> območje. Nato preklopi na manjše, dokler kazalec ni v drugi polovici skale.',
    '<strong>Voltmeter</strong> priključiš <strong>vzporedno</strong> s porabnikom. <strong>Ampermeter</strong> priključiš <strong>zaporedno</strong>: krog prekineš in merilnik vključiš vmes.',
    'Izberi skalo, ki ustreza območju. Območje je končna številka skale ali njen večkratnik z 10, 100 … (območje 15 V → skala 0–15, območje 300 V → skala 0–30).',
    'Preštej razdelke <strong>α</strong> od ničle do kazalca. Glej naravnost nanj. Če ima skala zrcalo, se morata kazalec in njegova slika pokrivati.',
    'Izračunaj: <strong>k = območje / N</strong> in <strong>X = α · k</strong>. Napiši enoto.']) \
    + '\n<p><strong>k</strong> je vrednost enega razdelka. <strong>N</strong> je število razdelkov na skali.</p>'

pozor = box('pozor', 'Pozor', '<p>Ampermetra nikoli ne priključi vzporedno z virom ali porabnikom. Nastane kratek stik.</p>\n<p>Pred priključitvijo ampermetra izklopi napajanje.</p>') \
    + box('pozor', 'Pozor', '<p>Napetost omrežja (230 V) je nevarna. Meri jo samo ob učitelju.</p>', '16px 0 0')

p1 = box('primer', 'Rešen primer 1: enosmerna napetost', '''<p style="margin-top:0">Merilnik je na območju 15 V =. Kazalec je na črni skali 0–15 na 45. razdelku. Koliko voltov kaže?</p>
''' + koraki([
    korak('Podatki', 'drsnik =, stikalo 15 V (bel napis), črna skala 0–15, N = 75, α = 45'),
    korak('Iskano', 'napetost U = ?'),
    korak('Formula', 'k = območje / N in U = α · k'),
    korak('Vstavim', 'k = 15 V / 75 = 0,2 V na razdelek'),
    korak('Vstavim', 'U = 45 · 0,2 V'),
    korak('Rezultat', 'U = 9,0 V', True),
    korak('Preverim', 'Kazalec je 5 razdelkov pred številko 10. Torej 10 V − 5 · 0,2 V = 9,0 V. Rezultat je manjši od območja 15 V.')]) + '''
''') + box('pozor', 'Pogosta napaka', '<p>Odčitaš napačno skalo. Kazalec je pri 60 % skale. Na skali 0–5 bi prebral 3,0 V namesto 9,0 V.</p>', '16px 0 0')

p2 = box('primer', 'Rešen primer 2: izmenična napetost', '''<p style="margin-top:0">Merilnik je na območju 300 V ~. Kazalec je na rdeči skali 0–30 na 23. razdelku. Koliko voltov kaže?</p>
''' + koraki([
    korak('Podatki', 'drsnik ~, stikalo 300 V (rdeč napis), rdeča skala 0–30, N = 30, α = 23'),
    korak('Iskano', 'napetost U = ?'),
    korak('Formula', 'k = območje / N in U = α · k'),
    korak('Vstavim', 'k = 300 V / 30 = 10 V na razdelek'),
    korak('Vstavim', 'U = 23 · 10 V'),
    korak('Rezultat', 'U = 230 V', True),
    korak('Preverim', 'Kazalec je 3 razdelke za številko 20, ki pomeni 200 V. Torej 200 V + 3 · 10 V = 230 V. To je običajna napetost omrežja.')]) + '''
''') + box('pozor', 'Pogosta napaka', '<p>Odčitaš 23 in pozabiš na faktor 10. Napišeš 23 V namesto 230 V. Vedno izračunaj k.</p>', '16px 0 0')

preveri = H2 + 'Preveri se</h2>' \
    + q('1. Območje 5 V =, črna skala 0–5, kazalec na 32. razdelku. Koliko voltov kaže?',
        'k = 5 V / 50 = 0,1 V na razdelek. U = 32 · 0,1 V = 3,2 V.') \
    + q('2. Območje 100 V ~. Katero skalo uporabiš in koliko voltov kaže kazalec na 37. razdelku?',
        'Izmenično → rdeča skala 0–10 (N = 50). k = 100 V / 50 = 2 V na razdelek. U = 37 · 2 V = 74 V.') \
    + q('3. Kako priključiš ampermeter?',
        'Zaporedno. Krog prekineš in merilnik vključiš vmes, da gre skozenj ves tok. Voltmeter priključiš vzporedno.')

kratko = box('cilj', 'Na kratko', ul([
    '= → črna skala, ~ → rdeča skala.',
    'k = območje / N, X = α · k.',
    'Ne poznaš vrednosti? Začni z največjim območjem.',
    'Voltmeter vzporedno, ampermeter zaporedno.',
    'Rezultat mora biti manjši od območja.']))

out = sec(
    row(col('4_4', text(cilj('Uporaba univerzalnega merilnika', [
        'izbrati veličino, vrsto toka in merilno območje,',
        'pravilno priključiti voltmeter in ampermeter,',
        'odčitati kazalec in izračunati izmerjeno vrednost.']))))
  + row(col('1_2', text(kaj) + text(skale)) + col('1_2', img(SLIKA, 'Analogni univerzalni merilnik Iskra MI 7043: zgoraj skale s kazalcem (črni 0–5 in 0–15, rdeči 0–10 in 0–30), pod njimi drsnik ~ / = in vrtljivo stikalo z območji za napetost (levo) in tok (desno).') + cap('Univerzalni merilnik Iskra MI 7043.')), '1_2,1_2')
  + row(col('1_2', text(navodila)) + col('1_2', text(pozor)), '1_2,1_2')
  + row(col('1_2', text(p1)) + col('1_2', text(p2)), '1_2,1_2'))
out += sec(row(col('4_4', text(H2 + 'Preizkusi sam: priključitev merilnikov</h2>\n<p>Priključi ampermeter in voltmeter v tokokrog. Tok merimo zaporedno: najprej odstrani mostiček, nato vstavi ampermeter na njegovo mesto. Napetost merimo vzporedno s porabnikom. Uporabiš lahko tudi tipko Tab in Enter.</p>\n'
    + f'[iframe src="{GH}priklop-merilnikov.html?kompakt" width="100%" height="1220" title="Animacija: priključitev voltmetra in ampermetra"]')
    + f'[et_pb_button button_url="{GH}priklop-merilnikov.html" url_new_window="on" button_text="Odpri animacijo v celem oknu" module_class="pg-btn" _builder_version="4.27.9"][/et_pb_button]')), '#f5f3ef')
out += sec(row(col('4_4', anim('odcitavanje-instrumenta.html', 'odčitavanje univerzalnega instrumenta',
    'Nastavi merilnik, preštej razdelke in izračunaj vrednost. Nato preveri rezultat.', 1450))), '#f5f3ef')
out += sec(row(col('1_2', text(preveri)) + col('1_2', text(kratko)), '1_2,1_2'))
write('uporaba-merilnika', out)
