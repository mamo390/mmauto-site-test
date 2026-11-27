import json
K=json.load(open('data/knowledge.json',encoding='utf-8'))
C = {
"en": dict(lang="en", dir="ltr", other="ar", other_label="العربية", title="M&M Auto Center | Auto repair & parts, Mississauga",
 desc="Auto repair, parts and tires in Mississauga. Tell our chat what you need and we confirm price and availability.",
 nav=["Services","Parts","Tires & rims","Book"], tagline="Auto repair & parts in Mississauga",
 h1="Tell us what your car needs. We take it from there.",
 sub="Pick an option, our chat asks a few quick questions, and we confirm price and availability with you.",
 cta="Chat to book", call="Call (647) 448-0876",
 choices=[("services","Repair & service","Repairs, collision, A/C, battery, diagnostics and pre-purchase inspections.","Book a repair"),
          ("parts","Find a part","Parts and filters for your vehicle.","Find my part"),
          ("tires","Find a tire or rim","Tell us the size or your vehicle and we find it.","Find tires & rims"),
          ("book","Book an appointment","Choose a service and a time that suits you.","Start booking")],
 chat_title="M&M Auto Assistant", online="Online", chat_hello={"welcome":"Hi! I'm the M&M Auto Center assistant. I can help you book an appointment, get a quote, or find a part. How can I help you today?","services":"What service do you need? Please share your name, phone and vehicle.",
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
 choices=[("services","إصلاح وصيانة","إصلاحات وحوادث وتكييف وبطاريات وتشخيص وفحص ما قبل الشراء.","احجز إصلاحًا"),
          ("parts","ابحث عن قطعة","قطع غيار وفلاتر لسيارتك.","ابحث عن قطعتي"),
          ("tires","ابحث عن إطار أو جنط","أخبرنا بالمقاس أو سيارتك ونبحث لك عنه.","ابحث عن إطارات وجنوط"),
          ("book","احجز موعدًا","اختر الخدمة والوقت المناسب لك.","ابدأ الحجز")],
 chat_title="مساعد إم آند إم", online="متصل الآن", chat_hello={"welcome":"أهلًا بك! أنا مساعد مركز إم آند إم للسيارات. أستطيع مساعدتك في حجز موعد، أو طلب عرض سعر، أو البحث عن قطعة. كيف أساعدك اليوم؟","services":"ما الخدمة التي تحتاجها؟ من فضلك أرسل اسمك ورقم هاتفك وبيانات سيارتك.",
  "parts":"ما القطعة التي تحتاجها؟ اذكر اسمها وبيانات سيارتك (السنة والماركة والموديل) أو رقم الشاسيه.",
  "tires":"تبحث عن إطارات أو جنوط؟ أخبرني أيهما، وسأسألك عن المقاس أو سيارتك.",
  "book":"ما الخدمة وأي يوم يناسبك؟ من فضلك أرسل اسمك ورقم هاتفك."},
 note="نؤكد لك السعر والتوفر. الأسعار ليست نهائية حتى نؤكدها.",
 addr="1765 Shawson Dr, Unit 14, Mississauga", foot="إصلاح سيارات وقطع غيار", priv="نقيس استخدام الموقع دون حفظ بياناتك الشخصية.", ph="اسأل عن القطع والخدمات والحجز...", send="إرسال", close="إغلاق"),
}
IMG = {"services":"services.png","parts":"parts.png","tires":None,"book":None}
CLR = {"services":"#1E5FA8","parts":"#D9480F","tires":"#0F8B6D","book":"#6741D9"}
TT={"en":{
"svc":[["repair","Auto repair"],["battery","Battery"],["prepurchase","Pre-purchase inspection"],["diag","Not sure what's wrong"],["ac","A/C service"],["other","Something else"]],
"q_service":"Which service do you need?","q_part":"Which part do you need? Name it, or describe it.","q_kind":"What are you looking for?","kinds":[["tire","Buy tires"],["rim","Buy rims"],["both","Tires and rims"],["swap","Seasonal swap (tires on rims)"],["changeover","Tire changeover (mount & balance)"]],"q_size":"What is the size (for example 205/55R16), or your vehicle (year, make, model)? Rims: add bolt pattern if you know it.","q_season":"Which season?","seasons":[["all","All-season"],["winter","Winter"],["summer","Summer"]],
"q_vehicle":"What is your vehicle? Year, make and model, or paste the 17-character VIN.","q_battery":"Which vehicle is the battery for? Year, make and model, or the 17-character VIN. We confirm the right battery and price.","q_buy":"Which used car are you thinking of buying? Year, make and model, or the 17-character VIN, so we can inspect it before you buy.","q_mileage":"Roughly how many kilometres or miles are on it? (Your best guess is fine.)","q_mileage_buy":"What is the odometer reading on the car you are considering? We use it to check the maintenance and recall history.","q_dtc":"If a warning light is on and you know the code (like P0301), type it. If not, tap Skip.","skip":"Skip","known":"I will use your saved details, {n}.","same_veh":"Is it still your {v}?","yes":"Yes","other":"A different vehicle","keep_q":"Want me to remember your name, phone and vehicle on this device so you do not have to type them again? They stay on your device only.","keep_yes":"Yes, remember me","keep_no":"No thanks","kept":"Done. Welcome back next time.","welcome_back":"Welcome back, {n}!","forget":"Forget me","forgot":"Done. I removed your saved details from this device.","q_symptom":"Describe what you notice (noise, vibration, warning light, smell, hard to start). A few words are enough.","stepLbl":"Progress {p}%","q_name":"What is your name?","q_phone":"Best phone number to reach you?",
"bad_phone":"Please enter a valid phone number (at least 10 digits).","vin_ok":"Found:","vin_fail":"I could not decode that VIN, I will save it as typed.",
"done":"Thank you! We have your request and will contact you to confirm price and availability.","test":"(Test mode: nothing was saved.)","fail":"I could not save that right now. Please call us at (647) 448-0876.",
"book_msg":"You can book online now. If you prefer, we can call you back.","book_btn":"Book online","callback":"Call me back","call":"Call us",
"hours":"Hours: Mon-Thu 9:30 AM-6:00 PM. Fri 9:30 AM-12:00 PM and 2:00-6:00 PM (break for Friday prayer). Sat 9:30 AM-4:00 PM. Sunday closed.","loc":"We are at 1765 Shawson Dr, Unit 14, Mississauga, ON L4W 1N8.","map":"Open map","dir":"Get directions",
"price":"Prices depend on your vehicle. Leave your details and we confirm price and availability with you.","fallback":"I can help with repairs, parts, tires and rims, or booking. Please choose an option below, or call us.",
"chips_home":[["book","Book online"],["services","Repair & service"],["parts","Find a part"],["tires","Tires & rims"],["hours","Hours"],["loc","Location"]],
"again":"Anything else?","intent_words":{"hours":"hour|open|close|when","loc":"where|address|location|direction","price":"price|cost|quote|how much|estimate","book":"book|appoint|schedule","insp":"inspect|pre-purchase|before buy|used car|buying a car","battery":"battery|won.t start|dead battery","parts":"part|tire|brake pad|filter|oil","urgent":"urgent|asap|emergency|today|right now|broken down|stranded"}},"ar":{
"svc":[["repair","إصلاح سيارات"],["battery","بطارية"],["prepurchase","فحص قبل شراء سيارة"],["diag","لا أعرف المشكلة"],["ac","صيانة التكييف"],["other","شيء آخر"]],
"q_service":"ما الخدمة التي تحتاجها؟","q_part":"ما القطعة التي تحتاجها؟ اذكر اسمها أو صفها.","q_kind":"ماذا تبحث عنه؟","kinds":[["tire","شراء إطارات"],["rim","شراء جنوط"],["both","إطارات وجنوط"],["swap","تبديل موسمي (الإطارات على الجنوط)"],["changeover","تغيير إطار (فك وتركيب وترصيص)"]],"q_size":"ما المقاس (مثل 205/55R16) أو سيارتك (السنة والماركة والموديل)؟ للجنوط أضف عدد وتباعد الفتحات إن عرفتهما.","q_season":"أي موسم؟","seasons":[["all","كل المواسم"],["winter","شتوي"],["summer","صيفي"]],
"q_vehicle":"ما سيارتك؟ السنة والماركة والموديل، أو الصق رقم الشاسيه (17 خانة).","q_battery":"لأي سيارة البطارية؟ السنة والماركة والموديل أو رقم الشاسيه (17 خانة)، ونؤكد لك البطارية المناسبة والسعر.","q_buy":"أي سيارة مستعملة تفكر في شرائها؟ السنة والماركة والموديل أو رقم الشاسيه (17 خانة)، لنفحصها لك قبل الشراء.","q_mileage":"كم تقريبًا المسافة المقطوعة (كم أو ميل)؟ يكفي تقدير تقريبي.","q_mileage_buy":"كم قراءة العداد في السيارة التي تفكر بشرائها؟ نستخدمها لمراجعة الصيانة والاستدعاءات.","q_dtc":"إن كان ضوء التحذير مضاءً وتعرف الكود (مثل P0301) اكتبه، وإن لم تعرفه اضغط تخطي.","skip":"تخطي","known":"سأستخدم بياناتك المحفوظة يا {n}.","same_veh":"هل ما زالت سيارتك {v}؟","yes":"نعم","other":"سيارة أخرى","keep_q":"هل أتذكر اسمك ورقمك وسيارتك على هذا الجهاز كي لا تكتبها مرة أخرى؟ تبقى على جهازك فقط.","keep_yes":"نعم، تذكّرني","keep_no":"لا شكرًا","kept":"تم. أهلًا بك عند عودتك.","welcome_back":"أهلًا بعودتك يا {n}!","forget":"انسَ بياناتي","forgot":"تم. حذفت بياناتك المحفوظة من هذا الجهاز.","q_symptom":"صف ما تلاحظه (صوت، اهتزاز، ضوء تحذير، رائحة، صعوبة تشغيل). كلمات قليلة تكفي.","stepLbl":"التقدم {p}٪","q_name":"ما اسمك؟","q_phone":"ما أنسب رقم هاتف للتواصل معك؟",
"bad_phone":"من فضلك أدخل رقم هاتف صحيحًا (10 أرقام على الأقل).","vin_ok":"تم التعرف على:","vin_fail":"لم أستطع قراءة رقم الشاسيه، سأحفظه كما كتبته.",
"done":"شكرًا لك! وصلنا طلبك وسنتواصل معك لنؤكد السعر والتوفر.","test":"(وضع تجريبي: لم يُحفظ شيء.)","fail":"تعذّر الحفظ الآن. من فضلك اتصل بنا على (647) 448-0876.",
"book_msg":"يمكنك الحجز عبر الإنترنت الآن. وإن فضّلت، نتصل بك نحن.","book_btn":"احجز عبر الإنترنت","callback":"اتصلوا بي","call":"اتصل بنا",
"hours":"مواعيد العمل: الاثنين إلى الخميس 9:30 ص - 6:00 م. الجمعة 9:30 ص - 12:00 ظ ثم 2:00 - 6:00 م (استراحة صلاة الجمعة). السبت 9:30 ص - 4:00 م. الأحد مغلق.","loc":"نحن في 1765 Shawson Dr, Unit 14, Mississauga, ON L4W 1N8.","map":"افتح الخريطة","dir":"الاتجاهات إلى الورشة",
"price":"السعر يعتمد على سيارتك. اترك بياناتك ونؤكد لك السعر والتوفر.","fallback":"أستطيع مساعدتك في الإصلاح أو قطع الغيار أو الإطارات والجنوط أو الحجز. اختر من الأزرار أدناه أو اتصل بنا.",
"chips_home":[["book","احجز عبر الإنترنت"],["services","إصلاح وصيانة"],["parts","ابحث عن قطعة"],["tires","إطارات وجنوط"],["hours","المواعيد"],["loc","الموقع"]],
"again":"هل تحتاج شيئًا آخر؟","intent_words":{"hours":"مواعيد|دوام|ساعات|متى|مفتوح","loc":"فين|وين|اين|أين|عنوان|موقع","price":"سعر|كم|تكلفة|عرض سعر|بكام","book":"حجز|احجز|موعد","insp":"فحص|قبل الشراء|مستعملة|مستعمل","battery":"بطارية|بطاريه|بطاريات","parts":"قطعة|قطع|اطار|إطار|فلتر|زيت|تيل","urgent":"عاجل|مستعجل|طارئ|الان|الآن|اليوم|معطلة|عطلانة"}}}
for L in ("en","ar"):
    top=[[s["id"],s[L]["title"],s["flow"]] for s in K["services"] if s["chip_top"]]
    rest=[[s["id"],s[L]["title"],s["flow"]] for s in K["services"] if not s["chip_top"]]
    other=[["other","Something else" if L=="en" else "شيء آخر","vehicle"]]
    TT[L]["svc_top"]=top+[["more","More services…" if L=="en" else "خدمات أخرى…","more"]]
    TT[L]["svc_rest"]=rest+other
    TT[L].update({"used_intro":"We are a licensed car dealer since 2011. We value cars using current auction market prices. What do you need?","used_buy":"Buy a used car","used_sell":"Value my car (to sell)","used_price":"Check a car's real price before buying","fast_tires":"Good to know: most tire sizes can be ready the same day when you confirm before 1 PM, otherwise usually by the next morning. We will confirm availability for your size.","lifetime":"Good to know: for radiator and A/C parts we offer an option with a lifetime warranty (on selected parts, subject to availability). We will confirm the details when we contact you."} if L=="en" else {"used_intro":"نحن تاجر سيارات مرخّص منذ 2011، ونقيّم السيارات بناءً على أسعار المزادات الحالية في السوق. ماذا تحتاج؟","used_buy":"شراء سيارة مستعملة","used_sell":"تقييم سيارتي للبيع","used_price":"تقييم سعر سيارة أريد شراءها","fast_tires":"معلومة تهمّك: أغلب مقاسات الإطارات تكون جاهزة في نفس اليوم إذا أكّدت الطلب قبل الساعة 1 ظهرًا، وإلا فغالبًا صباح اليوم التالي. سنؤكد لك التوفر لمقاسك.","lifetime":"معلومة تهمّك: في قطع الرادياتير والتكييف نوفّر خيارًا بكفالة مدى الحياة (على قطع مختارة وحسب التوفر). سنؤكد لك التفاصيل عند تواصلنا معك."})
    TT[L]["q_used"]="What kind of used car are you looking for (type, budget, year)?" if L=="en" else "ما نوع السيارة المستعملة التي تبحث عنها (النوع، الميزانية، السنة)؟"
    TT[L]["closed_note"]="We are closed right now. We will reply when we open (Mon-Thu 9:30 AM-6:00 PM, Fri 9:30-12:00 and 2:00-6:00 PM, Sat 9:30 AM-4:00 PM)." if L=="en" else "نحن مغلقون الآن. سنرد عليك عند فتح الورشة (الاثنين-الخميس 9:30 ص-6:00 م، الجمعة 9:30-12:00 ثم 2:00-6:00 م، السبت 9:30 ص-4:00 م)."
    TT[L]["open_now"]="We are open now." if L=="en" else "نحن مفتوحون الآن."
    TT[L]["closed_now"]="We are closed right now." if L=="en" else "نحن مغلقون الآن."
    del TT[L]["svc"]
    TT[L]["vin_fail"]="I could not read that VIN. What are the vehicle year, make and model?" if L=="en" else "لم أستطع قراءة رقم الشاسيه. ما سنة وماركة وموديل السيارة؟"
    TT[L]["q_vehicle2"]="For example: 2017 Cadillac ATS" if L=="en" else "مثال: 2017 Cadillac ATS"
    TT[L]["done_more"]="We added this to your earlier request from today. We will contact you to confirm." if L=="en" else "أضفنا هذا إلى طلبك السابق اليوم. سنتواصل معك للتأكيد."
    C[L]["addr"]=K["business"]["address"].replace(", ON L4W 1N8","")

UI={"en":{"open":"Open now","closed":"Closed now - book online 24/7","review":"Leave a Google review","call":"Call","dir":"Directions","waze":"Waze","chat":"Chat","book":"Book","reels":"See our work"},"ar":{"open":"مفتوح الآن","closed":"مغلق الآن - احجز أونلاين 24/7","review":"اكتب تقييمك على Google","call":"اتصل","dir":"الاتجاهات","waze":"Waze","chat":"الشات","book":"احجز","reels":"شاهد أعمالنا"}}
RT={"en":"4.8 on Google (69 reviews, Nov 2026) - read our reviews","ar":"4.8 على Google (69 تقييمًا، نوفمبر 2026) - اقرأ التقييمات"}
OWN={"en":{"h":"Talk to Mohamed","p":"I am the owner of M&M Auto Center. Tell us what your car needs and I will make sure you get a clear answer. English or Arabic, whichever is easier for you.","b":"Chat with us","n":"Mohamed, owner"},
"ar":{"h":"تحدّث مع محمد","p":"أنا صاحب M&M Auto Center. أخبرنا بما تحتاجه سيارتك وسأحرص أن تحصل على جواب واضح. بالعربية أو الإنجليزية، كما يريحك.","b":"ابدأ المحادثة","n":"محمد، صاحب الورشة"}}
ICO={"tag":'<path d="M3 12V4h8l10 10-8 8z"/><circle cx="7.5" cy="7.5" r="1.6"/>',"doc":'<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M9 8h6M9 12h6M9 16h4"/>',"cal":'<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',"mag":'<circle cx="11" cy="11" r="6"/><path d="M20 20l-4.5-4.5"/>',"chat":'<path d="M4 5h11v8H8l-4 3z"/><path d="M15 9h5v8l-3-2h-6v-2"/>',"clock":'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',"check":'<circle cx="12" cy="12" r="9"/><path d="M8 12l3 3 5-6"/>',"wrench":'<path d="M14.5 5.5a4 4 0 0 0 4.9 4.9L11 18.8a2.1 2.1 0 0 1-3-3l8.4-8.4"/>',"brief":'<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5h6v2M3 12h18"/>',"cap":'<path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11v5c3 2 9 2 12 0v-5"/>',"badge":'<circle cx="12" cy="9" r="6"/><path d="M8.5 14l-1.5 7 5-3 5 3-1.5-7"/>',"key":'<circle cx="8" cy="15" r="4"/><path d="M11 12l9-9M17 6l3 3"/>',"bolt":'<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>'}
def ico(n,cls="ic"): return f'<span class="{cls}"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{ICO[n]}</svg></span>'
ABOUT={"en":{"nav":"About","h":"A family in the car business since 1952","p":"It started in 1952 with Mohamed's late father and his auto repair workshop in Abdeen, Cairo. Mohamed carried the trade forward: from 1993 in Kuwait at the official dealers of Nissan & Infiniti, Mercedes-Benz, Hyundai and Toyota & Lexus, and as a mechanics instructor; then from 2008 in Canada as a Red Seal licensed technician. M&M Auto Center has been his shop in Mississauga since 2021.","cap":"Mohamed's father's workshop, Abdeen, Cairo","th":"From Abdeen to Mississauga","m":[["1952","Cairo","The family repair workshop opens in Abdeen","wrench"],["1993","Kuwait","Official dealers of Nissan, Infiniti, Mercedes-Benz, Hyundai, Toyota and Lexus","brief"],["2008","Canada","Red Seal licensed technician","badge"],["2021","Mississauga","M&M Auto Center opens its doors","key"]],"more":"Full experience","g":[["Kuwait · 1993–2008",[
["brief","Al-Babtain (Abdulmohsen Abdulaziz Al-Babtain Co.)",["Nissan","Infiniti"],"Quality Control → Service Advisor → Senior Advisor"],
["brief","A.R. Albisher & Z. Alkazemi Co.",["Mercedes-Benz"],"Service Advisor"],
["cap","Kuwait Military Technical Institute, with TQ (UK)",[],"Mechanics Instructor"],
["brief","Northern Gulf Trading Co.",["Hyundai"],"Service Advisor → Assistant Service Manager, Body-Shop Estimator"],
["brief","Mohamed Naser Al-Sayer & Sons",["Toyota","Lexus"],"Team Lead & Estimator, Central Body Shop (body & paint)"],
["key","Osoul Investment Co. (vehicle leasing)",[],"Garage Manager"],
["key","KGL Car Rental (Kuwait & Gulf Link)",[],"Asset Supervisor"]]],
["Canada · 2008–today",[
["badge","Red Seal",[],"Licensed Automotive Service Technician (2008)"],
["wrench","Canadian Tire · Nissan",[],"Automotive Technician"],
["badge","Manufacturer certifications",["Honda (Gold level)","Volkswagen","Dodge"],"Certified Technician"],
["mag","ADESA · Manheim",[],"Vehicle Inspector; Manheim Technician"],
["badge","Body repair · EV",[],"Certified Body-Repair Estimator; EV certified (2024)"],
["key","Licensed car dealer",[],"Certified used-car salesperson (2008); dealer since 2011"],
["wrench","M&M Auto Center, Mississauga",[],"Owner since 2021"]]]]},
"ar":{"nav":"من نحن","h":"عائلة في مجال السيارات منذ 1952","p":"بدأت الحكاية عام 1952 مع الوالد رحمه الله وورشته لإصلاح السيارات في عابدين بالقاهرة. وحمل محمد المهنة من بعده: من 1993 في الكويت لدى الوكلاء الرسميين لنيسان وإنفينيتي ومرسيدس بنز وهيونداي وتويوتا ولكزس، ومدرّساً للميكانيكا، ثم من 2008 في كندا كفني مرخّص Red Seal. وM&M Auto Center ورشته في ميسيساغا منذ 2021.","cap":"ورشة الوالد رحمه الله، عابدين، القاهرة","th":"من عابدين إلى ميسيساغا","m":[["1952","القاهرة","افتتاح ورشة العائلة لإصلاح السيارات في عابدين","wrench"],["1993","الكويت","لدى وكلاء نيسان وإنفينيتي ومرسيدس بنز وهيونداي وتويوتا ولكزس","brief"],["2008","كندا","فني سيارات مرخّص Red Seal","badge"],["2021","ميسيساغا","افتتاح M&M Auto Center","key"]],"more":"الخبرة كاملة","g":[["الكويت · 1993–2008",[
["brief","مجموعة البابطين (شركة عبدالمحسن عبدالعزيز البابطين)",["Nissan","Infiniti"],"مراقبة الجودة ← مستشار خدمة ← مستشار أول"],
["brief","شركة عبدالرحمن البشر وزيد الكاظمي",["Mercedes-Benz"],"مستشار خدمة"],
["cap","المعهد الفني العسكري الكويتي، مع شركة TQ البريطانية",[],"مدرّس ميكانيكا"],
["brief","شركة الخليج الشمالي للتجارة",["Hyundai"],"مستشار خدمة ← مساعد مدير خدمة، مقدّر أضرار سمكرة"],
["brief","شركة محمد ناصر الساير وأولاده",["Toyota","Lexus"],"قائد فريق ومقدّر أضرار، المركز الرئيسي للسمكرة والصبغ (CBS)"],
["key","شركة أصول للاستثمار (تأجير السيارات)",[],"مدير كراج"],
["key","KGL لتأجير السيارات (رابطة الكويت والخليج للنقل)",[],"مشرف أصول"]]],
["كندا · 2008–اليوم",[
["badge","Red Seal",[],"فني سيارات مرخّص (2008)"],
["wrench","Canadian Tire · Nissan",[],"فني سيارات"],
["badge","اعتمادات المصنّعين",["Honda (Gold)","Volkswagen","Dodge"],"فني معتمد"],
["mag","ADESA · Manheim",[],"مفتش سيارات، وفني في Manheim"],
["badge","السمكرة والسيارات الكهربائية",[],"مقدّر أضرار سمكرة معتمد، وشهادة السيارات الكهربائية (2024)"],
["key","تاجر سيارات مرخّص",[],"بائع سيارات مستعملة معتمد (2008)، وتاجر منذ 2011"],
["wrench","M&M Auto Center، ميسيساغا",[],"المالك منذ 2021"]]]]}}
HOW={"en":{"h":"How it works","s":[["chat","Tell us","Your car (year, make, model or VIN) and what you need."],["check","We confirm","Price and availability, before any work."],["cal","Book & drive","Pick a time; we take care of the rest."]]},
"ar":{"h":"كيف نعمل","s":[["chat","أخبرنا","سيارتك (السنة والماركة والموديل أو رقم الشاسيه) وما تحتاجه."],["check","نؤكد لك","السعر والتوفر، قبل أي عمل."],["cal","احجز وانطلق","اختر الموعد، ونحن نهتم بالباقي."]]}}
FAQI=["tag","doc","cal","mag","chat","clock"]
FAQ={"en":{"h":"Common questions","q":[
["How do I get a price?","Prices depend on your vehicle and the part. Send us your request in the chat or call us, and we confirm price and availability with you. We do not post prices online."],
["What do you need to give me a quote?","Your vehicle year, make and model, or the 17-character VIN, and a short description of what you need."],
["Can I book online?","Yes. Use the Book online button, or start the chat and choose Book online."],
["Do you offer pre-purchase inspections?","Yes. Tell us the car you are thinking of buying and we inspect it before you buy."],
["Which languages do you speak?","English and Arabic. The whole website and the chat are available in both."],
["When are you open?","Monday to Thursday 9:30 AM to 6:00 PM. Friday 9:30 AM to 12:00 PM and 2:00 to 6:00 PM, with a break for Friday prayer. Saturday 9:30 AM to 4:00 PM. Closed Sunday. The chat takes your request at any hour and we reply when we open."]]},
"ar":{"h":"أسئلة شائعة","q":[
["كيف أعرف السعر؟","السعر يعتمد على سيارتك والقطعة. أرسل طلبك في الشات أو اتصل بنا ونؤكد لك السعر والتوفر. لا ننشر الأسعار على الموقع."],
["ماذا تحتاجون لتعطوني عرض سعر؟","سنة وماركة وموديل السيارة أو رقم الشاسيه (17 خانة)، ووصف قصير لما تحتاجه."],
["هل أستطيع الحجز عبر الإنترنت؟","نعم. استخدم زر احجز عبر الإنترنت، أو ابدأ المحادثة واختر الحجز."],
["هل تقدمون فحصًا قبل شراء السيارة؟","نعم. أخبرنا بالسيارة التي تفكر بشرائها ونفحصها لك قبل الشراء."],
["ما اللغات التي تتحدثونها؟","العربية والإنجليزية. الموقع كله والشات متاحان باللغتين."],
["متى ساعات العمل؟","الاثنين إلى الخميس 9:30 ص إلى 6:00 م. الجمعة 9:30 ص إلى 12:00 ظهرًا ثم 2:00 إلى 6:00 م مع استراحة لصلاة الجمعة. السبت 9:30 ص إلى 4:00 م. الأحد مغلق. الشات يستقبل طلبك في أي ساعة ونرد عند فتح الورشة."]]}}
CSS = open("style.css").read()
JS = open("app.js").read()
for k,c in C.items():
    cards=""
    for key,t,d,b in c["choices"]:
        img = f'<img src="../img/{IMG[key]}" alt="" loading="lazy">' if IMG[key] else '<div class="ph" style="background:linear-gradient(135deg,{CLR[key]},#0B1F3A)"><i></i></div>'
        cards += f'<article class="card" id="{key}" style="--c:{CLR[key]}"><div class="im">{img}</div><div class="bd"><h3>{t}</h3><p>{d}</p><button class="go" data-k="{key}">{b}</button></div></article>'
    k=[x for x in C if C[x] is c][0]
    faqhtml='<div class="fqg">'+''.join(f'<details><summary>{ico(FAQI[n])}<span>{q}</span></summary><p>{a}</p></details>' for n,(q,a) in enumerate(FAQ[k]['q']))+'</div>'
    howhtml='<ol class="how">'+''.join(f'<li>{ico(i_,"hi")}<b><em>{n+1}</em> {t}</b><span>{d}</span></li>' for n,(i_,t,d) in enumerate(HOW[k]['s']))+'</ol>'
    xphtml=''.join(f'<h3 class="xg">{g}</h3><div class="xp">'+''.join(f'<div class="xc">{ico(ic,"xi")}<div><b>{co}</b>'+(('<span class="br">'+''.join(f'<i>{b}</i>' for b in brs)+'</span>') if brs else '')+f'<small>{role}</small></div></div>' for ic,co,brs,role in items)+'</div>' for g,items in ABOUT[k]['g'])
    R=K.get("reels",[])
    REELS=('<section class="reels"><h2>'+UI[k]["reels"]+'</h2><div class="rl">'+"".join(f'<a href="{r["url"]}" target="_blank" rel="noopener"><b>{r["platform"]}</b><span>{r.get("title_"+k) or r.get("title_en","")}</span></a>' for r in R)+'</div></section>') if R else ""
    nav = "".join(f'<a href="#{a}" class="nv" data-k="{a}">{n}</a>' for a,n in zip(["services","parts","tires","book"],c["nav"]))
    html = f'''<!doctype html><html lang="{c["lang"]}" dir="{c["dir"]}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{c["title"]}</title><meta name="description" content="{c["desc"]}">
<link rel="alternate" hreflang="en" href="https://mmautocenter.ca/en/"><link rel="alternate" hreflang="ar" href="https://mmautocenter.ca/ar/"><link rel="alternate" hreflang="x-default" href="https://mmautocenter.ca/en/">
<style>{CSS}</style><script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQ[k]["q"]]},ensure_ascii=False)}</script></head><body>
<div class="topbar"><span id="ost" data-open="{UI[k]["open"]}" data-closed="{UI[k]["closed"]}"></span><a href="https://www.google.com/maps/dir/?api=1&amp;destination=1765+Shawson+Dr+Unit+14+Mississauga+ON" target="_blank" rel="noopener">{c["addr"]}</a><a href="tel:+16474480876">(647) 448-0876</a></div>
<header><a class="logo" href="./"><img src="/img/logo-white.svg" alt="M&amp;M Auto Center - Family since 1952" width="46" height="50"><span class="lt">M&amp;M <span>Auto Center</span></span></a><nav>{nav}<a href="#about">{ABOUT[k]["nav"]}</a></nav><a class="lang" href="../{c["other"]}/" data-lang="{c["other"]}">{c["other_label"]}</a></header>
<section class="hero"><div class="hero-in"><p class="tag">{c["tagline"]}</p><h1>{c["h1"]}</h1><p class="sub">{c["sub"]}</p>
<div class="cta"><button class="go big" data-k="book">{c["cta"]}</button><a class="call" href="tel:+16474480876">{c["call"]}</a></div></div>
<img class="hero-img" src="../img/hero.png" alt=""></section>
<main><div class="grid">{cards}</div><p class="note">{c["note"]}</p>
<p class="rate"><a href="https://www.google.com/maps/search/?api=1&amp;query=M%26M+Auto+Center+1765+Shawson+Dr+Unit+14+Mississauga" target="_blank" rel="noopener">&#9733; {RT[k]}</a> · <a class="rv" href="{K["business"]["review_url"]}" target="_blank" rel="noopener">{UI[k]["review"]}</a></p>{REELS}
<section class="own"><div class="av2" aria-hidden="true">M</div><div><h2>{OWN[k]["h"]}</h2><p>{OWN[k]["p"]}</p><button class="go" data-k="book">{OWN[k]["b"]}</button><small>{OWN[k]["n"]}</small></div></section>
<section class="about" id="about"><figure><img src="/img/family-1952.jpg" alt="{ABOUT[k]["cap"]}" loading="lazy" width="1600" height="1148"><figcaption>{ABOUT[k]["cap"]}</figcaption></figure><div><h2>{ABOUT[k]["h"]}</h2><p>{ABOUT[k]["p"]}</p><details class="xpd"><summary>{ABOUT[k]["more"]}</summary>{xphtml}</details></div></section><section class="tl" aria-label="{ABOUT[k]["th"]}"><h2>{ABOUT[k]["th"]}</h2><ol><i class="tlbar"><i></i></i>{"".join(f'<li style="--d:{n}">{ico(ic,"tli")}<b>{y}</b><strong>{c}</strong><span>{t}</span></li>' for n,(y,c,t,ic) in enumerate(ABOUT[k]["m"]))}</ol></section>
<section class="faq"><h2>{HOW[k]["h"]}</h2>{howhtml}<h2>{FAQ[k]["h"]}</h2>{faqhtml}</section></main>
<footer><div>{c["addr"]}</div><div>(647) 448-0876</div><div>{c["foot"]}</div><div class="priv">{c["priv"]}</div></footer>
<nav class="dock" aria-label="quick actions"><a href="tel:+16474480876">&#128222;<span>{UI[k]["call"]}</span></a><a href="https://www.google.com/maps/dir/?api=1&amp;destination=1765+Shawson+Dr+Unit+14+Mississauga+ON" target="_blank" rel="noopener">&#128205;<span>{UI[k]["dir"]}</span></a><a href="https://waze.com/ul?q=1765%20Shawson%20Dr%20Mississauga&amp;navigate=yes" target="_blank" rel="noopener">&#128663;<span>{UI[k]["waze"]}</span></a><button type="button" class="dkc" data-k="welcome">&#128172;<span>{UI[k]["chat"]}</span></button><a href="{K["business"]["booking_url"]}" target="_blank" rel="noopener">&#128197;<span>{UI[k]["book"]}</span></a></nav>
<button id="fab" type="button" aria-label="{c["chat_title"]}"><svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/><path d="M8.5 11h.01M12 11h.01M15.5 11h.01" stroke-width="2.6"/></svg></button><aside id="chat" hidden><div class="ch"><span class="av"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="8" width="16" height="12" rx="3"/><path d="M12 4v4M9 14h.01M15 14h.01"/></svg></span><div class="tt"><b>{c["chat_title"]}</b><small><i></i>{c["online"]}</small></div><button id="mn" aria-label="minimize">&#8722;</button><button id="x" aria-label="{c["close"]}">&times;</button></div><div id="vc" hidden></div><div id="pg" hidden><i></i></div><div id="log"></div>
<form id="f"><input id="m" placeholder="{c["ph"]}" autocomplete="off"><button aria-label="{c["send"]}"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2"><path d="m22 2-7 20-4-9-9-4zM22 2 11 13"/></svg></button></form></aside>
<script>const HELLO={json.dumps(c["chat_hello"],ensure_ascii=False)};const T={json.dumps(TT[k],ensure_ascii=False)};const LANG="{k}";const HRS={json.dumps(K["hours"])};const TZ="{K["business"]["timezone"]}";const BOOK="{K["business"]["booking_url"]}";const INTAKE="{K["business"].get("intake_url","")}";{JS}</script></body></html>'''
    open(f"{k}/index.html","w",encoding="utf-8").write(html)
open("index.html","w").write('<!doctype html><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=en/"><a href="en/">English</a> · <a href="ar/">العربية</a>')
