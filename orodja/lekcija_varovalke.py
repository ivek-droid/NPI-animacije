import math
src = open('/home/claude/npi-animacije/orodja/lekcije_pomocniki_in_ivep.py').read().split('# ======================================================== SERIJSKA')[0]
exec(src)

def f(x, n=1): return f'{x:.{n}f}'.replace('.', ',')
# ---- preračun vseh števil v primerih ----
def magn(In, tip):  # spodnja in zgornja meja magnetnega sprožnika (tabela 6)
    a, b = {'B': (3, 5), 'C': (5, 10), 'D': (10, 20)}[tip]
    return a * In, b * In
assert magn(16, 'B') == (48, 80) and magn(16, 'C') == (80, 160) and magn(16, 'D') == (160, 320)
assert magn(10, 'B') == (30, 50)
assert f(230 / 1.2) == '191,7'
assert 80 <= 230 / 1.2 and 160 <= 230 / 1.2 and 320 > 230 / 1.2
assert f(230 / 0.8, 0) == '288'          # naloga Preveri se (Z_k = 0,8)
assert 63 / 25 >= 1.6 and 63 / 40 < 1.6 and 80 / 40 >= 1.6
assert f(63 / 25, 2) == '2,52' and abs(63 / 40 - 1.575) < 1e-9 and f(80 / 25, 2) == '3,20' and f(40 / 25, 2) == '1,60'
assert 25 * 1.6 == 40.0 and 40 * 1.6 == 64.0

TD = 'style="padding:8px 10px;border-bottom:1px solid #c9c4bb;text-align:left;vertical-align:top"'
def tr(c, th=False):
    t = 'th' if th else 'td'
    return '<tr>' + ''.join(f'<{t} {TD}>{x}</{t}>' for x in c) + '</tr>'
def tab(rows, head):
    return '<table style="width:100%;border-collapse:collapse;font-size:18px">' + tr(head, True) + ''.join(tr(r) for r in rows) + '</table>'
def btn(url, label, new=True):
    return f'[et_pb_button button_url="{url}" url_new_window="{"on" if new else "off"}" button_text="{label}" module_class="pg-btn" _builder_version="4.27.9" custom_margin="0||12px||false|false"][/et_pb_button]'
def korak(oznaka, vsebina, rez=False):
    v = f'<span class="pg-rezultat">{vsebina}</span>' if rez else vsebina
    return f'<li><span><span class="pg-koraki__oznaka">{oznaka}</span>{v}</span></li>'
def koraki(items): return '<ol class="pg-koraki">\n' + '\n'.join(items) + '\n</ol>'
In_ = 'I<sub>n</sub>'; Ia = 'I<sub>a</sub>'; Zk = 'Z<sub>k</sub>'; U0 = 'U<sub>0</sub>'

# ---------------- razlaga ----------------
zakaj = H2 + 'Zakaj sploh varovalka</h2>' + '''
<p>Pomisli na verigo. Če jo preveč obremeniš, poči najšibkejši člen, ostala veriga ostane cela.</p>
<p>Varovalka je namerno najšibkejši člen tokokroga. Prekine tok, preden se vodnik pregreje in se stali njegova izolacija.</p>''' \
    + box('pozor', 'Dva različna nadtoka', '''<p style="margin-top:0"><strong>Preobremenitev:</strong> tok je malo prevelik in teče dlje časa. Vodnik se počasi segreva.</p>
<p><strong>Kratek stik:</strong> upornost bremena je skoraj 0 Ω. Tok je lahko stokrat ali tisočkrat večji od nazivnega. Nevarnost je takoj.</p>''', '16px 0 0')

varovalka = H2 + 'Taljiva varovalka (gG)</h2>' + '''
<p>V ohišju je tanka žička, ki prevaja tok. Pri prevelikem toku se žička segreje in se stali. Tokokrog je prekinjen.</p>
<p>Tok se prekine v nekaj sekundah ali v delčku sekunde. Večji je nadtok, hitreje se žička stali. Nazivni tok varovalka prenaša neomejeno dolgo.</p>''' \
    + ul(['Ohišje je napolnjeno s kremenčevim peskom, ki ugasne električni oblok.', 'Barvni indikator pokaže, da je vložek pregorel.', 'Velikostni obroč prepreči, da bi vstavil vložek za večji tok.']) \
    + box('pozor', 'Nikoli ne popravljaj', '<p style="margin-top:0">Vložka ne smeš zakrpati z žico ali ga premostiti. Potem varovalke ni več. Vodnik se pregreje in lahko nastane požar.</p>', '16px 0 0')

oznaka = box('cilj', 'Kaj pomeni oznaka gG', '''<p style="margin-top:0"><strong>Prva črka (mala):</strong> kaj varovalka varuje.</p>
<p>g = pred preobremenitvijo in kratkim stikom (celotno območje)<br>a = samo pred kratkim stikom (delno območje)</p>
<p><strong>Druga črka (velika):</strong> kaj varuje.</p>
<p>G = splošna uporaba (vodniki in kabli)<br>M = elektromotorji</p>
<p>gG je torej varovalka za splošno uporabo, ki varuje pred obema nadtokoma.</p>''')

odklopnik = H2 + 'Inštalacijski odklopnik</h2>' + '''
<p>To je stikalo, ki se samo izklopi. Po izklopu ga ročno vklopiš nazaj. Zamenjava vložka ni potrebna.</p>
<p>Ima dva sprožnika, vezana zaporedno v tokokrog:</p>''' \
    + ul(['<strong>Bimetalni (toplotni)</strong> sprožnik je počasen. Varuje pred preobremenitvijo. Tok segreje bimetalni trak, ta se ukrivi in sproži zaklep.', '<strong>Elektromagnetni</strong> sprožnik je hiter. Varuje pred kratkim stikom. Velik tok v tuljavi potegne jedro in sproži zaklep.']) \
    + '<p>Prednosti pred varovalko: ponovni vklop, uporaba kot stikalo, majhna poraba prostora v razdelilni omari.</p>'

tipi = H2 + 'Tipi B, C in D</h2>' + '<p>Počasni toplotni del je pri vseh tipih enak. Tipi se razlikujejo po tem, pri kolikšnem toku sproži <strong>hitri magnetni del</strong>.</p>\n' \
    + tab([['B', '3 do 5 · ' + In_, 'vodniki v inštalacijah (razsvetljava, vtičnice)'],
           ['C', '5 do 10 · ' + In_, 'vodniki pri večjih zagonskih tokovih'],
           ['D', '10 do 20 · ' + In_, 'porabniki z zelo velikim zagonskim tokom (npr. motorji)']], ['Tip', 'Magnetni sprožnik ' + Ia, 'Kdaj']) \
    + f'''
<p style="margin-top:16px">Pod spodnjo mejo magnetni del še ne sproži. Nad zgornjo mejo <strong>zanesljivo</strong> sproži v delčku sekunde. Vmes se lahko sproži, lahko pa ne.</p>
<p style="font-size:16px;color:#4a4f5c">Tabela 6 na maturi: B: {Ia} = (3 … 5) · {In_}, C: {Ia} = (5 … 10) · {In_}, D: {Ia} = (10 … 20) · {In_}.</p>'''

nazivni = H2 + 'Nazivni toki</h2>' + f'''
<p><strong>Taljiva varovalka gG (tabela 4):</strong><br>2, 4, 6, 8, 10, 13, 16, 20, 25, 32, 35, 40, 50, 63, 80, 100, 125, 160, 200 A</p>
<p><strong>Inštalacijski odklopnik (tabela 5):</strong><br>6, 8, 10, 13, 16, 20, 25, 32, 40, 50, 63, 80, 100, 125 A</p>
<p style="font-size:16px;color:#4a4f5c">Učbenik (pregl. 20.9) navaja nekoliko drugačen nabor odklopnikov. Pri maturi uporabi tabelo 5. Kako izbereš {In_} glede na vodnik, je v lekciji <a href="https://npi.splet.arnes.si/dimenzioniranje-vodnika/">Dimenzioniranje vodnika</a>.</p>'''

selektivnost = H2 + 'Selektivnost</h2>' + '''
<p>Pomisli na hišo z glavno omarico in z omarico v kleti. Če se pokvari ena svetilka, se mora izklopiti samo njen tokokrog. Preostala hiša ostane pod napetostjo.</p>
<p><strong>Selektivnost pomeni, da nadtok prekine tista zaščitna naprava, ki je najbližje mestu okvare.</strong></p>''' \
    + box('cilj', 'Pravilo za varovalke gG', '''<p style="margin-top:0">Za nazivne tokove nad 16 A je selektivnost zagotovljena, če je razmerje nazivnih tokov dveh zaporednih varovalk vsaj 1 : 1,6.</p>
<p>Primer: 35 A in 63 A (63 / 35 = 1,8).</p>''', '16px 0 0') \
    + '<p style="margin-top:16px">Pri odklopnikih običajno že zaporedje nazivnih tokov zagotovi selektivnost.</p>'

# ---------------- rešeni primeri ----------------
p1 = box('primer', 'Rešen primer 1: odklopni tok', f'''<p style="margin-top:0">V tokokrogu je odklopnik 16 A. Ob kratkem stiku teče 100 A. Ali tip B ali tip C zanesljivo sproži hitri magnetni del?</p>
''' + koraki([
    korak('Podatki', f'{In_} = 16 A, tok kratkega stika 100 A'),
    korak('Iskano', f'zgornja meja magnetnega sprožnika {Ia} za tip B in tip C'),
    korak('Formula', f'B: {Ia} = (3 … 5) · {In_}, C: {Ia} = (5 … 10) · {In_}'),
    korak('Vstavim', 'B: 3 · 16 = 48 A … 5 · 16 = 80 A, C: 5 · 16 = 80 A … 10 · 16 = 160 A'),
    korak('Primerjam', 'B: 100 A &gt; 80 A, to je nad zgornjo mejo. C: 100 A &lt; 160 A, to je pod zgornjo mejo.'),
    korak('Rezultat', 'tip B zanesljivo sproži, tip C ne', True),
    korak('Preverim', 'Tip C ima višje meje, zato potrebuje večji tok. 100 A je v njegovem območju 80 … 160 A, kjer sprožitev ni zagotovljena.'),
]) + '\n') + box('pozor', 'Pogosta napaka', '<p>Primerjaš s spodnjo mejo (3 · In ali 5 · In). Spodnja meja ne zagotavlja izklopa. Za zanesljiv izklop vedno vzemi zgornjo mejo.</p>', '16px 0 0')

p2 = box('primer', 'Rešen primer 2: samodejni odklop', f'''<p style="margin-top:0">Zanka okvare ima impedanco {Zk} = 1,2 Ω, napetost proti zemlji je {U0} = 230 V. Za zaščito s samodejnim odklopom mora veljati {Zk} · {Ia} ≤ {U0}. Kateri od odklopnikov B16, C16 in D16 ustreza?</p>
''' + koraki([
    korak('Podatki', f'{Zk} = 1,2 Ω, {U0} = 230 V, odklopniki B16, C16, D16'),
    korak('Iskano', f'ali velja {Zk} · {Ia} ≤ {U0}'),
    korak('Formula', f'{Ia} ≤ {U0} / {Zk}'),
    korak('Vstavim', f'{Ia} ≤ 230 / 1,2 = 191,7 A'),
    korak('Zgornje meje', 'B16: 5 · 16 = 80 A, C16: 10 · 16 = 160 A, D16: 20 · 16 = 320 A'),
    korak('Primerjam', '80 A ≤ 191,7 A ✓, 160 A ≤ 191,7 A ✓, 320 A &gt; 191,7 A ✗'),
    korak('Rezultat', 'ustrezata B16 in C16, D16 ne ustreza', True),
    korak('Preverim', f'Pri D16 bi moral teči vsaj 320 A, zanka pa pri 230 V dovoli največ 191,7 A. Odklopnik ne bi sprožil zanesljivo.'),
]) + '\n') + box('pozor', 'Pogosta napaka', '<p>Vzameš spodnjo mejo magnetnega sprožnika. Potem se ti zdi, da ustreza tudi D16 (10 · 16 = 160 A). Za zanesljiv odklop vzemi zgornjo mejo.</p>', '16px 0 0')

p3 = box('primer', 'Rešen primer 3: selektivnost', '''<p style="margin-top:0">Pred porabnikom je varovalka gG 25 A. Kakšna sme biti varovalka pred njo: 40 A, 63 A ali 80 A?</p>
''' + koraki([
    korak('Podatki', 'manjša varovalka 25 A, kandidati 40 A, 63 A, 80 A'),
    korak('Iskano', 'razmerje nazivnih tokov vsaj 1 : 1,6'),
    korak('Najmanjša vrednost', '25 · 1,6 = 40 A'),
    korak('Razmerja', '40 / 25 = 1,60, 63 / 25 = 2,52, 80 / 25 = 3,20'),
    korak('Rezultat', 'ustrezajo vse tri (40 A je prav na meji)', True),
    korak('Preverim', 'Vsi presegajo 1,6. Najmanjša ustrezna je 40 A, ker je v tabeli 4.'),
]) + '\n') + box('pozor', 'Pogosta napaka', '<p>Predpostaviš, da zadošča naslednja vrednost iz tabele. Za 40 A in 63 A razmerje znaša le 63 / 40 = 1,58. To je manj kot 1,6, zato selektivnost ni zagotovljena.</p>', '16px 0 0')

# ---------------- zaključek ----------------
preveri = H2 + 'Preveri se</h2>' \
    + q('1. Zakaj vložka taljive varovalke ne smeš premostiti z žico?', 'Potem varovalke ni več. Vodnik ni zaščiten pred nadtokom, pregreje se in lahko povzroči požar.') \
    + q('2. Odklopnik B10: pri katerem toku zanesljivo sproži hitri magnetni del?', f'Pri toku nad zgornjo mejo 5 · 10 = 50 A. Spodnja meja je 3 · 10 = 30 A. Med 30 A in 50 A sprožitev ni zagotovljena.') \
    + q('3. Zanka ima Z<sub>k</sub> = 0,8 Ω in U<sub>0</sub> = 230 V. Ali ustreza odklopnik D16?', f'{Ia} ≤ 230 / 0,8 = 288 A. Za D16 je zgornja meja 20 · 16 = 320 A. 320 A &gt; 288 A, zato D16 ne ustreza. Ustreza C16 (160 A).')
kratko = box('cilj', 'Na kratko', ul(['Varovalka je najšibkejši člen tokokroga.', 'gG: varuje pred preobremenitvijo in kratkim stikom, vložek se po izklopu zamenja.', 'Odklopnik: bimetal za preobremenitev, elektromagnet za kratek stik.', f'Tip B: 3 … 5 · {In_}, C: 5 … 10 · {In_}, D: 10 … 20 · {In_}. Za zanesljiv izklop vzemi zgornjo mejo.', 'Selektivnost gG: razmerje nazivnih tokov vsaj 1 : 1,6 (nad 16 A).']))
matura = box('matura', 'Matura', '<p>Tabele 4, 5 in 6 ter pogoj samodejnega odklopa imaš na listu s formulami. Za vajo odpri zbirko nalog.</p>\n<p><a href="https://npi.splet.arnes.si/elektricne-instalacije/">Zbirka maturitetnih nalog</a> · <a href="https://www.ric.si/poklicna-matura/predmeti/drugi-predmet/elektrotehnika/">Maturitetno gradivo (RIC)</a></p>', '16px 0 0')

out = sec(
    row(col('4_4', text(cilj('Varovalke in odklopniki', ['povedati, kaj varujejo varovalka in odklopnik,', 'razložiti, kako deluje taljiva varovalka gG in inštalacijski odklopnik,', 'ločiti tipe odklopnikov B, C in D ter izračunati njihov odklopni tok,', 'preveriti selektivnost dveh varovalk,', 'izbrati tip odklopnika za samodejni odklop.']))))
  + row(col('1_2', text(zakaj)) + col('1_2', text(varovalka)), '1_2,1_2')
  + row(col('1_2', text(oznaka)) + col('1_2', text(odklopnik)), '1_2,1_2')
  + row(col('1_2', text(tipi)) + col('1_2', text(nazivni) + btn(U + '2024/01/formule-na-maturi.pdf', 'Formule na maturi (PDF)')), '1_2,1_2')
  + row(col('4_4', text(selektivnost))))
out += sec(row(col('1_2', text(p1)) + col('1_2', text(p2)), '1_2,1_2') + row(col('1_2', text(p3)) + col('1_2', text(kratko)), '1_2,1_2'), '#f5f3ef')
out += sec(row(col('1_2', text(preveri)) + col('1_2', text(matura)), '1_2,1_2'))
write('varovalke-in-odklopniki', out)
