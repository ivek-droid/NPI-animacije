# Stanje strani (1. 11. 2026)

## Objavljeno v novem slogu
- IVEp: menjalna (809), enopolna (798), serijska (804), križna (813), impulzni rele (1075).
- INEp: Trifazni izmenični sistem (89), Pridobivanje električne energije (82).
- INEp → ELEKTRIČNE INŠTALACIJE (185, meni 188): zbirka maturitetnih nalog (slike in PDF-ji, nespremenjena) in podmeniji:
  - Dimenzioniranje vodnika (1338, meni 1343), `/dimenzioniranje-vodnika/`
  - Padec napetosti (1344, meni 1346), `/padec-napetosti/`
  - Varovalke in odklopniki (1347, meni 1349), `/varovalke-in-odklopniki/`, generator `orodja/lekcija_varovalke.py`

## Naslednje
- Zbirka po temah: osnutek `slog/osnutki/zbirka-po-temah.txt` (generator `orodja/lekcija_zbirka.py`), koncept na strani 1353 (3. 11. 2026), čaka potrditev. Nova vsebina pride za prvim razdelkom (Ohm) strani 185, stari razdelki ostanejo pod »Izvirne table in PDF-ji«. Manjkajo uradne rešitve točk 5.1, 5.2, 5.4 pri razsvetljavi. Datoteki »zimski 2020« in »zimski 2021« sta ista pola (P203); opomba na strani 185 pravi »2021«.
- Zbirka nalog (stran 185); po želji animacija »izberi presek«. Podmeniji pod 188.
- Stran 185: opomba k nalogi 5.4 (zimski 2021) objavljena 1. 11. 2026 (okvir »Pozor« pod gumboma za zimski 2021; napaka v faktorju 2 in varovalka 10 A). Slika table ni zamenjana. Analiza: `slog/analiza-elektricne-instalacije.md`, preračuni `orodja/preveri_dimenzioniranje.py`.

## Odprto
- INEp: Nadtokovna zaščita (619), Izvedba električnih inštalacij (662), Nevarnosti el. toka (995).
- IVEp: Vezave za razsvetljavo – uvod (764), Zaključno delo in dokumentacija (1123).
- IEKp (44), STR (145), VUI (58), Pomoč (822): še stari slog.
- Domača stran s karticami predmetov (IVE, INE, IEK, STR, VUI; polna imena za `aria-label` manjkajo).
- Čakajo potrditev: omejitev širine odstavkov (~68 znakov) v globalnem CSS, naslov »TRIFAZNI IZMENIČNI SISTEM« z velikimi črkami (vpliva na meni), gumb »na vrh strani«.
