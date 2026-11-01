const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const R={};const F='file:///home/claude/npi-animacije/hidroelektrarna.html';
const ctx=await b.newContext({viewport:{width:1000,height:300}});const p=await ctx.newPage();const errs=[],ext=[];
p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()=='error')errs.push(m.text())});p.on('request',r=>{if(!r.url().startsWith('file:'))ext.push(r.url())});
await p.goto(F);const st=()=>p.evaluate(()=>[document.getElementById('chip').textContent,document.getElementById('status').textContent,document.getElementById('calc').textContent]);
R.default=await st();
await p.focus('#hPlus');await p.keyboard.press('Enter');R.h15=await st();
await p.focus('#h');await p.keyboard.press('End');await p.focus('#q');await p.keyboard.press('Home');R.pelton=await st();
await p.click('#q');for(let i=0;i<13;i++)await p.keyboard.press('ArrowRight');R.none=await st();
await p.click('#reset');R.reset=await st();
R.anim1=await p.evaluate(()=>getComputedStyle(document.querySelector('.ct-flow')).animationPlayState);await p.click('#pause');R.anim2=await p.evaluate(()=>getComputedStyle(document.querySelector('.ct-flow')).animationPlayState);
await p.click('#pause');await p.screenshot({path:'/home/claude/he1000.png',fullPage:true});
for(const w of [1000,480]){await p.setViewportSize({width:w,height:200});await p.goto(F+'?kompakt');R['H'+w]=await p.evaluate(()=>document.documentElement.scrollHeight);R['lbl'+w]=await p.evaluate(()=>Math.min(...[...document.querySelectorAll('svg text')].map(t=>t.getBoundingClientRect().height)).toFixed(1));R['btn'+w]=await p.evaluate(()=>Math.min(...[...document.querySelectorAll('.ct-btn,input')].map(t=>t.getBoundingClientRect().height)));}
await p.screenshot({path:'/home/claude/he480.png',fullPage:true});await p.click('#vChart');R.H480chart=await p.evaluate(()=>document.documentElement.scrollHeight);R.chartVis=await p.evaluate(()=>[getComputedStyle(document.getElementById('chart')).display,getComputedStyle(document.getElementById('scene')).display]);await p.screenshot({path:'/home/claude/he480b.png',fullPage:true});
const c2=await b.newContext({reducedMotion:'reduce'});const q=await c2.newPage();await q.goto(F);R.reduced=await q.evaluate(()=>[getComputedStyle(document.querySelector('.ct-flow')).animationPlayState,document.getElementById('pause').textContent]);
R.errs=errs;R.ext=ext;console.log(JSON.stringify(R,null,1));await b.close();})();
