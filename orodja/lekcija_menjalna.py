F='/files/2024/03/'
U='https://npi.splet.arnes.si'
TXT='_builder_version="4.27.9" text_font_size="19px" text_line_height="1.6em" text_text_color="#1b1e28"'
def sec(inner,bg='#ffffff'):
    return f'[et_pb_section fb_built="1" _builder_version="4.27.9" background_color="{bg}" custom_padding="20px||28px||false|false"]{inner}[/et_pb_section]'
def row(cols,structure=None):
    cs=f' column_structure="{structure}"' if structure else ''
    return f'[et_pb_row{cs} _builder_version="4.27.9" width="90%" max_width="1080px" custom_padding="10px||10px||false|false" column_gap="3"]{cols}[/et_pb_row]'
def col(t,inner): return f'[et_pb_column type="{t}" _builder_version="4.27.9"]{inner}[/et_pb_column]'
def text(html): return f'[et_pb_text {TXT}]{html}[/et_pb_text]'
def img(src,alt,lightbox=True,extra=''):
    lb=' show_in_lightbox="on"' if lightbox else ''
    return f'[et_pb_image src="{src}" alt="{alt}" title_text="{alt}"{lb} _builder_version="4.27.9" border_radii="on|14px|14px|14px|14px"{extra}][/et_pb_image]'

cilj='''<h1 style="margin-bottom:16px">Menjalna vezava za razsvetljavo</h1>
<div class="pg-okvir pg-okvir--cilj" style="margin:0">
<p class="pg-okvir__oznaka">Po tej lekciji znaš</p>
<ul>
<li>povedati, kje uporabimo menjalno vezavo,</li>
<li>prebrati enopolno in dvopolno shemo menjalne vezave,</li>
<li>povedati, kam priključiš fazni, nevtralni in stikalne vodnike.</li>
</ul>
</div>'''

razlaga='''<h2 style="margin-top:0">Kaj je menjalna vezava</h2>
<p>Primer je soba, kjer pri vratih vklopimo razsvetljavo in jo nato pri postelji z drugim menjalnim stikalom izklopimo. Ali pa stopnišče, ki ima možnost vklopa in izklopa pri vznožju stopnišča ter prav tako na vrhu stopnišča, kot kaže slika.</p>
<p>Takšno vezavo imenujemo menjalna vezava, pogosto tudi izmenična vezava. Omogoča vklop in izklop ene ali več svetilk z dveh različnih mest. Zato v tem primeru uporabljamo dve krajevno ločeni stikali.</p>'''

pravilo='''<h2 style="margin-top:0">Pravilo vezave</h2>
<p>Fazni vodnik vodimo od dovoda k bližnjemu menjalnemu stikalu (da prihranimo material) na kontakt, ki je označen s puščico ali črko L ali črko P. Nevtralni vodnik vodimo od dovoda k vsem svetilkam na navojni kontakt. Stikalni vodniki so trije:</p>
<ul>
<li>en stikalni vodnik vodimo od drugega menjalnega stikala s skupnega kontakta (označen s puščico, L ali P) do vseh svetilk na centralni kontakt okova.</li>
<li>dva stikalna vodnika pa povezujeta obe stikali in sta priključena na oba še prosta priključka stikal; vrstni red ni važen.</li>
</ul>
<div class="pg-okvir pg-okvir--pozor" style="margin:0">
<p class="pg-okvir__oznaka">Pogosta napaka</p>
<p>Fazni vodnik priključiš na napačen kontakt stikala – ne na tistega s puščico, črko L ali P.</p>
<p>Potem svetilka sveti samo pri enem položaju obeh stikal. Z enega mesta je ne moreš vedno prižgati in ugasniti.</p>
</div>'''

anim='''<h2 style="margin-top:0">Preizkusi sam</h2>
<p>Preklapljaj stikali in opazuj, po katerem vodniku teče tok. Uporabiš lahko tudi tipko Tab in Enter.</p>
[iframe src="https://ivek-droid.github.io/NPI-animacije/menjalna-vezava.html?kompakt" width="100%" height="620" title="Animacija: menjalna vezava"]'''

video='''<h2 style="margin-top:0">Poglej video</h2>
<p>Klikni sliko. Video o menjalni vezavi se odpre v novem oknu.</p>'''

preveri='''<h2 style="margin-top:0">Preveri se</h2>
<details style="margin:0 0 10px;padding:10px 16px;border:2px solid #c9c4bb;border-radius:14px">
<summary style="cursor:pointer;font-weight:700;min-height:32px">1. Koliko stikalnih vodnikov ima menjalna vezava?</summary>
<p style="margin-top:12px">Tri. Dva povezujeta obe stikali, tretji vodi od drugega stikala do svetilke.</p>
</details>
<details style="margin:0 0 10px;padding:10px 16px;border:2px solid #c9c4bb;border-radius:14px">
<summary style="cursor:pointer;font-weight:700;min-height:32px">2. Na kateri kontakt okova priključiš nevtralni vodnik?</summary>
<p style="margin-top:12px">Na navojni kontakt. Stikalni vodnik gre na centralni kontakt.</p>
</details>
<details style="margin:0 0 10px;padding:10px 16px;border:2px solid #c9c4bb;border-radius:14px">
<summary style="cursor:pointer;font-weight:700;min-height:32px">3. Stikali sta v istem položaju in svetilka sveti. Kaj se zgodi, ko preklopiš eno stikalo?</summary>
<p style="margin-top:12px">Svetilka ugasne. Vsak preklop enega stikala spremeni stanje svetilke.</p>
</details>'''

CAP='<p style="font-size:16px;color:#4a4f5c;margin-top:6px;line-height:1.4">'
gumb='[et_pb_button button_url="https://ivek-droid.github.io/NPI-animacije/menjalna-vezava.html" url_new_window="on" button_text="Odpri animacijo v celem oknu" module_class="pg-btn" _builder_version="4.27.9"][/et_pb_button]'
out = sec(
  row(col('4_4', text(cilj)))
 +row(col('1_2', text(razlaga))
     +col('1_2', img(U+F+'FB_IMG_1708346014869.jpg','Stopnišče z menjalnim stikalom spodaj (two way switch 1) in zgoraj (two way switch 2) ter svetilko nad stopnicami.', extra=' max_width="420px"')
               +text(CAP+'Angleške oznake: two way switch = menjalno stikalo, bulb holder = okov svetilke.</p>')), '1_2,1_2')
 +row(col('4_4', text('<h2 style="margin-top:0">Sheme</h2><p>Enopolna shema pokaže, koliko vodnikov je na vsakem odseku. Dvopolna shema pokaže vsak vodnik posebej. Klikni sliko, da jo povečaš.</p>')))
 +row(col('1_3', img(U+F+'vezave_menjalno-splet.jpg','Shema menjalne vezave v sobi: dovod iz električne omarice, dve menjalni stikali na stenah in svetilka na stropu. Barve: fazni vodnik črn, nevtralni moder, zaščitni rumeno-zelen.')
               +text(CAP+'Vezava v prostoru. »Ničelni vodnik« je starejše ime za nevtralni vodnik (N). Vir: trgovina-elbi.si</p>'))
     +col('1_3', img(U+F+'enopolna-menjalna-vezava.png','Enopolna shema menjalne vezave z dvema svetilkama La1 in La2. Med stikaloma so trije vodniki, od dovoda dva.')+text(CAP+'Enopolna shema</p>'))
     +col('1_3', img(U+F+'dvopolna-menjalna-vezava.png','Dvopolna shema menjalne vezave: dovod L in N, dve menjalni stikali in dve svetilki, vsak vodnik narisan posebej.')+text(CAP+'Dvopolna shema</p>')), '1_3,1_3,1_3')
 +row(col('1_2', text(pravilo.split('<div class="pg-okvir')[0]))
     +col('1_2', text('<div class="pg-okvir'+pravilo.split('<div class="pg-okvir',1)[1])), '1_2,1_2')
)
out += sec(row(col('4_4', text(anim)+gumb)), '#f5f3ef')
out += sec(
  row(col('1_2', text(preveri))
     +col('1_2', text(video)+img(U+F+'video-menjalna-vezava.png','Video: menjalna vezava (odpre se v novem oknu)', lightbox=False, extra=' url="https://video.arnes.si/watch/myfjpxlrzwyb" url_new_window="on" max_width="420px"')), '1_2,1_2')
)
open('/home/claude/npi-animacije/slog/osnutki/menjalna-vezava.txt','w').write(out)
print(len(out))
