import math
src = open('/home/claude/npi-animacije/orodja/lekcije_pomocniki_in_ivep.py').read().split('# ======================================================== SERIJSKA')[0]
exec(src)

# ---- preračun vseh števil v primerih (če se kaj ne ujema, generator se ustavi) ----
def f(x, n=2): return f'{x:.{n}f}'.replace('.', ',')
Ib1 = 2000 / 230
Ib2 = 38000 / (math.sqrt(3) * 400)
Ib3 = 2500 / 230
assert f(Ib1) == '8,70' and f(Ib2) == '54,85' and f(Ib3) == '10,87'
assert 1.9 * 10 == 19 and round(1.45 * 14, 1) == 20.3
assert round(1.6 * 63, 1) == 100.8 and round(1.45 * 64, 1) == 92.8 and round(1.45 * 82, 1) == 118.9
assert round(1.9 * 13, 1) == 24.7 and round(1.45 * 18.5, 1) == 26.8
assert f(3000 / 230) == '13,04' and round(1.6 * 16, 1) == 25.6 and round(1.45 * 20, 1) == 29.0

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
Ib_ = 'I<sub>b</sub>'; In_ = 'I<sub>n</sub>'; Iz_ = 'I<sub>z</sub>'; I2_ = 'I<sub>2</sub>'

kaj = H2 + f'''Zakaj vodnik ne sme biti pretanek</h2>
<p>Pomisli na podaljšek, na katerega priključiš grelnik. Podaljšek se segreje. Tanek podaljšek se segreje bolj kot debel.</p>
<p>Izolacija iz PVC prenese 70 °C. Pri višji temperaturi se pokvari. Zato vsak vodnik trajno prenese le omejen tok. Ta tok je <strong>zdržni tok {Iz_}</strong>.</p>
<p>Varovalka ali odklopnik prekine tok, preden se vodnik pregreje. Njen <strong>nazivni tok {In_}</strong> mora biti manjši od zdržnega toka vodnika.</p>'''
pravilo1 = box('cilj', '1. pogoj', f'''<p style="font-size:26px;font-weight:700;margin-top:0">{Ib_} ≤ {In_} ≤ {Iz_}</p>
''' + ul([f'<strong>{Ib_}</strong>: tok, ki ga porabnik vleče (bremenski tok)', f'<strong>{In_}</strong>: nazivni tok varovalke ali odklopnika', f'<strong>{Iz_}</strong>: tok, ki ga vodnik trajno prenese (zdržni tok)']) + '<p>Pomni: porabnik &lt; varovalka &lt; vodnik.</p>')

postopek = H2 + 'Postopek v šestih korakih</h2>\n' + ol([
    f'<strong>Bremenski tok.</strong> Enofazno: {Ib_} = P / U<sub>f</sub>. Trifazno: {Ib_} = P / (√3 · U · cos φ).',
    '<strong>Način polaganja</strong> (A1, A2, B1, B2, C, D) in število obremenjenih vodnikov (2 ali 3). Podatka sta v nalogi.',
    f'<strong>Nazivni tok {In_}.</strong> Vzemi najmanjšo vrednost, ki je večja ali enaka {Ib_}. Za taljive varovalke je tabela 4, za odklopnike tabela 5.',
    f'<strong>Presek.</strong> V tabeli 3 poišči najmanjši presek, pri katerem je {Iz_} ≥ {In_}. Če je v skupini več tokokrogov, uporabi {Iz_}\' = {Iz_} · f<sub>p</sub> (tabela 1).',
    f'<strong>2. pogoj:</strong> k · {In_} ≤ 1,45 · {Iz_}\'. Faktor k je v tabeli 2.',
    f'<strong>Če 2. pogoj ne drži,</strong> vzemi večji presek. Varovalke ne povečuj.']) + '\n<p style="font-size:16px;color:#4a4f5c">Formule so zapisane z navadnim besedilom. Tabele 1 do 5 so na listu s formulami za maturo.</p>'

tab2 = tab([['taljiva varovalka, I<sub>n</sub> ≤ 4 A', '2,1'], ['taljiva varovalka, I<sub>n</sub> ≤ 13 A', '1,9'], ['taljiva varovalka, I<sub>n</sub> ≥ 16 A', '1,6'], ['inštalacijski odklopnik', '1,45'], ['odklopnik', '1,2']], ['Zaščitna naprava', 'k'])
tab1 = tab([['1', '1'], ['2', '0,8'], ['3', '0,7'], ['4', '0,65'], ['5', '0,6'], ['6', '0,55'], ['7', '0,55'], ['8', '0,5'], ['10', '0,5']], ['Število tokokrogov v skupini', 'f<sub>p</sub>'])
tabele = H2 + f'Tabela 2: faktor k</h2>\n<p>Zgornji preizkusni tok zaščitne naprave je {I2_} = k · {In_}.</p>\n' + tab2 + \
    H2.replace('margin-top:0', 'margin-top:24px') + 'Tabela 1: skupina tokokrogov</h2>\n<p>Tokokrogi v skupini na površini, v cevi ali v zaprtem kanalu.</p>\n' + tab1

# ---- rešeni primeri ----
p1 = box('primer', 'Rešen primer 1', f'''<p style="margin-top:0">Grelnik vode ima moč 2 kW in je priključen na fazno napetost 230 V. Vodnik je v kabelski cevi neposredno v toplotni izolaciji (način A2), z dvema obremenjenima vodnikoma. Zaščita je taljiva varovalka.</p>
''' + koraki([
    korak('Podatki', 'P = 2000 W, U<sub>f</sub> = 230 V, način A2, 2 obremenjena vodnika, taljiva varovalka'),
    korak('Iskano', f'{Ib_}, {In_}, presek A'),
    korak('Formula', f'{Ib_} = P / U<sub>f</sub>'),
    korak('Vstavim', f'{Ib_} = 2000 W / 230 V = 8,70 A'),
    korak('Varovalka', f'{In_} = 10 A (najmanjša, ki je ≥ 8,70 A; tabela 4)'),
    korak('Vodnik', f'1,5 mm², A2, 2 vodnika: {Iz_} = 14 A (tabela 3)'),
    korak('1. pogoj', f'8,70 A ≤ 10 A ≤ 14 A ✓'),
    korak('2. pogoj', f'k = 1,9, ker je {In_} ≤ 13 A. 1,9 · 10 A = 19 A. 1,45 · 14 A = 20,3 A. 19 A ≤ 20,3 A ✓'),
    korak('Rezultat', f'A = 1,5 mm², {In_} = 10 A', True),
    korak('Preverim', f'Varovalka je med porabnikom (8,70 A) in vodnikom (14 A).'),
]) + '\n') + box('pozor', 'Pogosta napaka', f'<p>Izbereš varovalko 13 A, ker je bližje 14 A. Potem je 1,9 · 13 A = 24,7 A, to je več kot 20,3 A. 2. pogoj ne drži.</p>', '16px 0 0')

p2 = box('primer', 'Rešen primer 2', f'''<p style="margin-top:0">Trifazni porabnik ima moč 38 kW, napetost 400 V in cos φ = 1. Kabel je v zemlji (način D), z tremi obremenjenimi vodniki. Zaščita je taljiva varovalka.</p>
''' + koraki([
    korak('Podatki', 'P = 38 000 W, U = 400 V, cos φ = 1, način D, 3 vodniki, taljiva varovalka'),
    korak('Iskano', f'{Ib_}, {In_}, presek A'),
    korak('Formula', f'{Ib_} = P / (√3 · U · cos φ)'),
    korak('Vstavim', f'{Ib_} = 38 000 W / (√3 · 400 V · 1) = 54,85 A'),
    korak('Varovalka', f'{In_} = 63 A (tabela 4)'),
    korak('16 mm², 1. pogoj', f'{Iz_} = 64 A. 54,85 A ≤ 63 A ≤ 64 A ✓'),
    korak('16 mm², 2. pogoj', f'k = 1,6. 1,6 · 63 A = 100,8 A. 1,45 · 64 A = 92,8 A. 100,8 A &gt; 92,8 A ✗'),
    korak('25 mm², 1. pogoj', f'{Iz_} = 82 A. 54,85 A ≤ 63 A ≤ 82 A ✓'),
    korak('25 mm², 2. pogoj', f'1,45 · 82 A = 118,9 A. 100,8 A ≤ 118,9 A ✓'),
    korak('Rezultat', f'A = 25 mm², {In_} = 63 A', True),
    korak('Preverim', 'Pri 16 mm² drži le 1. pogoj. Zato potrebujemo večji presek.'),
]) + '\n') + box('pozor', 'Pogosta napaka', '<p>Ustaviš se pri 1. pogoju. Presek 16 mm² se zdi dober, a 2. pogoj ne drži.</p>', '16px 0 0')

p3 = box('pozor', 'Kaj, če zamenjamo porabnik?', f'''<p style="margin-top:0">V primeru 1 zamenjamo grelnik z močnejšim, 2,5 kW. Kabel in varovalka ostaneta.</p>
<p>Novi bremenski tok je {Ib_} = 2500 W / 230 V = 10,87 A. To je več kot {In_} = 10 A. 1. pogoj ne drži, varovalka bi pogosto izklapljala.</p>
<p>Naslednja varovalka je 13 A. Za 1,5 mm² velja 1,9 · 13 A = 24,7 A &gt; 20,3 A. 2. pogoj ne drži. Zato vzamemo presek 2,5 mm² ({Iz_} = 18,5 A): 24,7 A ≤ 1,45 · 18,5 A = 26,8 A ✓.</p>
<p>Presek povečamo zaradi segrevanja. Padec napetosti pri 1,5 mm² je 2,25 % in bi bil v mejah (dopustno 3 %).</p>''')

hitra = H2 + 'Hitra preverba</h2>\n' + DET + 'Največji nazivni tok za dani presek (taljiva varovalka / odklopnik)</summary>' + '''
<p style="margin-top:12px">Pomoč za preverjanje svojega računa. Velja za tabelo 3 brez skupine tokokrogov (f<sub>p</sub> = 1). Obe pogoja sta že upoštevana. Če je tvoj I<sub>n</sub> večji, presek ne zadošča.</p>
''' + tab([['A2, 2 vodnika', '10 / 13', '16 / 16', '20 / 25', '25 / 32', '35 / 40', '50 / 50', '63 / 63'],
          ['B2, 3 vodniki', '10 / 13', '16 / 20', '20 / 25', '25 / 32', '40 / 40', '50 / 50', '63 / 80'],
          ['C, 3 vodniki', '13 / 16', '20 / 20', '25 / 32', '35 / 40', '50 / 50', '63 / 63', '80 / 80'],
          ['D, 3 vodniki', '16 / 16', '20 / 20', '25 / 25', '32 / 32', '40 / 50', '50 / 63', '63 / 80']],
         ['Način', '1,5 mm²', '2,5 mm²', '4 mm²', '6 mm²', '10 mm²', '16 mm²', '25 mm²']) + '\n</details>'

preveri = H2 + 'Preveri se</h2>' \
    + q('1. Zakaj varovalka ne sme imeti večjega nazivnega toka, kot ga vodnik zdrži?', 'Varovalka bi prepustila tok, ki vodnik segreje nad 70 °C. Izolacija bi se poškodovala.') \
    + q('2. Porabnik ima I<sub>b</sub> = 14,43 A, vodnik je v načinu B2 s tremi obremenjenimi vodniki, zaščita je taljiva varovalka. Ali zadošča 1,5 mm² (I<sub>z</sub> = 15 A)?', 'Ne. Najmanjša varovalka je 16 A, to je več kot 15 A. 1. pogoj ne drži. Vzameš 2,5 mm² (I<sub>z</sub> = 20 A): 1,6 · 16 A = 25,6 A ≤ 1,45 · 20 A = 29 A ✓.') \
    + q('3. Grelnik ima 3 kW pri 230 V. Katera taljiva varovalka ustreza po 1. pogoju?', 'I<sub>b</sub> = 3000 W / 230 V = 13,04 A. Varovalka 13 A je premajhna, zato 16 A.')
kratko = box('cilj', 'Na kratko', ul([f'{Ib_} ≤ {In_} ≤ {Iz_}: porabnik &lt; varovalka &lt; vodnik.', f'2. pogoj: k · {In_} ≤ 1,45 · {Iz_}\'.', 'Če 2. pogoj ne drži, povečaj presek, ne varovalke.', 'Pri več tokokrogih skupaj popravi I<sub>z</sub> s faktorjem f<sub>p</sub>.', 'Tabele 1 do 5 so na maturitetnem listu s formulami.']))
matura = box('matura', 'Matura', '<p>Takšne naloge rešuješ s tabelami 1 do 5 z lista s formulami. Za vajo odpri zbirko nalog: zimski rok 2020, 2021 in 2022 ter spomladanski rok 2021 (naloge 5, 2. pola).</p>\n<p><a href="https://npi.splet.arnes.si/elektricne-instalacije/">Zbirka maturitetnih nalog</a> · <a href="https://www.ric.si/poklicna-matura/predmeti/drugi-predmet/elektrotehnika/">Maturitetno gradivo (RIC)</a></p>', '16px 0 0')

out = sec(
    row(col('4_4', text(cilj('Dimenzioniranje vodnika: tok in segrevanje', [f'izračunati bremenski tok {Ib_},', f'prebrati zdržni tok {Iz_} iz tabele,', f'izbrati nazivni tok {In_} varovalke ali odklopnika,', 'preveriti 1. in 2. pogoj in izbrati presek vodnika.']))))
  + row(col('1_2', text(kaj)) + col('1_2', text(pravilo1)), '1_2,1_2')
  + row(col('1_2', text(postopek)) + col('1_2', text(tabele) + btn(U + '2024/01/formule-na-maturi.pdf', 'Formule na maturi (PDF)')), '1_2,1_2'))
out += sec(row(col('1_2', text(p1)) + col('1_2', text(p2)), '1_2,1_2') + row(col('4_4', text(p3))), '#f5f3ef')
out += sec(row(col('1_2', text(preveri) + text(hitra)) + col('1_2', text(kratko) + text(matura)), '1_2,1_2'))
write('dimenzioniranje-tok', out)
