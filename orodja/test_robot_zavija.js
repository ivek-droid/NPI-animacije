const {chromium}=require('playwright');
// Test: node orodja/test_robot_zavija.js (iz korena repozitorija)
(async()=>{const b=await chromium.launch();const R={};
const FILE='file:///home/claude/npi-animacije/robot-zavija.html';
for(const w of [1000,480]){
 const ctx=await b.newContext({viewport:{width:w,height:300}});const p=await ctx.newPage();
 const errs=[],ext=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()=='error')errs.push(m.text())});
 p.on('request',r=>{if(!r.url().startsWith('file:'))ext.push(r.url())});
 await p.goto(FILE);
 const out=[];let ok=true;
 const chk=(name,cond)=>{if(!cond)ok=false;out.push([name,cond]);};
 const rd=async()=>p.evaluate(()=>({n:nVal.textContent,b:blockTxt.textContent,c1:c1.textContent,c2:c2.textContent,c3:c3.textContent,a:angleTxt.textContent,rot:robot.getAttribute('transform'),arc:arc.getAttribute('d')}));
 let s=await rd();
 chk('zacetno n=0,54 desno',s.n==='0,54'&&s.b==='move right: 100 for 0,54 rotations'&&s.rot==='rotate(0.00)'&&s.arc==='');
 chk('racun 9,5 / 37,7 / 91',s.c1.endsWith('= 9,5 cm')&&s.c2.endsWith('= 37,7 cm')&&s.c3==='Zasuk = 9,5 / 37,7 · 360° = 91°');
 // gumbi n
 await p.click('#nMinus'); s=await rd(); chk('n=0,53',s.n==='0,53');
 await p.click('#nPlus'); await p.click('#nPlus'); await p.click('#nPlus'); await p.click('#nPlus'); s=await rd(); chk('n=0,57',s.n==='0,57');
 // slider
 await p.evaluate(()=>{const e=nSlider;e.value='0.5';e.dispatchEvent(new Event('input',{bubbles:true}));});
 s=await rd(); chk('slider 0,5 -> 84°',s.n==='0,5'&&s.c3.endsWith('= 84°'));
 await p.evaluate(()=>{const e=nSlider;e.value='2';e.dispatchEvent(new Event('input',{bubbles:true}));});
 s=await rd(); chk('n=2 -> 336°, plus onemogocen',s.c3.endsWith('= 336°')&&await p.isDisabled('#nPlus'));
 await p.evaluate(()=>{const e=nSlider;e.value='0.05';e.dispatchEvent(new Event('input',{bubbles:true}));});
 s=await rd(); chk('n=0,05 min',s.n==='0,05'&&await p.isDisabled('#nMinus'));
 // 0,54 desno do konca
 await p.evaluate(()=>{const e=nSlider;e.value='0.54';e.dispatchEvent(new Event('input',{bubbles:true}));});
 await p.click('#run'); await p.waitForTimeout(500);
 const mid=await rd(); chk('med tekom zasuk>0 in <91',/^\d+°$/.test(mid.a)&&parseInt(mid.a)>0&&parseInt(mid.a)<91);
 await p.click('#pause'); const a1=(await rd()).a; await p.waitForTimeout(400); const a2=(await rd()).a;
 chk('pavza ustavi',a1===a2&&await p.getAttribute('#pause','aria-pressed')==='true'&&(await p.textContent('#run'))==='Nadaljuj');
 await p.click('#run'); await p.waitForFunction(()=>angleTxt.textContent.startsWith('91°'),null,{timeout:8000});
 s=await rd(); chk('konec 91° pravi kot, desno (rotate 90,8)',s.a==='91° = pravi kot'&&s.rot==='rotate(90.80)');
 // levo
 await p.click('#dirL'); s=await rd(); chk('levo: blok -100, zasuk 0',s.b==='move left: -100 for 0,54 rotations'&&s.rot==='rotate(0.00)'&&await p.getAttribute('#dirL','aria-pressed')==='true');
 await p.click('#run'); await p.waitForFunction(()=>angleTxt.textContent.startsWith('91°'),null,{timeout:8000});
 s=await rd(); chk('levo konec rotate(-90.80), lok sweep 0',s.rot==='rotate(-90.80)'&&/ 0 0 0 /.test(s.arc.replace(/\s+/g,' ')+' ')|| /A120 120 0 0 0 /.test(s.arc));
 // 0,5 ni pravi kot
 await p.evaluate(()=>{const e=nSlider;e.value='0.5';e.dispatchEvent(new Event('input',{bubbles:true}));});
 await p.click('#run'); await p.waitForFunction(()=>angleTxt.textContent.startsWith('84°'),null,{timeout:8000});
 s=await rd(); chk('0,5: 84°, brez pravi kot',s.a==='84°');
 await p.screenshot({path:`/home/claude/work/rz-end-${w}.png`});
 // tipkovnica
 await p.click('#reset'); await p.focus('#run'); await p.keyboard.press('Enter'); await p.waitForTimeout(300);
 const k1=(await rd()).a; chk('Enter zažene',k1!=='0°');
 await p.keyboard.press('Tab'); await p.keyboard.press('Space'); const k2=(await rd()).a; await p.waitForTimeout(300); const k3=(await rd()).a; chk('Tab+Space pavza',k2===k3);
 await p.click('#reset'); await p.focus('#nSlider'); await p.keyboard.press('ArrowRight'); s=await rd(); chk('slider s tipkovnico',s.n==='0,51');
 // velikosti
 const labelPx=await p.evaluate(()=>{const t=document.querySelector('.ct-l');const sc=scene.getBoundingClientRect().width/560;return +(parseFloat(getComputedStyle(t).fontSize)*sc).toFixed(1)});
 const minBtn=await p.evaluate(()=>Math.min(...[...document.querySelectorAll('.ct-btn')].map(x=>Math.min(x.offsetHeight,x.offsetWidth))));
 const hPage=await p.evaluate(()=>document.documentElement.scrollHeight);
 await p.evaluate(()=>document.documentElement.classList.add('ct-kompakt'));
 const hKompakt=await p.evaluate(()=>document.documentElement.scrollHeight);
 const overflowX=await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth);
 await p.screenshot({path:`/home/claude/work/rz-${w}.png`,fullPage:true});
 R[w]={ok,failed:out.filter(x=>!x[1]).map(x=>x[0]),nChecks:out.length,labelPx,minBtn,hPage,hKompakt,overflowX,errs,ext};await ctx.close();}
const ctx=await b.newContext({reducedMotion:'reduce'});const p=await ctx.newPage();await p.goto(FILE);
await p.click('#run'); R.reduced=await p.evaluate(()=>angleTxt.textContent);
console.log(JSON.stringify(R,null,1));await b.close();})();
