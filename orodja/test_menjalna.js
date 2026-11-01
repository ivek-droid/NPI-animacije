const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const R={};
for(const w of [1000,480]){
 const ctx=await b.newContext({viewport:{width:w,height:900}});const p=await ctx.newPage();
 const errs=[],ext=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()=='error')errs.push(m.text())});
 p.on('request',r=>{if(!r.url().startsWith('file:'))ext.push(r.url())});
 await p.goto('file:///home/claude/npi-animacije/menjalna-vezava.html');
 const st=async()=>p.evaluate(()=>({lamp:document.getElementById('svg').classList.contains('ct-lamp-on'),p1:pos1.textContent,p2:pos2.textContent,chip:chipText.textContent}));
 const seq=[await st()]; await p.click('#btn1'); seq.push(await st()); await p.click('#btn2'); seq.push(await st()); await p.click('#btn1'); seq.push(await st());
 // tipkovnica: Tab do hit1 in Enter
 await p.keyboard.press('Tab'); const f1=await p.evaluate(()=>document.activeElement.id); await p.keyboard.press('Enter'); seq.push(await st());
 await p.click('#pause'); const paused=await p.evaluate(()=>getComputedStyle(document.querySelector('.ct-flow.ct-show')||document.querySelector('.ct-flow')).animationPlayState);
 const fs=await p.evaluate(()=>{const t=document.querySelector('.ct-t.ct-m');return t.getBoundingClientRect().height});
 const H=await p.evaluate(()=>document.documentElement.scrollHeight);
 const minBtn=await p.evaluate(()=>Math.min(...[...document.querySelectorAll('.ct-btn')].map(x=>x.offsetHeight)));
 await p.screenshot({path:`/home/claude/mv-${w}.png`,fullPage:true});
 R[w]={seq,f1,paused,labelPx:+fs.toFixed(1),H,minBtn,errs,ext};await ctx.close();}
const ctx=await b.newContext({reducedMotion:'reduce'});const p=await ctx.newPage();await p.goto('file:///home/claude/npi-animacije/menjalna-vezava.html');
R.reduced=await p.evaluate(()=>getComputedStyle(document.querySelector('.ct-flow')).animationName);
console.log(JSON.stringify(R,null,1));await b.close();})();
