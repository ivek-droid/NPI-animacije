# CLAUDE.md – Pomožna gradiva (npi.splet.arnes.si)

Repozitorij je javen: ne zapisuj gesel in osebnih podatkov dijakov. Navodila projekta (vloga, točnost, pisanje za dijake, rešeni primeri) so v claude.ai projektu »moja spletna stran«. Tu je samo tehnika in stanje.

## Delo z uporabnikom
- Slovenščina, tikanje, direktno. Učitelj potrdi **vsako objavo** na javni strani in **vsak popravek svojega besedila** (popravke naštej).
- Strani predelujeva **eno po eno**: osnutek → potrditev → objava. Na GitHub lahko potiskam brez potrditve.
- Ob začetku pogovora repozitorij priključi sam. Preberi `docs/stanje.md`, drugih datotek ne prebiraj vnaprej.
- Poraba: sam predlagaj nov pogovor po zaključeni celoti (ena ali dve lekciji) ali ko je pogovor dolg. Posnetke zaslona čim manj (`scale` 0,5–0,7), za preverjanje raje JS/DOM.
- Podatke in dolge opise ne podvajaj v CLAUDE.md. Podrobnosti gredo v `docs/`, stanje v `docs/stanje.md`.

## Kdaj kaj prebrati
| Naloga | Datoteka |
|---|---|
| kaj je objavljeno, kaj sledi | `docs/stanje.md` |
| REST, meni, objava, predpomnilnik, GitHub Pages | `docs/okolje.md` |
| slog, predloga lekcije, generatorji, terminologija | `docs/slog-in-lekcije.md` |
| animacije, višine iframov | `docs/animacije.md` |
| napake v maturitetnih nalogah, tabele k in I_n | `slog/analiza-elektricne-instalacije.md` |

## Ključna pravila (podrobnosti v docs/)
- Brez `unfiltered_html`: WP odstrani `<script>`, `onclick`, inline `<svg>` in `style` z `div`.
- Lekcijo generira `orodja/lekcija_*.py` v `slog/osnutki/<ime>.txt`; števila v primerih preveri `assert`.
- Osnutek v brskalnik prenesi po commit SHA, ne z `main` (predpomnilnik).
- Nove strani serije »Električne inštalacije« so podmeniji pod postavko 188.
