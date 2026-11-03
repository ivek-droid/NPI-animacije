// Test animacije »Izberi presek«. Zagon iz korena: python3 orodja/ref_presek.py /tmp/ref.json && node orodja/test_presek.js /tmp/ref.json
const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const R={};const F='file://'+process.cwd()+'/izberi-presek.html';
const ref=JSON.parse(fs.readFileSync(process.argv[2]||'/tmp/ref.json'));
const ctx=await b.newContext({viewport:{width:1000,height:300}});const p=await ctx.newPage();const errs=[],ext=[];
p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()=='error')errs.push(m.text())});p.on('request',r=>{if(!r.url().startsWith('file:'))ext.push(r.url())});
await p.goto(F);await p.evaluate(()=>{document.getElementById('det').open=true});
// 1. izračun proti Pythonu
const res=await p.evaluate(rs=>{let bad=[];for(const r of rs){const [fa,P,c,l,g,k,n,du]=r.inp;const o=window.ctIzracun(fa,P,c,l,g,k,n,du);
 if(o.min!==r.min||o.In!==r.In||Math.abs(o.Ib-r.Ib)>1e-9)bad.push([r.inp,o,r.min,r.In]);}return {n:rs.length,bad:bad.slice(0,5),nbad:bad.length}},ref);
R.model=res;
// 2. primeri v UI
const txt=id=>p.evaluate(i=>document.getElementById(i).textContent,id);
R.p0=[await txt('chip'),await txt('status')];
await p.click('[data-i="1"]');R.p0b=[await txt('chip'),await txt('status')];
await p.click('[data-pr="1"]');await p.click('[data-i="2"]');R.p1=[await txt('chip'),await txt('status')];
await p.click('[data-i="3"]');R.p1b=[await txt('chip'),await txt('status')];
await p.click('[data-pr="2"]');await p.click('[data-i="3"]');R.p2=[await txt('chip'),await txt('status')];
await p.click('[data-i="4"]');R.p2b=[await txt('chip'),await txt('status')];
R.calc=await p.evaluate(()=>[...document.querySelectorAll('#calc li')].map(x=>x.textContent));
// neustrezno brez In
await p.click('[data-pr="0"]');for(let i=0;i<11;i++)await p.click("#pP");await p.click('[data-faza="1"]');
R.big=[await txt('chip'),await txt('status')];
// 3. tipkovnica: Tab do gumba in Enter
await p.click('[data-pr="0"]');await p.focus('#vec');await p.keyboard.press('Enter');R.kbd=await txt('chip');
// 4. predvajanje in pavza
await p.click('[data-pr="0"]');await p.click('#play');const a1=await txt('chip');await p.waitForTimeout(2700);const a2=await txt('chip');
await p.click('#play');const pa=await p.getAttribute('#play','aria-pressed');await p.waitForTimeout(2800);const a3=await txt('chip');
R.play=[a1,a2,pa,a3];
// 5. velikosti ciljev
R.small0=0;await p.evaluate(()=>{document.getElementById('det').open=true});R.small=await p.evaluate(()=>[...document.querySelectorAll('button,input')].filter(e=>{const r=e.getBoundingClientRect();return r.width<44||r.height<44}).map(e=>e.id||e.textContent));
R.errs=errs;R.ext=ext;
for(const w of [1000,700,480]){await p.setViewportSize({width:w,height:200});await p.goto(F+'?kompakt');R['H'+w]=await p.evaluate(()=>document.documentElement.scrollHeight);R['lbl'+w]=await p.evaluate(()=>{const t=document.querySelector('svg .ct-t');const sv=document.getElementById('svg');return (22*sv.getBoundingClientRect().width/900).toFixed(1)});
 if(w==480)await p.screenshot({path:'/home/claude/work/presek-480.png',fullPage:true,scale:'css'});else await p.screenshot({path:'/home/claude/work/presek-1000.png',fullPage:true});}
const r2=await b.newContext({reducedMotion:'reduce'});const q=await r2.newPage();await q.goto(F);R.reduced=await q.evaluate(()=>getComputedStyle(document.body).transitionDuration);
console.log(JSON.stringify(R,null,1));await b.close();})();
