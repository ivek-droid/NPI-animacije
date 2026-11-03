# Zbirka maturitetnih nalog po temah (stran 185). Zapiše slog/osnutki/zbirka-po-temah.txt
# Vsa števila preveri assert; ob neskladju se generator ustavi.
# Zagon: python3 orodja/lekcija_zbirka.py
import math
src = open('/home/claude/npi-animacije/orodja/lekcije_pomocniki_in_ivep.py').read().split('# ======================================================== SERIJSKA')[0]
exec(src)

def f(x, n=2): return f'{x:.{n}f}'.replace('.', ',')
S3 = math.sqrt(3)
Ib_ = 'I<sub>b</sub>'; In_ = 'I<sub>n</sub>'; Iz_ = 'I<sub>z</sub>'; Uf_ = 'U<sub>f</sub>'

# ---------- preračun ----------
# A1: matura 2023/19
A1 = 2 * 14 * 10 / (56 * 2); assert f(A1, 1) == '2,5' and f(2 * 14 * 10 / (56 * 2.5), 1) == '2,0'
# A2: matura 2022/5
I1 = 1200 / 230; I2 = 1800 / 230; IAB = I1 + I2
k = 2 / (56 * 2.5)
dBC = k * 5 * I1; dBD = k * 6 * I2; dAB = k * 8 * IAB; dAC = dAB + dBC; dAD = dAB + dBD
assert (f(I1), f(I2), f(IAB)) == ('5,22', '7,83', '13,04')
assert (f(dBC), f(dBD), f(dAB), f(dAC), f(dAD)) == ('0,37', '0,67', '1,49', '1,86', '2,16')
assert f(100 * dAD / 230) == '0,94'
# A3: jesen 2022 / naloga 5.3 (tudi šolska naloga 3)
A3 = 1.5 * 56 * 1 * 230 / (200 * 20); assert f(A3) == '4,83' and f(2 * 20 * A3 / (56 * 1.5)) == '2,30'
# A4: zimski 2020 5.4
eps = 200 * 20 * 2500 / (56 * 1.5 * 230 ** 2); assert f(eps) == '2,25'
assert f(2 * 20 * (2500 / 230) / (56 * 1.5) / 230 * 100) == '2,25'
# B1: zimski 2020 5.1-5.3
Ib = 2000 / 230; assert f(Ib) == '8,70'
assert 1.9 * 10 == 19 and round(1.45 * 14, 1) == 20.3 and round(1.9 * 13, 1) == 24.7
# B2: spomladanski 2021
Ib2 = 38000 / (S3 * 400); assert f(Ib2) == '54,85'
assert round(1.6 * 63, 1) == 100.8 and round(1.45 * 64, 1) == 92.8 and round(1.45 * 82, 1) == 118.9
L2 = 1.5 * 56 * 25 * 400 ** 2 / (100 * 38000); assert f(L2, 1) == '88,4'
assert f(100 * 88.4 * 38000 / (56 * 25 * 400 ** 2)) == '1,50'
# B3: zimski 2022
Ib3 = 9000 / (S3 * 400 * 0.9); assert f(Ib3) == '14,43'
assert round(1.6 * 16, 1) == 25.6 and round(1.45 * 20, 1) == 29.0
L3 = 1 * 56 * 2.5 * 400 ** 2 / (100 * 9000); assert f(L3, 1) == '24,9' and f(100 * 24.89 * 9000 / (56 * 2.5 * 400 ** 2)) == '1,00'
# B4: šolska naloga 2
Ib4 = 10000 / (S3 * 400); assert f(Ib4) == '14,43'
# C: razsvetljava 5.3
assert f(2 * 100 / 230) == '0,87' and f(75 / 230) == '0,33'
assert f(230 * 1.57 / 3, 1) == '120,4' and f(230 * 2.61 / 3, 1) == '200,1'

# O: upornost žice (vaja)
Aok = math.pi * 0.3 ** 2 / 4; assert f(Aok, 4) == '0,0707'
lok = 2.5 * 56 * 0.0707; assert f(lok, 1) == '9,9' and f(9.9 / (56 * 0.0707)) == '2,50'
assert f(2.5 * 0.0707 / 0.5, 4) == '0,3535'  # napačen račun z ρ = 0,5 Ω·m in neusklajenimi enotami

# ---------- gradniki ----------
def korak(o, v, rez=False):
    v = f'<span class="pg-rezultat">{v}</span>' if rez else v
    return f'<li><span><span class="pg-koraki__oznaka">{o}</span>{v}</span></li>'
def koraki(items): return '<ol class="pg-koraki">\n' + '\n'.join(items) + '\n</ol>'
def napaka(t): return box('pozor', 'Pogosta napaka', f'<p>{t}</p>', '14px 0 0')
def povezave(*pari):
    return '<p style="font-size:17px;margin-top:14px">' + ' · '.join(f'<a href="{u}" target="_blank" rel="noopener">{t}</a>' for t, u in pari) + '</p>'
def naloga(naslov, besedilo, koraki_html, nap, pov=''):
    return (f'{DET}{naslov}</summary>\n<p style="margin-top:12px"><strong>Naloga.</strong> {besedilo}</p>\n'
            f'<p><strong>Rešitev.</strong></p>\n{koraki_html}\n{nap}{pov}</details>')
def btn(url, label):
    return f'[et_pb_button button_url="{url}" url_new_window="on" button_text="{label}" module_class="pg-btn" _builder_version="4.27.9" custom_margin="0||12px||false|false"][/et_pb_button]'
SITE = 'https://npi.splet.arnes.si/'
def sec_row(modul_id, inner):
    return (f'[et_pb_row module_id="{modul_id}" _builder_version="4.27.9" width="90%" max_width="1080px" custom_padding="10px||10px||false|false"]'
            f'[et_pb_column type="4_4" _builder_version="4.27.9"]{inner}[/et_pb_column][/et_pb_row]')

# ---------- uvod ----------
uvod = cilj('Zbirka maturitetnih nalog', [
    'najti nalogo po temi,',
    'najprej poskusiti sam, nato odpreti rešitev po korakih,',
    'preveriti svoj rezultat in se vrniti na lekcijo, če ti ne gre.'])
uvod += '\n' + H2.replace('margin-top:0', 'margin-top:22px') + 'Teme</h2>\n' + ul([
    '<a href="#upornost-naloge">Upornost in dolžina vodnika</a> (1 vaja)',
    '<a href="#padec-napetosti-naloge">Padec napetosti in presek vodnika</a> (4 naloge)',
    '<a href="#dimenzioniranje-naloge">Dimenzioniranje vodnika in varovalke</a> (4 naloge)',
    '<a href="#razsvetljava-naloge">Razsvetljava: tok in moč žarnic</a> (4 naloge)',
    '<a href="#izvirniki">Izvirne table in PDF-ji</a> (spodaj)']) + \
    '\n<p style="font-size:17px">Rešitve so odprte s klikom na naslov naloge. Formule so zapisane z navadnim besedilom. Tabele 1 do 7 so na listu s formulami za maturo.</p>'

LEK_PN = SITE + 'padec-napetosti/'; LEK_DIM = SITE + 'dimenzioniranje-vodnika/'; LEK_VAR = SITE + 'varovalke-in-odklopniki/'
PDF = SITE + 'files/'; FORM = PDF + '2024/01/formule-na-maturi.pdf'

o1 = naloga('Vaja: dolžina žice iz upornosti',
    'Bakrena žica okroglega preseka ima premer d = 0,3 mm in upornost R = 2,5 Ω. Specifična prevodnost bakra je λ = 56 Sm/mm². Kako dolga je žica?',
    koraki([korak('Podatki', 'R = 2,5 Ω, d = 0,3 mm, λ = 56 Sm/mm²'),
            korak('Iskano', 'dolžina žice l'),
            korak('Formula', 'R = l / (λ · A). Iz nje: l = R · λ · A'),
            korak('Presek', 'A = π · d² / 4 = π · (0,3 mm)² / 4 = 0,0707 mm²'),
            korak('Vstavim', 'l = 2,5 Ω · 56 Sm/mm² · 0,0707 mm² = 9,9 m'),
            korak('Rezultat', 'l ≈ 9,9 m', True),
            korak('Preverim', 'R = 9,9 m / (56 Sm/mm² · 0,0707 mm²) = 2,5 Ω ✓. Tanka žica (0,3 mm) je dolga skoraj 10 m: to je smiselno za upornost nekaj ohmov.')]),
    napaka('Mešaš enote: specifično upornost v Ωm in presek v mm². Rezultat je potem napačen za faktor milijon. Uporabi λ v Sm/mm² skupaj s presekom v mm² in dolžino v m.'))
sekcija_O = (H2 + 'Upornost in dolžina vodnika</h2>\n<p>Osnova za vse račune padca napetosti: R = l / (λ · A). Pazi na enote: λ v Sm/mm², A v mm², l v m.</p>\n' + o1)

# ---------- A: padec napetosti ----------
a1 = naloga('Matura 2023, spomladanski rok, 1. pola, naloga 19: presek vodnika',
    'Na kablu, ki napaja fazni porabnik, je padec napetosti ΔU = 2 V. Vodniki specifične prevodnosti λ = 56 Sm/mm² so dolgi l = 14 m. Izračunaj presek vodnika A pri faznem toku 10 A.',
    koraki([korak('Podatki', 'ΔU = 2 V, λ = 56 Sm/mm², l = 14 m, I = 10 A'),
            korak('Iskano', 'presek A'),
            korak('Formula', 'A = 2 · l · I / (λ · ΔU). Faktor 2: tok teče po faznem in po nevtralnem vodniku.'),
            korak('Vstavim', 'A = 2 · 14 m · 10 A / (56 Sm/mm² · 2 V) = 280 / 112'),
            korak('Rezultat', 'A = 2,5 mm²', True),
            korak('Preverim', 'ΔU = 2 · 14 · 10 / (56 · 2,5) = 2,0 V ✓')]),
    napaka('Pozabiš povratni vodnik in izračunaš 1,25 mm². Kabel ima dve žili v seriji, zato je pot toka 2 · l.'),
    povezave(('postopek (PDF)', PDF + '2023/11/Matura-2023-spomladanski-rok-19.naloga_-prva-pola.pdf'), ('zapis s table', PDF + '2023/12/matura-2023-spml-19.-naloga-scaled.jpg'), ('lekcija: padec napetosti', LEK_PN)))

a2 = naloga('Matura 2022, spomladanski rok, 1. pola, naloga 5: dva odcepa',
    'Enopolna shema ima dva odcepa. Porabnik 1 (točka C) ima P<sub>1</sub> = 1200 W, porabnik 2 (točka D) ima P<sub>2</sub> = 1800 W. Fazna napetost je 230 V, presek vodnikov 2,5 mm², λ = 56 Sm/mm². Dolžine: l<sub>AB</sub> = 8 m, l<sub>BC</sub> = 5 m, l<sub>BD</sub> = 6 m. Izračunaj tokova I<sub>1</sub> in I<sub>2</sub> ter padce napetosti ΔU<sub>BC</sub>, ΔU<sub>BD</sub>, ΔU<sub>AB</sub>, ΔU<sub>AC</sub> in ΔU<sub>AD</sub>.',
    koraki([korak('Podatki', 'P<sub>1</sub> = 1200 W, P<sub>2</sub> = 1800 W, U<sub>f</sub> = 230 V, A = 2,5 mm², λ = 56 Sm/mm²'),
            korak('Tok 1', 'I<sub>1</sub> = P<sub>1</sub> / U<sub>f</sub> = 1200 / 230 = 5,22 A'),
            korak('Tok 2', 'I<sub>2</sub> = P<sub>2</sub> / U<sub>f</sub> = 1800 / 230 = 7,83 A'),
            korak('Formula', 'ΔU = 2 · l · I / (λ · A). Faktor 2: fazni in nevtralni vodnik.'),
            korak('ΔU<sub>BC</sub>', '2 · 5 m · 5,22 A / (56 · 2,5) = 0,37 V'),
            korak('ΔU<sub>BD</sub>', '2 · 6 m · 7,83 A / (56 · 2,5) = 0,67 V'),
            korak('Tok v AB', 'po odseku AB teče vsota obeh tokov: I<sub>AB</sub> = 5,22 A + 7,83 A = 13,04 A (brez zaokroževanja)'),
            korak('ΔU<sub>AB</sub>', '2 · 8 m · 13,04 A / (56 · 2,5) = 1,49 V'),
            korak('ΔU<sub>AC</sub>', 'ΔU<sub>AB</sub> + ΔU<sub>BC</sub> = 1,49 V + 0,37 V = 1,86 V'),
            korak('ΔU<sub>AD</sub>', 'ΔU<sub>AB</sub> + ΔU<sub>BD</sub> = 1,49 V + 0,67 V = 2,16 V'),
            korak('Rezultat', 'ΔU<sub>AC</sub> = 1,86 V, ΔU<sub>AD</sub> = 2,16 V', True),
            korak('Preverim', 'najslabši porabnik (D): 2,16 V od 230 V je 0,94 %. To je manj od 3 % (tabela 7).')]),
    napaka('Padec ΔU<sub>AB</sub> izračunaš samo z I<sub>1</sub> ali samo z I<sub>2</sub>. Po odseku AB teče tok obeh porabnikov.'),
    povezave(('postopek (PDF)', PDF + '2023/11/Matura-2022-spomladanski-rok-5.naloga_-prva-pola.pdf'), ('zapis s table', PDF + '2023/12/matura-2022-spml-5.-naloga-druga-pola-scaled.jpg'), ('lekcija: padec napetosti', LEK_PN)))

a3 = naloga('Matura 2022, jesenski rok, 2. pola, naloga 5.3: največji tok pri dovoljenem padcu',
    'Žarnico napaja vodnik preseka A = 1,5 mm² in dolžine l = 20 m, priključen na fazno napetost 230 V. Specifična prevodnost je λ = 56 Sm/mm². Največji dovoljeni padec napetosti je Δu% = 1 %. Izračunaj največji dovoljeni tok skozi vodnik. (Enako nalogo vsebuje tudi šolska naloga za ponovitev, 15. 1. 2024.)',
    koraki([korak('Podatki', 'A = 1,5 mm², l = 20 m, U<sub>f</sub> = 230 V, λ = 56 Sm/mm², Δu% = 1 %'),
            korak('Iskano', 'največji tok I'),
            korak('Formula', 'A = 200 · l · I / (λ · Δu% · U<sub>f</sub>). Iz nje: I = A · λ · Δu% · U<sub>f</sub> / (200 · l)'),
            korak('Vstavim', 'I = 1,5 · 56 · 1 · 230 / (200 · 20) = 19 320 / 4000'),
            korak('Rezultat', 'I = 4,83 A', True),
            korak('Preverim', 'ΔU = 2 · 20 · 4,83 / (56 · 1,5) = 2,30 V. To je 1 % od 230 V ✓')]),
    napaka('Pozabiš število 200. V njem je faktor 2 (fazni in nevtralni vodnik) in faktor 100 (odstotki).'))

a4 = naloga('Matura, zimski rok 2020, 2. pola, naloga 5.4: ali smo presegli padec napetosti?',
    'Grelnik 2 kW smo zamenjali z grelnikom P′ = 2,5 kW. Vodnik: A = 1,5 mm², l = 20 m, U<sub>f</sub> = 230 V, λ = 56 Sm/mm². Ali smo presegli dopustni padec napetosti 3 %?',
    koraki([korak('Podatki', 'P′ = 2500 W, l = 20 m, A = 1,5 mm², U<sub>f</sub> = 230 V, λ = 56 Sm/mm²'),
            korak('Iskano', 'padec napetosti Δu% in primerjava s 3 %'),
            korak('Formula', 'Δu% = 200 · l · P′ / (λ · A · U<sub>f</sub>²)'),
            korak('Vstavim', 'Δu% = 200 · 20 · 2500 / (56 · 1,5 · 230²) = 10 000 000 / 4 443 600'),
            korak('Rezultat', 'Δu% = 2,25 %. To je manj od 3 %: dopustnega padca nismo presegli.', True),
            korak('Preverim', 'I = 2500 / 230 = 10,87 A. ΔU = 2 · 20 · 10,87 / (56 · 1,5) = 5,18 V. To je 2,25 % od 230 V ✓')]),
    napaka('Faktor 2 dodaš še enkrat. Formula s formul na maturi ga že vsebuje. Z dvojnim faktorjem dobiš 4,5 % in napačen sklep.'),
    povezave(('postopek (PDF)', PDF + '2024/01/zimski-2020-5drugi-del.pdf'), ('zapis s table', PDF + '2024/01/zimski-2020-5druga-pola-scaled.jpg'), ('lekcija: padec napetosti', LEK_PN)))

sekcija_A = (H2 + 'Padec napetosti in presek vodnika</h2>\n<p>Formule za padec napetosti so na maturitetnem listu. Dopustni padec je v nalogi ali v tabeli 7. Rešitve preveri tudi z obratnim računom.</p>\n'
             + a1 + a2 + a3 + a4 + btn(LEK_PN, 'Lekcija: padec napetosti'))

# ---------- B: dimenzioniranje ----------
b1 = naloga('Matura, zimski rok 2020, 2. pola, naloga 5.1 do 5.3: grelnik vode',
    'Grelnik vode P = 2 kW je priključen na U<sub>f</sub> = 230 V. Vodnik je v gibki kabelski cevi neposredno v toplotni izolaciji (skupina A2), zaščita je taljiva varovalka. Izračunaj tok, izberi nazivni tok varovalke in zdržni tok vodnika, preveri 2. pogoj in izberi presek.',
    koraki([korak('Podatki', 'P = 2000 W, U<sub>f</sub> = 230 V, skupina A2, 2 obremenjena vodnika, taljiva varovalka'),
            korak('5.1 Tok', f'{Ib_} = P / U<sub>f</sub> = 2000 / 230 = 8,70 A'),
            korak('5.2 Varovalka', f'{In_} = 10 A. To je najmanjša vrednost iz tabele 4, ki je ≥ 8,70 A.'),
            korak('5.2 Zdržni tok', f'Za 1,5 mm², A2, 2 vodnika: {Iz_} = 14 A (tabela 3). 1. pogoj: 8,70 A ≤ 10 A ≤ 14 A ✓'),
            korak('5.3 2. pogoj', f'k = 1,9 (taljiva vložka do 13 A). 1,9 · 10 A = 19 A. 1,45 · 14 A = 20,3 A. 19 A ≤ 20,3 A ✓'),
            korak('Rezultat', f'{In_} = 10 A, A = 1,5 mm²', True),
            korak('Preverim', 'varovalka (10 A) je med porabnikom (8,70 A) in vodnikom (14 A).')]),
    napaka('Izbereš varovalko 13 A, ker je blizu 14 A. Potem je 1,9 · 13 A = 24,7 A in to je več kot 20,3 A: 2. pogoj ne drži.'),
    povezave(('postopek (PDF)', PDF + '2024/01/zimski-2020-5drugi-del.pdf'), ('zapis s table', PDF + '2024/01/zimski-2020-5druga-pola-scaled.jpg'), ('lekcija: dimenzioniranje', LEK_DIM)))

b2 = naloga('Matura 2021, spomladanski rok, 2. pola, naloga 5: trifazni porabnik 38 kW',
    'Trifazni porabnik P = 38 kW, U = 400 V, cos φ = 1. Kabel je v cevi v zemlji (skupina D), zaščita so taljive varovalke, λ = 56 Sm/mm². Izračunaj fazni tok, izberi nazivni tok, preveri 1. in 2. pogoj ter izračunaj največjo dolžino vodnika pri Δu% = 1,5 %.',
    koraki([korak('Podatki', 'P = 38 000 W, U = 400 V, cos φ = 1, skupina D, 3 obremenjeni vodniki, taljiva varovalka'),
            korak('5.1 Tok', f'{Ib_} = P / (√3 · U · cos φ) = 38 000 / (√3 · 400 · 1) = 54,85 A'),
            korak('5.2 Varovalka', f'{In_} = 63 A (tabela 4)'),
            korak('16 mm²', f'{Iz_} = 64 A. 1. pogoj drži. 2. pogoj: k = 1,6, 1,6 · 63 A = 100,8 A. 1,45 · 64 A = 92,8 A. 100,8 A &gt; 92,8 A ✗'),
            korak('25 mm²', f'{Iz_} = 82 A. 1. pogoj: 54,85 A ≤ 63 A ≤ 82 A ✓. 2. pogoj: 100,8 A ≤ 1,45 · 82 A = 118,9 A ✓'),
            korak('5.3 Presek', 'A = 25 mm²'),
            korak('5.4 Formula', 'l = Δu% · λ · A · U² / (100 · P)'),
            korak('5.4 Vstavim', 'l = 1,5 · 56 · 25 · 400² / (100 · 38 000) = 336 000 000 / 3 800 000'),
            korak('Rezultat', f'{In_} = 63 A, A = 25 mm², l = 88,4 m', True),
            korak('Preverim', 'Δu% = 100 · 88,4 · 38 000 / (56 · 25 · 400²) = 1,50 % ✓')]),
    napaka('Ustaviš se pri 16 mm², ker 1. pogoj drži. 2. pogoj pove, da je presek premajhen.'),
    povezave(('postopek (PDF)', PDF + '2024/01/matura-spoml-2021-5-2del.pdf'), ('zapis s table', PDF + '2024/01/tabla-spom-2021-5-2del-scaled-e1704886292353.jpg'), ('lekcija: dimenzioniranje', LEK_DIM)))

b3 = naloga('Matura 2022, zimski rok, 2. pola, naloga 5: toplotna črpalka 9 kW',
    'Toplotna črpalka zrak-voda P = 9 kW, U = 400 V, cos φ = 0,9. Kabel je v zaščitni cevi, skupina B2, λ = 56 Sm/mm². Varujejo jo taljive varovalke. Izračunaj tok v fazi, izberi nazivni tok, preveri pogoja in izračunaj največjo dolžino kabla pri Δu% = 1 %.',
    koraki([korak('Podatki', 'P = 9000 W, U = 400 V, cos φ = 0,9, skupina B2, 3 obremenjeni vodniki'),
            korak('5.1 Tok', f'{Ib_} = P / (√3 · U · cos φ) = 9000 / (√3 · 400 · 0,9) = 14,43 A'),
            korak('5.2 Varovalka', f'{In_} = 16 A (tabela 4)'),
            korak('1,5 mm²', f'{Iz_} = 15 A. 16 A &gt; 15 A: 1. pogoj ne drži ✗'),
            korak('2,5 mm²', f'{Iz_} = 20 A. 1. pogoj: 14,43 A ≤ 16 A ≤ 20 A ✓'),
            korak('5.3 2. pogoj', 'k = 1,6 (vložek 16 A ali več). 1,6 · 16 A = 25,6 A. 1,45 · 20 A = 29 A. 25,6 A ≤ 29 A ✓'),
            korak('5.4 Formula', 'l = Δu% · λ · A · U² / (100 · P)'),
            korak('5.4 Vstavim', 'l = 1 · 56 · 2,5 · 400² / (100 · 9000) = 22 400 000 / 900 000'),
            korak('Rezultat', f'{In_} = 16 A, A = 2,5 mm², l = 24,9 m', True),
            korak('Preverim', 'Δu% = 100 · 24,9 · 9000 / (56 · 2,5 · 400²) = 1,00 % ✓')]),
    napaka('Pri izračunu padca napetosti vstaviš navidezno moč ali tok namesto delovne moči P. Formula s P že upošteva cos φ.'),
    povezave(('postopek (PDF)', PDF + '2024/02/zimski-2021-5-naloga-2del-19.pdf'), ('zapis s table', PDF + '2024/02/zimski-2022-5naloga-2del-scaled.jpg'), ('lekcija: dimenzioniranje', LEK_DIM)))

b4 = naloga('Šolska naloga za ponovitev, 15. 1. 2024, naloga 2: odklopnik za 10 kW',
    'Ohmski porabnik P = 10 kW ima trifazni priključek, medfazna napetost je U = 400 V. Izračunaj tok v fazi in določi nazivni tok inštalacijskega odklopnika.',
    koraki([korak('Podatki', 'P = 10 000 W, U = 400 V, ohmski porabnik (cos φ = 1)'),
            korak('Formula', f'{Ib_} = P / (√3 · U)'),
            korak('Vstavim', f'{Ib_} = 10 000 / (√3 · 400) = 14,43 A'),
            korak('Odklopnik', f'Tabela 5: 13 A je premalo (&lt; 14,43 A). Prva večja vrednost je {In_} = 16 A.'),
            korak('Rezultat', f'{Ib_} = 14,43 A, {In_} = 16 A', True),
            korak('Preverim', 'moči: √3 · 400 V · 14,43 A = 10 000 W ✓')]),
    napaka('Izbereš odklopnik 13 A, ker je najbližji. Odklopnik mora imeti nazivni tok večji ali enak toku porabnika.'),
    povezave(('naloge (PDF)', PDF + '2024/01/SOLSKA-NALOGA-ponovitev-15-1-2024.pdf'), ('zapis s table', PDF + '2024/01/poprava-ponovitve-testa-scaled-e1705491362804.jpg'), ('lekcija: varovalke in odklopniki', LEK_VAR)))

sekcija_B = (H2 + 'Dimenzioniranje vodnika in varovalke</h2>\n<p>Vedno preveri oba pogoja: 1. pogoj I<sub>b</sub> ≤ I<sub>n</sub> ≤ I<sub>z</sub> in 2. pogoj k · I<sub>n</sub> ≤ 1,45 · I<sub>z</sub>. Tabele 1 do 5 so na maturitetnem listu.</p>\n'
             + b1 + b2 + b3 + b4 + btn(LEK_DIM, 'Lekcija: dimenzioniranje vodnika'))

# ---------- C: razsvetljava ----------
c1 = naloga('Matura 2020, spomladanski rok, 2. pola, naloga 5: dve žarnici na hodniku',
    'Na načrtu hodnika s štirimi stikali (S1 do S4) vklapljamo in izklapljamo dve žarnici. Zapiši vrsto in število stikal (5.1) in način polaganja (5.2). Izračunaj tok skozi tokokrog žarnic (5.3): fazna napetost je 230 V, moč vsake žarnice 100 W.',
    koraki([korak('5.1 Stikala', 'dve menjalni stikali (S1 in S4, na začetku in koncu) in dve križni stikali (S2 in S3, vmes)'),
            korak('5.2 Polaganje', 'inštalacija je položena v omet'),
            korak('Podatki za 5.3', 'U<sub>f</sub> = 230 V, P<sub>Ž</sub> = 100 W, 2 žarnici'),
            korak('Skupna moč', 'P = 2 · 100 W = 200 W'),
            korak('Formula', 'I = P / U<sub>f</sub>'),
            korak('Vstavim', 'I = 200 W / 230 V'),
            korak('Rezultat', 'I = 0,87 A', True),
            korak('Preverim', 'ena žarnica vleče 100 / 230 = 0,43 A, dve vlečeta dvakrat toliko ✓')]),
    napaka('Pri 5.3 vstaviš moč ene žarnice in dobiš 0,43 A. V tokokrogu sta dve žarnici. Pri 5.1 zapišeš samo »stikala« brez vrste in števila.'),
    povezave(('lekcija: križna vezava', SITE + '?page_id=813')))
c2 = naloga('Matura 2020, jesenski rok, 2. pola, naloga 5.3: žarnica 75 W',
    'S stikaloma vklapljamo žarnico z dveh mest. Fazna napetost je 230 V, moč žarnice P<sub>Ž</sub> = 75 W. Izračunaj tok skozi žarnico.',
    koraki([korak('Podatki', 'U<sub>f</sub> = 230 V, P<sub>Ž</sub> = 75 W'),
            korak('Formula', 'I = P<sub>Ž</sub> / U<sub>f</sub>'),
            korak('Vstavim', 'I = 75 W / 230 V'),
            korak('Rezultat', 'I = 0,33 A', True),
            korak('Preverim', '0,33 A · 230 V = 75 W ✓')]),
    napaka('Zamenjaš vrstni red in delš 230 / 75. Moč delimo z napetostjo, ne obratno.'))
c3 = naloga('Matura 2021, jesenski rok, 2. pola, naloga 5: tri žarnice na hodniku',
    'Na načrtu hodnika s štirimi stikali (S1 do S4) vklapljamo in izklapljamo tri žarnice enakih moči (Ž1, Ž2, Ž3). Zapiši vrsti stikal (5.1) in način polaganja (5.2). Izračunaj moč ene žarnice (5.3): fazna napetost je 230 V, tok skozi tokokrog žarnic je 1,57 A.',
    koraki([korak('5.1 Stikala', 'menjalno in križno stikalo'),
            korak('5.2 Polaganje', 'inštalacija je položena pod ometom'),
            korak('Podatki za 5.3', 'U<sub>f</sub> = 230 V, I = 1,57 A, 3 žarnice enakih moči'),
            korak('Skupna moč', 'P = U<sub>f</sub> · I = 230 V · 1,57 A = 361,1 W'),
            korak('Moč ene žarnice', 'P<sub>Ž</sub> = P / 3 = 361,1 W / 3'),
            korak('Rezultat', 'P<sub>Ž</sub> = 120 W (120,4 W)', True),
            korak('Preverim', '3 · 120 W / 230 V = 1,57 A ✓')]),
    napaka('Skupno moč pustiš kot moč ene žarnice. Število žarnic preberi iz načrta.'))
c4 = naloga('Matura 2023, spomladanski rok, 2. pola, naloga 5: tri žarnice na hodniku',
    'Na načrtu hodnika vklapljamo in izklapljamo tri žarnice enakih moči (Ž1, Ž2, Ž3). Zapiši vrsti stikal (5.1). Izračunaj moč ene žarnice (5.3): fazna napetost je 230 V, tok skozi tokokrog žarnic je 2,61 A.',
    koraki([korak('5.1 Stikala', 'menjalno in križno stikalo'),
            korak('Podatki za 5.3', 'U<sub>f</sub> = 230 V, I = 2,61 A, 3 žarnice enakih moči'),
            korak('Skupna moč', 'P = U<sub>f</sub> · I = 230 V · 2,61 A = 600,3 W'),
            korak('Moč ene žarnice', 'P<sub>Ž</sub> = P / 3 = 600,3 W / 3'),
            korak('Rezultat', 'P<sub>Ž</sub> = 200 W (200,1 W)', True),
            korak('Preverim', '3 · 200 W / 230 V = 2,61 A ✓')]),
    napaka('Skupno moč pustiš kot moč ene žarnice. Število žarnic preberi iz načrta.'))
assert f(230 * 1.57, 1) == '361,1' and f(230 * 2.61, 1) == '600,3' and f(3 * 120 / 230) == '1,57' and f(3 * 200 / 230) == '2,61'
assert f(100 / 230) == '0,43'

sekcija_C = (H2 + 'Razsvetljava: tok in moč žarnic</h2>\n<p>V nalogah z razsvetljavo je točka 5.3 račun. Vrsto stikal (5.1) in način polaganja (5.2) preberi iz načrta, vezalni načrt (5.4) narišeš po pravilih iz lekcij: '
             f'<a href="{SITE}?page_id=809">menjalna vezava</a>, <a href="{SITE}?page_id=813">križna vezava</a>, <a href="{SITE}?page_id=804">serijska vezava</a> in <a href="{SITE}?page_id=798">enopolna vezava</a>.</p>\n'
             + c1 + c2 + c3 + c4)

izv = H2 + 'Izvirne table in PDF-ji</h2>\n<p>Spodaj so izvirni posnetki table, naloge iz učbenika in maturitetne tabele, kot so bili doslej.</p>'

out = sec(row(col('4_4', text(uvod))))
out += sec(sec_row('upornost-naloge', text(sekcija_O)), '#f5f3ef')
out += sec(sec_row('padec-napetosti-naloge', text(sekcija_A)))
out += sec(sec_row('dimenzioniranje-naloge', text(sekcija_B)), '#f5f3ef')
out += sec(sec_row('razsvetljava-naloge', text(sekcija_C)))
out += sec(sec_row('izvirniki', text(izv)), '#f5f3ef')
write('zbirka-po-temah', out)
