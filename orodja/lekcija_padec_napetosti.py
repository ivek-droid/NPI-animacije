import math
src = open('/home/claude/npi-animacije/orodja/lekcije_pomocniki_in_ivep.py').read().split('# ======================================================== SERIJSKA')[0]
exec(src)

LAM = 56
def d1(l, P, A, U=230): return 200 * l * P / (LAM * A * U ** 2)
def d3(l, P, A, U=400): return 100 * l * P / (LAM * A * U ** 2)
def f(x, n=2): return f'{x:.{n}f}'.replace('.', ',')
# ---- preračun vseh števil v primerih ----
assert f(2 * 14 * 10 / (LAM * 2)) == '2,50'
assert f(d1(20, 2500, 1.5)) == '2,25' and f(2 * d1(20, 2500, 1.5)) == '4,50'
assert f(LAM * 25 * 1.5 * 400 ** 2 / (100 * 38000), 1) == '88,4'
assert f(d3(120, 38000, 25)) == '2,04' and f(d3(120, 38000, 35)) == '1,45'
assert f(d1(30, 2000, 1.5)) == '2,70'
assert f(2 * 14 * 10 / (LAM * 2) / 2, 2) == '1,25'

TD = 'style="padding:8px 10px;border-bottom:1px solid #c9c4bb;text-align:left;vertical-align:top"'
def tr(c, th=False):
    t = 'th' if th else 'td'
    return '<tr>' + ''.join(f'<{t} {TD}>{x}</{t}>' for x in c) + '</tr>'
def tab(rows, head):
    return '<table style="width:100%;border-collapse:collapse;font-size:18px">' + tr(head, True) + ''.join(tr(r) for r in rows) + '</table>'
def btn(url, label):
    return f'[et_pb_button button_url="{url}" url_new_window="on" button_text="{label}" module_class="pg-btn" _builder_version="4.27.9" custom_margin="0||12px||false|false"][/et_pb_button]'
def korak(oznaka, vsebina, rez=False):
    v = f'<span class="pg-rezultat">{vsebina}</span>' if rez else vsebina
    return f'<li><span><span class="pg-koraki__oznaka">{oznaka}</span>{v}</span></li>'
def koraki(items): return '<ol class="pg-koraki">\n' + '\n'.join(items) + '\n</ol>'
du = 'Δu'; dU = 'ΔU'
Uf = 'U<sub>f</sub>'

kaj = H2 + '''Zakaj napetost na koncu vodnika pade</h2>
<p>Pomisli na dolg tanek vrtni cevovod. Voda na koncu teče šibkeje kot na pipi.</p>
<p>Tudi vodnik se upira toku. Ima upornost R. Na njej nastane padec napetosti ΔU = I · R. Porabnik zato dobi manj napetosti, kot je ima vir.</p>
<p>Upornost je večja, če je vodnik daljši ali tanjši. Tok teče po poti tja in nazaj, zato vzamemo <strong>dvakratno dolžino 2 · l</strong>.</p>'''
def_ = box('cilj', 'Definicija', f'''<p style="margin-top:0">Padec napetosti je razlika med napetostjo na viru in na porabniku.</p>
<p>{dU} = U<sub>vir</sub> − U<sub>porabnik</sub> (v V)</p>
<p>{du} = {dU} / U<sub>vir</sub> · 100 (v %)</p>
<p>Primer: vir 230 V, porabnik 225 V. ΔU = 5 V, Δu = 5 / 230 · 100 = 2,17 %.</p>''')

enofazno = box('cilj', 'Enofazni tokokrog (U<sub>f</sub> = 230 V)', f'''<p style="margin-top:0">{du} = 200 · l · P / (λ · A · U<sub>f</sub>²)</p>
<p>A = 200 · l · P / (λ · {du} · U<sub>f</sub>²)</p>
<p>l = λ · A · {du} · U<sub>f</sub>² / (200 · P)</p>''')
trifazno = box('cilj', 'Trifazni tokokrog (U = 400 V)', f'''<p style="margin-top:0">{du} = 100 · l · P / (λ · A · U²)</p>
<p>A = 100 · l · P / (λ · {du} · U²)</p>
<p>l = λ · A · {du} · U² / (100 · P)</p>''') + box('pozor', 'Enote', '<p>l v m, P v W, A v mm², λ = 56 S·m/mm², napetost v V, Δu v %. Pri trifaznem tokokrogu je U medfazna napetost 400 V.</p>', '16px 0 0')

postopek = H2 + 'Postopek v petih korakih</h2>\n' + ol([
    'Zapiši podatke: l, P, napetost in λ = 56 S·m/mm².',
    f'Določi dopustni padec {du} (naloga ali tabela 7).',
    f'Izračunaj presek A iz formule.',
    'Izberi prvi standardni presek, ki je ≥ izračunani: 1,5; 2,5; 4; 6; 10; 16; 25; 35; 50 mm².',
    'Preveri še segrevanje (lekcija <a href="https://npi.splet.arnes.si/dimenzioniranje-vodnika/">Dimenzioniranje vodnika</a>). Vzemi večji presek od obeh.'])
tabela7 = H2 + 'Dopustni padec napetosti (tabela 7)</h2>\n' + tab([
    ['3 %', 'razsvetljava, napajanje iz nizkonapetostnega omrežja'],
    ['5 %', 'razsvetljava, napajanje iz lastne transformatorske postaje'],
    ['5 %', 'drugi porabniki, napajanje iz nizkonapetostnega omrežja'],
    ['8 %', 'drugi porabniki, napajanje iz lastne transformatorske postaje']], ['Δu', 'Kje velja']) + \
    '\n<p style="font-size:16px;color:#4a4f5c">Če naloga poda vrednost, uporabi njo. Učbenik za vse porabnike navaja 3 %.</p>'

p1 = box('primer', 'Rešen primer 1: potreben presek', f'''<p style="margin-top:0">Fazni porabnik je napajan po vodniku dolžine 14 m. Specifična prevodnost je λ = 56 S·m/mm², tok je 10 A, padec napetosti 2 V. Izračunaj presek vodnika.</p>
''' + koraki([
    korak('Podatki', 'l = 14 m, I = 10 A, ΔU = 2 V, λ = 56 S·m/mm²'),
    korak('Iskano', 'presek A'),
    korak('Formula', 'ΔU = 2 · l · I / (λ · A), zato A = 2 · l · I / (λ · ΔU)'),
    korak('Vstavim', 'A = 2 · 14 m · 10 A / (56 S·m/mm² · 2 V)'),
    korak('Izračunam', 'A = 280 / 112 = 2,50 mm²'),
    korak('Rezultat', 'A = 2,5 mm² (standardni presek)', True),
    korak('Preverim', 'Tok 10 A, vodnik 2,5 mm²: ΔU = 2 · 14 · 10 / (56 · 2,5) = 2 V ✓'),
]) + '\n') + box('pozor', 'Pogosta napaka', '<p>Pozabiš na število 2 (pot tja in nazaj). Dobiš 1,25 mm² in izbereš 1,5 mm². Vodnik je pretanek.</p>', '16px 0 0')

p2 = box('primer', 'Rešen primer 2: preveri padec', f'''<p style="margin-top:0">Grelnik moči 2,5 kW je priključen na 230 V z vodnikom 1,5 mm², dolgim 20 m. Ali je padec napetosti pod 3 %?</p>
''' + koraki([
    korak('Podatki', 'P = 2500 W, U<sub>f</sub> = 230 V, l = 20 m, A = 1,5 mm², λ = 56 S·m/mm²'),
    korak('Iskano', f'{du}'),
    korak('Formula', f'{du} = 200 · l · P / (λ · A · U<sub>f</sub>²)'),
    korak('Vstavim', f'{du} = 200 · 20 · 2500 / (56 · 1,5 · 230²)'),
    korak('Izračunam', f'{du} = 10 000 000 / 4 443 600 = 2,25 %'),
    korak('Rezultat', f'{du} = 2,25 % ≤ 3 % ✓', True),
    korak('Preverim', 'Vodnik je kratek, tok majhen: pričakujemo manj kot 3 %.'),
]) + '\n') + box('pozor', 'Pogosta napaka', '<p>Faktor 2 dodaš še enkrat. Formula z 200 ga že vsebuje (2 · 100). Dobiš 4,5 % in napačen sklep, da vodnik ni dober.</p>', '16px 0 0')

p3 = box('primer', 'Rešen primer 3: največja dolžina', f'''<p style="margin-top:0">Trifazni porabnik 38 kW na 400 V je priključen s kablom 25 mm². Dopustni padec je 1,5 %. Kako dolg je lahko kabel?</p>
''' + koraki([
    korak('Podatki', 'P = 38 000 W, U = 400 V, A = 25 mm², Δu = 1,5 %, λ = 56 S·m/mm²'),
    korak('Iskano', 'dolžina l'),
    korak('Formula', f'l = λ · A · {du} · U² / (100 · P)'),
    korak('Vstavim', 'l = 56 · 25 · 1,5 · 400² / (100 · 38 000)'),
    korak('Izračunam', 'l = 336 000 000 / 3 800 000 = 88,4 m'),
    korak('Rezultat', 'l = 88,4 m', True),
    korak('Preverim', f'{du} pri 88,4 m: 100 · 88,4 · 38 000 / (56 · 25 · 400²) = 1,5 % ✓'),
]) + '\n') + box('pozor', 'Pogosta napaka', '<p>V trifazni formuli vzameš 230 V. Pri trifazni formuli je U = 400 V.</p>', '16px 0 0')

dva = box('pozor', 'Dva preverjanja, en presek', f'''<p style="margin-top:0">Presek mora zadostiti <strong>segrevanju</strong> in <strong>padcu napetosti</strong>. Končni presek je večji od obeh.</p>
<p>Primer: kabel za 38 kW je dolg 120 m. Pri 25 mm² je Δu = 100 · 120 · 38 000 / (56 · 25 · 400²) = 2,04 %. To je več kot 1,5 %. Pri 35 mm² je Δu = 1,45 % ✓. Vzamemo 35 mm², čeprav segrevanje zadošča že pri 25 mm².</p>''')

preveri = H2 + 'Preveri se</h2>' \
    + q('1. Zakaj je v formuli za enofazni tokokrog število 2?', 'Tok teče po faznem vodniku do porabnika in po nevtralnem nazaj. Pot je dvakrat daljša od dolžine kabla.') \
    + q('2. Enofazni porabnik 2000 W na 230 V, vodnik 1,5 mm², dolžina 30 m. Koliko je Δu?', 'Δu = 200 · 30 · 2000 / (56 · 1,5 · 230²) = 12 000 000 / 4 443 600 = 2,70 %. To je manj kot 3 %, vodnik ustreza.') \
    + q('3. Za segrevanje zadošča 2,5 mm², za padec napetosti pa potrebuješ 4 mm². Kateri presek vzameš?', '4 mm². Končni presek je večji od obeh.')
kratko = box('cilj', 'Na kratko', ul(['Padec napetosti je razlika med virom in porabnikom.', 'Pot toka je 2 · l, zato je v enofazni formuli 200 = 2 · 100.', 'Enofazno U<sub>f</sub> = 230 V, trifazno U = 400 V.', 'Najprej izračunaj presek, nato izberi standardnega.', 'Presek mora zadostiti segrevanju in padcu napetosti.']))
matura = box('matura', 'Matura', '<p>Formule za padec napetosti in tabelo 7 imaš na listu s formulami. Za vajo odpri zbirko nalog (spomladanski rok 2023, naloga 19; zimski rok 2020, 2021 in 2022, naloge 5).</p>\n<p><a href="https://npi.splet.arnes.si/elektricne-instalacije/">Zbirka maturitetnih nalog</a> · <a href="https://www.ric.si/poklicna-matura/predmeti/drugi-predmet/elektrotehnika/">Maturitetno gradivo (RIC)</a></p>', '16px 0 0')

out = sec(
    row(col('4_4', text(cilj('Padec napetosti na vodniku', ['povedati, zakaj napetost na porabniku pade,', f'izračunati padec napetosti {dU} in {du},', 'izračunati potreben presek in največjo dolžino vodnika,', 'izbrati presek, ki zadošča tudi segrevanju.']))))
  + row(col('1_2', text(kaj)) + col('1_2', text(def_)), '1_2,1_2')
  + row(col('1_2', text(enofazno)) + col('1_2', text(trifazno)), '1_2,1_2')
  + row(col('1_2', text(postopek)) + col('1_2', text(tabela7) + btn(U + '2024/01/formule-na-maturi.pdf', 'Formule na maturi (PDF)')), '1_2,1_2'))
out += sec(row(col('1_2', text(p1)) + col('1_2', text(p2)), '1_2,1_2') + row(col('1_2', text(p3)) + col('1_2', text(dva)), '1_2,1_2'), '#f5f3ef')
out += sec(row(col('1_2', text(preveri)) + col('1_2', text(kratko) + text(matura)), '1_2,1_2'))
write('padec-napetosti', out)
