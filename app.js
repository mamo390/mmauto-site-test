(function(){
var SB="https://wzfdeihefnobnnoafajd.supabase.co",KEY="sb_publishable_FkP47Keqd7iduzuGVwms5g_QHXTZkI_";
var ARI=BOOK;
var ADDR=encodeURIComponent("1765 Shawson Dr Unit 14, Mississauga, ON L4W 1N8");var MAP="https://www.google.com/maps/search/?api=1&query="+ADDR;var DIR="https://www.google.com/maps/dir/?api=1&destination="+ADDR;
var SRC=(function(){try{var s=new URLSearchParams(location.search).get("src")||"chat";return /^[a-z0-9_-]{1,20}$/i.test(s)?s:"chat"}catch(e){return "chat"}})();
var LIVE=/(^|\.)mmautocenter\.ca$/.test(location.hostname),STAGE=/\.github\.io$/.test(location.hostname),PROD=LIVE||STAGE;
var chat=document.getElementById('chat'),log=document.getElementById('log'),inp=document.getElementById('m'),form=document.getElementById('f');
var sid=(window.crypto&&crypto.randomUUID)?crypto.randomUUID():"00000000-0000-4000-8000-"+Date.now().toString(16).padStart(12,"0").slice(-12);
var S={step:"idle",flow:"",d:{}};
function openNow(){try{var p={};new Intl.DateTimeFormat('en-CA',{timeZone:TZ,weekday:'short',hour:'2-digit',minute:'2-digit',hour12:false}).formatToParts(new Date()).forEach(function(x){p[x.type]=x.value});var h=HRS[p.weekday];if(!h)return false;var n=(+p.hour%24)*60+ +p.minute,R=typeof h[0]==='string'?[h]:h;return R.some(function(r){var a=r[0].split(':'),z=r[1].split(':');return n>=(+a[0])*60+ +a[1]&&n<(+z[0])*60+ +z[1]})}catch(e){return true}}
function el(t,c,x){var e=document.createElement(t);if(c)e.className=c;if(x!=null)e.textContent=x;return e}
function scroll(){log.scrollTop=log.scrollHeight}
function bot(t){log.appendChild(el('div','b',t));scroll()}
function user(t){log.appendChild(el('div','u',t));scroll()}
var IC={services:'<path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4L15 12l-3-3z"/>',repair:'<path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4L15 12l-3-3z"/>',parts:'<circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/>',tires:'<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="4"/><path d="M12 2v4M12 18v4M2 12h4M18 12h4"/>',book:'<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',hours:'<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',loc:'<path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',cb:'<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>'};IC.call=IC.cb;IC.battery='<rect x="2" y="7" width="18" height="11" rx="2"/><path d="M22 11v3M7 10v5M11 12.5h-4"/>';IC.prepurchase='<path d="M9 11l3 3 8-8"/><path d="M20 12v7a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h9"/>';IC.diag='<circle cx="12" cy="12" r="10"/><path d="M9.1 9a3 3 0 0 1 5.8 1c0 2-3 3-3 3M12 17h.01"/>';IC.swap='<path d="M17 1l4 4-4 4"/><path d="M3 11V9a4 4 0 0 1 4-4h14M7 23l-4-4 4-4"/><path d="M21 13v2a4 4 0 0 1-4 4H3"/>';IC.changeover=IC.swap;IC.tire=IC.tires;IC.rim=IC.tires;IC.both=IC.tires;
function ico(k){return IC[k]?'<svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">'+IC[k]+'</svg>':''}
function chips(list){var w=el('div','chips');list.forEach(function(c){var b=el('button','chip'+(c[0]==='book'?' gold':'')+((c[0]==='cb'||c[0]==='call')?' green':''));b.innerHTML=ico(c[0])+'<span></span>';b.lastChild.textContent=c[1];b.type='button';b.onclick=function(){w.remove();user(c[1]);c[2]?c[2]():0};w.appendChild(b)});log.appendChild(w);scroll()}
function link(label,href){var a=el('a','chip lk',label);a.addEventListener('click',function(){track(href.indexOf('tel:')===0?'call_click':href===ARI?'book_click':'step',S.flow,'link')});a.href=href;a.target='_blank';a.rel='noopener';log.appendChild(a);scroll()}
function home(){chips(T.chips_home.map(function(c){return [c[0],c[1],function(){start(c[0])}]}))}
var P=(function(){try{var m=JSON.parse(localStorage.getItem('mm')||'{}');return m.keep===1&&m.p?m.p:{}}catch(e){return {}}})();
function mem(){try{return JSON.parse(localStorage.getItem('mm')||'{}')}catch(e){return {}}}
function setMem(o){try{localStorage.setItem('mm',JSON.stringify(o))}catch(e){}}
function vid(){var m=mem();if(!m.vid){m.vid=(window.crypto&&crypto.randomUUID)?crypto.randomUUID():"00000000-0000-4000-8000-"+Date.now().toString(16).padStart(12,"0").slice(-12);setMem(m)}return m.vid}
var DNT=(navigator.doNotTrack==="1"||window.doNotTrack==="1");
function track(ev,flow,step,detail){
 if(!PROD||DNT)return;
 var slug=function(x){return x&&/^[a-z0-9_]{1,40}$/.test(x)?x:null};
 try{fetch(SB+"/rest/v1/chat_events",{method:"POST",keepalive:true,headers:{"Content-Type":"application/json",apikey:KEY,Authorization:"Bearer "+KEY,Prefer:"return=minimal"},
  body:JSON.stringify({visitor_id:vid(),session_id:sid,lang:LANG,src:(LIVE?SRC.toLowerCase():"test"),event:ev,flow:slug(flow),step:slug(step),detail:slug(detail),shop_open:openNow()})}).catch(function(){})}catch(e){}
}

var vc=document.getElementById('vc'),pg=document.getElementById('pg');
var PCT={mileage:60,dtc:70,vehicle2:50,want:25,part:25,size:25,symptom:25,vehicle:50,name:75,phone:90};
function prog(step){var p=PCT[step];if(!p){pg.hidden=true;return}pg.hidden=false;pg.firstChild.style.width=p+'%';pg.setAttribute('aria-label',T.stepLbl.replace('{p}',p))}
function pin(){var d=S.d,v=d.veh,txt=v?[v.year,v.make,v.model].filter(Boolean).join(' '):'';if(!txt){vc.hidden=true;return}vc.hidden=false;vc.innerHTML='';var i=el('span','vi','\u2713');vc.appendChild(i);vc.appendChild(el('span','vt',txt))}
function ask(step,q){var d=S.d;
 if(step==="name"&&P.name&&P.phone&&d.service){d.name=P.name;d.phone=P.phone;bot(T.known.replace("{n}",P.name));S.step="saving";return save()}
 if(step==="vehicle"&&P.veh&&!d.veh&&!S.vehAsked){S.vehAsked=1;var vt=[P.veh.year,P.veh.make,P.veh.model].filter(Boolean).join(" ");bot(T.same_veh.replace("{v}",vt));return chips([["yes",T.yes,function(){d.veh=P.veh;d.vin=P.vin||null;d.vehText=P.vehText||vt;pin();afterVeh()}],["other",T.other,function(){ask("vehicle",q)}]])}
 S.step=step;track('step',S.flow||S.d.service,step);prog(step);pin();bot(q);inp.focus()}
function afterVeh(){var d=S.d;if(d.service==="diagnosis")return ask("mileage",T.q_mileage);if(d.service==="pre_purchase_inspection")return ask("mileage",T.q_mileage_buy);if(d.service==="car_valuation_sell")return ask("mileage",T.q_mileage);if(d.service==="car_valuation_buy")return ask("mileage",T.q_mileage_buy);ask("name",T.q_name)}
function cool(t){if(!S.cool&&/radiat|a\/c|\bac\b|air ?con|compressor|condenser|coolant|رادياتير|ردياتير|راديتر|تكييف|مكيف|التكييف|كمبريسور|كمبروسر/i.test(t||"")){S.cool=1;track("lifetime_note",S.flow);bot(T.lifetime)}}
function start(k){
 S={step:"idle",flow:k,d:{}};track('flow_start',k);if(k==="ac")cool("ac");
 if(k==="hours"){bot(T.hours);bot(openNow()?T.open_now:T.closed_now);return home()}
 if(k==="loc"){bot(T.loc);link(T.map,MAP);link(T.dir,DIR);return home()}
 if(k==="book"){bot(T.book_msg);link(T.book_btn,ARI);chips([["cb",T.callback,function(){track('callback_click','book');S.flow="callback";S.d.service="appointment";ask("vehicle",T.q_vehicle)}],["call",T.call,function(){track('call_click',S.flow);location.href="tel:+16474480876"}]]);return}
 if(k==="battery"){S.d.service="battery";ask("vehicle",T.q_battery);return}
 if(k==="prepurchase"){S.d.service="pre_purchase_inspection";ask("vehicle",T.q_buy);return}
 if(k==="diag"){S.d.service="diagnosis";ask("symptom",T.q_symptom);return}
 if(k==="used"){bot(T.used_intro);return chips([["used",T.used_buy,function(){S.d.service="used_car_inquiry";ask("want",T.q_used)}],["used",T.used_sell,function(){S.d.service="car_valuation_sell";ask("vehicle",T.q_vehicle)}],["used",T.used_price,function(){S.d.service="car_valuation_buy";ask("vehicle",T.q_vehicle)}]])}
 if(k==="services"){bot(T.q_service);function pick(c){return [c[0],c[1],function(){if(c[2]==="more"){return chips(T.svc_rest.map(pick))}if(c[2]==="tires")return start("tires");if(c[2]!=="vehicle")return start(c[2]);S.d.service=c[0];if(c[0]==="other")return ask("symptom",T.q_symptom);ask("vehicle",T.q_vehicle)}]}chips(T.svc_top.map(pick));return}
 if(k==="parts"){S.d.service="parts";ask("part",T.q_part);return}
 if(k==="tires"){bot(T.q_kind);chips(T.kinds.map(function(c){return [c[0],c[1],function(){if(c[0]==="swap"||c[0]==="changeover"){S.d.service="tire_"+c[0];S.d.part=c[1];return ask("vehicle",T.q_vehicle)}S.d.service=c[0]==="rim"?"rims":"tires";S.d.kind=c[0];ask("size",T.q_size)}]}));return}
}
var fab=document.getElementById('fab');
function openFlow(k){track('chat_open',k);chat.hidden=false;fab.hidden=true;log.innerHTML='';vc.hidden=true;pg.hidden=true;var m=mem();m.visits=(m.visits||0)+1;setMem(m);bot(HELLO.welcome);var FL={services:1,parts:1,tires:1,book:1};if(k!=='welcome'&&!FL[k]&&HELLO[k])bot(HELLO[k]);if(P.name&&mem().keep===1)bot(T.welcome_back.replace('{n}',P.name));if(k==="services"||k==="parts"||k==="tires"||k==="book")start(k);else home()}
function vinDecode(v){return fetch("https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVinValues/"+v+"?format=json").then(function(r){return r.json()}).then(function(j){var r=(j.Results||[])[0]||{};return r.Make?{year:r.ModelYear,make:r.Make,model:r.Model}:null}).catch(function(){return null})}
function urgency(t){return new RegExp(T.intent_words.urgent,"i").test(t)?"high":"low"}
function save(){
 var d=S.d,m=mem(),v=d.veh||{};if(d.phone&&d.vin&&d.vin.length===17&&!S.greeted){fetch(SB+"/rest/v1/rpc/check_returning",{method:"POST",headers:{"Content-Type":"application/json",apikey:KEY,Authorization:"Bearer "+KEY},body:JSON.stringify({p_phone:d.phone,p_vin:d.vin})}).then(function(r){return r.ok?r.json():null}).then(function(x){if(x&&x.known&&x.first_name){S.greeted=1;track('returning_customer',S.flow);bot(T.welcome_back.replace("{n}",x.first_name)+" \ud83d\udc4b")}}).catch(function(){})}P={name:d.name,phone:d.phone,veh:d.veh||P.veh,vin:d.vin||P.vin,vehText:d.vehText||P.vehText};
 var row={name:d.name,phone:d.phone,service_type:d.service||"other",vehicle_year:v.year||null,vehicle_make:v.make||null,vehicle_model:v.model||null,vin:d.vin||null,
  message:(d.want?("Looking for: "+d.want+" | "):"")+(d.symptom?("Symptoms: "+d.symptom+" | "):"")+(d.part?("Part: "+d.part+" | "):"")+(d.mileage?("Mileage: "+d.mileage+" | "):"")+(d.dtc?("Codes: "+d.dtc+" | "):"")+(d.vehText?("Vehicle: "+d.vehText):""),intent:/^(parts|tires|rims)$/.test(d.service)?"parts_inquiry":"appointment",
  urgency_level:urgency((d.part||"")+" "+(d.symptom||"")+" "+(d.vehText||"")),segment:(m.visits||1)>=5?"loyal":(m.visits||1)>=2?"returning":"new",session_id:sid,status:"new",
  source:/^(parts|tires|rims)$/.test(d.service)?"chatbot_parts":"chatbot_booking",notes:"lang="+LANG+(LIVE?"":" test")};
 if(!PROD){bot(T.done);if(!openNow())bot(T.closed_note);bot(T.test);after();return}
 row.notes+=" src="+SRC;var url=INTAKE||(SB+"/rest/v1/leads");if(INTAKE){delete row.status}
 fetch(url,{method:"POST",headers:{"Content-Type":"application/json",apikey:KEY,Authorization:"Bearer "+KEY,Prefer:"return=minimal"},body:JSON.stringify(row)})
 .then(function(r){if(!r.ok)throw 0;return INTAKE?r.json():{status:"created"}}).then(function(x){track('lead_saved',S.flow,null,d.service);if(x.status==="updated")bot(T.done_more);else bot(T.done);if(!openNow())bot(T.closed_note);after()}).catch(function(){track('lead_error',S.flow);bot(T.fail);link(T.call,"tel:+16474480876")})
}
function persistP(){var m=mem();m.keep=1;m.p=P;setMem(m)}
function after(){S.step="idle";prog("idle");link(T.book_btn,ARI);var m=mem();
 if(m.keep===1){persistP();bot(T.again);home();return chips([["forget",T.forget,function(){var q=mem();delete q.p;delete q.keep;q.keep=0;setMem(q);P={};bot(T.forgot)}]])}
 if(m.keep===undefined&&P.name&&P.phone){bot(T.keep_q);return chips([["yes",T.keep_yes,function(){persistP();bot(T.kept);bot(T.again);home()}],["no",T.keep_no,function(){var q=mem();q.keep=0;setMem(q);bot(T.again);home()}]])}
 bot(T.again);home()}
function handle(t){
 var d=S.d;
 if(S.step==="size"){d.part=(d.kind==="rim"?"Rims: ":d.kind==="both"?"Tires+rims: ":"Tires: ")+t;if(d.kind==="rim"){return ask("vehicle",T.q_vehicle)}bot(T.q_season);return chips(T.seasons.map(function(c){return [c[0],c[1],function(){d.part+=" | "+c[1];ask("vehicle",T.q_vehicle)}]}))}
 if(S.step==="part"){d.part=t;cool(t);return ask("vehicle",T.q_vehicle)}
 if(S.step==="want"){d.want=t.slice(0,300);return ask("name",T.q_name)}
 if(S.step==="symptom"){d.symptom=t.slice(0,500);cool(t);return ask("vehicle",T.q_vehicle)}
 if(S.step==="vehicle"){d.vehText=t;var vin=t.replace(/\s/g,"").toUpperCase();
  if(/^[A-HJ-NPR-Z0-9]{17}$/.test(vin)){d.vin=vin;return vinDecode(vin).then(function(r){if(r&&r.year&&r.make&&r.model){track('vin_ok',S.flow);d.veh=r;bot(T.vin_ok+" "+[r.year,r.make,r.model].join(" "));afterVeh()}else{track('vin_fail',S.flow);bot(T.vin_fail);ask("vehicle2",T.q_vehicle2)}})}
  var p=t.match(/^(\d{4})\s+(\S+)\s*(.*)$/);if(p)d.veh={year:p[1],make:p[2],model:p[3]};return afterVeh()}
 if(S.step==="vehicle2"){d.vehText=(d.vin?d.vin+" | ":"")+t;var q=t.match(/^(\d{4})\s+(\S+)\s*(.*)$/);if(q)d.veh={year:q[1],make:q[2],model:q[3]};return afterVeh()}
 if(S.step==="mileage"){d.mileage=t.replace(/[^\w\s.,]/g,"").slice(0,20);if(d.service==="diagnosis"){ask("dtc",T.q_dtc);return chips([["skip",T.skip,function(){ask("name",T.q_name)}]])}return ask("name",T.q_name)}
 if(S.step==="dtc"){var cs=(t.toUpperCase().match(/[PBCU][0-3][0-9A-F]{3}/g)||[]).slice(0,5);d.dtc=cs.join(", ")||t.slice(0,40);return ask("name",T.q_name)}
 if(S.step==="name"){d.name=t.slice(0,80);return ask("phone",T.q_phone)}
 if(S.step==="phone"){if(t.replace(/\D/g,"").length<10){bot(T.bad_phone);return}d.phone=t.slice(0,30);S.step="saving";return save()}
 var w=T.intent_words,x=t;
 function m(k){return new RegExp(w[k],"i").test(x)}
 if(m("hours"))return start("hours");if(m("loc"))return start("loc");if(m("book"))return start("book");if(m("insp"))return start("prepurchase");if(m("battery"))return start("battery");if(m("parts"))return start("parts");
 if(m("price")){bot(T.price);return start("services")}
 bot(T.fallback);home();link(T.call,"tel:+16474480876")
}
form.onsubmit=function(e){e.preventDefault();var t=inp.value.trim();if(!t)return;inp.value='';user(t);handle(t)};
document.querySelectorAll('.go').forEach(function(b){b.onclick=function(){openFlow(b.dataset.k)}});document.querySelectorAll('nav .nv').forEach(function(a){a.onclick=function(){openFlow(a.dataset.k)}});
document.getElementById('x').onclick=function(){track('chat_close',S.flow,S.step);chat.hidden=true;fab.hidden=false};fab.onclick=function(){if(log.children.length){chat.hidden=false;fab.hidden=true;inp.focus()}else openFlow('welcome')};document.getElementById('mn').onclick=function(){chat.classList.toggle('min')};
log.setAttribute('aria-live','polite');track('page_view');
try{document.querySelectorAll('.lang').forEach(function(a){a.addEventListener('click',function(){localStorage.setItem('lang',a.dataset.lang)})})}catch(e){}
(function(){try{var c=document.getElementById('chat');new MutationObserver(function(){document.body.classList.toggle('chat-open',!c.hidden)}).observe(c,{attributes:true,attributeFilter:['hidden']});var s=c.querySelector('.ch small');if(s&&!openNow()){s.className='off';s.lastChild.textContent=LANG==='ar'?'خارج ساعات العمل - اترك رسالتك':'Away - leave a message'}if(/[?&]theme=blue/.test(location.search))document.body.classList.add('th-blue')}catch(e){}})();
})();
