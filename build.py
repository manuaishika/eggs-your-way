#!/usr/bin/env python3
"""Assembles the pages so the nav and footer stay identical everywhere."""

from urllib.parse import quote

PHONE = "919599327947"


def wa(text):
    return "https://wa.me/%s?text=%s" % (PHONE, quote(text))


WA = wa("Hi! I'd like to order eggs.")

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="favicon.png">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Karla:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>

<header class="bar">
  <div class="wrap bar-in">
    <a class="mark" href="index.html">
      <img src="logo.png" alt="Eggs Your Way">
      <span>Eggs Your Way</span>
    </a>
    <nav>
      <a href="index.html"{c_home}>Home</a>
      <a href="shop.html"{c_shop}>Shop</a>
      <a href="why-it-works.html"{c_why}>Why it works</a>
      <a href="recipes.html"{c_recipes}>Recipes</a>
      <a href="business.html"{c_business}>For Business</a>
      <a href="about.html"{c_about}>About</a>
      <a href="contact.html"{c_contact}>Contact</a>
    </nav>
  </div>
</header>

<main>
"""

FOOT = """</main>

<footer>
  <div class="wrap foot-in">
    <div>
      <h3>Eggs Your Way</h3>
      <p>Pasteurised shell eggs and liquid egg, delivered across Gurugram.</p>
    </div>
    <div>
      <p><a href="https://wa.me/919599327947">+91 95993 27947</a></p>
      <p><a href="mailto:eggzurway@gmail.com">eggzurway@gmail.com</a></p>
      <p>Orders taken 9am to 7pm, Monday to Saturday.</p>
    </div>
    <nav>
      <a href="index.html">Home</a>
      <a href="shop.html">Shop</a>
      <a href="why-it-works.html">Why it works</a>
      <a href="recipes.html">Recipes</a>
      <a href="business.html">For Business</a>
      <a href="about.html">About</a>
      <a href="contact.html">Contact</a>
    </nav>
  </div>
  <div class="wrap"><p class="foot-note"><a href="about.html#certifications">Certifications</a> &middot; &copy; <span id="yr">2026</span> Eggs Your Way</p></div>
</footer>
<script>document.getElementById('yr').textContent=new Date().getFullYear();</script>
{extra}
</body>
</html>
"""

CURVE = """    <svg class="curve" viewBox="0 0 1440 100" preserveAspectRatio="none" aria-hidden="true">
      <path d="M0 26 C400 112 1040 112 1440 26 L1440 100 L0 100 Z" fill="#E9F5FC"/>
    </svg>"""

ARC = """<svg class="arc" viewBox="0 0 240 16" aria-hidden="true"><path d="M8 12 Q120 -3 232 12" fill="none" stroke="currentColor" stroke-width="7" stroke-linecap="round"/></svg>"""

EGG = "M48 7C65 7 79 31 79 52c0 20-14 37-31 37S17 72 17 52C17 31 31 7 48 7Z"


def egg_icon(cid, label, fill=None, level=None, wave_stroke=None, highlight=False):
    """One egg outline, optionally holding liquid."""
    out = ['<svg viewBox="0 0 96 96" role="img" aria-label="%s">' % label]
    if fill:
        out.append('<defs><clipPath id="%s"><path d="%s"/></clipPath></defs>' % (cid, EGG))
    out.append('<path d="%s" fill="#fff"/>' % EGG)
    if fill:
        wave = "M6 %dc11-8 21 8 32 0s21-8 32 0 21 6 32 0v%d H6Z" % (level, 96 - level + 6)
        out.append('<g clip-path="url(#%s)"><path d="%s" fill="%s"/>' % (cid, wave, fill))
        if wave_stroke:
            out.append('<path d="M6 %dc11-8 21 8 32 0s21-8 32 0 21 6 32 0" fill="none" stroke="%s" stroke-width="4"/>'
                       % (level, wave_stroke))
        out.append('</g>')
    out.append('<path d="%s" fill="none" stroke="#105E82" stroke-width="5"/>' % EGG)
    if highlight:
        out.append('<path d="M32 34c4-8 12-12 19-11" fill="none" stroke="#84C8EE" stroke-width="5" stroke-linecap="round"/>')
    out.append('</svg>')
    return "".join(out)


BOTTLE = ("M30 22h36c3 0 5 2 6 5l4 14c1 5 2 10 2 15v26c0 6-5 11-11 11H29"
          "c-6 0-11-5-11-11V56c0-5 1-10 2-15l4-14c1-3 3-5 6-5Z")


def bottle_icon(cid, label, fill, level=50, top_stroke=None):
    """A cute little bottle, filled to `level` (lower number = fuller)."""
    out = ['<svg viewBox="0 0 96 96" role="img" aria-label="%s">' % label]
    out.append('<defs><clipPath id="%s"><path d="%s"/></clipPath></defs>' % (cid, BOTTLE))
    out.append('<rect x="40" y="6" width="16" height="10" rx="3" fill="#105E82"/>')
    out.append('<rect x="43" y="14" width="10" height="8" fill="#fff" stroke="#105E82" stroke-width="4"/>')
    out.append('<path d="%s" fill="#fff"/>' % BOTTLE)
    out.append('<g clip-path="url(#%s)"><rect x="14" y="%d" width="68" height="80" fill="%s"/>' % (cid, level, fill))
    if top_stroke:
        out.append('<rect x="14" y="%d" width="68" height="3" fill="%s"/>' % (level, top_stroke))
    out.append('</g>')
    out.append('<rect x="20" y="58" width="56" height="8" fill="#105E82" opacity=".1"/>')
    out.append('<path d="%s" fill="none" stroke="#105E82" stroke-width="5"/>' % BOTTLE)
    out.append('<path d="M34 30c-2 6-3 12-3 18" fill="none" stroke="#84C8EE" stroke-width="4" stroke-linecap="round"/>')
    out.append('</svg>')
    return "".join(out)


ICONS = {
 "cake": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20.5h16"/><path d="M5.5 20.5v-6a2 2 0 012-2h9a2 2 0 012 2v6"/><path d="M12 12.5V9.5"/><path d="M12 7.8c.9-.9.6-1.9 0-2.5-.6.6-.9 1.6 0 2.5Z"/></svg>',
 "cup":  '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4.5 9h11v6.5a4 4 0 01-4 4h-3a4 4 0 01-4-4V9Z"/><path d="M15.5 10.5h2a2.6 2.6 0 010 5.2h-2"/><path d="M7.5 3.5v2M11.5 3v2.5"/></svg>',
 "pan":  '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9.5" cy="13.5" r="6.2"/><path d="M15.4 11.2l5.4-3.4"/><circle cx="9.5" cy="13.5" r="2.1" fill="currentColor" stroke="none"/></svg>',
 "shaker":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 3.2h6v2.6l1.1 2.2v11a2 2 0 01-2 2h-5.2a2 2 0 01-2-2v-11L8 5.8V3.2Z"/><path d="M7.9 12.4h8.2"/></svg>',
}


NAV_KEYS = ("home", "shop", "why", "recipes", "business", "about", "contact")


def page(name, title, desc, body, extra="", filename=None):
    cur = {k: "" for k in NAV_KEYS}
    if name in cur:
        cur[name] = ' aria-current="page"'
    fmt = {"c_" + k: v for k, v in cur.items()}
    html = HEAD.format(title=title, desc=desc, **fmt)
    html += body
    html += FOOT.format(extra=extra)
    fn = filename or (name + ".html")
    open(fn, "w", encoding="utf-8").write(html)
    print("wrote", fn)


# ----------------------------------------------------------------- home
home = """
  <div class="sky-panel hero">
    <div class="wrap">
      <img class="hero-logo" src="logo.png" alt="Eggs Your Way logo: bold lettering inside an egg with a yolk trailing speed lines">
      <h1>Eggs you can eat raw. And eggs you can pour.</h1>
      <div class="hero-cta">
        <a class="btn btn-yolk" href="%(wa)s" target="_blank" rel="noopener">Order on WhatsApp</a>
        <a class="btn btn-plain" href="why-it-works.html">See why it works</a>
      </div>
    </div>
%(curve)s
  </div>

  <section id="range">
    <div class="wrap">
      <div class="head">
        %(arc)s
        <h2>What we make</h2>
        <p>Four things, done properly. Every pack is pasteurised before it leaves us.</p>
      </div>
      <div class="range">
        <article class="egg-card">%(i1)s
          <h3>Pasteurised shell eggs</h3>
          <p>Ordinary eggs, heat-treated in the shell. Crack them into tiramisu or a shake without a second thought.</p>
        </article>
        <article class="egg-card">%(i2)s
          <h3>Liquid whole egg</h3>
          <p>Cracked, blended and pasteurised. One litre pours about twenty eggs, no shells.</p>
        </article>
        <article class="egg-card">%(i3)s
          <h3>Liquid egg white</h3>
          <p>Just the whites, ready to whisk. For meringue, omelettes, and anyone counting protein.</p>
        </article>
        <article class="egg-card">%(i4)s
          <h3>Liquid egg yolk</h3>
          <p>Only yolks, deep and rich. For custard, ice cream bases and a glossy carbonara.</p>
        </article>
      </div>
      <div style="text-align:center;margin-top:30px">
        <a class="btn btn-plain" href="shop.html">See the full shop</a>
      </div>
    </div>
  </section>

  <section class="on-sky">
    <div class="wrap">
      <div class="head">
        <h2>Why pasteurised</h2>
        <p>Warmed just below the point an egg sets &mdash; enough to deal with salmonella, gentle enough to still behave like an egg.</p>
      </div>
      <div class="trio">
        <div class="card">
          <h3>Raw recipes, no gamble</h3>
          <p>Tiramisu, mousse, aioli, cookie dough. The recipes that came with a warning stop being risky.</p>
        </div>
        <div class="card">
          <h3>Safe for everyone at the table</h3>
          <p>Kids, pregnant women, older parents &mdash; anyone can eat what the rest of the family is eating.</p>
        </div>
        <div class="card">
          <h3>Nothing else goes in</h3>
          <p>No preservatives, no colour, no additives. Heat and time do the work.</p>
        </div>
      </div>
    </div>
  </section>

  <section id="reviews">
    <div class="wrap">
      <div class="head">
        %(arc)s
        <h2>What people say</h2>
        <p>Real words from real customers, swapped in as they come in.</p>
      </div>
      <div class="trio">
        <div class="card">
          <p>&ldquo;[A real quote about reliability, freshness, or how it changed a recipe.]&rdquo;</p>
          <p class="cite">[Name], [context &mdash; e.g. home baker in Gurugram]</p>
        </div>
        <div class="card">
          <p>&ldquo;[A real quote from a caf&eacute; or business customer about consistency or convenience.]&rdquo;</p>
          <p class="cite">[Name], [business name]</p>
        </div>
        <div class="card">
          <p>&ldquo;[A real quote from someone using it for raw recipes or protein tracking.]&rdquo;</p>
          <p class="cite">[Name], [context]</p>
        </div>
      </div>
    </div>
  </section>

  <section id="convert">
    <div class="wrap">
      <div class="head">
        %(arc)s
        <h2>How much is that, really?</h2>
        <p>Recipes count eggs, macros count grams, the carton's in millilitres. Here's the sum.</p>
      </div>
      <div class="calc">
        <div>
          <label for="count">I need</label>
          <div class="stepper">
            <button type="button" id="minus" aria-label="One fewer egg">&minus;</button>
            <input id="count" type="number" min="1" max="99" value="3" inputmode="numeric" aria-label="Number of eggs">
            <button type="button" id="plus" aria-label="One more egg">+</button>
          </div>
          <label for="kind" style="margin-top:20px">worth of</label>
          <select id="kind" aria-label="Type of egg">
            <option value="whole">whole eggs</option>
            <option value="white">egg whites</option>
            <option value="yolk">egg yolks</option>
          </select>
        </div>
        <div class="readout">
          <span class="amount" id="amount">150 ml</span>
          <p class="caption" id="caption">of liquid whole egg</p>
          <div class="macros"><span id="pro">19 g protein</span><span id="kcal">215 kcal</span></div>
          <div class="dots" id="dots" aria-hidden="true"></div>
        </div>
      </div>
      <p class="footnote">Based on a large egg: 50 ml whole, 33 ml white, 17 ml yolk.</p>
    </div>
  </section>

  <section id="for">
    <div class="wrap">
      <div class="head">
        <h2>Made for</h2>
        <p>Ordering for a caf&eacute;, hotel or cloud kitchen? <a href="business.html">See our business page</a>.</p>
      </div>
      <div class="for-grid">
        <div class="for-item">
          <div class="blob" aria-hidden="true">%(cake)s</div>
          <h3>Home bakers</h3>
          <p>Pour what you need, seal the rest, carry on tomorrow.</p>
        </div>
        <div class="for-item">
          <div class="blob" aria-hidden="true">%(cup)s</div>
          <h3>Caf&eacute;s and bakeries</h3>
          <p>No cracking, no separating, no bin full of shells at closing.</p>
        </div>
        <div class="for-item">
          <div class="blob" aria-hidden="true">%(pan)s</div>
          <h3>Hotels and cloud kitchens</h3>
          <p>The same volume every service, and a food-safety box already ticked.</p>
        </div>
        <div class="for-item">
          <div class="blob" aria-hidden="true">%(shaker)s</div>
          <h3>Anyone tracking macros</h3>
          <p>Egg white straight into the shaker, measured to the millilitre.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="on-sky">
    <div class="wrap">
      <div class="head">
        <h2>Getting it to you</h2>
      </div>
      <div class="trio">
        <div class="card">
          <h3>Cold the whole way</h3>
          <p>Chilled from the pasteuriser to your door. If it turns up warm, we replace it.</p>
        </div>
        <div class="card">
          <h3>Pack sizes</h3>
          <p>Trays of 6, 12 and 30 for homes. One-kilo pouches and five-kilo boxes for kitchens.</p>
        </div>
        <div class="card">
          <h3>Keeps for weeks</h3>
          <p>Sealed and refrigerated, liquid egg outlasts a fresh crack. The date's on every pack.</p>
        </div>
      </div>
      <div style="text-align:center;margin-top:38px">
        <a class="btn btn-yolk" href="%(wa)s" target="_blank" rel="noopener">Order on WhatsApp</a>
      </div>
    </div>
  </section>

  <section class="on-sky egg-band">
    <div class="wrap">
      <div class="egg-anim" id="eggAnim">
        <svg viewBox="0 0 256 200" aria-hidden="true">
          <defs>
            <clipPath id="yolkClip"><circle cx="136" cy="118" r="40"/></clipPath>
          </defs>
          <path class="egg-white" d="M128 16 C160 12 190 22 208 48 C226 72 222 100 214 118 C228 136 224 160 204 176 C186 190 162 184 140 190 C112 196 80 192 58 172 C34 150 26 122 36 98 C20 82 28 54 54 36 C78 18 104 20 128 16 Z" fill="#fff"/>
          <g class="yolk">
            <circle class="yolk-outline" cx="136" cy="118" r="40" fill="none" stroke="#F0B71E" stroke-width="2" opacity=".35"/>
            <g clip-path="url(#yolkClip)">
              <g class="wave-group">
                <path class="wave-back" d="M-160,0 q10,-8,20,0 q10,8,20,0 q10,-8,20,0 q10,8,20,0 q10,-8,20,0 q10,8,20,0 q10,-8,20,0 q10,8,20,0 q10,-8,20,0 q10,8,20,0 q10,-8,20,0 q10,8,20,0 q10,-8,20,0 q10,8,20,0 q10,-8,20,0 q10,8,20,0 V220 H-160 Z" fill="#F0B71E" opacity=".55"/>
                <path class="wave-front" d="M-160,0 q10,6,20,0 q10,-6,20,0 q10,6,20,0 q10,-6,20,0 q10,6,20,0 q10,-6,20,0 q10,6,20,0 q10,-6,20,0 q10,6,20,0 q10,-6,20,0 q10,6,20,0 q10,-6,20,0 q10,6,20,0 q10,-6,20,0 q10,6,20,0 q10,-6,20,0 V220 H-160 Z" fill="#FFD447"/>
              </g>
              <circle class="bubble" cx="124" cy="148" r="4"/>
              <circle class="bubble" cx="148" cy="150" r="3"/>
              <circle class="bubble" cx="132" cy="142" r="5"/>
              <circle class="bubble" cx="140" cy="146" r="3.5"/>
            </g>
          </g>
        </svg>
      </div>
      <p class="egg-caption">Still just an egg &mdash; pasteurised, not processed.</p>
    </div>
  </section>
""" % dict(
    wa=WA, curve=CURVE, arc=ARC,
    i1=egg_icon("c1", "A whole egg in its shell", highlight=True),
    i2=bottle_icon("c2", "A bottle of liquid whole egg", fill="#FFD447", level=50),
    i3=bottle_icon("c3", "A bottle of liquid egg white", fill="#EDF7FD", level=50, top_stroke="#84C8EE"),
    i4=bottle_icon("c4", "A bottle of liquid egg yolk", fill="#F0B71E", level=34),
    **ICONS)

CALC_JS = """<script>
(function(){
  var data = {
    whole:{ml:50, pro:6.3, kcal:72, name:'of liquid whole egg'},
    white:{ml:33, pro:3.6, kcal:17, name:'of liquid egg white'},
    yolk: {ml:17, pro:2.7, kcal:55, name:'of liquid egg yolk'}
  };
  var count=document.getElementById('count'), kind=document.getElementById('kind'),
      amount=document.getElementById('amount'), caption=document.getElementById('caption'),
      pro=document.getElementById('pro'), kcal=document.getElementById('kcal'),
      dots=document.getElementById('dots');

  function render(){
    var n=parseInt(count.value,10);
    if(isNaN(n)||n<1) n=1;
    if(n>99) n=99;
    count.value=n;
    var d=data[kind.value];
    amount.textContent=(n*d.ml)+' ml';
    caption.textContent=d.name;
    pro.textContent=Math.round(n*d.pro)+' g protein';
    kcal.textContent=Math.round(n*d.kcal)+' kcal';
    amount.classList.remove('pop'); void amount.offsetWidth; amount.classList.add('pop');
    dots.innerHTML='';
    if(n<=12){ for(var i=0;i<n;i++) dots.appendChild(document.createElement('i')); }
  }
  document.getElementById('minus').addEventListener('click',function(){
    count.value=Math.max(1,parseInt(count.value,10)-1); render();
  });
  document.getElementById('plus').addEventListener('click',function(){
    count.value=Math.min(99,parseInt(count.value,10)+1); render();
  });
  count.addEventListener('input',render);
  kind.addEventListener('change',render);
  render();
})();
</script>"""

EGG_JS = """<script>
(function(){
  var el = document.getElementById('eggAnim');
  if(!el) return;
  if('IntersectionObserver' in window){
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(entry){
        if(entry.isIntersecting){
          el.classList.add('in-view');
          io.unobserve(el);
        }
      });
    }, {threshold:.4});
    io.observe(el);
  } else {
    el.classList.add('in-view');
  }
})();
</script>"""

page("home", "Eggs Your Way — pasteurised eggs and liquid egg",
     "Pasteurised shell eggs and ready-to-pour liquid egg. Safe to eat raw, kept cold from the pasteuriser to your kitchen.",
     home, CALC_JS + EGG_JS, filename="index.html")

# ---------------------------------------------------------- why it works
why_it_works = """
  <div class="sky-panel page-head">
    <div class="wrap">
      <h1>A warm bath, and nothing else</h1>
      <p>Pasteurising sounds industrial. It is mostly patience and a thermometer.</p>
    </div>
%(curve)s
  </div>

  <section>
    <div class="wrap">
      <div class="head">
        %(arc)s
        <h2>The whole trick is six degrees</h2>
        <p>An egg white sets at about 63&deg;C; salmonella gives up a bit below that. Hold the egg in that gap and one dies while the other stays liquid.</p>
      </div>
      <div class="temp">
        <div class="temp-bar">
          <div class="pin" style="left:47%%"><b>57&deg;C</b><em>we hold it here, for about an hour</em></div>
          <div class="pin" style="left:82%%"><b>63&deg;C</b><em>the white would start to cook</em></div>
        </div>
        <div class="temp-scale"><span>40&deg;C</span><span>55&deg;C</span><span>70&deg;C</span></div>
      </div>
    </div>
  </section>

  <section class="on-sky">
    <div class="wrap">
      <div class="head"><h2>Shell eggs, step by step</h2></div>
      <div class="steps">
        <div class="step"><div class="n">1</div><div>
          <h3>They arrive fresh and get graded</h3>
          <p>Eggs arrive from the farm, checked for cracks and washed. A cracked egg never makes the bath.</p>
        </div></div>
        <div class="step"><div class="n">2</div><div>
          <h3>Into the water</h3>
          <p>Held at 57&deg;C for about an hour, watched throughout &mdash; a couple of degrees either way is safe versus scrambled.</p>
        </div></div>
        <div class="step"><div class="n">3</div><div>
          <h3>Chilled straight down</h3>
          <p>Out of the bath and cooled fast, so it spends as little time as possible at temperatures bacteria like.</p>
        </div></div>
        <div class="step"><div class="n">4</div><div>
          <h3>Sealed, stamped, boxed</h3>
          <p>Marked so you can tell it apart from an ordinary egg, then trayed into cold storage.</p>
        </div></div>
      </div>
      <div class="photo-slot">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 8h3l2-2h6l2 2h3v11H4z"/><circle cx="12" cy="13.5" r="3.5"/></svg>
        <b>Photo placeholder</b>
        <p>Add a real photo here &mdash; eggs going into the water bath, or trays coming out of it.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="head">
        %(arc)s
        <h2>Liquid egg, step by step</h2>
        <p>Same idea, different shape &mdash; out of the shell, it can be heated harder for much less time.</p>
      </div>
      <div class="steps">
        <div class="step"><div class="n">1</div><div>
          <h3>Cracked and separated</h3>
          <p>Machines crack and split whites from yolks, or keep them together for whole egg, filtering out shell fragments.</p>
        </div></div>
        <div class="step"><div class="n">2</div><div>
          <h3>Blended smooth</h3>
          <p>Mixed so every millilitre pours the same &mdash; no fishing a stray chalaza out of your batter.</p>
        </div></div>
        <div class="step"><div class="n">3</div><div>
          <h3>Through the pasteuriser</h3>
          <p>A few minutes at 60&ndash;64&deg;C in a continuous flow, then straight into a chiller &mdash; quick, since nothing travels through a shell.</p>
        </div></div>
        <div class="step"><div class="n">4</div><div>
          <h3>Filled and sealed cold</h3>
          <p>Packed into sealed pouches at low temperature, dated, and kept at 4&deg;C until it reaches you.</p>
        </div></div>
      </div>
      <div class="photo-slot">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 8h3l2-2h6l2 2h3v11H4z"/><circle cx="12" cy="13.5" r="3.5"/></svg>
        <b>Photo placeholder</b>
        <p>Add a real photo here &mdash; the pasteuriser line, or liquid egg being poured into pouches.</p>
      </div>
    </div>
  </section>

  <section class="on-sky">
    <div class="wrap">
      <div class="head">
        <h2>Why it lasts longer</h2>
        <p>No preservatives &mdash; shelf life just comes from fewer bacteria to start and never letting the pack warm up.</p>
      </div>
      <div class="bars">
        <div class="bar-row">
          <div class="lab"><span>Eggs you crack yourself, in a bowl</span><span>use today</span></div>
          <div class="bar-track"><div class="bar-fill" style="width:6%%"></div></div>
        </div>
        <div class="bar-row">
          <div class="lab"><span>Liquid egg, opened</span><span>a few days</span></div>
          <div class="bar-track"><div class="bar-fill" style="width:22%%"></div></div>
        </div>
        <div class="bar-row">
          <div class="lab"><span>Liquid egg, sealed and chilled</span><span>weeks &mdash; see the pack</span></div>
          <div class="bar-track"><div class="bar-fill long" style="width:92%%"></div></div>
        </div>
      </div>
      <div class="trio" style="margin-top:40px">
        <div class="card">
          <h3>Less waste at home</h3>
          <p>Half a recipe no longer means three lonely yolks waiting in the fridge.</p>
        </div>
        <div class="card">
          <h3>Nothing added</h3>
          <p>The longer life comes from heat and cold, not anything on an ingredients list. It says: egg.</p>
        </div>
        <div class="card">
          <h3>Same egg, same cooking</h3>
          <p>It whisks, sets and browns as expected. Meringue just takes a minute longer to peak.</p>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="head">
        %(arc)s
        <h2>If you train, this bit is for you</h2>
        <p>The case for liquid egg white is mostly that it turns breakfast into a number you can repeat.</p>
      </div>
      <div class="trio">
        <div class="card">
          <h3>Pour it, don't count it</h3>
          <p>200 ml of egg white is about 22 g protein, 105 calories, no fat worth mentioning. Same pour, every morning.</p>
        </div>
        <div class="card">
          <h3>Raw is actually fine now</h3>
          <p>Straight into the shaker with oats or a scoop &mdash; no cooking, no salmonella roulette.</p>
        </div>
        <div class="card">
          <h3>Six minutes back</h3>
          <p>Cracking eight eggs takes time and leaves a mess. Pouring takes ten seconds.</p>
        </div>
      </div>
      <div style="text-align:center;margin-top:38px">
        <a class="btn btn-yolk" href="%(wa)s" target="_blank" rel="noopener">Order on WhatsApp</a>
      </div>
    </div>
  </section>
""" % dict(curve=CURVE, arc=ARC, wa=WA)

page("why", "Why it works — Eggs Your Way",
     "How pasteurised shell eggs and liquid egg are made, why they keep longer, and what that means if you bake or track your macros.",
     why_it_works, filename="why-it-works.html")

def product_card(title, desc, packs, wa_link, icon):
    return """<article class="egg-card">
          <div class="product-visual">
            %s
            <p>Real pack photo coming soon</p>
          </div>
          <h3>%s</h3>
          <p>%s</p>
          <p class="footnote">%s</p>
          <a class="btn btn-plain" href="%s" target="_blank" rel="noopener">Order on WhatsApp</a>
        </article>""" % (icon, title, desc, packs, wa_link)


# ------------------------------------------------------------------ shop
shop = """
  <div class="sky-panel page-head">
    <div class="wrap">
      <h1>Shop the range</h1>
      <p>Four products, every one pasteurised before it leaves us. Pick a pack size on WhatsApp and we'll confirm the price.</p>
    </div>
%(curve)s
  </div>

  <section>
    <div class="wrap">
      <div class="range">
        %(p1)s
        %(p2)s
        %(p3)s
        %(p4)s
      </div>
      <p class="footnote" style="margin-top:30px">Ordering for a business? See <a href="business.html">bulk pack sizes and business pricing</a>. Questions first? Check the <a href="contact.html#faq">FAQ</a>.</p>
    </div>
  </section>
""" % dict(
    curve=CURVE,
    p1=product_card("Pasteurised shell eggs",
                     "Ordinary eggs, heat-treated in the shell. Crack them into tiramisu or a shake without a second thought.",
                     "Trays of 6, 12 and 30. [Price per tray]",
                     wa("Hi! I'd like to order pasteurised shell eggs."),
                     egg_icon("s1", "A whole egg in its shell", highlight=True)),
    p2=product_card("Liquid whole egg",
                     "Cracked, blended and pasteurised. One litre pours about twenty eggs, no shells.",
                     "1 kg pouch or 5 kg box. [Price]",
                     wa("Hi! I'd like to order liquid whole egg."),
                     bottle_icon("s2", "A bottle of liquid whole egg", fill="#FFD447", level=50)),
    p3=product_card("Liquid egg white",
                     "Just the whites, ready to whisk. For meringue, omelettes, and anyone counting protein.",
                     "1 kg pouch or 5 kg box. [Price]",
                     wa("Hi! I'd like to order liquid egg white."),
                     bottle_icon("s3", "A bottle of liquid egg white", fill="#EDF7FD", level=50, top_stroke="#84C8EE")),
    p4=product_card("Liquid egg yolk",
                     "Only yolks, deep and rich. For custard, ice cream bases and a glossy carbonara.",
                     "1 kg pouch or 5 kg box. [Price]",
                     wa("Hi! I'd like to order liquid egg yolk."),
                     bottle_icon("s4", "A bottle of liquid egg yolk", fill="#F0B71E", level=34)),
)

page("shop", "Shop — Eggs Your Way",
     "Pasteurised shell eggs, liquid whole egg, liquid egg white and liquid egg yolk. Order any of them on WhatsApp.",
     shop)

# --------------------------------------------------------------- recipes
recipes = """
  <div class="sky-panel page-head">
    <div class="wrap">
      <h1>Recipes</h1>
      <p>Once the egg is already safe to eat raw, a few things get a lot simpler.</p>
    </div>
%(curve)s
  </div>

  <section>
    <div class="wrap">
      <div class="trio">
        <div class="card">
          <h3>Classic tiramisu</h3>
          <p>No stovetop, no worrying about raw yolk. [Real recipe and quantities to come.]</p>
          <p class="cite">Uses liquid egg yolk</p>
        </div>
        <div class="card">
          <h3>No-cook mayonnaise</h3>
          <p>Whole egg, oil and a whisk. [Real recipe and quantities to come.]</p>
          <p class="cite">Uses liquid whole egg</p>
        </div>
        <div class="card">
          <h3>Meringue &amp; macarons</h3>
          <p>Whisks the same way, just takes longer to reach stiff peaks. [Real recipe and quantities to come.]</p>
          <p class="cite">Uses liquid egg white</p>
        </div>
      </div>
      <div class="trio" style="margin-top:20px">
        <div class="card">
          <h3>Post-workout shake</h3>
          <p>Straight into the blender with oats or a scoop. [Real recipe and quantities to come.]</p>
          <p class="cite">Uses liquid egg white</p>
        </div>
        <div class="card">
          <h3>Carbonara</h3>
          <p>Glossy, not scrambled, and safe to eat a little looser than usual. [Real recipe and quantities to come.]</p>
          <p class="cite">Uses liquid whole egg or yolk</p>
        </div>
        <div class="card">
          <h3>Hollandaise</h3>
          <p>Rich and forgiving to whisk over gentle heat. [Real recipe and quantities to come.]</p>
          <p class="cite">Uses liquid egg yolk</p>
        </div>
      </div>
      <p class="footnote" style="margin-top:30px">Have a recipe you want featured, or one that failed and you want fixed? <a href="%(wa)s" target="_blank" rel="noopener">Tell us on WhatsApp</a>.</p>
    </div>
  </section>
""" % dict(curve=CURVE, wa=WA)

page("recipes", "Recipes — Eggs Your Way",
     "Recipe ideas that get simpler once the egg is already pasteurised and safe to eat raw.",
     recipes)

# -------------------------------------------------------------- business
business = """
  <div class="sky-panel page-head">
    <div class="wrap">
      <h1>For your business</h1>
      <p>The same pasteurised eggs, sized and scheduled for a kitchen that orders every week.</p>
    </div>
%(curve)s
  </div>

  <section>
    <div class="wrap">
      <div class="head"><h2>Built for</h2></div>
      <div class="for-grid three">
        <div class="for-item">
          <div class="blob" aria-hidden="true">%(cup)s</div>
          <h3>Caf&eacute;s and bakeries</h3>
          <p>No cracking, no separating, no bin full of shells at closing.</p>
        </div>
        <div class="for-item">
          <div class="blob" aria-hidden="true">%(pan)s</div>
          <h3>Hotels and cloud kitchens</h3>
          <p>The same volume every service, and a food-safety box already ticked.</p>
        </div>
        <div class="for-item">
          <div class="blob" aria-hidden="true">%(shaker)s</div>
          <h3>Gyms and meal-prep services</h3>
          <p>Egg white by the litre, measured the same way every batch.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="on-sky">
    <div class="wrap">
      <div class="head"><h2>How a business account works</h2></div>
      <div class="trio">
        <div class="card">
          <h3>Bulk pack sizes</h3>
          <p>Five-kilo boxes of liquid egg, and trays of 30 for shell eggs. [Confirm the largest pack size actually offered.]</p>
        </div>
        <div class="card">
          <h3>Standing orders</h3>
          <p>[Fixed weekly schedule for business accounts? Include the cut-off time to change an order.]</p>
        </div>
        <div class="card">
          <h3>Paperwork sorted</h3>
          <p>FSSAI licensed, with certificates available on request. See our <a href="about.html#certifications">certifications</a>.</p>
        </div>
      </div>
      <div style="text-align:center;margin-top:38px">
        <a class="btn btn-yolk" href="%(wa_biz)s" target="_blank" rel="noopener">Set up a business account</a>
      </div>
    </div>
  </section>
""" % dict(curve=CURVE, wa_biz=wa("Hi! I run a business and would like to set up a standing order."), **ICONS)

page("business", "For Business — Eggs Your Way",
     "Bulk pasteurised eggs and liquid egg for cafes, hotels, cloud kitchens and meal-prep services.",
     business)

# ---------------------------------------------------------------- about
about = """
  <div class="sky-panel page-head">
    <div class="wrap">
      <h1>We got tired of throwing eggs away</h1>
      <p>[The real reason he started &mdash; one honest sentence beats a mission statement.]</p>
    </div>
%(curve)s
  </div>

  <section>
    <div class="wrap">
      <div class="duo">
        <div class="prose">
          <h3>How it started</h3>
          <p>[A few sentences: what he did before, what he noticed, and the moment it became a business. Be specific.]</p>
          <p>[Where the eggs come from, and why those farms.]</p>
        </div>
        <div class="prose">
          <h3>How we work</h3>
          <p>[A normal week &mdash; batch sizes, how often you pasteurise, how fast an order ships.]</p>
          <p>[Anything he refuses to do &mdash; no preservatives, no reselling, no breaking the cold chain. Often the most convincing line on an about page.]</p>
        </div>
      </div>
    </div>
  </section>

  <section class="on-sky">
    <div class="wrap">
      <div class="head"><h2>What we care about</h2></div>
      <div class="trio">
        <div class="card">
          <h3>Cold, always</h3>
          <p>Every batch stays chilled from the pasteuriser to your door. If a delivery cannot stay cold, it does not go out.</p>
        </div>
        <div class="card">
          <h3>One ingredient</h3>
          <p>Egg. Nothing is added to make it last longer or look better, because heat and cold already do that job.</p>
        </div>
        <div class="card">
          <h3>Tell you the truth</h3>
          <p>Real dates on packs, real answers about where things come from, and a straight no when we cannot do something.</p>
        </div>
      </div>
    </div>
  </section>

  <section id="certifications">
    <div class="wrap">
      <div class="head"><h2>Certifications</h2><p>Real licences, not badges we made up.</p></div>
      <div class="trio">
        <div class="card">
          <h3>FSSAI licence</h3>
          <p>Licence number [FSSAI number]. Certificate available on request.</p>
        </div>
        <div class="card">
          <h3>Cold-chain handling</h3>
          <p>[How the cold chain is kept and checked &mdash; temperature logs, insulated transport, whatever's true.]</p>
        </div>
        <div class="card">
          <h3>Batch testing</h3>
          <p>[Name the lab if one tests each batch, or say what check actually happens.]</p>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="head">
        %(arc)s
        <h2>Who you'll be talking to</h2>
        <p>[Names and one line each &mdash; a small business can sound like people, not a company.]</p>
      </div>
      <div style="text-align:center">
        <a class="btn btn-yolk" href="contact.html">Say hello</a>
      </div>
    </div>
  </section>
""" % dict(curve=CURVE, arc=ARC)

page("about", "About — Eggs Your Way",
     "Who we are, where the eggs come from, and how we work.",
     about)

# -------------------------------------------------------------- contact
contact = """
  <div class="sky-panel page-head">
    <div class="wrap">
      <h1>Tell us what you cook</h1>
      <p>And roughly how much of it. We'll suggest the right pack and send a price.</p>
    </div>
%(curve)s
  </div>

  <section>
    <div class="wrap">
      <div class="form">
        <div class="field">
          <label for="f-name">Your name</label>
          <input id="f-name" type="text" autocomplete="name" placeholder="">
        </div>
        <div class="field">
          <label for="f-kind">I'm ordering for</label>
          <select id="f-kind">
            <option>my own kitchen</option>
            <option>a caf&eacute; or bakery</option>
            <option>a hotel or cloud kitchen</option>
            <option>a gym or meal-prep service</option>
          </select>
        </div>
        <div class="field">
          <label for="f-what">What you're after</label>
          <textarea id="f-what" placeholder="e.g. 5 litres of egg white a week, and a tray of shell eggs"></textarea>
        </div>
        <button class="btn btn-yolk" id="send" type="button">Send on WhatsApp</button>
        <p class="footnote" id="formnote">This fills in a WhatsApp message for you. Nothing is sent until you press send in WhatsApp.</p>
      </div>

      <div class="contact-lines">
        <p>Or reach us directly</p>
        <p><a href="https://wa.me/919599327947">+91 95993 27947</a></p>
        <p><a href="mailto:eggzurway@gmail.com">eggzurway@gmail.com</a></p>
        <p>9am to 7pm, Monday to Saturday. Deliveries across Gurugram.</p>
      </div>
    </div>
  </section>

  <section class="on-sky" id="faq">
    <div class="wrap">
      <div class="head"><h2>Before you ask</h2></div>
      <div class="trio">
        <div class="card">
          <h3>Is there a minimum order?</h3>
          <p>[Yes or no, and the number &mdash; say it plainly.]</p>
        </div>
        <div class="card">
          <h3>How fast is delivery?</h3>
          <p>[Same day, next day, or fixed days &mdash; plus the order cut-off time.]</p>
        </div>
        <div class="card">
          <h3>Can I see the licence?</h3>
          <p>Yes &mdash; see our <a href="about.html#certifications">certifications</a>, and we'll happily send the certificate if you need it on file.</p>
        </div>
      </div>
    </div>
  </section>
""" % dict(curve=CURVE)

FORM_JS = """<script>
(function(){
  var phone = '919599327947';   // change this in one place
  var btn = document.getElementById('send');
  if(!btn) return;
  btn.addEventListener('click', function(){
    var name = document.getElementById('f-name').value.trim();
    var kind = document.getElementById('f-kind').value;
    var what = document.getElementById('f-what').value.trim();
    if(!what){
      document.getElementById('formnote').textContent =
        'Add a line about what you need, then press send.';
      document.getElementById('f-what').focus();
      return;
    }
    var msg = 'Hi! ' + (name ? 'This is ' + name + '. ' : '') +
              "I'm ordering for " + kind + '. ' + what;
    window.open('https://wa.me/' + phone + '?text=' + encodeURIComponent(msg), '_blank', 'noopener');
  });
})();
</script>"""

page("contact", "Contact — Eggs Your Way",
     "Order pasteurised eggs and liquid egg, or ask us anything.",
     contact, FORM_JS)
