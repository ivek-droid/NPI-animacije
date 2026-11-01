const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const R={};
const ctx=await b.newContext({viewport:{width:1000,height:300}});const p=await ctx.newPage();const errs=[],ext=[];
p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()=='error')errs.push(m.text())});p.on('request',r=>{if(!r.url().startsWith('file:'))ext.push(r.url())});
await p.goto('file:///home/claude/npi-animacije/trifazni-sistem.html');
const rows=()=>p.evaluate(()=>[document.getElementById('chip').textContent,...[...document.querySelectorAll('#tbody tr')].map(r=>r.innerText.replace(/\s+/g,' '))]);
await p.waitForTimeout(600); const a1=await p.evaluate(()=>document.getElementById('chip').textContent);
await p.click('#pause'); const s1=await p.evaluate(()=>document.getElementById('chip').textContent); await p.waitForTimeout(500); const s2=await p.evaluate(()=>document.getElementById('chip').textContent);
R.moves=a1!=='α = 90°'; R.pauseHolds=s1===s2;
// nastavi 90°
for(let i=0;i<30;i++){const c=await p.evaluate(()=>document.getElementById('chip').textContent); if(c==='α = 90°')break; await p.click('#fwd');}
R.at90=await rows(); await p.click('#u12'); R.at90u12=await rows(); await p.click('#fwd'); await p.click('#fwd'); R.at120=await rows();
await p.screenshot({path:'/home/claude/3f.png',fullPage:true});
await p.focus('#back'); await p.keyboard.press('Enter'); R.kbd=await p.evaluate(()=>document.getElementById('chip').textContent);
R.errs=errs;R.ext=ext;
for(const w of [1000,700,480]){await p.setViewportSize({width:w,height:200});await p.goto('file:///home/claude/npi-animacije/trifazni-sistem.html?kompakt');R['H'+w]=await p.evaluate(()=>document.documentElement.scrollHeight);R['lbl'+w]=await p.evaluate(()=>document.querySelector('.ct-tm').getBoundingClientRect().height.toFixed(1));}
const c2=await b.newContext({reducedMotion:'reduce'});const q=await c2.newPage();await q.goto('file:///home/claude/npi-animacije/trifazni-sistem.html');const x1=await q.evaluate(()=>document.getElementById('chip').textContent);await q.waitForTimeout(600);R.reducedStatic=x1===await q.evaluate(()=>document.getElementById('chip').textContent);
console.log(JSON.stringify(R,null,1));await b.close();})();
