const {chromium}=require('playwright');
// Test: node orodja/test_robot_vozi.js (iz korena repozitorija)
(async()=>{const b=await chromium.launch();const R={};
const FILE='file:///home/claude/npi-animacije/robot-vozi-naravnost.html';
for(const w of [1000,480]){
 const ctx=await b.newContext({viewport:{width:w,height:300}});const p=await ctx.newPage();
 const errs=[],ext=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()=='error')errs.push(m.text())});
 p.on('request',r=>{if(!r.url().startsWith('file:'))ext.push(r.url())});
 await p.goto(FILE);
 const out=[];let ok=true;
 const rd=async()=>p.evaluate(()=>({r:readout.textContent,n:nVal.textContent,o:oVal.textContent,d:dist.textContent,t:turns.textContent,marks:document.querySelectorAll('#marks circle').length}));
 const chk=(name,cond)=>{if(!cond)ok=false;out.push([name,cond]);};
 let s=await rd();
 chk('zacetno 3*20=60',s.r==='Pot s = n · o = 3 · 20 cm = 60 cm'&&s.d==='s = 0 cm'&&s.marks===3);
 // n +, o +
 await p.click('#nPlus'); s=await rd(); chk('n=3,5',s.n==='3,5'&&s.r.endsWith('= 70 cm')&&s.marks===3);
 await p.click('#nMinus'); await p.click('#nMinus'); await p.click('#nMinus'); await p.click('#nMinus'); await p.click('#nMinus'); await p.click('#nMinus');
 s=await rd(); chk('n=0,5 min, 3 minus gumb onemogocen',s.n==='0,5'&&await p.isDisabled('#nMinus'));
 for(let i=0;i<20;i++) await p.click('#nPlus',{timeout:500}).catch(()=>{});
 s=await rd(); chk('n=6 max',s.n==='6'&&await p.isDisabled('#nPlus'));
 for(let i=0;i<10;i++) await p.click('#oPlus'); s=await rd(); chk('o=25,n=6 -> 150 cm',s.o==='25'&&s.r.endsWith('= 150 cm')&&s.marks===6);
 // nazaj na 3 in 20
 for(let i=0;i<6;i++) await p.click('#nMinus'); for(let i=0;i<10;i++) await p.click('#oMinus');
 s=await rd(); chk('nazaj 3 in 20',s.n==='3'&&s.o==='20');
 // tek do konca
 await p.click('#run'); await p.waitForTimeout(500);
 const mid=await rd(); chk('med tekom pot>0 in <60',mid.d!=='s = 0 cm'&&mid.d!=='s = 60 cm');
 // pavza
 await p.click('#pause'); const d1=(await rd()).d; await p.waitForTimeout(400); const d2=(await rd()).d;
 chk('pavza ustavi',d1===d2&&await p.getAttribute('#pause','aria-pressed')==='true'&&(await p.textContent('#run'))==='Nadaljuj');
 await p.click('#run'); await p.waitForFunction(()=>dist.textContent==='s = 60 cm',null,{timeout:8000});
 s=await rd(); chk('konec 60 cm, vrtljaji 3',s.d==='s = 60 cm'&&s.t==='vrtljaji: 3');
 // položaj sprednjega roba = ravnilo 0..60 (max 60 => x=850)
 const rx=await p.evaluate(()=>robot.getAttribute('transform')); chk('robot na koncu ravnila',rx==='translate(850.0 0)');
 // kot kolesa 3*360
 const ang=await p.evaluate(()=>bigSpin.getAttribute('transform')); chk('kot 1080',ang==='rotate(1080.0)');
 await p.screenshot({path:`/home/claude/work/rv-end-${w}.png`}); // tipkovnica
 await p.click('#reset'); s=await rd(); chk('reset',s.d==='s = 0 cm');
 await p.focus('#run'); await p.keyboard.press('Enter'); await p.waitForTimeout(300); const k1=(await rd()).d; chk('Enter zažene',k1!=='s = 0 cm');
 await p.keyboard.press('Tab'); await p.keyboard.press('Space'); const k2=(await rd()).d; await p.waitForTimeout(300); const k3=(await rd()).d; chk('Tab+Space pavza',k2===k3);
 // velikosti
 const labelPx=await p.evaluate(()=>{const t=document.querySelector('.ct-l');const sc=scene.getBoundingClientRect().width/970;return +(parseFloat(getComputedStyle(t).fontSize)*sc).toFixed(1)});
 const minBtn=await p.evaluate(()=>Math.min(...[...document.querySelectorAll('.ct-btn')].map(x=>Math.min(x.offsetHeight,x.offsetWidth))));
 const hPage=await p.evaluate(()=>document.documentElement.scrollHeight);
 await p.evaluate(()=>document.documentElement.classList.add('ct-kompakt'));
 const hKompakt=await p.evaluate(()=>document.documentElement.scrollHeight);
 const overflowX=await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth);
 await p.screenshot({path:`/home/claude/work/rv-${w}.png`,fullPage:true});
 R[w]={ok,out:out.filter(x=>!x[1]),nChecks:out.length,labelPx,minBtn,hPage,hKompakt,overflowX,errs,ext};await ctx.close();}
// reduced motion: konec takoj
const ctx=await b.newContext({reducedMotion:'reduce'});const p=await ctx.newPage();await p.goto(FILE);
await p.click('#run'); R.reduced=await p.evaluate(()=>dist.textContent);
console.log(JSON.stringify(R,null,1));await b.close();})();
