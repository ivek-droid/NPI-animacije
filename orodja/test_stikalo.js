const {chromium}=require('playwright');
// Test: node orodja/test_stikalo.js (iz korena repozitorija)
(async()=>{const b=await chromium.launch();const R={};
const EXP={ // [mode, closed] -> [navoj V, centralni V, sveti]
 'L1':[0,230,true],'L0':[0,0,false],'N1':[0,230,true],'N0':[230,230,false]};
for(const w of [1000,480]){
 const ctx=await b.newContext({viewport:{width:w,height:900}});const p=await ctx.newPage();
 const errs=[],ext=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()=='error')errs.push(m.text())});
 p.on('request',r=>{if(!r.url().startsWith('file:'))ext.push(r.url())});
 await p.goto('file:///home/claude/npi-animacije/stikalo-v-fazi.html');
 const st=async()=>p.evaluate(()=>({t:vThread.textContent,c:vCentral.textContent,lamp:svg.classList.contains('ct-lamp-on'),warn:warnThread.getAttribute('display'),chip:chipThreadText.textContent,row:document.querySelector('#tbody tr.ct-cur')?.dataset.m+document.querySelector('#tbody tr.ct-cur')?.dataset.c}));
 const out=[];let ok=true;
 const chk=async(key)=>{const s=await st();const e=EXP[key];const good=s.t==e[0]+' V'&&s.c==e[1]+' V'&&s.lamp===e[2]&&(s.warn==='inline')===(e[0]>0)&&s.row===key;if(!good)ok=false;out.push([key,s.t,s.c,s.lamp,s.warn,good]);};
 await chk('L1'); await p.click('#toggle'); await chk('L0');
 await p.click('#modeN'); await chk('N0'); await p.click('#toggle'); await chk('N1');
 await p.click('#toggle'); await chk('N0');
 // tipkovnica: fokus na stikalo v SVG in Enter / presledek
 await p.focus('#hit'); await p.keyboard.press('Enter'); await chk('N1'); await p.keyboard.press('Space'); await chk('N0');
 await p.click('#modeL'); await chk('L0');
 // pavza
 await p.click('#pause'); const paused=await p.evaluate(()=>document.documentElement.classList.contains('ct-paused')&&getComputedStyle(document.querySelector('.ct-flow')).animationPlayState);
 // velikosti
 const labelPx=await p.evaluate(()=>{const t=document.querySelector('.ct-l');const sc=svg.getBoundingClientRect().width/900;return +(parseFloat(getComputedStyle(t).fontSize)*sc).toFixed(1)});
 const svgW=await p.evaluate(()=>svg.getBoundingClientRect().width);
 const minBtn=await p.evaluate(()=>Math.min(...[...document.querySelectorAll('.ct-btn')].map(x=>x.offsetHeight)));
 const hPage=await p.evaluate(()=>document.documentElement.scrollHeight);
 await p.evaluate(()=>document.documentElement.classList.add('ct-kompakt'));
 const hKompakt=await p.evaluate(()=>document.documentElement.scrollHeight);
 const overflowX=await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth);
 await p.screenshot({path:`/home/claude/sw-${w}.png`,fullPage:true});
 R[w]={ok,out,paused,labelPx,svgW,minBtn,hPage,hKompakt,overflowX,errs,ext};await ctx.close();}
const ctx=await b.newContext({reducedMotion:'reduce'});const p=await ctx.newPage();await p.goto('file:///home/claude/npi-animacije/stikalo-v-fazi.html');
R.reduced=await p.evaluate(()=>getComputedStyle(document.querySelector('.ct-flow')).animationName);
console.log(JSON.stringify(R,null,1));await b.close();})();
