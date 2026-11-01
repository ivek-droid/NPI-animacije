# Animacije (GitHub Pages)

Pravila: ena datoteka, sistemske pisave, razredi `ct-`, pavza, tipkovnica, `prefers-reduced-motion`, gumbi ≥44 px, oznake ≥16 px pri 480 px, brez zunanjih zahtev in localStorage, `?kompakt` za vdelavo. Dodatna pravila (en učni cilj, slider ali gumbi, besedilni opis, test s Playwrightom, višina iframa pri 1000 in 480 px) so v navodilih projekta.

Generator `orodja/animacije_build.py` (serijska, križna, rele, trifazni); menjalna in enopolna sta samostojni datoteki. Testi `orodja/test_*.js` (Playwright, poženi iz korena repozitorija).

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
| ohmov-zakon.html, ura.html | – | starejši, niso v novem slogu |
