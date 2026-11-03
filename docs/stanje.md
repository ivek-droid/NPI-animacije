# Stanje strani (3. 11. 2026)

## Objavljeno v novem slogu
- IVEp: menjalna (809), enopolna (798), serijska (804), križna (813), impulzni rele (1075).
- INEp: Trifazni izmenični sistem (89), Pridobivanje električne energije (82).
- INEp → ELEKTRIČNE INŠTALACIJE (185, meni 188): zbirka maturitetnih nalog (slike in PDF-ji, nespremenjena) in podmeniji:
  - Dimenzioniranje vodnika (1338, meni 1343), `/dimenzioniranje-vodnika/`
  - Padec napetosti (1344, meni 1346), `/padec-napetosti/`
  - Varovalke in odklopniki (1347, meni 1349), `/varovalke-in-odklopniki/`, generator `orodja/lekcija_varovalke.py`

## Naslednje
- Zbirka po temah objavljena 3. 11. 2026 na strani 185 (generator `orodja/lekcija_zbirka.py`); stari razdelki so pod »Izvirne table in PDF-ji«. Razsvetljava: 5.1 in 5.2 po uradnih navodilih za spom 2020, jesen 2021, spom 2023. Manjkajo navodila za jesen 2020 (P202) in jesen 2022 (P222) ter risbe 5.4. Vaja »upornost žice« (iz `resitev-1.pdf`, popravljene enote, baker λ = 56) objavljena 3. 11. 2026 v razdelku Upornost. Opomba pri nalogi zimski 2020 5.4 popravljena (prej napačno »2021«; datoteki »zimski 2020/2021« sta ista pola P203).
- Zbirka nalog (stran 185); animacija »izberi presek« je izdelana (`izberi-presek.html`, 3. 11. 2026), vdelana na stran 1338 (3. 11. 2026). Višine iframa ni bilo mogoče izmeriti v izrisu (pane skrit): preveri vizualno. Podmeniji pod 188.
- Stran 185: opomba k nalogi 5.4 (zimski 2020) objavljena 1. 11., popravljena 3. 11. 2026 (okvir »Pozor«; napaka v faktorju 2 in varovalka 10 A). Slika table ni zamenjana. Analiza: `slog/analiza-elektricne-instalacije.md`, preračuni `orodja/preveri_dimenzioniranje.py`.
- Okvir »Matura« na straneh 1338 in 1344 popravljen v »zimski rok 2020 in 2022« (3. 11. 2026).

- IVEp: stran »Uporaba univerzalnega merilnika« (1367, meni 1369 pod IVEp, `/uporaba-univerzalnega-merilnika/`) objavljena 3. 11. 2026; generator `orodja/lekcija_merilnik.py`, animacija `odcitavanje-instrumenta.html`, slika instrumenta Iskra MI 7043 (medij 1366). Skale in območja potrjene s fotografijo. Okvir »Matura« manjka (ni potrjeno, ali je tema v katalogu). Višine iframa (1450) po objavi ni vizualno preverjena.
- IVEp, stran 1367: dodana animacija »Priključitev voltmetra in ampermetra« (`priklop-merilnikov.html`, 3. 11. 2026, iframe 1220, nov razdelek »Preizkusi sam: priključitev merilnikov« pred animacijo odčitavanja). Okvir »Matura« po dogovoru ni dodan. Globalni CSS v5 (3. 11. 2026): zgoščeni koraki rešenih primerov (`.pg-koraki`: viseča zamaknjenost, oznaka 120 px levo, besedilo se ne lomi pod oznako; pod 560 px oznaka nad besedilom). Mreža (v4) je razbijala indekse in poševni tisk v celice, zato je ne uporabljaj. Velja za strani 82, 89, 185, 798, 813, 1338, 1344, 1347, 1367; primera na 1367 831 → 368 px pri 618 px. Stran 82 ima pri 400 px vodoravni preliv zaradi tabele (ni povezano s koraki). Višina iframa na telefonu (potrebnih ~1700 px) ni vizualno preverjena v izrisu strani.

## Odprto
- INEp: Nadtokovna zaščita (619), Izvedba električnih inštalacij (662), Nevarnosti el. toka (995).
- IVEp: Vezave za razsvetljavo – uvod (764), Zaključno delo in dokumentacija (1123).
- IEKp (44), STR (145), VUI (58), Pomoč (822): še stari slog.
- Domača stran s karticami predmetov (IVE, INE, IEK, STR, VUI; polna imena za `aria-label` manjkajo).
- Globalni CSS v3 (3. 11. 2026; v2 je po pomoti zožil vse iframe-e, ker so v `<p>`, zdaj izvzeti z `p:has(> iframe)`): odstavki in seznami največ 68 znakov (`--measure`), gumb »na vrh strani« vklopljen (Divi → Splošno) in oblikovan (56 px). Naslov strani 89 in postavka menija 161 sta zdaj »Trifazni izmenični sistem«. Pri shranjevanju CSS prek JS uporabi CodeMirror (`.CodeMirror.CodeMirror.setValue`, nato `#epanel-save`); sama sprememba `textarea.value` se ne shrani. Gumb »na vrh« nima besedilne oznake za bralnik zaslona (Divi ga ne doda).
