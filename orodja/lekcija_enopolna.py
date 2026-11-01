U='https://npi.splet.arnes.si'
OKOV='__OKOV__'
TXT='_builder_version="4.27.9" text_font_size="19px" text_line_height="1.6em" text_text_color="#1b1e28"'
def sec(inner,bg='#ffffff'):
    return f'[et_pb_section fb_built="1" _builder_version="4.27.9" background_color="{bg}" custom_padding="20px||28px||false|false"]{inner}[/et_pb_section]'
def row(cols,structure=None):
    cs=f' column_structure="{structure}"' if structure else ''
    return f'[et_pb_row{cs} _builder_version="4.27.9" width="90%" max_width="1080px" custom_padding="10px||10px||false|false" column_gap="3"]{cols}[/et_pb_row]'
def col(t,inner): return f'[et_pb_column type="{t}" _builder_version="4.27.9"]{inner}[/et_pb_column]'
def text(html): return f'[et_pb_text {TXT}]{html}[/et_pb_text]'
def img(src,alt,extra=''):
    return f'[et_pb_image src="{src}" alt="{alt}" title_text="{alt}" show_in_lightbox="on" _builder_version="4.27.9" border_radii="on|14px|14px|14px|14px"{extra}][/et_pb_image]'
CAP='<p style="font-size:16px;color:#4a4f5c;margin-top:6px;line-height:1.4">'
H2='<h2 style="margin-top:0">'
DET='<details style="margin:0 0 10px;padding:10px 16px;border:2px solid #c9c4bb;border-radius:14px"><summary style="cursor:pointer;font-weight:700;min-height:32px">'
def q(v,a): return f'{DET}{v}</summary><p style="margin-top:12px">{a}</p></details>'

cilj='''<h1 style="margin-bottom:16px">Enopolna vezava za razsvetljavo</h1>
<div class="pg-okvir pg-okvir--cilj" style="margin:0">
<p class="pg-okvir__oznaka">Po tej lekciji znaš</p>
<ul>
<li>pravilno priključiti okov svetilke,</li>
<li>vezati eno svetilko z enopolnim stikalom,</li>
<li>dodati drugo in tretjo svetilko in povedati, zakaj jih vežemo vzporedno.</li>
</ul>
</div>'''

kaj=H2+'''Kaj je enopolna vezava</h2>
<p>Pomisli na svojo sobo. Pri vratih je eno stikalo, na stropu ena luč. S stikalom luč prižgeš in ugasneš.</p>
<p>Takšni vezavi rečemo enopolna vezava. Z enega mesta prižgemo in ugasnemo eno ali več svetilk. Uporabimo eno enopolno stikalo.</p>
<div class="pg-okvir pg-okvir--pozor" style="margin:16px 0 0">
<p class="pg-okvir__oznaka">Ne zamenjaj</p>
<p><strong>Enopolna vezava</strong> je vezava z enopolnim stikalom.</p>
<p><strong>Enopolna shema</strong> je način risanja: več vodnikov narišemo z eno črto.</p>
</div>'''

okov=H2+'''Okov svetilke</h2>
<p>Okov je del svetilke, v katerega privijemo žarnico. Ima dva kontakta.</p>
<ul>
<li><strong>Centralni kontakt</strong> je na dnu okova. Nanj priključiš stikalni vodnik L'.</li>
<li><strong>Navojni kontakt</strong> je kovinski navoj. Nanj priključiš nevtralni vodnik N.</li>
</ul>
<p>Zakaj tako? Navoja se pri menjavi žarnice lahko dotakneš. Na navoju je nevtralni vodnik. Ko je stikalo izklopljeno, okov ni pod napetostjo.</p>
<p>Zaščitni vodnik PE (rumeno-zelen) priključiš na sponko kovinskega ohišja svetilke, ne na okov.</p>'''

ena=H2+'''Vezava ene svetilke</h2>
<ol>
<li>Fazni vodnik L pripelješ do stikala.</li>
<li>Iz stikala greš s stikalnim vodnikom L' do svetilke, na centralni kontakt.</li>
<li>Nevtralni vodnik N pripelješ naravnost do svetilke, na navojni kontakt.</li>
<li>Zaščitni vodnik PE pripelješ do sponke ohišja svetilke.</li>
</ol>
<p>Barve vodnikov: N je moder, PE je rumeno-zelen, fazni in stikalni vodnik sta rjava, črna ali siva.</p>'''

napaka1='''<div class="pg-okvir pg-okvir--pozor" style="margin:0">
<p class="pg-okvir__oznaka">Pogosta napaka</p>
<p>Stikalo vežeš v nevtralni vodnik namesto v faznega.</p>
<p>Luč sicer ugasne, a okov ostane pod napetostjo. Pri menjavi žarnice te lahko strese.</p>
<p>Pravilo: stikalo je vedno v faznem vodniku.</p>
</div>'''

vec=H2+'''Dodamo drugo in tretjo svetilko</h2>
<p>Novo svetilko priključiš na isti stikalni vodnik L' in na isti nevtralni vodnik N. Vsaka svetilka dobi svoj par vodnikov.</p>
<p>Takšni vezavi rečemo <strong>vzporedna</strong> (paralelna) vezava. Zapomni si:</p>
<ul>
<li>vsaka svetilka ima polnih 230 V,</li>
<li>ko ena svetilka pregori, ostale svetijo naprej,</li>
<li>skupni tok je vsota tokov vseh svetilk.</li>
</ul>
<p>Enako velja za LED sijalke. Tudi te vežemo vzporedno, le tok je manjši, ker imajo manjšo moč.</p>'''

primer='''<div class="pg-okvir pg-okvir--primer" style="margin:0">
<p class="pg-okvir__oznaka">Rešen primer</p>
<p style="margin-top:0">Tri žarnice po 60 W so vezane vzporedno na 230 V. Kolikšen tok teče skozi eno žarnico? Kolikšen je skupni tok?</p>
<ol class="pg-koraki">
<li><span><span class="pg-koraki__oznaka">Podatki</span>U = 230 V, P = 60 W, 3 žarnice</span></li>
<li><span><span class="pg-koraki__oznaka">Iskano</span>I₁ = ?, I = ?</span></li>
<li><span><span class="pg-koraki__oznaka">Formula</span>I₁ = P / U, I = 3 · I₁</span></li>
<li><span><span class="pg-koraki__oznaka">Vstavim</span>I₁ = 60 W / 230 V</span></li>
<li><span><span class="pg-koraki__oznaka">Izračunam</span>I₁ ≈ 0,26 A</span></li>
<li><span><span class="pg-koraki__oznaka">Vstavim</span>I = 3 · 0,26 A</span></li>
<li><span><span class="pg-koraki__oznaka">Rezultat</span><span class="pg-rezultat">I₁ ≈ 0,26 A, I ≈ 0,78 A</span></span></li>
<li><span><span class="pg-koraki__oznaka">Preverim</span>W / V = A. Animacija spodaj pokaže enak skupni tok.</span></li>
</ol>
</div>
<div class="pg-okvir pg-okvir--pozor" style="margin:16px 0 0">
<p class="pg-okvir__oznaka">Pogosta napaka</p>
<p>Napetost deliš s številom svetilk (230 V / 3). Pri vzporedni vezavi ima vsaka svetilka polnih 230 V.</p>
</div>'''

anim=H2+'''Preizkusi sam</h2>
<p>1. Dodajaj svetilke. 2. Pusti, da svetilka 2 pregori. 3. Preklopi na zaporedno in primerjaj. Uporabiš lahko tudi tipko Tab in Enter.</p>
[iframe src="https://ivek-droid.github.io/NPI-animacije/enopolna-vezava.html?kompakt" width="100%" height="800" title="Animacija: enopolna vezava z eno, dvema ali tremi svetilkami"]'''
gumb='[et_pb_button button_url="https://ivek-droid.github.io/NPI-animacije/enopolna-vezava.html" url_new_window="on" button_text="Odpri animacijo v celem oknu" module_class="pg-btn" _builder_version="4.27.9"][/et_pb_button]'

preveri=H2+'Preveri se</h2>'+q('1. Na kateri kontakt okova priključiš stikalni vodnik?','Na centralni kontakt. Nevtralni vodnik gre na navojni kontakt.')+q('2. Zakaj stikalo vežemo v fazni vodnik?','Ko je stikalo izklopljeno, svetilka in okov nista pod napetostjo.')+q('3. Svetilke so vezane vzporedno in ena pregori. Kaj se zgodi z ostalimi?','Svetijo naprej. Vsaka svetilka ima svojo pot toka in polnih 230 V.')+q('4. Kolikšen je skupni tok dveh žarnic po 60 W na 230 V?','I = 2 · 0,26 A ≈ 0,52 A.')

nakratko='''<div class="pg-okvir pg-okvir--cilj" style="margin:0">
<p class="pg-okvir__oznaka">Na kratko</p>
<ul>
<li>Stikalo je vedno v faznem vodniku.</li>
<li>Stikalni vodnik → centralni kontakt, N → navojni kontakt.</li>
<li>PE → sponka kovinskega ohišja svetilke.</li>
<li>Svetilke vežemo vzporedno: vsaka ima 230 V.</li>
<li>Skupni tok = vsota tokov svetilk.</li>
</ul>
</div>'''

out = sec(
  row(col('4_4', text(cilj)))
 +row(col('1_2', text(kaj)) + col('1_2', img(U+'/files/2024/03/vezave_navadno-splet.jpg','Vezava navadnega enopolnega stikala v prostoru: dovod iz električne omarice, stikalo pri vratih in svetilka na stropu. Barve: fazni vodnik črn, nevtralni moder, zaščitni rumeno-zelen.')
     + text(CAP+'Vezava navadnega enopolnega stikala. »Ničelni vodnik« je starejše ime za nevtralni vodnik (N). Vir: trgovina-elbi.si</p>')), '1_2,1_2')
 +row(col('1_2', text(okov)) + col('1_2', img(OKOV,"Prerez okova z žarnico: stikalni vodnik L' (rjav) je priključen na centralni kontakt na dnu, nevtralni vodnik N (moder) na navojni kontakt.", ' max_width="480px"')), '1_2,1_2')
 +row(col('1_2', text(ena)) + col('1_2', text(napaka1)), '1_2,1_2')
 +row(col('1_2', text(vec)) + col('1_2', text(primer)), '1_2,1_2')
)
out += sec(row(col('4_4', text(anim)+gumb)), '#f5f3ef')
out += sec(row(col('1_2', text(preveri)) + col('1_2', text(nakratko)), '1_2,1_2'))
import sys
okov_url=sys.argv[1] if len(sys.argv)>1 else OKOV
out=out.replace(OKOV, okov_url)
open('/home/claude/npi-animacije/slog/osnutki/enopolna-vezava.txt','w').write(out)
print(len(out))
