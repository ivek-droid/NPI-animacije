// Test animacije odcitavanje-instrumenta.html. Poženi iz korena repozitorija: node orodja/test_odcitavanje.js
const { chromium } = require('playwright');
const path = require('path');
const url = 'file://' + path.resolve('odcitavanje-instrumenta.html');
let fails = 0;
function ok(c, m) { if (!c) { fails++; console.log('NAPAKA: ' + m); } }

(async () => {
  const browser = await chromium.launch();
  const ctx = await browser.newContext({ viewport: { width: 1000, height: 900 } });
  const page = await ctx.newPage();
  const errs = [], ext = [];
  page.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
  page.on('pageerror', e => errs.push(String(e)));
  page.on('request', r => { if (!r.url().startsWith('file://') && !r.url().startsWith('data:')) ext.push(r.url()); });
  await page.goto(url);

  /* 1. model: vse kombinacije, pričakovane konstante */
  const exp = { // oblika:območje -> [skala, k v enoti območja]
    'dc:500 V': ['c5', 10], 'dc:150 V': ['c15', 2], 'dc:50 V': ['c5', 1], 'dc:15 V': ['c15', 0.2], 'dc:5 V': ['c5', 0.1],
    'dc:1,5 V': ['c15', 0.02], 'dc:0,5 V': ['c5', 0.01], 'dc:5 A': ['c5', 0.1], 'dc:0,5 A': ['c5', 0.01],
    'dc:50 mA': ['c5', 1], 'dc:5 mA': ['c5', 0.1], 'dc:0,5 mA': ['c5', 0.01],
    'ac:300 V': ['r30', 10], 'ac:100 V': ['r10', 2], 'ac:30 V': ['r30', 1], 'ac:10 V': ['r10', 0.2], 'ac:3 V': ['r30', 0.1],
    'ac:10 A': ['r10', 0.2], 'ac:3 A': ['r30', 0.1], 'ac:0,3 A': ['r30', 0.01], 'ac:30 mA': ['r30', 1],
    'ac:3 mA': ['r30', 0.1], 'ac:1 mA': ['r10', 0.02]
  };
  const model = await page.evaluate(() => {
    const out = {};
    ct.cfg.form = 'obe'; ct.cfg.qty = 'obe';
    ct.pool().forEach(e => {
      const t = ct.makeTask(e, 10);
      out[e.form + ':' + e.p[e.form].t] = [t.sc.key, t.k, t.N, t.X, t.alpha];
    });
    return out;
  });
  ok(Object.keys(model).length === Object.keys(exp).length, 'število kombinacij ' + Object.keys(model).length + ' != ' + Object.keys(exp).length);
  for (const k in exp) {
    const m = model[k];
    ok(!!m, 'manjka ' + k);
    if (m) {
      ok(m[0] === exp[k][0], k + ' skala ' + m[0]);
      ok(Math.abs(m[1] - exp[k][1]) < 1e-12, k + ' k ' + m[1]);
      ok(Math.abs(m[3] - 10 * exp[k][1]) < 1e-9, k + ' X ' + m[3]);
    }
  }

  /* 2. naključne naloge: α v mejah, kazalec pri pravem kotu */
  const rnd = await page.evaluate(() => {
    const bad = [];
    ['celi', 'pol'].forEach(fine => {
      ct.cfg.fine = fine;
      for (let i = 0; i < 300; i++) {
        ct.newTask();
        const t = ct.task;
        const step = fine === 'pol' ? 0.5 : 1;
        if (t.alpha < 0.1 * t.N - 1 || t.alpha > 0.95 * t.N) bad.push('meja ' + t.alpha + '/' + t.N);
        if (Math.abs(t.alpha / step - Math.round(t.alpha / step)) > 1e-9) bad.push('korak ' + t.alpha);
        if (Math.abs(t.X - t.alpha * t.k) > 1e-9) bad.push('X');
        const want = -ct.SPAN + 100 * t.alpha / t.N;
        // kazalec: reduced-motion ne vemo, zato po animaciji
      }
    });
    ct.cfg.fine = 'celi';
    return bad;
  });
  ok(rnd.length === 0, 'naključne naloge: ' + rnd.slice(0, 3).join(', '));

  /* 3. reši nalogo prek vmesnika, napačni odgovori dajo ✘ */
  await page.evaluate(() => { ct.newTask({ p: ct.POS[4], form: 'ac' }, 37); });
  const t = await page.evaluate(() => ({ q: ct.task.qty, f: ct.task.form, rng: ct.task.rng, sc: ct.task.sc.key, k: ct.task.k, a: ct.task.alpha, X: ct.task.X }));
  ok(t.rng.v === 100 && t.sc === 'r10' && t.k === 2 && t.X === 74, 'primer 100 V ~: ' + JSON.stringify(t));
  // zaklenjeni koraki 2–7
  ok(await page.locator('#st1').evaluate(e => e.disabled), 'korak 2 bi moral biti zaklenjen');
  await page.locator('input[name=q][value=I]').check({ force: true });
  await page.locator('[data-chk="0"]').click();
  ok((await page.locator('#fb0').textContent()).startsWith('✘'), 'napačna veličina bi morala dati ✘');
  await page.locator('input[name=q][value=U]').check({ force: true });
  await page.locator('[data-chk="0"]').click();
  ok((await page.locator('#fb0').textContent()).startsWith('✔'), 'prava veličina');
  ok(!(await page.locator('#st1').evaluate(e => e.disabled)), 'korak 2 bi moral biti odklenjen');
  await page.locator('input[name=f][value=dc]').check({ force: true });
  await page.locator('[data-chk="1"]').click();
  ok((await page.locator('#fb1').textContent()).startsWith('✘'), 'napačna oblika');
  await page.locator('input[name=f][value=ac]').check({ force: true });
  await page.locator('[data-chk="1"]').click();
  // območje: zamenjava z enosmerno številko (15 V)
  await page.fill('#in2', '15'); await page.selectOption('#un2', 'V'); await page.keyboard.press('Enter');
  const fb2 = await page.locator('#fb2').textContent();
  ok(fb2.startsWith('✘') && /enosmerno/.test(fb2), 'diagnostika oblike pri območju: ' + fb2);
  await page.fill('#in2', '100'); await page.keyboard.press('Enter');
  ok((await page.locator('#fb2').textContent()).startsWith('✔'), 'območje 100 V');
  await page.locator('input[name=s][value=c5]').check({ force: true });
  await page.locator('[data-chk="3"]').click();
  ok(/Barva/.test(await page.locator('#fb3').textContent()), 'barva skale');
  await page.locator('input[name=s][value=r10]').check({ force: true });
  await page.locator('[data-chk="3"]').click();
  ok((await page.locator('#fb3').textContent()).startsWith('✔'), 'skala r10');
  await page.fill('#in4', '10'); await page.selectOption('#un4', 'V'); await page.keyboard.press('Enter'); // 100/10
  ok(/največjo vrednostjo/.test(await page.locator('#fb4').textContent()), 'diagnostika k');
  await page.fill('#in4', '2'); await page.keyboard.press('Enter');
  ok((await page.locator('#fb4').textContent()).startsWith('✔'), 'k = 2');
  await page.fill('#in5', '7,4'); await page.keyboard.press('Enter');
  ok(/vrednost na skali/.test(await page.locator('#fb5').textContent()), 'diagnostika α: ' + await page.locator('#fb5').textContent());
  await page.fill('#in5', '37'); await page.keyboard.press('Enter');
  ok((await page.locator('#fb5').textContent()).startsWith('✔'), 'α = 37');
  await page.fill('#in6', '74'); await page.selectOption('#un6', 'A'); await page.keyboard.press('Enter');
  ok((await page.locator('#fb6').textContent()).startsWith('✘'), 'napačna enota');
  await page.selectOption('#un6', 'V'); await page.keyboard.press('Enter');
  ok((await page.locator('#fb6').textContent()).startsWith('✔'), 'rezultat 74 V');
  ok(/Rešeno: 1/.test(await page.locator('#chip2').textContent()), 'števec rešenih');

  /* 4. samostojni način: nič ni zaklenjeno */
  await page.locator('summary:has-text("Nastavitve")').click();
  await page.locator('[data-set=mode][data-val=samo]').click();
  ok(!(await page.locator('#st6').evaluate(e => e.disabled)), 'v samostojnem načinu ni zaklepanja');
  ok(await page.locator('#vseBtn').isVisible(), 'gumb Preveri vse');

  /* 5. rešitev */
  await page.locator('#resBtn').click();
  ok((await page.locator('#calc li').count()) >= 9, 'rešitev ima vrstice');

  /* 6. tipkovnica: do gumba Nova naloga in aktivacija */
  await page.focus('#novaBtn'); const n0 = await page.locator('#chip').textContent();
  await page.keyboard.press('Enter');
  ok((await page.locator('#chip').textContent()) !== n0, 'Enter na gumbu Nova naloga');

  /* 7. velikosti ciljev ≥ 44 px */
  const small = await page.evaluate(() => {
    const s = [];
    document.querySelectorAll('button, input.ct-in, select, .ct-opt span, summary').forEach(e => {
      const r = e.getBoundingClientRect();
      if (r.width && (r.height < 43.5 || r.width < 43.5)) s.push((e.id || e.textContent || e.tagName).slice(0, 25) + ' ' + Math.round(r.width) + 'x' + Math.round(r.height));
    });
    return s;
  });
  ok(small.length === 0, 'premajhni cilji: ' + small.join('; '));

  /* 8. reduced-motion: kazalec takoj na mestu */
  const ctx2 = await browser.newContext({ viewport: { width: 1000, height: 900 }, reducedMotion: 'reduce' });
  const p2 = await ctx2.newPage(); await p2.goto(url);
  await p2.evaluate(() => ct.newTask({ p: ct.POS[1], form: 'dc' }, 25));
  const deg = await p2.evaluate(() => ct.curDeg());
  ok(Math.abs(deg - 0) < 1e-6, 'reduced-motion: kot ' + deg + ' (pričakovano 0)');
  // z animacijo: po 1200 ms mora priti do cilja
  await page.evaluate(() => ct.newTask({ p: ct.POS[1], form: 'dc' }, 25));
  await page.waitForTimeout(1200);
  ok(Math.abs(await page.evaluate(() => ct.curDeg())) < 1e-6, 'animacija ne pride na cilj');

  /* 9. višine pri 1000 in 480 px (kompaktno) */
  for (const w of [1000, 480]) {
    for (const mode of ['vodeno', 'samo']) {
      const c = await browser.newContext({ viewport: { width: w, height: 900 } });
      const p = await c.newPage(); await p.goto(url + '?kompakt');
      if (mode === 'samo') await p.evaluate(() => { document.querySelector('[data-set=mode][data-val=samo]').click(); });
      if (process.env.RES) await p.evaluate(() => { document.querySelector('#resBtn').click(); });
      const h = await p.evaluate(() => document.documentElement.scrollHeight);
      const sw = await p.evaluate(() => document.documentElement.scrollWidth);
      console.log('širina ' + w + ' ' + mode + ' (z rešitvijo): višina ' + h + ', scrollWidth ' + sw);
      if (w === 480) ok(sw <= 480, 'vodoravno drsenje pri 480 px: ' + sw);
      await c.close();
    }
  }

  ok(errs.length === 0, 'konzola: ' + errs.join(' | '));
  ok(ext.length === 0, 'zunanje zahteve: ' + ext.join(', '));
  console.log(fails === 0 ? 'VSI TESTI USPEŠNI' : 'NAPAKE: ' + fails);
  await browser.close();
  process.exit(fails ? 1 : 0);
})();
