src = open('/home/claude/npi-animacije/orodja/lekcije_pomocniki_in_ivep.py').read().split('# ======================================================== SERIJSKA')[0]
exec(src)

# IVEp, prva stran (id 139): besedilo uporabnika je ohranjeno dobesedno, spremenjena sta samo razporeditev in slog.
# Dodano po predlogi: okvir »Po tej lekciji znaš«, »Preveri se«, »Na kratko«.

uvod = H2 + '''Vezica iz bakrenega vodnika</h2>
<p>Izolirane bakrene vodnike uporabljamo za prenos električne energije. Vodnik je sestavljen iz notranje kovine - največkrat bakra. Obdaja pa ga plašč izolacije – PVC ali guma. Izdelali bomo nekaj vezic, da se navadimo uporabljati orodje.</p>'''
orodje_h = H2 + 'Orodje</h2>'
usesce = H2 + '''Privijanje ušesca</h2>
''' + ul(['Ušesca morajo biti obrnjena / zavita v smeri privijanja vijaka.',
         'Pri privijanju več ušesc moramo dati vmes podložka.',
         'Za privijanje uporabimo izvijač primerne velikosti, da ne poškodujemo glave vijakov (ploščati  / križni).',
         'Izvedemo kontrolo spoja.'])
vodniki = H2 + '''Inštalacijski vodniki in kabli</h2>
<p>Za prenos električne energije uporabljamo izolirane električne <strong>vodnike</strong> (a) in <strong>kable</strong> (b in c). Enožilne izolirane vodnike imenujemo kar <strong>vodniki</strong>. <strong>Kabli</strong> pa so sestavljeni iz več izoliranih vodnikov, ki so obdani z izolacijskim plaščem. Žila vodnika je lahko <strong>masivna</strong> (a in b) ali <strong>pramenasta</strong> (c). Masivne vodnike uporabljamo za <strong>nepremične</strong>, pramenaste (gibke, fleksibilne) pa za <strong>premične</strong> električne porabnike.</p>'''
barve = H2 + '''Barvne oznake vodnikov in kablov</h2>
<p>Barvno označevanje uporabljamo zaradi medsebojnega razpoznavanja in zaradi ugotavljanja namembnosti vodov.</p>
''' + ul(['L1, L2, L3 fazni vodniki - črna (čr) ali rjava (rj)',
         'N nevtralni ali ničelni vodnik - svetlomodra (smo)',
         'PE zaščitni vodnik - rumeno-zelena (ru-ze)',
         'PEN zaščitno - nevtralni vodnik (ru-ze)'])
vtic_uvod = H2 + '''Vtično-spojne naprave</h2>
<p>Služijo nam za priključevanje premičnih električnih porabnikov na inštalacije. V stanovanjih uporabljamo predvsem enofazne vtično-spojne naprave z zaščitnim kontaktom (L, N, PE). Redkeje za priklop uporabljamo trifazne vtično-spojne naprave. (L1, L2, L3, N, PE). Med vtično-spojne naprave štejemo vtičnice, vtiče, prenosne vtičnice, natičnice in natiče.</p>'''
vtic = H2 + '''Enofazna vtičnica, vtič</h2>
''' + ul(['Fazni in nevtralni vodnik lahko priključimo na poljuben čep.',
         'Pazljivo moramo pritrditi zaščitni vodnik na zaščitni kontakt vtiča. Zaščitni vodnik mora biti tako dolg, da ga tudi ob nasilnem izvleku kabla odtrgamo zadnjega.',
         'Pred sestavljanjem obvezna kontrola.'])
VIDEO = H2 + 'Poglej video</h2>\n<p>Klikni sliko. Video se odpre v novem oknu.</p>'

preveri = H2 + 'Preveri se</h2>' \
    + q('1. Kaj je razlika med vodnikom in kablom?', 'Vodnik je enožilen izoliran vodnik. Kabel je sestavljen iz več izoliranih vodnikov, ki jih obdaja skupni izolacijski plašč.') \
    + q('2. Kakšne barve je nevtralni vodnik N in kakšne zaščitni vodnik PE?', 'N je svetlomodre barve, PE je rumeno-zelene barve.') \
    + q('3. V katero smer obrneš ušesce, preden ga privijaš z vijakom?', 'V smeri privijanja vijaka.') \
    + q('4. Zakaj mora biti zaščitni vodnik v vtiču daljši od ostalih?', 'Da se ob nasilnem izvleku kabla odtrga zadnji. Zaščita ostane povezana do konca.')
kratko = box('cilj', 'Na kratko', ul([
    'Vodnik je enožilen, kabel ima več izoliranih vodnikov v skupnem plašču.',
    'Masivni vodniki so za nepremične, pramenasti za premične porabnike.',
    'N je svetlomodra, PE rumeno-zelena.',
    'Ušesce obrni v smeri privijanja vijaka.',
    'Po vsakem spoju naredi kontrolo.']))

orodja = [('scipalke.jpg', 'Ščipalne klešče', 'ščipalne klešče'),
          ('snemalke.jpg', 'Snemalne klešče', 'snemalne klešče'),
          ('konicaste-kombinirke.jpg', 'Koničaste kombinirke', 'koničaste kombinirke'),
          ('okrogle-klesce.jpg', 'Okrogle klešče', 'okrogle klešče'),
          ('olfa.jpg', 'Olfa nož', 'olfa nož')]
def orodje(i): return col('1_3', img('2024/03/' + orodja[i][0], orodja[i][1]) + cap(orodja[i][2]))

out = sec(
    row(col('4_4', text(cilj('Izdelava vezice iz bakrenega vodnika', [
        'izbrati orodje za delo z vodniki,',
        'pravilno privijati ušesce na vijak,',
        'ločiti vodnike in kable ter masivne in pramenaste žile,',
        'prepoznati barvne oznake vodnikov,',
        'pravilno priključiti enofazni vtič.']))))
  + row(col('1_2', text(uvod)) + col('1_2', text(VIDEO) + video('2024/03/vezice.png', 'Video: izdelava vezice (odpre se v novem oknu)', 'https://video.arnes.si/watch/srp4jj64kbm6')), '1_2,1_2')
  + row(col('4_4', text(orodje_h)))
  + row(orodje(0) + orodje(1) + orodje(2), '1_3,1_3,1_3')
  + row(orodje(3) + orodje(4), '1_3,1_3')
  + row(col('1_2', text(usesce)) + col('1_2', img('2024/03/okrogle-klesce-uporaba.png', 'Okrogle klešče: oblikovanje ušesca na koncu vodnika') + cap('Uporaba okroglih klešč')
        + img('2024/03/usesce.png', 'Ušesce na koncu vodnika, zavito v smeri privijanja vijaka') + cap('Ušesce')), '1_2,1_2')
  + row(col('1_2', text(vodniki)) + col('1_2', img('2024/03/masivni-in-pramenasti.png', 'Vodnik (a), kabel z masivnimi žilami (b) in kabel s pramenastimi žilami (c).') + cap('Masivni (a, b) in pramenasti (c) vodniki')), '1_2,1_2')
  + row(col('1_2', text(barve)) + col('1_2', img('2024/03/barve-vodnikov.png', 'Barve vodnikov: fazni črn ali rjav, nevtralni svetlomodri, zaščitni rumeno-zelen.') + cap('Barvne oznake vodnikov')), '1_2,1_2'))

out += sec(
    row(col('1_2', text(vtic_uvod)) + col('1_2', img('2024/03/1f-vticnica.png', 'Enofazna vtičnica') + cap('Enofazna vtičnica')), '1_2,1_2')
  + row(col('1_2', text(vtic)) + col('1_2', img('2024/03/1f-vtic-razlaga.png', 'Enofazni vtič z razlago priključkov') + cap('Enofazni vtič: razlaga')), '1_2,1_2')
  + row(col('1_2', img('2024/03/1f-vtic.png', 'Enofazni vtič') + cap('Enofazni vtič')) + col('1_2', img('2024/03/3f-vtic.png', 'Trifazni vtič') + cap('Trifazni vtič')), '1_2,1_2')
  + row(col('1_2', img('2024/03/3f-vtic-sponke.png', 'Trifazni vtič: priključne sponke') + cap('Trifazni vtič: sponke')) + col('1_2', img('2024/03/3f-napacna-smer.png', 'Trifazni vtič: primer napačne smeri') + cap('Trifazni vtič: napačna smer')), '1_2,1_2'))

out += sec(row(col('1_2', text(preveri)) + col('1_2', text(kratko)), '1_2,1_2'))
write('ivep-prva-stran', out)
