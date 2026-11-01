const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const R={};const F='file:///home/claude/npi-animacije/vodne-turbine.html';
const ctx=await b.newContext({viewport:{width:1000,height:300}});const p=await ctx.newPage();const errs=[],ext=[];
p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()=='error')errs.push(m.text())});p.on('request',r=>{if(!r.url().startsWith('file:'))ext.push(r.url())});
await p.goto(F);const st=()=>p.evaluate(()=>[document.getElementById('title').textContent,document.getElementById('pwr').textContent,document.getElementById('desc').textContent,document.getElementById('eff').hidden?'':document.getElementById('eff').textContent]);
R.p0=await st();
await p.focus('[data-k=igla][data-d="-1"]');for(let i=0;i<4;i++)await p.keyboard.press('Enter');R.p_closed=await st();R.focusKept=await p.evaluate(()=>document.activeElement.getAttribute('data-k'));
await p.keyboard.press('Tab');await p.keyboard.press('Enter');await p.keyboard.press('Enter');await p.keyboard.press('Enter');R.p_open=await st();
await p.click('#noz');R.p_noz=await st();await p.screenshot({path:'/home/claude/vt_pel.png',fullPage:true});
await p.click('#noz');
const tr=()=>p.evaluate(()=>document.querySelector('#svg circle[r="20"]')?.parentNode.getAttribute('transform'));
const a1=await tr();await p.waitForTimeout(300);const a2=await tr();await p.click('#pause');const a3=await tr();await p.waitForTimeout(300);const a4=await tr();R.rotates=a1!==a2;R.pauseHolds=a3===a4;await p.click('#pause');
await p.click('[data-t=francis]');R.f=await st();await p.screenshot({path:'/home/claude/vt_fra.png',fullPage:true});
await p.click('[data-t=kaplan]');R.k=await st();await p.click('[data-k=nak][data-d="-1"]');await p.click('[data-k=nak][data-d="-1"]');R.k_bad=await st();await p.screenshot({path:'/home/claude/vt_kap.png',fullPage:true});
R.errs=errs;R.ext=ext;
for(const w of [1000,480]){await p.setViewportSize({width:w,height:200});await p.goto(F+'?kompakt');let m=0;for(const t of ['pelton','francis','kaplan']){await p.click('[data-t='+t+']');await p.waitForTimeout(50);m=Math.max(m,await p.evaluate(()=>document.documentElement.scrollHeight));}R['H'+w]=m;R['lbl'+w]=await p.evaluate(()=>Math.min(...[...document.querySelectorAll('svg text')].map(t=>t.getBoundingClientRect().height)).toFixed(1));R['btn'+w]=await p.evaluate(()=>Math.min(...[...document.querySelectorAll('.ct-btn')].map(t=>t.getBoundingClientRect().height)));}
await p.screenshot({path:'/home/claude/vt_480.png',fullPage:true});
const c2=await b.newContext({reducedMotion:'reduce'});const q=await c2.newPage();await q.goto(F);R.reduced=await q.evaluate(()=>document.getElementById('pause').textContent);
console.log(JSON.stringify(R,null,1));await b.close();})();
