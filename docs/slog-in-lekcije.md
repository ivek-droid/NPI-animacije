# Slog in predloga lekcije

## Slog
- Slogovni sistem (artefakt): https://claude.ai/artifact/AYXzUAqfGAidgGmhJ9Hx92
- Globalni CSS: `slog/pomozna-gradiva-globalni.css`, prilepljen v Divi → Možnosti teme → Splošno → Lasten CSS (shrani z »Save Changes«). Varnostna kopija prejšnjega: `slog/varnostna-kopija-2026-10-31.md`.
- Barve: primary #4b1585, accent #f2b705 (samo polnilo), ink #1b1e28, surface-alt #f5f3ef.
- Komponente: okvirji `pg-okvir--cilj|primer|pozor|matura`, rešen primer `ol.pg-koraki` + `.pg-rezultat`, gumbi Divi z `module_class="pg-btn"`.
- Pisava sistemska, besedilo 19 px, levo. Logotip: električar, ki razmišlja (`slog/logo-pomozna-gradiva-128.png`, medij 1303), ikona strani stikalo (medij 1304).

## Predloga lekcije (kompaktna, potrjena)
H1 + okvir »Po tej lekciji znaš« → vrstice v dveh stolpcih: vsakdanji primer + besedilo | pravilo ali slika → rešena primera (podatki, iskano, formula, vstavim, rezultat, preverim, vsak korak ena vrstica) + okvir »Pogosta napaka« → po želji siva sekcija »Preizkusi sam« (iframe `?kompakt` + gumb »Odpri animacijo v celem oknu«) → »Preveri se« (`<details>`, 3 vprašanja) | »Na kratko« + okvir »Matura«.

## Generatorji
- `orodja/lekcije_pomocniki_in_ivep.py`: pomožne funkcije `sec/row/col/text/img/box/q/ol/ul/cilj/anim`. Datoteke `orodja/lekcija_*.py` jih naložijo z `exec` in pišejo v `slog/osnutki/<ime>.txt`.
- Vzorec za strani z računi: `orodja/lekcija_dimenzioniranje.py`, `orodja/lekcija_padec_napetosti.py`. Vsa števila v primerih preveri `assert` v generatorju, ob neskladju se ustavi.
- Okvir »Matura«: povezava na RIC (`https://www.ric.si/poklicna-matura/predmeti/drugi-predmet/elektrotehnika/`) in na zbirko nalog (stran 185). Gumb »Formule na maturi (PDF)«: `files/2024/01/formule-na-maturi.pdf`.
- Terminologija: nevtralni vodnik N (»ničelni vodnik« samo v opombi), tipkalo (ne tipka), zaščitni vodnik PE. Pri izrazih sledi učbeniku (npr. »lopate«, Δh, P_vode = 9,81 · Q · Δh).
- Vir snovi: učbenik `elektricne-instalacije-za-IEK-tehnik.pdf` v claude.ai projektu (sken, 54 str., OCR `tesseract -l eng`; pogl. 19 trifazni sistem in pridobivanje, pogl. 20 inštalacije, pogl. 21 nevarnosti).
