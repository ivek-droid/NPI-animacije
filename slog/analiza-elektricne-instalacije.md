# Električne inštalacije (stran 185) – analiza, 1. 11. 2026

Vir: stran `/elektricne-instalacije/`, učbenik (pogl. 20, str. 369–392), formule na maturi (tabele 1–7), table učitelja.
Preračuni: `orodja/preveri_dimenzioniranje.py`.

## Kaj je zdaj na strani
Zbirka slik in PDF-jev, brez besedila: Ohmov zakon (animacija), maturitetne naloge (2023/19, 2022/5, 2020/10, 2020–2022/5 2. pola), table za primere 1–6 iz učbenika (str. 235, 375), poprava testa. Rešitve so fotografije table. Ni strukture lekcije, ni besedila za bralnik zaslona, ni korakov, ni povezave med učbenikom in maturo.

## Napake in neskladja (označeno, nič ni spremenjeno)
1. **Tabla »zimski 2021 / 5 / 2. del«, naloga 5.4:** v formuli je dodan faktor 2 (`200·2·20·2500 / (56·1,5·230²) = 4,5 %`). Formula s formul na maturi (200·l·P / (λ·A·U²)) že vsebuje 2 (tja in nazaj). Pravilno: 2,25 %. Sklep »prevelik padec, povečamo presek na 2,5 mm²« zaradi padca napetosti je napačen. Tabla »zimski 2020« z enakimi podatki ima pravilnih 2,25 %.
2. **Naloga 5.4 (2020 in 2021):** z grelnikom 2,5 kW je I_b = 10,87 A, varovalka pa je 10 A → pogoj 1 ni izpolnjen. Z 13 A varovalko pogoj 2 pri 1,5 mm² ne drži (1,9·13 = 24,7 A > 1,45·14 = 20,3 A). Presek 1,5 mm² torej ne zadošča, vendar zaradi varovalke, ne zaradi padca napetosti. Tabla 2020 pravi »vse OK«, ker tega ne preveri.
3. **Primer 3 (str. 375):** učbenik ima za A2, 1,5 mm², 2 obremenjena vodnika I_z = 15,5 A, tabela 3 na maturi 14 A. Po maturitetni tabeli je I_z' = 14·0,94 = 13,16 A (učbenik 14,57 A). Nazivni tok: odklopnik 13 A, taljiva varovalka gG le 10 A. Table in učbenik: In = 13 A brez navedbe naprave.
4. **Pogoj 2 (I₂ ≤ 1,45·I_z') učbenik za varovalke ne obravnava s faktorji k** (2,1 / 1,9 / 1,6). Na maturi ga zahtevajo (tabela 2). Stolpec »I_N« v tabeli 20.2 učbenika je primeren za odklopnike, ne za varovalke (npr. B1, 1,5 mm²: I_N = 16 A, gG 16 A pa 1,6·16 = 25,6 > 1,45·17,5 = 25,4).
5. **Tabela 20.2 (učbenik) in tabela 3 (matura):** enaki so vsi podatki razen 1,5 mm², 2 obremenjena vodnika: A1 15,5 vs 14,5 A, A2 15,5 vs 14 A. Zadnji stolpec: učbenik E (v zraku), matura D (v zemlji).
6. **Dopustni padec napetosti:** učbenik 3 % do najbolj oddaljenega porabnika (+0,5 % do števca), tabela 7 na maturi 3 / 5 / 8 % glede na vrsto in napajanje. Dijak naj uporabi vrednost iz naloge, sicer tabelo 7.
7. **Specifična prevodnost:** učbenik 57,1·10⁶ S/m (str. 376) in ρ = 0,018 (str. 377), matura 56 S·m/mm². Pri maturi vedno 56.
8. **Temperaturni faktor f₁:** učbenik ga uporablja (tabela 20.3), formule na maturi nimajo tabele zanj. Če ga naloga ne poda, ga na maturi ni mogoče uporabiti.
9. **Poprava testa, naloga 3:** po moji kontroli je I = 1,5·56,5·1·230 / (200·20) = 4,87 A, na tabli je prebrano 4,83 A (nejasna pisava, preveri v izvirniku).

## Vrzeli glede na formule na maturi
V učbeniku (pogl. 20) in na strani ni: toplotna preverba kratkega stika (I_k²·t ≤ k²·A²), več porabnikov na enem vodu (Σ P_i·l_i), razsvetljava (E = Φ/A, η), pogoj samodejnega odklopa Z_k·I_a ≤ U₀ z odklopnimi toki B/C/D (tabela 6; učbenik ima B/C/D v pogl. 20.2.3.3 in TN zaščito v pogl. 21). Ali se te teme na maturi res pojavljajo, nisem preveril (izpitne pole niso dosegljive).

## Najvišji I_n pri dani ustrezni kombinaciji (tabela 3, brez faktorja skupine)
Izračun: pogoj 1 (I_b ≤ I_n ≤ I_z') in pogoj 2 (k·I_n ≤ 1,45·I_z'); gG iz tabele 4, odklopniki iz tabele 5. Zapis: gG / odklopnik, v A. Polna tabela v izpisu skripte.
| Način | Obr. žil | 1,5 mm² | 2,5 mm² | 4 mm² | 6 mm² | 10 mm² | 16 mm² | 25 mm² |
|---|---|---|---|---|---|---|---|---|
| A2 | 2 | 10/13 | 16/16 | 20/25 | 25/32 | 35/40 | 50/50 | 63/63 |
| B2 | 3 | 10/13 | 16/20 | 20/25 | 25/32 | 40/40 | 50/50 | 63/80 |
| C | 3 | 13/16 | 20/20 | 25/32 | 35/40 | 50/50 | 63/63 | 80/80 |
| D | 3 | 16/16 | 20/20 | 25/25 | 32/32 | 40/50 | 50/63 | 63/80 |

## Predlog razdelitve zavihka (po eno stran naenkrat, osnutek → potrditev → objava)
1. **Dimenzioniranje vodnika: tok in toplotna obremenitev** (I_b, način polaganja, I_z, faktor skupine, pogoja 1 in 2). Rešeni primeri: 2020/5, 2022/5, 2021/5 (spomladanski).
2. **Padec napetosti** (enofazni, trifazni, največja dolžina). Matura 2023/19, 2022/5, primer pralnega stroja iz učbenika.
3. **Nadtokovna zaščita: varovalke in odklopniki** (gG, tipi B/C/D, k-faktorji, selektivnost).
4. **Ohmov zakon in upornost vodnika** (obstoječa animacija in gradivo ostanejo).
5. **Zbirka maturitetnih nalog** z iskanjem po temi, z besedilom rešitve pod sliko table.
Vsaka stran: cilj, razlaga, rešen primer v korakih, »pogosta napaka«, preveri se, povezava na maturo, tabela z maturitetnih formul kot besedilo.
