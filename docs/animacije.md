# Animacije (GitHub Pages)

Privzeta tehnika: samostojna HTML datoteka (HTML/CSS/SVG/JavaScript) v tem repozitoriju, objavljena na GitHub Pages `https://ivek-droid.github.io/NPI-animacije/IME.html` in vdelana na stran s shortcodom:
`[iframe src="https://ivek-droid.github.io/NPI-animacije/IME.html" width="100%" height="…" title="Animacija: …"]`
Pod vdelavo gumb »Odpri … v celem oknu« (oblika kot drugi gumbi, brez razreda `utripanje-gumba`, belo besedilo na #4B1585, v lekcijah `module_class="pg-btn"`). Divijev modul »Koda« ne deluje, ker WP odstrani skripte.

## Pravila
- Ena datoteka, brez zunanjih knjižnic in pisav (razen z izrecno odobritvijo), sistemske pisave. Vsi CSS-razredi s predpono `ct-`.
- Dostopnost je obvezna: gumb za pavzo/ponovitev, `prefers-reduced-motion`, upravljanje s tipkovnico (dijaki z gibalnimi ovirami pogosto ne uporabljajo miške), ciljne površine ≥44 px, visok kontrast, nobenega utripanja, besedilni opis pod animacijo (`aria-label` ali vidno besedilo), zvok ni edini nosilec informacije.
- En učni cilj. Parametre dijak spreminja s sliderjem ali števnimi gumbi. Vlečenje le z alternativo z gumbi.
- Brez `localStorage` in brez zunanjih klicev.
- Kompaktna postavitev (višina iframa je fiksna). Oznake v SVG ≥16 px pri širini 480 px. `?kompakt` za vdelavo.
- Pred objavo test s Playwrightom: izračuni, tipkovnica, pavza, reduced-motion, brez napak v konzoli, brez zunanjih zahtev. Izmeri višino strani pri 1000 in 480 px in predlagaj višino iframa.
- Ob oddaji napiši: kaj animacija prikazuje, česa ne (poenostavitve), povezavo na GitHub Pages in shortcode.
- V animacijah formule z besedilnimi oznakami; LaTeX le tu ali kot slika (na Arnesu MathJax ni mogoč).

## Orodja
Generator `orodja/animacije_build.py` (serijska, križna, rele, trifazni); menjalna in enopolna sta samostojni datoteki. Testi `orodja/test_*.js` (Playwright, poženi iz korena repozitorija). `odcitavanje-instrumenta.html` je samostojna datoteka (skale: črna 0–5 = 50 razdelkov, 0–15 = 75, rdeča 0–10 = 50, 0–30 = 30; brez 1000 V in ohmmetra; test: `node orodja/test_odcitavanje.js`). `priklop-merilnikov.html` je samostojna datoteka (vozliščna analiza: vir 12 V, ampermeter 0,001 Ω, voltmeter 100 kΩ; mostički kot mesta prekinitve; presoja je fizikalna, ne po seznamu povezav; test: `node orodja/test_priklop.js`). `izberi-presek.html` je samostojna datoteka; model preverja `orodja/ref_presek.py` (tabele 1–7 na maturi): `python3 orodja/ref_presek.py /tmp/ref.json && node orodja/test_presek.js /tmp/ref.json`.

## Vdelane animacije
| Animacija | iframe višina | stran |
|---|---|---|
| menjalna-vezava.html | 620 | Menjalna vezava (809) |
| enopolna-vezava.html | 800 | Enopolna vezava (798) |
| serijska-vezava.html | 720 | Serijska vezava (804) |
| krizna-vezava.html | 700 | Križna vezava (813) |
| impulzni-rele.html | 680 | Bistabilni impulzni rele (1075); uporabnik želi **to** različico črtkane povezave (desno, gor, desno do kontakta) |
| trifazni-sistem.html | 780 | Trifazni izmenični sistem (89) |
| vodne-turbine.html | 620 | Pridobivanje el. energije (82) |
| hidroelektrarna.html | 730 | Pridobivanje el. energije (82) |
| izberi-presek.html | 1220 (pri 480 px 1530) | Dimenzioniranje vodnika (1338), razdelek »Izberi presek sam« pred »Preveri se« |
| priklop-merilnikov.html | 1220 (pri 480 px 1700) | IVEp, stran »Uporaba univerzalnega merilnika« (1367), pred animacijo odčitavanja; test `orodja/test_priklop.js` |
| odcitavanje-instrumenta.html | 1450 (pri 480 px 2300) | IVEp, stran »Uporaba univerzalnega merilnika« (1367); test `orodja/test_odcitavanje.js` |
| stikalo-v-fazi.html | 800 (pri 480 px 790, pod 400 px do 950) | Vezave za razsvetljavo – uvod (764, osnutek 1398); test `node orodja/test_stikalo.js`; statična shema `node orodja/shema_razsvetljava.js` |
| ohmov-zakon.html, ura.html | – | starejši, niso v novem slogu |
