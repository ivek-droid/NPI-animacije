const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const out={};
const ctx=await b.newContext({viewport:{width:1000,height:300}});const p=await ctx.newPage();const errs=[],ext=[];
p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()=='error')errs.push(m.text())});p.on('request',r=>{if(!r.url().startsWith('file:'))ext.push(r.url())});
await p.goto('file:///home/claude/npi-animacije/enopolna-vezava.html');
const tab=async()=>p.evaluate(()=>[...document.querySelectorAll('#tbody tr')].map(r=>[...r.cells].map(c=>c.textContent).join(' | ')).concat([document.getElementById('chip').textContent]));
const shot=async(n)=>p.screenshot({path:`/home/claude/en-${n}.png`,fullPage:true});
out.p1=await tab(); await p.click('[data-n="3"]'); out.p3=await tab(); await shot('par3');
await p.click('#burn'); out.p3b=await tab(); await shot('par3b');
await p.click('[data-mode="ser"]'); out.s3b=await tab(); await p.click('#burn'); out.s3=await tab(); await shot('ser3');
await p.click('[data-n="2"]'); out.s2=await tab();
await p.click('#sw'); out.s2off=await tab();
await p.click('[data-n="1"]'); out.burnDisabled=await p.evaluate(()=>document.getElementById('burn').disabled);
// tipkovnica
await p.click('[data-mode="par"]'); await p.focus('[data-n="1"]'); await p.keyboard.press('Tab'); await p.keyboard.press('Enter'); out.kbd=await p.evaluate(()=>document.querySelector('[data-n="2"]').getAttribute('aria-pressed'));
await p.click('#pause'); out.paused=await p.evaluate(()=>document.getElementById('svg').classList.contains('ct-paused'));
out.errs=errs; out.ext=ext;
for(const w of [1000,700,480]){await p.setViewportSize({width:w,height:200}); await p.goto('file:///home/claude/npi-animacije/enopolna-vezava.html?kompakt'); await p.click('[data-n="3"]'); out['H'+w]=await p.evaluate(()=>document.documentElement.scrollHeight); out['lbl'+w]=await p.evaluate(()=>document.querySelector('.ct-t').getBoundingClientRect().height.toFixed(1));}
await p.setViewportSize({width:480,height:200}); await p.screenshot({path:'/home/claude/en-480.png',fullPage:true});
const r=await b.newContext({reducedMotion:'reduce'});const q=await r.newPage();await q.goto('file:///home/claude/npi-animacije/enopolna-vezava.html');out.reduced=await q.evaluate(()=>getComputedStyle(document.querySelector('.ct-flow')).animationName);
console.log(JSON.stringify(out,null,1));await b.close();})();
