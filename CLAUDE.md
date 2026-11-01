# CLAUDE.md – Pomožna gradiva (npi.splet.arnes.si)

Delovni zapiski za Claudove seje. Repozitorij je javen: sem ne zapisuj gesel ali osebnih podatkov dijakov.
Navodila projekta (vloga, pravila točnosti, pisanje za dijake) so v claude.ai projektu »moja spletna stran« – ta datoteka jih dopolnjuje s tehničnim stanjem.

## Način dela z uporabnikom
- Slovenščina, tikanje, direktno. Učitelj potrdi **vsako objavo** na javni strani in **vsak popravek svojega besedila** (popravke naštej, ne vnašaj molče).
- Na GitHub (ta repozitorij) lahko potiskam brez potrditve.
- Ob začetku novega pogovora repozitorij ivek-droid/NPI-animacije priključi sam, brez vprašanja.
- Strani predelujeva **eno po eno** (osnutek → potrditev → objava), ne več naenkrat.
- **Poraba (usage):** sam predlagaj nov pogovor ali strnitev konteksta:
  - nov pogovor po zaključeni celoti (npr. ena ali dve lekciji) ali ko je pogovor zelo dolg (veliko posnetkov zaslona);
  - pred novim sklopom (nov predmet, domača stran) vedno začni nov pogovor;
  - posnetke zaslona delaj z `scale` 0.5–0.7 in jih omeji na nujne; za preverjanje raje JS/DOM;
  - na začetku novega pogovora preberi to datoteko, ne prebiraj znova celih strani.

## Okolje
- Stran: WordPress multisite pri Arnesu, tema Divi 4.27, vsebina v Divi shortcodih. Prijava Arnes AAI (seja poteče → uporabnik se prijavi sam v podoknu brskalnika; gesel ne vpisujem).
- Brez `unfiltered_html`: WP odstrani `<script>`, `onclick`, inline `<svg>`. Dovoljeni so `<details>`, `class`, `style`, `aria-*`.
- Urejanje: vgrajeni brskalnik (prijava uporabnika) + REST API iz strani:
  - nonce: `await (await fetch('/wp-admin/admin-ajax.php?action=rest-nonce')).text()` → glava `X-WP-Nonce`
  - strani: `/wp-json/wp/v2/pages/<id>?context=edit`, nalaganje medijev `POST /wp-json/wp/v2/media`
- Postopek objave lekcije: osnutek (`status:draft`, `meta._et_pb_use_builder:'on'`) → preveri, da je `content.raw` enak poslanemu (filter) → ogled 1280/480 px → potrditev → preveri `modified` ciljne strani in da je stara vsebina v revizijah → zamenjaj `content` → preveri javno stran brez prijave (`credentials:'omit'`) → osnutek v smeti (DELETE brez force).
- Varnostni klasifikator lahko zavrne zapis na objavljeno stran → prosi uporabnika za izrecno potrditev, ne obhajaj.
- Vsebina osnutka se v brskalnik prenese z GitHuba: `https://raw.githubusercontent.com/ivek-droid/NPI-animacije/main/slog/osnutki/<ime>.txt` (raw je takoj na voljo; Pages ima zamik ~1 min).
- **Predpomnilnik:** GitHub Pages hrani datoteke do 10 min. Po spremembi že vdelane animacije povečaj različico v naslovu (`?kompakt=N` v iframu, `?v=N` na gumbu; `VER` v generatorju lekcije). Znaka `&` v naslovu ne uporabljaj – WP filter ga spremeni.
- **GitHub Pages zastoj:** če `pages build and deployment` pade pri »deploy« (»in progress deployment«), uporabnik v Settings → Pages preklopi vir na None in nazaj na main / (root). Stanje: `https://api.github.com/repos/ivek-droid/NPI-animacije/actions/runs?per_page=3`.

## Slog
- Slogovni sistem (claude.ai artefakt): https://claude.ai/artifact/AYXzUAqfGAidgGmhJ9Hx92
- Globalni CSS: `slog/pomozna-gradiva-globalni.css` → prilepljen v Divi → Možnosti teme → Splošno → Lasten CSS (CodeMirror; shrani z gumbom »Save Changes«). Varnostna kopija prejšnjih nastavitev: `slog/varnostna-kopija-2026-10-31.md`.
- Barve: primary #4b1585, accent #f2b705 (samo polnilo), ink #1b1e28, surface-alt #f5f3ef; okvirji `pg-okvir--cilj|primer|pozor|matura`, rešen primer `ol.pg-koraki` + `.pg-rezultat`, gumbi Divi z `module_class="pg-btn"`.
- Pisava: sistemska (Google Fonts izklopljene). Besedilo 19 px, levo.
- Logotip: električar, ki razmišlja (`slog/logo-pomozna-gradiva-128.png`, medij 1303), ikona strani stikalo (medij 1304). Prilagajalnik: glava 80 px, logo 80 %, napis v nogi »Pomožna gradiva · Cirius Kamnik«.

## Predloga lekcije (kompaktna, potrjena)
H1 + okvir »Po tej lekciji znaš« → vrstice v dveh/treh stolpcih: vsakdanji primer + uporabnikovo besedilo | slika z opisom → pravilo vezave | »Pogosta napaka« → rešen primer (podatki, iskano, formula, koraki, rezultat, preverim) → siva sekcija »Preizkusi sam« (iframe `?kompakt` + gumb »Odpri animacijo v celem oknu«) → »Preveri se« (`<details>`) | »Na kratko« + video.
Generatorji: `orodja/lekcije_pomocniki_in_ivep.py` (pomožne funkcije sec/row/col/text/img/box/q + serijska, križna, rele), `orodja/lekcija_*.py`. Izhod v `slog/osnutki/<ime>.txt`.

## Animacije (ta repozitorij, GitHub Pages)
Pravila: ena datoteka, sistemske pisave, razredi `ct-`, pavza, tipkovnica, `prefers-reduced-motion`, ≥44 px gumbi, oznake ≥16 px pri 480 px, brez zunanjih zahtev, `?kompakt` za vdelavo.
Generator `orodja/animacije_build.py` (serijska, križna, rele, trifazni); menjalna in enopolna sta samostojni datoteki. Testi `orodja/test_*.js` (Playwright, poženi iz `/home/claude/npi-animacije`).

| Animacija | iframe višina | stran |
|---|---|---|
| menjalna-vezava.html | 620 | Menjalna vezava (809) |
| enopolna-vezava.html | 800 | Enopolna vezava (798) |
| serijska-vezava.html | 720 | Serijska vezava (804) |
| krizna-vezava.html | 700 | Križna vezava (813) |
| impulzni-rele.html | 680 | Bistabilni impulzni rele (1075) – uporabnik želi **to** različico črtkane povezave (desno, gor, desno do kontakta) |
| trifazni-sistem.html | 780 | Trifazni izmenični sistem (89) |
| vodne-turbine.html | 620 | Pridobivanje el. energije (82) – Pelton/Francis/Kaplan, regulacija pretoka |
| hidroelektrarna.html | 730 | Pridobivanje el. energije (82) – P = 9,81·Q·Δh, graf turbin |
| ohmov-zakon.html, ura.html | – | starejši, niso v novem slogu |

## Stanje (1. 11. 2026, popoldne)
Objavljeno v novem slogu: vse vezave pod IVEp (menjalna, enopolna, serijska, križna, impulzni rele) in INEp → Trifazni izmenični sistem, Pridobivanje električne energije (hidroelektrarne; videi mp4 odstranjeni, datoteke še v knjižnici medijev).

Odprto:
- INEp: Električne inštalacije (glej spodaj), Nadtokovna zaščita, Izvedba električnih inštalacij, Nevarnosti el. toka (`/995-2/`).
- Električne inštalacije (stran 185, `/elektricne-instalacije/`): zbirka slik in PDF-jev maturitetnih nalog in tabel. Analiza z napakami (tabla 2021/5: dodaten faktor 2 pri padcu napetosti) in predlogom razdelitve v `slog/analiza-elektricne-instalacije.md`, preračuni v `orodja/preveri_dimenzioniranje.py`. Prva stran OBJAVLJENA 1. 11. 2026: »Dimenzioniranje vodnika« (`/dimenzioniranje-vodnika/`, page 1338, meni 1343 kot podmeni pod ELEKTRIČNE INŠTALACIJE (188) v INEp; generator `orodja/lekcija_dimenzioniranje.py`, vir `slog/osnutki/dimenzioniranje-tok.txt`). Stran 185 ostaja zbirka maturitetnih nalog, nespremenjena. Nove strani te serije dodaj kot podmenije pod 188 (uporabnik je odobril dodajanje zavihkov). Naslednje: padec napetosti, varovalke in odklopniki, zbirka nalog (in animacija »izberi presek«, če uporabnik želi). Obstaja 2. pogoj s faktorjem k; v zbirki nalog so napake na tabli 2021/5 (glej analizo) – uporabnik še ni odločil, ali jih popraviti. Opomba: WP odstrani `style` z `div` (npr. overflow-x), zato naj bodo tabele ozke. Izpitne pole (ric.si, sc-nm.si) iz oblaka niso dosegljive; table in PDF-je se bere prek vgrajenega brskalnika.
- IVEp: Vezave za razsvetljavo – uvod, Zaključno delo in dokumentacija.
- IEKp, STR, VUI, Pomoč – še stari slog.
- Domača stran s karticami predmetov (kratice IVE, INE, IEK, STR, VUI; polna imena za `aria-label` še manjkajo).
- Predlog: omejitev širine odstavkov (~68 znakov) v globalnem CSS – čaka potrditev.
- Naslov strani »TRIFAZNI IZMENIČNI SISTEM« z velikimi črkami (vpliva na meni) – čaka potrditev.
- Gumb »na vrh strani« (Divi možnost) – predlog.
- Okvir »Matura« dodaj le s povezavo na katalog, ki jo da uporabnik.

Vir snovi: učbenik `elektricne-instalacije-za-IEK-tehnik.pdf` v claude.ai projektu (sken, 54 str., OCR s tesseract `-l eng` deluje zadovoljivo; pogl. 19 = trifazni sistem, pridobivanje, prenos). Pri izrazih sledi učbeniku (npr. »lopate«, Δh, P_vode = 9,81 · Q · Δh).

Terminologija: nevtralni vodnik N (na starih slikah »ničelni vodnik« – opomba v podnapisu), tipkalo (ne tipka), zaščitni vodnik PE.
