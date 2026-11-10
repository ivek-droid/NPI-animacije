// Statična shema pravilne vezave (stikalo v L, vklopljeno) iz stikalo-v-fazi.html -> slike/razsvetljava-pravilna-vezava.png
// Zagon iz korena repozitorija: node orodja/shema_razsvetljava.js
const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();
const p=await (await b.newContext({viewport:{width:1000,height:800},deviceScaleFactor:1,reducedMotion:'reduce'})).newPage();
await p.goto('file://'+process.cwd()+'/stikalo-v-fazi.html');
await p.addStyleTag({content:'*{transition:none!important}'});
await p.waitForTimeout(500);
const el=await p.$('#svg');
await el.screenshot({path:'slike/razsvetljava-pravilna-vezava.png'});
const bb=await el.boundingBox();console.log(bb.width,bb.height);
await b.close();})();
