from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import os
OUT='/home/claude/ds/project/assets/Logotipi'
P='#4b1585'; A='#f2b705'; INK='#1b1e28'; MUTED='#4a4f5c'
fonts={w:TTFont(f'/usr/share/fonts/opentype/inter/Inter-{w}.otf') for w in ('Bold','Medium')}
def text_path(txt,w,size,x,y,kern=0):
    f=fonts[w]; gs=f.getGlyphSet(); cmap=f.getBestCmap(); upm=f['head'].unitsPerEm
    s=size/upm; pen=SVGPathPen(gs); cx=0
    for ch in txt:
        g=cmap[ord(ch)]
        tp=TransformPen(pen,(s,0,0,-s,x+cx,y)); gs[g].draw(tp)
        cx+=gs[g].width*s+kern
    return pen.getCommands(), cx
def word(x,ybase,title_size=34,sub=True,color=INK,subcolor=MUTED):
    d,wd=text_path('Pomožna gradiva','Bold',title_size,x,ybase,-0.4)
    out=f'<path fill="{color}" d="{d}"/>'
    w2=0
    if sub:
        d2,w2=text_path('ELEKTROTEHNIKA','Medium',title_size*0.42,x+1,ybase+title_size*0.62,title_size*0.42*0.12)
        out+=f'<path fill="{subcolor}" d="{d2}"/>'
    return out,max(wd,w2)
def save(name,body,w,h,title):
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h}" width="{w:.0f}" height="{h}" role="img" aria-label="{title}"><title>{title}</title>{body}</svg>'
    open(f'{OUT}/{name}.svg','w').write(svg)

# A — svetilka (IEC simbol svetilke: krog z X), "prižgana"
def markA(cx,cy,r,ring=P,fill=A,xcol=P):
    k=r*0.62
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{ring}" stroke-width="{r*0.2:.1f}"/>'
            f'<path d="M{cx-k:.1f} {cy-k:.1f} L{cx+k:.1f} {cy+k:.1f} M{cx+k:.1f} {cy-k:.1f} L{cx-k:.1f} {cy+k:.1f}" stroke="{xcol}" stroke-width="{r*0.2:.1f}" stroke-linecap="round"/>')
wb,ww=word(88,44)
save('A-svetilka-vodoravni',markA(36,36,26)+wb,88+ww+6,72,'Pomožna gradiva – elektrotehnika')
save('A-svetilka-znak',markA(36,36,26),72,72,'Pomožna gradiva')
# B — stikalo (shematski simbol zaprtega stikala)
def markB(x,y,s=1,c=P,a=A):
    # sponka - noz - sponka; konec noza na amber sponki
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<rect x="0" y="0" width="72" height="72" rx="16" fill="{c}"/>'
            f'<line x1="10" y1="46" x2="22" y2="46" stroke="#fff" stroke-width="6" stroke-linecap="round"/>'
            f'<circle cx="24" cy="46" r="5.5" fill="#fff"/>'
            f'<line x1="24" y1="46" x2="48" y2="24" stroke="#fff" stroke-width="6" stroke-linecap="round"/>'
            f'<circle cx="50" cy="46" r="7" fill="{a}"/>'
            f'<line x1="56" y1="46" x2="64" y2="46" stroke="#fff" stroke-width="6" stroke-linecap="round"/>'
            f'</g>')
wb,ww=word(88,44)
save('B-stikalo-vodoravni',markB(0,0)+wb,88+ww+6,72,'Pomožna gradiva – elektrotehnika')
save('B-stikalo-znak',markB(0,0),72,72,'Pomožna gradiva')
# C — monogram PG z amber piko (tok)
def markC(x,y):
    d,_=text_path('PG','Bold',40,x+11,y+50,-1)
    return (f'<rect x="{x}" y="{y}" width="72" height="72" rx="36" fill="{P}"/><path fill="#fff" d="{d}"/>'
            f'<circle cx="{x+60}" cy="{y+14}" r="9" fill="{A}" stroke="#fff" stroke-width="3"/>')
wb,ww=word(88,44)
save('C-monogram-vodoravni',markC(0,0)+wb,88+ww+6,72,'Pomožna gradiva – elektrotehnika')
save('C-monogram-znak',markC(0,0),72,72,'Pomožna gradiva')
# negativ za temno podlago (A)
wb,ww=word(88,44,color='#ffffff',subcolor='#d9d3e6')
save('A-svetilka-negativ',markA(36,36,26,ring='#ffffff',fill=A,xcol=P)+wb,88+ww+6,72,'Pomožna gradiva – elektrotehnika')
print(os.listdir(OUT))
