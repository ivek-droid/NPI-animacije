import sys; sys.path.insert(0,'/home/claude/logo2'); sys.path.insert(0,'/home/claude/tools')
from char import *
import importlib.util
spec=importlib.util.spec_from_file_location('lg','/home/claude/tools/logo.py')
# reuse text_path without running file side effects
src=open('/home/claude/tools/logo.py').read().split('# A — svetilka')[0].replace("OUT='/home/claude/ds/project/assets/Logotipi'","OUT='/home/claude/logo2'")
exec(src)
def svg(name,body,w,h,vb=None,title='Pomožna gradiva – elektrotehnika'):
    vb=vb or f'0 0 {w:.0f} {h}'
    open(f'/home/claude/logo2/{name}.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" width="{w:.0f}" height="{h}" role="img" aria-label="{title}"><title>{title}</title>{body}</svg>')
# 1 maskota z oblačkom (kvadrat)
svg('E1-elektricar',character(),290,244,'0 -4 290 248')
# 2 vodoravni: lik + napis
wb,ww=word(282,142,title_size=70)
svg('E2-elektricar-vodoravni',character()+wb,282+ww+12,244,f'0 -4 {282+ww+12:.0f} 248')
# 3 znak: samo glava v krogu (za glavo strani / favicon)
head=f'<defs><clipPath id="c"><circle cx="120" cy="120" r="112"/></clipPath></defs><circle cx="120" cy="120" r="112" fill="{P}"/><g clip-path="url(#c)">{character(think=False)}</g><circle cx="120" cy="120" r="112" fill="none" stroke="{INK}" stroke-width="5"/>'
svg('E3-elektricar-znak',head,240,240)
