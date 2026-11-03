// Test animacije priklop-merilnikov.html. Poženi iz korena repozitorija: node orodja/test_priklop.js
const { chromium } = require('playwright');
const path = require('path');
const url = 'file://' + path.resolve('priklop-merilnikov.html');
let fails = 0;
function ok(c, m) { if (!c) { fails++; console.log('NAPAKA: ' + m); } }
const near = (a, b) => Math.abs(a - b) < 0.02;

(async () => {
  const browser = await chromium.launch();
  const ctx = await browser.newContext({ viewport: { width: 1000, height: 900 } });
  const page = await ctx.newPage();
  const errs = [], ext = [];
  page.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
  page.on('pageerror', e => errs.push(String(e)));
  page.on('request', r => { if (!r.url().startsWith('file://') && !r.url().startsWith('data:')) ext.push(r.url()); });
  await page.goto(url);

  /* 1. model: začetno stanje (vsi mostički vstavljeni) in rešitve vseh stopenj, 30 naključnih nalog */
  const res = await page.evaluate(() => {
    const bad = [];
    for (const lev of [1, 2, 3]) {
      ct.st.level = lev; ct.st.mode = 'samo';
      for (let i = 0; i < 30; i++) {
        ct.newTask();
        let S = ct.solveNet();
        if (S.Isrc < 0.1) bad.push('L' + lev + ' začetni tok ' + S.Isrc);
        ct.applySol(); ct.refresh();
        S = ct.solveNet();
        const T = ct.st.T, r = ct.judge(S);
        if (!r.amm.ok) bad.push('L' + lev + ' ampermeter ' + JSON.stringify(ct.st.v) + ' ' + S.Ia + ' ' + r.amm.msg);
        if (!r.vol.ok) bad.push('L' + lev + ' voltmeter ' + JSON.stringify(ct.st.v) + ' ' + S.Uv + ' ' + r.vol.msg);
        if (Math.abs(S.Ia - T.I) > 0.02 * T.I + 0.005) bad.push('I ' + S.Ia + ' vs ' + T.I);
        if (Math.abs(S.Uv - T.U) > 0.02 * T.U + 0.005) bad.push('U ' + S.Uv + ' vs ' + T.U);
      }
    }
    return bad;
  });
  ok(res.length === 0, 'rešitve: ' + res.slice(0, 3).join(' | '));

  /* 2. zahtevne številke (L2 8+16 Ω, L3 R2 = 12 Ω) */
  const nums = await page.evaluate(() => {
    const out = {};
    ct.st.level = 2; ct.st.mode = 'samo'; ct.newTask();
    ct.st.v = { R1: 8, R2: 16, which: 'R2' }; ct.st.T = ct.LV[2].tgt(ct.st.v);
    ct.st.J = { J1: false, J2: true }; ct.st.w = { Ap: 'A', Am: 'B', Vp: 'C', Vm: 'D' }; ct.refresh();
    let S = ct.solveNet(); out.l2 = [S.Ia, S.Uv];
    ct.st.level = 3; ct.newTask();
    ct.st.v = { R1: 24, R2: 12 }; ct.st.T = ct.LV[3].tgt(ct.st.v);
    ct.st.J = { J1: false, J2: true }; ct.st.w = { Ap: 'P', Am: 'A', Vp: 'B', Vm: 'E' }; ct.refresh();
    S = ct.solveNet(); out.l3tot = S.Ia;
    return out;
  });
  ok(near(nums.l2[0], 0.5) && near(nums.l2[1], 8), 'L2: ' + nums.l2);
  ok(near(nums.l3tot, 1.5), 'L3 skupni tok ' + nums.l3tot);

  /* 3. napake in diagnostika */
  const diag = await page.evaluate(() => {
    const o = {};
    function set(level, v, J, w) {
      ct.st.level = level; ct.st.mode = 'samo'; ct.newTask(); ct.st.v = v; ct.st.T = ct.LV[level].tgt(v);
      ct.st.J = J; ct.st.w = w; ct.refresh(); const S = ct.solveNet(); return [S, ct.judge(S)];
    }
    let [S, r] = set(1, { R: 24 }, { J1: true, J2: true }, { Ap: 'B', Am: 'C', Vp: null, Vm: null });
    o.short = [Math.abs(S.Ia) > 10, r.amm.msg.startsWith('Kratek stik')];
    [S, r] = set(1, { R: 24 }, { J1: true, J2: true }, { Ap: 'A', Am: 'B', Vp: null, Vm: null });
    o.parJ = [S.Ia, /vzporedno z mostičkom/.test(r.amm.msg)];
    [S, r] = set(1, { R: 24 }, { J1: false, J2: true }, { Ap: 'B', Am: 'A', Vp: null, Vm: null });
    o.rev = [S.Ia, /zamenjani/.test(r.amm.msg)];
    [S, r] = set(1, { R: 24 }, { J1: false, J2: true }, { Ap: null, Am: null, Vp: null, Vm: null });
    o.open = [S.Isrc, ''];
    [S, r] = set(1, { R: 24 }, { J1: false, J2: true }, { Ap: 'A', Am: 'A', Vp: null, Vm: null });
    o.same = [S.Ia, /isto napetostjo/.test(r.amm.msg)];
    [S, r] = set(1, { R: 24 }, { J1: false, J2: true }, { Ap: null, Am: null, Vp: 'A', Vm: 'B' });
    o.vser = [S.Uv, S.Isrc, /zaporedno/.test(r.vol.msg)];
    [S, r] = set(1, { R: 24 }, { J1: true, J2: true }, { Ap: null, Am: null, Vp: 'C', Vm: 'B' });
    o.vrev = [S.Uv, /zamenjani/.test(r.vol.msg)];
    [S, r] = set(2, { R1: 8, R2: 16, which: 'R2' }, { J1: false, J2: true }, { Ap: 'A', Am: 'B', Vp: 'B', Vm: 'C' });
    o.other = [S.Uv, /drugem uporu/.test(r.vol.msg)];
    [S, r] = set(3, { R1: 24, R2: 12 }, { J1: false, J2: true }, { Ap: 'P', Am: 'A', Vp: 'B', Vm: 'E' });
    o.tot = [S.Ia, /skupni tok/.test(r.amm.msg)];
    return o;
  });
  ok(diag.short[0] && diag.short[1], 'kratek stik ' + diag.short);
  ok(near(diag.parJ[0], 0) && diag.parJ[1], 'vzporedno z mostičkom ' + diag.parJ);
  ok(diag.rev[0] < -0.4 && diag.rev[1], 'zamenjana polariteta ampermetra ' + diag.rev);
  ok(diag.open[0] < 1e-6, 'odprt krog ' + diag.open);
  ok(diag.same[1], 'ista točka');
  ok(diag.vser[0] > 11.9 && diag.vser[1] < 1e-3 && diag.vser[2], 'voltmeter zaporedno ' + diag.vser);
  ok(diag.vrev[0] < -11.9 && diag.vrev[1], 'zamenjan voltmeter ' + diag.vrev);
  ok(near(diag.other[0], 4) && diag.other[1], 'napetost na drugem uporu ' + diag.other);
  ok(near(diag.tot[0], 1.5) && diag.tot[1], 'skupni tok ' + diag.tot);

  /* 4. vmesnik: vodeni način, tipkovnica/izbirni seznami, klik na sponko in točko */
  await page.evaluate(() => { ct.st.level = 1; ct.st.mode = 'vodeno'; ct.newTask(); ct.st.v = { R: 24 }; ct.st.T = ct.LV[1].tgt(ct.st.v); ct.refresh(); });
  ok(await page.locator('#fsV').evaluate(e => e.disabled), 'voltmeter zaklenjen v 1. koraku');
  await page.locator('#chkBtn').click();
  ok(/ni priključen/.test(await page.locator('#fbA').textContent()), 'ampermeter ni priključen');
  await page.locator('#jb-J1').click();
  await page.selectOption('#sel-Ap', 'A'); await page.selectOption('#sel-Am', 'B');
  ok(/kaže 0,50 A|0,50/.test(await page.locator('#sv').textContent()) , 'živi odčitek ampermetra');
  await page.locator('#chkBtn').click();
  ok((await page.locator('#fbA').textContent()).startsWith('✔'), 'ampermeter pravilen: ' + await page.locator('#fbA').textContent());
  ok(!(await page.locator('#fsV').evaluate(e => e.disabled)), 'voltmeter odklenjen');
  // klik: sponka Vp, nato točka B
  await page.locator('g[aria-label^="Sponka: voltmeter, sponka +"]').click();
  await page.locator('g[aria-label="Točka B"]').click();
  await page.locator('g[aria-label^="Sponka: voltmeter, sponka −"]').focus();
  await page.keyboard.press('Enter');
  await page.locator('g[aria-label="Točka C"]').focus(); await page.keyboard.press('Enter');
  ok(await page.locator('#sel-Vp').inputValue() === 'B' && await page.locator('#sel-Vm').inputValue() === 'C', 'žice s klikom/tipkovnico');
  await page.locator('#chkBtn').click();
  ok((await page.locator('#fbV').textContent()).startsWith('✔'), 'voltmeter pravilen');
  ok(/Rešeno: 1/.test(await page.locator('#chip2').textContent()), 'števec rešenih');
  ok((await page.locator('#calc li').count()) >= 2, 'izračun');
  // pokaži rešitev ne šteje
  await page.locator('#novaBtn').click();
  await page.locator('#resBtn').click();
  ok(/Rešeno: 1/.test(await page.locator('#chip2').textContent()), 'rešitev se ne šteje');

  /* 5. pavza */
  await page.locator('#pauseBtn').click();
  const p0 = await page.evaluate(() => document.querySelector('#sv circle[fill="#4b1585"]').getAttribute('cx'));
  await page.waitForTimeout(400);
  const p1 = await page.evaluate(() => document.querySelector('#sv circle[fill="#4b1585"]').getAttribute('cx'));
  ok(p0 === p1, 'pavza ustavi pike');
  await page.locator('#pauseBtn').click();
  await page.waitForTimeout(400);
  const p2 = await page.evaluate(() => document.querySelector('#sv circle[fill="#4b1585"]').getAttribute('cx'));
  ok(p2 !== p1, 'pike se gibljejo');

  /* 6. ciljne površine ≥ 44 px (v px na zaslonu) */
  const small = await page.evaluate(() => {
    const s = [];
    document.querySelectorAll('button, select, summary').forEach(e => {
      const r = e.getBoundingClientRect();
      if (r.width && (r.height < 43.5 || r.width < 43.5)) s.push((e.id || e.textContent).slice(0, 25) + ' ' + Math.round(r.width) + 'x' + Math.round(r.height));
    });
    document.querySelectorAll('g.ct-hot').forEach(g => {
      const h = g.querySelector('.ct-hit, rect'); const r = h.getBoundingClientRect();
      if (r.width < 40 || r.height < 40) s.push((g.getAttribute('aria-label')).slice(0, 25) + ' ' + Math.round(r.width) + 'x' + Math.round(r.height));
    });
    return s;
  });
  ok(small.length === 0, 'premajhni cilji: ' + small.join('; '));

  /* 7. reduced-motion: pike se ne gibljejo */
  const ctx2 = await browser.newContext({ viewport: { width: 1000, height: 900 }, reducedMotion: 'reduce' });
  const p = await ctx2.newPage(); await p.goto(url);
  const a = await p.evaluate(() => document.querySelector('#sv circle[fill="#4b1585"]').getAttribute('cx'));
  await p.waitForTimeout(400);
  const b = await p.evaluate(() => document.querySelector('#sv circle[fill="#4b1585"]').getAttribute('cx'));
  ok(a === b, 'reduced-motion: pike mirujejo');
  await ctx2.close();

  /* 8. višine strani */
  for (const w of [1000, 480]) {
    const c = await browser.newContext({ viewport: { width: w, height: 900 } });
    const pg = await c.newPage(); await pg.goto(url + '?kompakt');
    for (const lev of [1, 2, 3]) {
      await pg.evaluate(l => { ct.st.level = l; ct.st.mode = 'vodeno'; ct.newTask(); ct.applySol(); ct.refresh(); ct.check(); }, lev);
      const h = await pg.evaluate(() => document.documentElement.scrollHeight);
      const ov = await pg.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
      console.log('širina ' + w + ' stopnja ' + lev + ' višina ' + h + ' preliv ' + ov);
      ok(ov <= 0, 'vodoravni preliv pri ' + w);
    }
    const minfs = await pg.evaluate(() => {
      const sv = document.querySelector('#sv'), k = sv.getBoundingClientRect().width / 520; let m = 99;
      sv.querySelectorAll('text').forEach(t => { if (t.getAttribute('class') === 'ct-tt') return; const fs = parseFloat(getComputedStyle(t).fontSize) * k; m = Math.min(m, fs); });
      return m;
    });
    console.log('najmanjša pisava v shemi pri ' + w + ': ' + minfs.toFixed(1) + ' px');
    ok(minfs >= 16, 'pisava v shemi ' + minfs);
    if (w === 480) await pg.screenshot({ path: '/tmp/priklop480.png', fullPage: true });
    else await pg.screenshot({ path: '/tmp/priklop1000.png', fullPage: true });
    await c.close();
  }

  ok(errs.length === 0, 'napake v konzoli: ' + errs.join('; '));
  ok(ext.length === 0, 'zunanje zahteve: ' + ext.join(', '));
  await browser.close();
  console.log(fails ? 'NAPAK: ' + fails : 'VSE V REDU');
  process.exit(fails ? 1 : 0);
})();
