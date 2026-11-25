# DESIGN.md — M&M Auto Center (mmautocenter.ca)

Identity **A: Navy + Orange**. Any agent or person building a page, email, chat screen,
social image or document for M&M Auto Center reads this file first and follows it.
Live reference: https://mmautocenter.ca/en/ and /ar/. Preview of tokens: `preview.html`.

---

## 1. Visual theme
- A trustworthy neighbourhood garage in Mississauga, presented professionally: calm deep navy,
  one warm orange for action, real workshop photography with warm light.
- Bilingual by design: complete separate English (default, LTR) and Arabic (RTL) pages, never
  side-by-side translations.
- Mood words: clear, honest, quick, friendly, professional. Never flashy, never "discount store".
- Motion is light only (soft pulse on the chat button, short fades); everything respects
  `prefers-reduced-motion`.

## 2. Colour palette and roles
| Token | Hex | Role |
|---|---|---|
| `--navy` / ink | `#0B1F3A` | Header, hero background, headings on light, button text on orange |
| `--navy2` | `#16406E` | Hero gradient partner, secondary dark surfaces |
| Chat base | `#0F172A` | Chat panel background |
| Chat header / input bar | `#0B1222` | Chat header and composer |
| Chat bubble (bot) | `#1E293B` | Bot messages, chip hover |
| Chat border | `#334155` | Chip and input borders |
| `--bg` | `#F4F6FA` | Light page background below the hero |
| **Brand orange** `--orange` | `#FF7A1A` | Primary call-to-action ("Chat to book"), "Auto Center" wordmark, kicker text |
| Chat accent `--ac` | `#F97316` | Chat accent: launcher, user bubbles, send button, bot avatar |
| Accent light `--ac2` | `#FDBA74` | Icons inside chips, focus rings, progress bar end |
| Booking gold | `#F59E0B` / text `#FBBF24` | The single "Book online" chip (primary chat action) |
| Callback green | `#10B981` / text `#34D399` | "Get a callback" chip, "Online" status dot |
| Away grey | `#94A3B8` | "Away – leave a message" status |
| Rating link | `#C2410C` | "4.8 on Google" link on light background (contrast-safe orange) |

Service-card category colours (card top border + button): Repair `#1E5FA8`, Parts `#D9480F`,
Tires & rims `#0F8B6D`, Booking `#6741D9`.

Rules: one orange family only; orange is for action, never for body text on white (use
`#C2410C` if orange text must sit on white). Body text on light = navy `#0B1F3A`; on dark = `#E2E8F0`.

## 3. Typography
- Font stack: `system-ui, "Segoe UI", Tahoma, Arial, sans-serif` (fast, no web-font download,
  renders Arabic well on every phone).
- H1 hero: bold, ~32–44px desktop / ~26–30px mobile, tight line-height (1.15).
- Section titles ~22–26px bold; card titles ~18px bold; body 15–16px, line-height 1.5–1.6.
- Chat text 15px; chips 14px.
- Arabic uses the same sizes; never italic; numbers stay Western digits for phone and hours.

## 4. Component styles
- **Primary button**: orange `#FF7A1A`, navy text, radius 8–12px, bold, generous padding.
- **Secondary button**: transparent with 1px light border on navy (e.g. "Call (647) 448-0876").
- **Service card**: white, radius 14–16px, image on top, 4px category-colour top accent,
  title + one-line description + one category-coloured button. Soft shadow `0 12px 26px #0b1f3a24`.
- **Chat launcher**: 56px orange circle with a chat-bubble icon, soft pulse, bottom-right
  (bottom-left in Arabic).
- **Chat panel**: dark `#0F172A`, radius 20px; header with circular bot avatar, name
  "M&M Auto Assistant", status dot (green Online / grey Away), minimise and close.
- **Bubbles**: bot `#1E293B` radius 18px with a 6px corner at the avatar side; user bubble in
  orange `--ac` with navy text on the opposite side.
- **Chips**: pill (radius 999px), 1px `#334155` border, icon in `--ac2`; "Book online" is gold,
  "Get a callback" is green. Max ~6 chips per message.
- **Composer**: dark input, radius 14px, square orange send button (48px, radius 14px).
- **Owner section** ("Talk to Mohamed"), **FAQ** (native `<details>`), **Google rating line**.

## 5. Layout principles
- Mobile first. Content width max ~1100px, centred; 16–24px side padding.
- Order on home: header → hero (headline, 2 buttons, photo) → 4 service cards → trust note +
  rating → owner → FAQ → footer (address, hours, phone, map link).
- Every action on the page opens the chat on the matching flow; booking itself stays in ARI.
- Spacing scale: 4, 8, 12, 16, 24, 32, 48px.

## 6. Depth and elevation
- Light surfaces: soft navy-tinted shadows (`0 2px 10px #0b1f3a14` small, `0 12px 26px #0b1f3a24` cards).
- Dark surfaces (chat): borders `#ffffff14` instead of shadows; the panel itself
  `0 20px 60px rgba(0,0,0,.5)`.
- Radii: 8 (small buttons), 12–16 (cards, inputs), 18–20 (bubbles, panel), 999 (chips), 50% (avatars).

## 7. Do's and don'ts
**Do**
- Keep one primary action per screen ("Chat to book" / "Book online").
- Use real workshop photos or warm-lit images; keep faces/plates out of stock-style photos.
- Show hours exactly: Mon–Thu 9:30–6:00, Fri 9:30–12:00 & 2:00–6:00 (Friday prayer break),
  Sat 9:30–4:00, Sun closed.
- Date any changing number (e.g. "4.8 on Google, 69 reviews, Nov 2026").

**Don't**
- Don't copy another brand's look, logo, wording or layout.
- Don't add new colours, gradients in many hues, or more than one orange.
- Don't put prices, discounts or "beat any price" anywhere.
- Don't use stat counters or fake urgency.

## 8. Responsive behaviour
- ≤600px: chat opens as a bottom sheet covering 92% of the screen with a dimmed backdrop;
  service cards stack in one column; hero image goes under the text.
- ≤760px: navigation collapses to the essentials (Services, Parts, Tires, Book, language).
- Desktop: chat is a 400px floating panel; launcher stays visible when chat is closed.
- Arabic pages mirror the layout (`dir="rtl"`), including chat side and bubble corners.

## 9. Agent prompt guide
When asked to build anything for M&M Auto Center:
1. Read this file and section 10 before writing code or copy.
2. Use only the tokens above; reuse existing components from `style.css` and `app.js`.
3. Produce both English and Arabic versions; English is the default.
4. Every new button must route into the chat flow (or ARI for booking), never a dead form.
5. After building, take mobile screenshots (390px) in EN and AR and compare with the live site.

## 10. Honesty rules (M&M-specific, mandatory)
- **Confirmed services only**: auto repair & maintenance, oil & filter, brakes, A/C,
  diagnostics & check-engine, battery service, electrical, collision repair, detailing,
  glass replacement, pre-purchase inspection, tires & rims (passenger, SUV, light truck),
  bring-your-own-parts (labour only), used car sales and car valuation
  (licensed dealer since 2011; values based on current auction market prices).
- **Never claim**: "safety certified", mobile / home / office service, EV service,
  "beat any price", any price or discount.
- The chat collects the request and promises a confirmation; it never quotes a price.
- Languages: English and Arabic. Phone (647) 448-0876. Address 1765 Shawson Dr, Unit 14,
  Mississauga, ON L4W 1N8.
- If something is not confirmed in this file, ask the owner before publishing it.
