# Okolje in postopek objave

## Stran
- WordPress multisite pri Arnesu, tema Divi 4.27, vsebina v Divi shortcodih. Prijava Arnes AAI: seja poteče, uporabnik se prijavi sam v vgrajenem brskalniku. Gesel ne vpisujem.
- Brez `unfiltered_html`: WP odstrani `<script>`, `onclick`, inline `<svg>` in `style` z `div` (npr. `overflow-x`). Dovoljeni so `<details>`, `class`, `style` na večini elementov, `aria-*`, tabele. Tabele naj bodo ozke (največ 5 stolpcev).
- Izpitne pole (ric.si, sc-nm.si) iz oblaka niso dosegljive. Slike in PDF-je s strani berem prek vgrajenega brskalnika (zoom na posnetku zaslona ne poveča, za natančno branje uporabi canvas v JS).

## REST iz vgrajenega brskalnika (stran mora biti odprta v prijavljeni seji)
- Nonce: `await (await fetch('/wp-admin/admin-ajax.php?action=rest-nonce')).text()` → glava `X-WP-Nonce`.
- Strani: `/wp-json/wp/v2/pages/<id>?context=edit`. Mediji: `POST /wp-json/wp/v2/media`.
- Meni (id 2, »Glavni meni«): `POST /wp-json/wp/v2/menu-items` z `{title, type:'post_type', object:'page', object_id, menus:2, parent, status:'publish'}`.
- Podmeniji INEp: nadrejena postavka INEp je 68, ELEKTRIČNE INŠTALACIJE postavka 188. Nove lekcije te serije so podmeniji pod 188.

## Postopek objave lekcije (osnutek → potrditev → objava)
1. Generator napiše `slog/osnutki/<ime>.txt`, commit in push.
2. V brskalniku prenesi vsebino z GitHuba **po commit SHA**: `https://raw.githubusercontent.com/ivek-droid/NPI-animacije/<sha>/slog/osnutki/<ime>.txt`. Naslov z `main` je predpomnjen in vrne staro različico.
3. `POST /pages` z `status:'draft'`, `meta:{_et_pb_use_builder:'on'}`. Preveri, da je `content.raw` enak poslanemu (filter ga ne sme spremeniti).
4. Ogled `?page_id=<id>&preview=true` pri 1280 in 480 px z JS (vodoravni preliv, najmanjša pisava 16 px, ostanki `[et_pb`). Posnetkov zaslona čim manj.
5. Uporabnik potrdi. Nato `POST /pages/<id>` z `{title, slug, status:'publish'}` in menijska postavka.
6. Preveri javno stran brez prijave (`credentials:'omit'`): status 200, ni ostankov shortcodov, ključne številke, postavka v meniju.
7. Zamenjava vsebine že objavljene strani: najprej suhi preizkus na osnutku, preveri `modified` in revizije. Začasne osnutke v smeti (DELETE brez force).
- Varnostni klasifikator lahko zavrne zapis na objavljeno stran: prosi uporabnika za izrecno potrditev, ne obhajaj.

## GitHub Pages
- Predpomnilnik do 10 min. Po spremembi že vdelane animacije povečaj različico v naslovu (`?kompakt=N` v iframu, `?v=N` na gumbu, `VER` v generatorju). Znaka `&` v naslovu ne uporabljaj, WP ga spremeni.
- Če `pages build and deployment` pade pri »deploy«: uporabnik v Settings → Pages preklopi vir na None in nazaj na main / (root). Stanje: `https://api.github.com/repos/ivek-droid/NPI-animacije/actions/runs?per_page=3`.
- Repozitorij se je preselil na `ivek-droid/NPI-animacije` (git opozori, push deluje).
