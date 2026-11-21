import json
K=json.load(open('data/knowledge.json',encoding='utf-8'))
C = {
"en": dict(lang="en", dir="ltr", other="ar", other_label="العربية", title="M&M Auto Center | Auto repair & parts, Mississauga",
 desc="Auto repair, parts and tires in Mississauga. Tell our chat what you need and we confirm price and availability.",
 nav=["Services","Parts","Tires & rims","Book"], tagline="Auto repair & parts in Mississauga",
 h1="Tell us what your car needs. We take it from there.",
 sub="Pick an option, our chat asks a few quick questions, and we confirm price and availability with you.",
 cta="Chat to book", call="Call (647) 448-0876",
 choices=[("services","Repair & service","Repairs, A/C, battery, body work, pre-purchase inspections and mobile service.","Book a repair"),
          ("parts","Find a part","Parts and filters for your vehicle.","Find my part"),
          ("tires","Find a tire or rim","Tell us the size or your vehicle and we find it.","Find tires & rims"),
          ("book","Book an appointment","Choose a service and a time that suits you.","Start booking")],
 chat_title="M&M Auto Assistant", online="Online", chat_hello={"services":"What service do you need? Please share your name, phone and vehicle.",
  "parts":"Which part do you need? Tell me the part name and your vehicle (year, make, model) or VIN.",
  "tires":"Looking for tires or rims? Tell me which one, and I will ask for the size or your vehicle.",
  "book":"Which service and what day suit you? Please share your name and phone."},
 note="We confirm price and availability with you. Prices are never final until we confirm.",
 addr="1765 Shawson Dr, Unit 14, Mississauga", foot="Auto repair & parts", priv="We measure site usage without saving personal details.", ph="Ask about parts, services, booking...", send="Send", close="Close"),
"ar": dict(lang="ar", dir="rtl", other="en", other_label="English", title="إم آند إم أوتو سنتر | إصلاح سيارات وقطع غيار في ميسيساجا",
 desc="إصلاح سيارات وقطع غيار وإطارات في ميسيساجا. أخبر الشات بما تحتاجه ونؤكد لك السعر والتوفر.",
 nav=["الخدمات","قطع الغيار","إطارات وجنوط","احجز"], tagline="إصلاح سيارات وقطع غيار في ميسيساجا",
 h1="أخبرنا بما تحتاجه سيارتك، ونتولى الباقي.",
 sub="اختر خيارًا، وسيسألك الشات بضعة أسئلة سريعة، ثم نؤكد لك السعر والتوفر.",
 cta="احجز عبر الشات", call="اتصل (647) 448-0876",
 choices=[("services","إصلاح وصيانة","إصلاحات وتكييف وبطاريات وسمكرة وفحص ما قبل الشراء وخدمة متنقلة.","احجز إصلاحًا"),
          ("parts","ابحث عن قطعة","قطع غيار وفلاتر لسيارتك.","ابحث عن قطعتي"),
          ("tires","ابحث عن إطار أو جنط","أخبرنا بالمقاس أو سيارتك ونبحث لك عنه.","ابحث عن إطارات وجنوط"),
          ("book","احجز موعدًا","اختر الخدمة والوقت المناسب لك.","ابدأ الحجز")],
 chat_title="مساعد إم آند إم", online="متصل الآن", chat_hello={"services":"ما الخدمة التي تحتاجها؟ من فضلك أرسل اسمك ورقم هاتفك وبيانات سيارتك.",
  "parts":"ما القطعة التي تحتاجها؟ اذكر اسمها وبيانات سيارتك (السنة والماركة والموديل) أو رقم الشاسيه.",
  "tires":"تبحث عن إطارات أو جنوط؟ أخبرني أيهما، وسأسألك عن المقاس أو سيارتك.",
  "book":"ما الخدمة وأي يوم يناسبك؟ من فضلك أرسل اسمك ورقم هاتفك."},
 note="نؤكد لك السعر والتوفر. الأسعار ليست نهائية حتى نؤكدها.",
 addr="1765 Shawson Dr, Unit 14, Mississauga", foot="إصلاح سيارات وقطع غيار", priv="نقيس استخدام الموقع دون حفظ بياناتك الشخصية.", ph="اسأل عن القطع والخدمات والحجز...", send="إرسال", close="إغلاق"),
}
IMG = {"services":"services.png","parts":"parts.png","tires":None,"book":None}
CLR = {"services":"#1E5FA8","parts":"#D9480F","tires":"#0F8B6D","book":"#6741D9"}
TT={"en":{
"svc":[["repair","Auto repair"],["battery","Battery"],["prepurchase","Pre-purchase inspection"],["diag","Not sure what's wrong"],["body","Body shop"],["ac","A/C service"],["mobile","Mobile service (GTA)"],["other","Something else"]],
"q_service":"Which service do you need?","q_part":"Which part do you need? Name it, or describe it.","q_kind":"What are you looking for?","kinds":[["tire","Buy tires"],["rim","Buy rims"],["both","Tires and rims"],["swap","Seasonal swap (tires on rims)"],["changeover","Tire changeover (mount & balance)"]],"q_size":"What is the size (for example 205/55R16), or your vehicle (year, make, model)? Rims: add bolt pattern if you know it.","q_season":"Which season?","seasons":[["all","All-season"],["winter","Winter"],["summer","Summer"]],
"q_vehicle":"What is your vehicle? Year, make and model, or paste the 17-character VIN.","q_battery":"Which vehicle is the battery for? Year, make and model, or the 17-character VIN. We confirm the right battery and price.","q_buy":"Which used car are you thinking of buying? Year, make and model, or the 17-character VIN, so we can inspect it before you buy.","q_symptom":"Describe what you notice (noise, vibration, warning light, smell, hard to start). A few words are enough.","stepLbl":"Progress {p}%","q_name":"What is your name?","q_phone":"Best phone number to reach you?",
"bad_phone":"Please enter a valid phone number (at least 10 digits).","vin_ok":"Found:","vin_fail":"I could not decode that VIN, I will save it as typed.",
"done":"Thank you! We have your request and will contact you to confirm price and availability.","test":"(Test mode: nothing was saved.)","fail":"I could not save that right now. Please call us at (647) 448-0876.",
"book_msg":"You can book online now. If you prefer, we can call you back.","book_btn":"Book online","callback":"Call me back","call":"Call us",
"hours":"Hours: Mon-Fri 9:30 AM-6:00 PM, Sat 9:30 AM-4:00 PM, Sunday closed.","loc":"We are at 1765 Shawson Dr, Unit 14, Mississauga, ON L4W 1N8.","map":"Open map",
"price":"Prices depend on your vehicle. Leave your details and we confirm price and availability with you.","fallback":"I can help with repairs, parts, tires and rims, or booking. Please choose an option below, or call us.",
"chips_home":[["services","Repair & service"],["parts","Find a part"],["tires","Tires & rims"],["book","Book online"],["hours","Hours"],["loc","Location"]],
"again":"Anything else?","intent_words":{"hours":"hour|open|close|when","loc":"where|address|location|direction","price":"price|cost|quote|how much|estimate","book":"book|appoint|schedule","insp":"inspect|pre-purchase|before buy|used car|buying a car","battery":"battery|won.t start|dead battery","parts":"part|tire|brake pad|filter|oil","urgent":"urgent|asap|emergency|today|right now|broken down|stranded"}},"ar":{
"svc":[["repair","إصلاح سيارات"],["battery","بطارية"],["prepurchase","فحص قبل شراء سيارة"],["diag","لا أعرف المشكلة"],["body","سمكرة ودهان"],["ac","صيانة التكييف"],["mobile","خدمة متنقلة (GTA)"],["other","شيء آخر"]],
"q_service":"ما الخدمة التي تحتاجها؟","q_part":"ما القطعة التي تحتاجها؟ اذكر اسمها أو صفها.","q_kind":"ماذا تبحث عنه؟","kinds":[["tire","شراء إطارات"],["rim","شراء جنوط"],["both","إطارات وجنوط"],["swap","تبديل موسمي (الإطارات على الجنوط)"],["changeover","تغيير إطار (فك وتركيب وترصيص)"]],"q_size":"ما المقاس (مثل 205/55R16) أو سيارتك (السنة والماركة والموديل)؟ للجنوط أضف عدد وتباعد الفتحات إن عرفتهما.","q_season":"أي موسم؟","seasons":[["all","كل المواسم"],["winter","شتوي"],["summer","صيفي"]],
"q_vehicle":"ما سيارتك؟ السنة والماركة والموديل، أو الصق رقم الشاسيه (17 خانة).","q_battery":"لأي سيارة البطارية؟ السنة والماركة والموديل أو رقم الشاسيه (17 خانة)، ونؤكد لك البطارية المناسبة والسعر.","q_buy":"أي سيارة مستعملة تفكر في شرائها؟ السنة والماركة والموديل أو رقم الشاسيه (17 خانة)، لنفحصها لك قبل الشراء.","q_symptom":"صف ما تلاحظه (صوت، اهتزاز، ضوء تحذير، رائحة، صعوبة تشغيل). كلمات قليلة تكفي.","stepLbl":"التقدم {p}٪","q_name":"ما اسمك؟","q_phone":"ما أنسب رقم هاتف للتواصل معك؟",
"bad_phone":"من فضلك أدخل رقم هاتف صحيحًا (10 أرقام على الأقل).","vin_ok":"تم التعرف على:","vin_fail":"لم أستطع قراءة رقم الشاسيه، سأحفظه كما كتبته.",
"done":"شكرًا لك! وصلنا طلبك وسنتواصل معك لنؤكد السعر والتوفر.","test":"(وضع تجريبي: لم يُحفظ شيء.)","fail":"تعذّر الحفظ الآن. من فضلك اتصل بنا على (647) 448-0876.",
"book_msg":"يمكنك الحجز عبر الإنترنت الآن. وإن فضّلت، نتصل بك نحن.","book_btn":"احجز عبر الإنترنت","callback":"اتصلوا بي","call":"اتصل بنا",
"hours":"مواعيد العمل: الاثنين إلى الجمعة 9:30 ص - 6:00 م، السبت 9:30 ص - 4:00 م، الأحد مغلق.","loc":"نحن في 1765 Shawson Dr, Unit 14, Mississauga, ON L4W 1N8.","map":"افتح الخريطة",
"price":"السعر يعتمد على سيارتك. اترك بياناتك ونؤكد لك السعر والتوفر.","fallback":"أستطيع مساعدتك في الإصلاح أو قطع الغيار أو الإطارات والجنوط أو الحجز. اختر من الأزرار أدناه أو اتصل بنا.",
"chips_home":[["services","إصلاح وصيانة"],["parts","ابحث عن قطعة"],["tires","إطارات وجنوط"],["book","احجز عبر الإنترنت"],["hours","المواعيد"],["loc","الموقع"]],
"again":"هل تحتاج شيئًا آخر؟","intent_words":{"hours":"مواعيد|دوام|ساعات|متى|مفتوح","loc":"فين|وين|اين|أين|عنوان|موقع","price":"سعر|كم|تكلفة|عرض سعر|بكام","book":"حجز|احجز|موعد","insp":"فحص|قبل الشراء|مستعملة|مستعمل","battery":"بطارية|بطاريه|بطاريات","parts":"قطعة|قطع|اطار|إطار|فلتر|زيت|تيل","urgent":"عاجل|مستعجل|طارئ|الان|الآن|اليوم|معطلة|عطلانة"}}}
for L in ("en","ar"):
    top=[[s["id"],s[L]["title"],s["flow"]] for s in K["services"] if s["chip_top"]]
    rest=[[s["id"],s[L]["title"],s["flow"]] for s in K["services"] if not s["chip_top"]]
    other=[["other","Something else" if L=="en" else "شيء آخر","vehicle"]]
    TT[L]["svc_top"]=top+[["more","More services…" if L=="en" else "خدمات أخرى…","more"]]
    TT[L]["svc_rest"]=rest+other
    TT[L]["q_used"]="What kind of used car are you looking for (type, budget, year)?" if L=="en" else "ما نوع السيارة المستعملة التي تبحث عنها (النوع، الميزانية، السنة)؟"
    TT[L]["closed_note"]="We are closed right now. We will reply when we open (Mon-Fri 9:30 AM-6:00 PM, Sat 9:30 AM-4:00 PM)." if L=="en" else "نحن مغلقون الآن. سنرد عليك عند فتح الورشة (الاثنين-الجمعة 9:30 ص-6:00 م، السبت 9:30 ص-4:00 م)."
    TT[L]["open_now"]="We are open now." if L=="en" else "نحن مفتوحون الآن."
    TT[L]["closed_now"]="We are closed right now." if L=="en" else "نحن مغلقون الآن."
    del TT[L]["svc"]
    TT[L]["vin_fail"]="I could not read that VIN. What are the vehicle year, make and model?" if L=="en" else "لم أستطع قراءة رقم الشاسيه. ما سنة وماركة وموديل السيارة؟"
    TT[L]["q_vehicle2"]="For example: 2017 Cadillac ATS" if L=="en" else "مثال: 2017 Cadillac ATS"
    TT[L]["done_more"]="We added this to your earlier request from today. We will contact you to confirm." if L=="en" else "أضفنا هذا إلى طلبك السابق اليوم. سنتواصل معك للتأكيد."
    C[L]["addr"]=K["business"]["address"].replace(", ON L4W 1N8","")
CSS = open("style.css").read()
JS = open("app.js").read()
for k,c in C.items():
    cards=""
    for key,t,d,b in c["choices"]:
        img = f'<img src="../img/{IMG[key]}" alt="" loading="lazy">' if IMG[key] else '<div class="ph" style="background:linear-gradient(135deg,{CLR[key]},#0B1F3A)"><i></i></div>'
        cards += f'<article class="card" style="--c:{CLR[key]}"><div class="im">{img}</div><div class="bd"><h3>{t}</h3><p>{d}</p><button class="go" data-k="{key}">{b}</button></div></article>'
    nav = "".join(f'<a href="#{a}">{n}</a>' for a,n in zip(["services","parts","tires","book"],c["nav"]))
    html = f'''<!doctype html><html lang="{c["lang"]}" dir="{c["dir"]}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{c["title"]}</title><meta name="description" content="{c["desc"]}">
<link rel="alternate" hreflang="en" href="https://mmautocenter.ca/en/"><link rel="alternate" hreflang="ar" href="https://mmautocenter.ca/ar/"><link rel="alternate" hreflang="x-default" href="https://mmautocenter.ca/en/">
<style>{CSS}</style></head><body>
<header><div class="logo">M&amp;M <span>Auto Center</span></div><nav>{nav}</nav><a class="lang" href="../{c["other"]}/" data-lang="{c["other"]}">{c["other_label"]}</a></header>
<section class="hero"><div class="hero-in"><p class="tag">{c["tagline"]}</p><h1>{c["h1"]}</h1><p class="sub">{c["sub"]}</p>
<div class="cta"><button class="go big" data-k="book">{c["cta"]}</button><a class="call" href="tel:+16474480876">{c["call"]}</a></div></div>
<img class="hero-img" src="../img/hero.png" alt=""></section>
<main><div class="grid">{cards}</div><p class="note">{c["note"]}</p></main>
<footer><div>{c["addr"]}</div><div>(647) 448-0876</div><div>{c["foot"]}</div><div class="priv">{c["priv"]}</div></footer>
<aside id="chat" hidden><div class="ch"><span class="av"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="8" width="16" height="12" rx="3"/><path d="M12 4v4M9 14h.01M15 14h.01"/></svg></span><div class="tt"><b>{c["chat_title"]}</b><small><i></i>{c["online"]}</small></div><button id="mn" aria-label="minimize">&#8722;</button><button id="x" aria-label="{c["close"]}">&times;</button></div><div id="vc" hidden></div><div id="pg" hidden><i></i></div><div id="log"></div>
<form id="f"><input id="m" placeholder="{c["ph"]}" autocomplete="off"><button aria-label="{c["send"]}"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2"><path d="m22 2-7 20-4-9-9-4zM22 2 11 13"/></svg></button></form></aside>
<script>const HELLO={json.dumps(c["chat_hello"],ensure_ascii=False)};const T={json.dumps(TT[k],ensure_ascii=False)};const LANG="{k}";const HRS={json.dumps(K["hours"])};const TZ="{K["business"]["timezone"]}";const BOOK="{K["business"]["booking_url"]}";const INTAKE="{K["business"].get("intake_url","")}";{JS}</script></body></html>'''
    open(f"{k}/index.html","w",encoding="utf-8").write(html)
open("index.html","w").write('<!doctype html><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=en/"><a href="en/">English</a> · <a href="ar/">العربية</a>')
