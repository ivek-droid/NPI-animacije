const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const R={};
async function open(f,w=1000,h=300,ctxo={}){const ctx=await b.newContext({viewport:{width:w,height:h},...ctxo});const p=await ctx.newPage();const errs=[],ext=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()=='error')errs.push(m.text())});p.on('request',r=>{if(!r.url().startsWith('file:'))ext.push(r.url())});await p.goto('file:///home/claude/npi-animacije/'+f);return {p,ctx,errs,ext};}
const chip=p=>p.evaluate(()=>document.getElementById('chip').textContent);
// SERIJSKA
{const {p,ctx,errs,ext}=await open('serijska-vezava.html');const s=[];s.push(await chip(p));await p.click('#b1');s.push(await chip(p));await p.click('#b2');s.push(await chip(p));await p.click('#b1');s.push(await chip(p));
 await p.screenshot({path:'/home/claude/ser.png',fullPage:true});R.serijska={s,errs,ext};await ctx.close();}
// KRIŽNA: preveri vse kombinacije
{const {p,ctx,errs,ext}=await open('krizna-vezava.html');const res=[];
 for(const nk of [1,2]){await p.click(`[data-k="${nk}"]`);
  for(let m=0;m<(nk==2?16:8);m++){const want={s1:m&1,k1:(m>>1)&1,s2:(m>>2)&1,k2:(m>>3)&1};
   const cur=await p.evaluate(()=>[...document.querySelectorAll('#tbody tr')].map(r=>r.cells[1].textContent));
   // nastavi preko klikov
   const get=async()=>p.evaluate(()=>{const t=[...document.querySelectorAll('#tbody tr')].map(r=>r.cells[1].textContent);return t});
   let t=await get(); const map=nk==2?{s1:0,k1:1,k2:2,s2:3}:{s1:0,k1:1,s2:2};
   const val=(k,txt)=>k.startsWith('s')?(txt.includes('2')?1:0):(txt=='navzkriž'?1:0);
   for(const k of Object.keys(map)){ if(k=='k2'&&nk==1)continue; if(val(k,t[map[k]])!==want[k]){await p.click('#b'+k);} }
   const lit=(await chip(p))=='Svetilka sveti'; const exp=((want.s1^want.k1^(nk==2?want.k2:0))===want.s2);
   res.push(lit===exp);}}
 // vsak preklop spremeni stanje
 const c0=await chip(p); await p.click('#bk1'); const c1=await chip(p);
 await p.screenshot({path:'/home/claude/kri.png',fullPage:true});R.krizna={allCorrect:res.every(Boolean),n:res.length,toggle:c0!==c1,errs,ext};await ctx.close();}
// RELE
{const {p,ctx,errs,ext}=await open('impulzni-rele.html');const s=[];s.push(await chip(p));await p.click('[data-t="1"]');s.push(await chip(p)+' imp='+await p.evaluate(()=>document.querySelector('[data-t="0"]').disabled));
 await p.screenshot({path:'/home/claude/rel-imp.png',fullPage:true});
 await p.waitForTimeout(1000);s.push(await chip(p));await p.click('[data-t="2"]');await p.waitForTimeout(1000);s.push(await chip(p));
 await p.keyboard.press('Enter'); await p.waitForTimeout(1000); s.push('kbd:'+await chip(p));
 await p.screenshot({path:'/home/claude/rel.png',fullPage:true});R.rele={s,errs,ext};await ctx.close();}
// višine kompakt in velikost oznak
for(const f of ['serijska-vezava.html','krizna-vezava.html','impulzni-rele.html']){R[f]={};for(const w of [1000,700,480]){const {p,ctx}=await open(f+'?kompakt',w,200);if(f.startsWith('kriz'))await p.click('[data-k="2"]');R[f]['H'+w]=await p.evaluate(()=>document.documentElement.scrollHeight);R[f]['lbl'+w]=await p.evaluate(()=>(document.querySelector('.ct-t').getBoundingClientRect().height).toFixed(1));await ctx.close();}
 const {p,ctx}=await open(f,1000,300,{reducedMotion:'reduce'}); R[f].reduced=await p.evaluate(()=>{const e=document.querySelector('.ct-flow');return e?getComputedStyle(e).animationName:'(ni toka)'});await ctx.close();}
console.log(JSON.stringify(R,null,1));await b.close();})();
