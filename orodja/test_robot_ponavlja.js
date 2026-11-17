const {chromium}=require('playwright');
// Test: node orodja/test_robot_ponavlja.js (iz korena repozitorija)
(async()=>{const b=await chromium.launch();const R={};
const FILE='file:///home/claude/npi-animacije/robot-ponavlja.html';
for(const w of [1000,480]){
 const ctx=await b.newContext({viewport:{width:w,height:300}});const p=await ctx.newPage();
 const errs=[],ext=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()=='error')errs.push(m.text())});
 p.on('request',r=>{if(!r.url().startsWith('file:'))ext.push(r.url())});
 await p.goto(FILE);
 const out=[];let ok=true;const chk=(n,c)=>{if(!c)ok=false;out.push([n,c]);};
 const rd=async()=>p.evaluate(()=>({n:nVal.textContent,rep:repTxt.textContent,cnt:count.textContent,c1:c1.textContent,c2:c2.textContent,c3:c3.textContent,tr:robot.getAttribute('transform'),pts:trail.getAttribute('points')}));
 let s=await rd();
 chk('zacetno 4 ponovitve',s.n==='4'&&s.rep==='repeat 4'&&s.cnt==='Ponovitev 0 od 4');
 chk('racun 39,95 -> 40 cm',s.c1==='Ena ponovitev: vožnja 2,27 · 17,6 = 40 cm + zavoj 90,8°'&&s.c2==='Skupaj 4 ponovitev: pot 160 cm');
 await p.click('#nPlus'); s=await rd(); chk('plus 5',s.n==='5'&&s.rep==='repeat 5');
 await p.click('#nMinus'); await p.click('#nMinus'); await p.click('#nMinus'); await p.click('#nMinus'); s=await rd(); chk('min 1, minus onemogocen',s.n==='1'&&await p.isDisabled('#nMinus'));
 await p.evaluate(()=>{const e=nSlider;e.value='8';e.dispatchEvent(new Event('input',{bubbles:true}));}); s=await rd(); chk('max 8, plus onemogocen',s.n==='8'&&await p.isDisabled('#nPlus'));
 await p.evaluate(()=>{const e=nSlider;e.value='4';e.dispatchEvent(new Event('input',{bubbles:true}));});
 await p.click('#run'); await p.waitForTimeout(600);
 s=await rd(); chk('med tekom ponovitev 1',s.cnt==='Ponovitev 1 od 4'&&s.pts.split(' ').length===2);
 await p.click('#pause'); const a1=(await rd()).pts; await p.waitForTimeout(400); const a2=(await rd()).pts;
 chk('pavza ustavi',a1===a2&&(await p.textContent('#run'))==='Nadaljuj');
 await p.click('#run'); await p.waitForFunction(()=>count.textContent.startsWith('Konec'),null,{timeout:15000});
 s=await rd(); const pts=s.pts.split(' ').map(q=>q.split(',').map(Number));
 chk('5 tock poti',pts.length===5);
 const d=(a,c)=>Math.hypot(a[0]-c[0],a[1]-c[1]);
 chk('stranice 199,8 px (39,95 cm)',pts.slice(1).every((q,i)=>Math.abs(d(q,pts[i])-199.76)<1));
 chk('skoraj zaprt kvadrat (<10 px)',d(pts[4],pts[0])<10);
 chk('skupni zasuk 363,2',s.c3==='Skupni zasuk: 4 · 90,8° = 363,2°');
 chk('rotacija 363,2',/rotate\(363\.2/.test(s.tr));
 // 8 ponovitev
 await p.evaluate(()=>{const e=nSlider;e.value='8';e.dispatchEvent(new Event('input',{bubbles:true}));});
 await p.click('#run'); await p.waitForFunction(()=>count.textContent.startsWith('Konec'),null,{timeout:25000});
 s=await rd(); chk('8 ponovitev: 9 tock, zasuk 726,4',s.pts.split(' ').length===9&&s.c3==='Skupni zasuk: 8 · 90,8° = 726,4°');
 // tipkovnica
 await p.click('#reset'); await p.focus('#run'); await p.keyboard.press('Enter'); await p.waitForTimeout(400);
 chk('Enter zažene',(await rd()).cnt!=='Ponovitev 0 od 8');
 await p.keyboard.press('Tab'); await p.keyboard.press('Space'); const k2=(await rd()).pts; await p.waitForTimeout(300); const k3=(await rd()).pts; chk('Tab+Space pavza',k2===k3);
 await p.click('#reset'); await p.focus('#nSlider'); await p.keyboard.press('ArrowLeft'); s=await rd(); chk('slider s tipkovnico',s.n==='7');
 const labelPx=await p.evaluate(()=>{const t=document.querySelector('.ct-l');const sc=scene.getBoundingClientRect().width/560;return +(parseFloat(getComputedStyle(t).fontSize)*sc).toFixed(1)});
 const minBtn=await p.evaluate(()=>Math.min(...[...document.querySelectorAll('.ct-btn')].map(x=>Math.min(x.offsetHeight,x.offsetWidth))));
 const hPage=await p.evaluate(()=>document.documentElement.scrollHeight);
 await p.evaluate(()=>document.documentElement.classList.add('ct-kompakt'));
 const hKompakt=await p.evaluate(()=>document.documentElement.scrollHeight);
 const overflowX=await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth);
 await p.click('#nPlus'); await p.click('#run'); await p.waitForFunction(()=>count.textContent.startsWith('Konec'),null,{timeout:25000});
 await p.screenshot({path:`/home/claude/work/rp-${w}.png`,fullPage:true});
 R[w]={ok,failed:out.filter(x=>!x[1]).map(x=>x[0]),nChecks:out.length,labelPx,minBtn,hPage,hKompakt,overflowX,errs,ext};await ctx.close();}
const ctx=await b.newContext({reducedMotion:'reduce'});const p=await ctx.newPage();await p.goto(FILE);
await p.click('#run'); R.reduced=await p.evaluate(()=>count.textContent);
console.log(JSON.stringify(R,null,1));await b.close();})();
