src = open('/home/claude/npi-animacije/orodja/lekcije_pomocniki_in_ivep.py').read().split('# ======================================================== SERIJSKA')[0]
exec(src)

# IVEp, stran »Vezave za razsvetljavo – uvod« (id 764). Predelava v novi slog (10. 11. 2026).
# Popravki besedila (potrjeni 10. 11. 2026): odklop/preverjanje napetosti, »ni nevarnih potencialov«, okov/okrov,
# »visok potencial«, utemeljitev centralnega kontakta, enotna oznaka L, lastna shema (U ne V), opis videa in alt.

SHEMA = '2026/11/razsvetljava-pravilna-vezava.png'

splosno = H2 + '''Splošno pravilo</h2>
<p>Pomisli, kako doma zamenjaš žarnico. Z roko primeš navoj sijalke. Zato na njem ne sme biti napetosti, ko je stikalo izklopljeno.</p>
''' + ul(['<strong>Stikalo</strong> vedno vežemo v fazni vodnik (L).',
         'Fazni vodnik pelje skozi stikalo na <strong>centralni kontakt</strong>. To je kontakt na dnu podnožja sijalke.',
         '<strong>Nevtralni vodnik</strong> (N) priključimo neposredno na <strong>navojni kontakt</strong>.'])

zakaj = H2 + '''Zakaj tako?</h2>
<p>Pri izklopljenem stikalu sta centralni kontakt in navoj na 0 V proti zemlji. Tako ni napetosti na delih sijalke, ki jih lahko primeš. To velja, če je inštalacija pravilno narejena.</p>
<p>Pri sijalkah z Edisonovim navojem (npr. E27) je navoj bolj izpostavljen dotiku kot kontakt na dnu. Zato je na navoju nevtralni vodnik. Če bi bila na navoju faza, bi bilo na njem 230 V proti zemlji, ko je stikalo vklopljeno. Dotik bi bil smrtno nevaren.</p>'''

pozor = box('pozor', 'Varen poseg pri sijalki',
    '<p>Ugasnjena sijalka ali izklopljeno stikalo ni dokaz, da ni napetosti. Pred posegom:</p>\n'
    + ol(['Izklopi odklopnik ali izvleci varovalko.',
          'Zavaruj pred ponovnim vklopom.',
          'Preveri z napetostnim preizkuševalnikom, da ni napetosti.',
          'Šele nato posegaj v priključek sijalke.'])
    + '\n<p>Pri izvlečeni varovalki prekinitev vidiš. Pri odklopniku je ne vidiš, zato vedno še preveri.</p>')
napaka = box('pozor', 'Pogosta napaka',
    '<p>Stikalo vežeš v nevtralni vodnik. Sijalka vseeno sveti in se ugasne.</p>\n'
    '<p>Ko je stikalo izklopljeno, je na navoju sijalke še vedno 230 V proti zemlji. Izprobaj v animaciji.</p>', '16px 0 0')

anim_blok = anim('stikalo-v-fazi.html', 'kam daš stikalo',
                 'Izklopi in vklopi stikalo. Nato ga prestavi v nevtralni vodnik in opazuj napetost na navojnem kontaktu.', 720)

preveri = H2 + 'Preveri se</h2>' \
    + q('1. V kateri vodnik vežemo stikalo za razsvetljavo?', 'V fazni vodnik (L). Tako je sijalka ob izklopljenem stikalu brez napetosti.') \
    + q('2. Na kateri kontakt sijalke priključimo fazni in na kateri nevtralni vodnik?', 'Fazni vodnik (skozi stikalo) na centralni kontakt, nevtralni vodnik na navojni kontakt.') \
    + q('3. Stikalo je pomotoma v nevtralnem vodniku in je izklopljeno. Sijalka ne sveti. Koliko voltov je na navoju proti zemlji?', '230 V. Fazni vodnik je prek nitke povezan z navojem. Dotik navoja je smrtno nevaren.')
kratko = box('cilj', 'Na kratko', ul([
    'Stikalo vežemo v fazni vodnik (L).',
    'Fazni vodnik gre skozi stikalo na centralni kontakt.',
    'Nevtralni vodnik gre na navojni kontakt.',
    'Pred posegom izklopi odklopnik, zavaruj in preveri, da ni napetosti.']))
matura = box('matura', 'Matura', '<p>Naloge o razsvetljavi (točke 5.1 do 5.4) so v zbirki maturitetnih nalog. Vezalni načrt narišeš po pravilih iz lekcij.</p>\n<p><a href="https://npi.splet.arnes.si/elektricne-instalacije/#razsvetljava-naloge">Zbirka maturitetnih nalog: razsvetljava</a> · <a href="https://www.ric.si/poklicna-matura/predmeti/drugi-predmet/elektrotehnika/">Maturitetno gradivo (RIC)</a></p>', '16px 0 0')
naprej = H2 + 'Naprej</h2>\n<p>Poglej še posamezne vezave:</p>\n' + ul([
    '<a href="https://npi.splet.arnes.si/?page_id=798">Enopolna vezava</a>',
    '<a href="https://npi.splet.arnes.si/?page_id=804">Serijska vezava</a>',
    '<a href="https://npi.splet.arnes.si/?page_id=809">Menjalna vezava</a>',
    '<a href="https://npi.splet.arnes.si/?page_id=813">Križna vezava</a>',
    '<a href="https://npi.splet.arnes.si/?page_id=1075">Bistabilni impulzni rele</a>'])

out = sec(
    row(col('4_4', text(cilj('Vezave za razsvetljavo – uvod', [
        'povedati, v kateri vodnik vežemo stikalo za razsvetljavo in zakaj,',
        'povedati, na kateri kontakt sijalke priključiš fazni in na kateri nevtralni vodnik,',
        'našteti korake varnega posega pri sijalki.']))))
  + row(col('1_2', text(splosno)) + col('1_2', img(SHEMA, 'Shema pravilne vezave sijalke: fazni vodnik L gre skozi varovalko in stikalo na centralni kontakt sijalke, nevtralni vodnik N pa neposredno na navojni kontakt. Ko je stikalo vklopljeno, je na centralnem kontaktu 230 V, na navoju 0 V.')
        + cap('Pravilna vezava: stikalo v faznem vodniku, vklopljeno. Napetosti so proti zemlji.')), '1_2,1_2')
  + row(col('1_2', text(zakaj)) + col('1_2', text(pozor + napaka)), '1_2,1_2'))
out += sec(row(col('4_4', anim_blok)), '#f5f3ef')
out += sec(
    row(col('1_2', text(preveri)) + col('1_2', text(kratko + matura)), '1_2,1_2')
  + row(col('1_2', text(naprej)) + col('1_2', text(VID) + video('2024/03/vpd-uvod-z-napotki.png', 'Video: uvod v vezave za razsvetljavo z napotki (odpre se v novem oknu)', 'https://video.arnes.si/watch/pqj752j255qt')), '1_2,1_2'))
write('vezave-za-razsvetljavo-uvod', out)
