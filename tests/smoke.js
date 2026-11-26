// M&M site smoke test: clicks every header link and card button on /en and /ar
// and checks the chat opens with ONE welcome + at most ONE question, then waits.
// Run: cd tests && node smoke.js   (exit code 1 = something is broken)
const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

let failures = 0;
const fail = (m) => { failures++; console.log('  ❌ ' + m); };
const ok = (m) => console.log('  ✅ ' + m);

function load(lang) {
  const html = fs.readFileSync(path.join(__dirname, '..', lang, 'index.html'), 'utf8');
  const dom = new JSDOM(html, {
    url: 'https://test.local/' + lang + '/', // not mmautocenter.ca, so no real leads are saved
    runScripts: 'dangerously',
    pretendToBeVisual: true,
    beforeParse(w) {
      w.fetch = () => Promise.resolve({ ok: true, json: () => Promise.resolve({}), text: () => Promise.resolve('') });
      w.scrollTo = () => {}; w.HTMLElement.prototype.scrollIntoView = () => {};
      w.matchMedia = () => ({ matches: false, addListener() {}, removeListener() {} });
    },
  });
  return dom.window;
}

const wait = (ms) => new Promise((r) => setTimeout(r, ms));

async function check(lang) {
  console.log(`\n[${lang}]`);
  let w = load(lang);
  const d = w.document;

  // 1) every in-page link points to an element that exists
  d.querySelectorAll('a[href^="#"]').forEach((a) => {
    const id = a.getAttribute('href').slice(1);
    if (id && !d.getElementById(id)) fail(`link "${a.textContent.trim()}" → #${id} has no target`);
  });

  // 1b) open/closed status must be filled
  await wait(50);
  const os = d.getElementById('ost');
  if (!os || !os.textContent.trim()) fail('top bar open/closed status is empty'); else ok('top bar: ' + os.textContent.trim());

  // 2) every header link and card button opens the chat with welcome + ≤1 question
  const triggers = [...d.querySelectorAll('nav .nv, .go, .dock .dkc')].map((e, i) => { const sel = e.matches('nav .nv') ? 'nav .nv' : e.matches('.dock .dkc') ? '.dock .dkc' : '.go'; return { i, sel, idx: [...d.querySelectorAll(sel)].indexOf(e), label: e.textContent.trim() }; });
  for (const t of triggers) {
    w = load(lang); // fresh page for each click
    await wait(50);
    const el = w.document.querySelectorAll(t.sel)[t.idx];
    el.click();
    await wait(150);
    const chat = w.document.getElementById('chat');
    const log = w.document.getElementById('log');
    if (!chat || chat.hidden) { fail(`"${t.label}" did not open the chat`); continue; }
    const bots = [...log.children].filter((m) => m.className === 'b');
    const texts = bots.map((b) => b.textContent.trim()).filter(Boolean);
    const qs = texts.slice(1).filter((x) => /\?|؟/.test(x));
    const dup = texts.length !== new Set(texts).size;
    if (qs.length > 1) fail(`"${t.label}" asks ${qs.length} questions before the customer answers: ${qs.map((q) => q.slice(0, 40)).join(' | ')}`);
    else if (dup) fail(`"${t.label}" repeats the same message`);
    else ok(`"${t.label}" → ${texts.length} message(s), waits for the customer`);
  }
}

(async () => {
  for (const lang of ['en', 'ar']) await check(lang);
  console.log(failures ? `\n${failures} problem(s) found — do not publish.` : '\nAll good — safe to publish.');
  process.exit(failures ? 1 : 0);
})();
