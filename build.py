#!/usr/bin/env python3
"""Assembles the four pages so the nav and footer stay identical everywhere."""

WA = "https://wa.me/919599327947?text=Hi!%20I%27d%20like%20to%20order%20eggs."

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
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;500;600&family=Karla:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
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
      <a href="process.html"{c_process}>How it's made</a>
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
      <a href="process.html">How it's made</a>
      <a href="about.html">About</a>
      <a href="contact.html">Contact</a>
    </nav>
  </div>
  <div class="wrap"><p class="foot-note">FSSAI licence [number] &middot; &copy; <span id="yr">2026</span> Eggs Your Way</p></div>
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


ICONS = {
 "cake": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20.5h16"/><path d="M5.5 20.5v-6a2 2 0 012-2h9a2 2 0 012 2v6"/><path d="M12 12.5V9.5"/><path d="M12 7.8c.9-.9.6-1.9 0-2.5-.6.6-.9 1.6 0 2.5Z"/></svg>',
 "cup":  '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4.5 9h11v6.5a4 4 0 01-4 4h-3a4 4 0 01-4-4V9Z"/><path d="M15.5 10.5h2a2.6 2.6 0 010 5.2h-2"/><path d="M7.5 3.5v2M11.5 3v2.5"/></svg>',
 "pan":  '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9.5" cy="13.5" r="6.2"/><path d="M15.4 11.2l5.4-3.4"/><circle cx="9.5" cy="13.5" r="2.1" fill="currentColor" stroke="none"/></svg>',
 "shaker":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 3.2h6v2.6l1.1 2.2v11a2 2 0 01-2 2h-5.2a2 2 0 01-2-2v-11L8 5.8V3.2Z"/><path d="M7.9 12.4h8.2"/></svg>',
}


def page(name, title, desc, body, extra=""):
    cur = {k: "" for k in ("process", "about", "contact")}
    if name in cur:
        cur[name] = ' aria-current="page"'
    html = HEAD.format(title=title, desc=desc,
                       c_process=cur["process"], c_about=cur["about"], c_contact=cur["contact"])
    html += body
    html += FOOT.format(extra=extra)
    open(name + ".html", "w").write(html)
    print("wrote", name + ".html")


# ----------------------------------------------------------------- home
home = """
  <div class="sky-panel hero">
    <div class="wrap">
      <img class="hero-logo" src="logo.png" alt="Eggs Your Way logo: bold lettering inside an egg with a yolk trailing speed lines">
      <h1>Eggs you can eat raw. And eggs you can pour.</h1>
      <p class="sub">Pasteurised in the shell or cracked into cartons, then kept cold all the way to your kitchen.</p>
      <div class="hero-cta">
        <a class="btn btn-yolk" href="%(wa)s" target="_blank" rel="noopener">Order on WhatsApp</a>
        <a class="btn btn-plain" href="process.html">See how it's made</a>
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
          <p>Ordinary-looking eggs, gently heat-treated in the shell. Crack them into tiramisu, mayonnaise or a morning shake without thinking twice.</p>
        </article>
        <article class="egg-card">%(i2)s
          <h3>Liquid whole egg</h3>
          <p>Whites and yolks cracked, blended and pasteurised. One litre pours about twenty eggs, and there are no shells to deal with.</p>
        </article>
        <article class="egg-card">%(i3)s
          <h3>Liquid egg white</h3>
          <p>Just the whites, ready to whisk. For meringue, macarons, omelettes and anyone counting their protein.</p>
        </article>
        <article class="egg-card">%(i4)s
          <h3>Liquid egg yolk</h3>
          <p>Only yolks, deep and rich. Made for custard, ice cream bases, hollandaise and a properly glossy carbonara.</p>
        </article>
      </div>
    </div>
  </section>

  <section class="on-sky">
    <div class="wrap">
      <div class="head">
        <h2>Why pasteurised</h2>
        <p>Warmed to just below the point where an egg sets. Long enough to deal with salmonella, gentle enough that it still behaves exactly like an egg.</p>
      </div>
      <div class="trio">
        <div class="card">
          <h3>Raw recipes, no gamble</h3>
          <p>Tiramisu, mousse, aioli, cookie dough, protein shakes. The recipes that always came with a warning simply stop being risky.</p>
        </div>
        <div class="card">
          <h3>Safe for everyone at the table</h3>
          <p>Small children, pregnant women, older parents and anyone with a fragile immune system can eat what the rest of the family is eating.</p>
        </div>
        <div class="card">
          <h3>Nothing else goes in</h3>
          <p>No preservatives, no colour, no additives. Heat and time do the work, so taste and texture stay where they should.</p>
        </div>
      </div>
    </div>
  </section>

  <section id="convert">
    <div class="wrap">
      <div class="head">
        %(arc)s
        <h2>How much is that, really?</h2>
        <p>Your recipe counts eggs and your macros count grams. The carton is in millilitres. Here's the sum, so nobody has to do it at the counter.</p>
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
      <p class="footnote">Based on a large egg: 50 ml whole, 33 ml white, 17 ml yolk. Millilitres and grams are near enough the same here.</p>
    </div>
  </section>

  <section id="for">
    <div class="wrap">
      <div class="head"><h2>Made for</h2></div>
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
          <p>Sealed and refrigerated, liquid egg outlasts a fresh crack by a long way. The date is printed on every pack.</p>
        </div>
      </div>
      <div style="text-align:center;margin-top:38px">
        <a class="btn btn-yolk" href="%(wa)s" target="_blank" rel="noopener">Order on WhatsApp</a>
      </div>
    </div>
  </section>
""" % dict(
    wa=WA, curve=CURVE, arc=ARC,
    i1=egg_icon("c1", "A whole egg in its shell", highlight=True),
    i2=egg_icon("c2", "An egg holding liquid whole egg", fill="#FFD447", level=50),
    i3=egg_icon("c3", "An egg holding liquid egg white", fill="#EDF7FD", level=50, wave_stroke="#84C8EE"),
    i4=egg_icon("c4", "An egg holding liquid egg yolk", fill="#F0B71E", level=34),
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

page("index", "Eggs Your Way — pasteurised eggs and liquid egg",
     "Pasteurised shell eggs and ready-to-pour liquid egg. Safe to eat raw, kept cold from the pasteuriser to your kitchen.",
     home, CALC_JS)

# -------------------------------------------------------------- process
process = """
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
        <p>An egg white starts to set at about 63&deg;C. Salmonella gives up a little below that. Hold the egg in the gap for long enough and one dies while the other stays liquid.</p>
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
          <p>Eggs come in from the farm, are checked for cracks and washed. A cracked egg never makes it to the bath.</p>
        </div></div>
        <div class="step"><div class="n">2</div><div>
          <h3>Into the water</h3>
          <p>Held at a steady 57&deg;C for roughly an hour. The temperature is watched the whole time, because a couple of degrees either way is the difference between safe and scrambled.</p>
        </div></div>
        <div class="step"><div class="n">3</div><div>
          <h3>Chilled straight down</h3>
          <p>Out of the bath and cooled quickly, so the egg spends as little time as possible at temperatures bacteria like.</p>
        </div></div>
        <div class="step"><div class="n">4</div><div>
          <h3>Sealed, stamped, boxed</h3>
          <p>Each egg is marked so you can tell it apart from an ordinary one, then trayed and moved into cold storage.</p>
        </div></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="head">
        %(arc)s
        <h2>Liquid egg, step by step</h2>
        <p>Same idea, different shape. Because the egg is already out of its shell, it can be heated harder for a much shorter time.</p>
      </div>
      <div class="steps">
        <div class="step"><div class="n">1</div><div>
          <h3>Cracked and separated</h3>
          <p>Machines crack and split whites from yolks, or keep them together for whole egg. Shell fragments are filtered out.</p>
        </div></div>
        <div class="step"><div class="n">2</div><div>
          <h3>Blended smooth</h3>
          <p>Gently mixed so every millilitre pours the same. No more fishing a stray chalaza out of your batter.</p>
        </div></div>
        <div class="step"><div class="n">3</div><div>
          <h3>Through the pasteuriser</h3>
          <p>A few minutes at around 60 to 64&deg;C in a continuous flow, then straight into a chiller. Quick, because nothing has to travel through a shell.</p>
        </div></div>
        <div class="step"><div class="n">4</div><div>
          <h3>Filled and sealed cold</h3>
          <p>Packed into sealed pouches and cartons at low temperature, dated, and kept at 4&deg;C until it reaches you.</p>
        </div></div>
      </div>
    </div>
  </section>

  <section class="on-sky">
    <div class="wrap">
      <div class="head">
        <h2>Why it lasts longer</h2>
        <p>Not a preservative in sight. Shelf life comes from starting with fewer bacteria and never letting the pack warm up.</p>
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
          <p>Half a recipe no longer means three lonely yolks in the fridge hoping to become something.</p>
        </div>
        <div class="card">
          <h3>Nothing added</h3>
          <p>The longer life comes from heat and cold, not from anything on an ingredients list. The ingredients list says: egg.</p>
        </div>
        <div class="card">
          <h3>Same egg, same cooking</h3>
          <p>It whisks, sets and browns the way you expect. Meringue takes a minute or two longer to reach stiff peaks, and that is the only difference you will notice.</p>
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
          <p>200 ml of egg white is about 22 g of protein for roughly 105 calories, with no fat worth mentioning. Same pour, same numbers, every morning.</p>
        </div>
        <div class="card">
          <h3>Raw is actually fine now</h3>
          <p>Straight into the shaker with oats or a scoop, no cooking, no salmonella roulette. That is the entire reason pasteurised egg exists.</p>
        </div>
        <div class="card">
          <h3>Six minutes back</h3>
          <p>Cracking and separating eight eggs takes time and leaves a mess. Pouring takes ten seconds and the bin stays empty.</p>
        </div>
      </div>
      <div style="text-align:center;margin-top:38px">
        <a class="btn btn-yolk" href="%(wa)s" target="_blank" rel="noopener">Order on WhatsApp</a>
      </div>
    </div>
  </section>
""" % dict(curve=CURVE, arc=ARC, wa=WA)

page("process", "How it's made — Eggs Your Way",
     "How pasteurised shell eggs and liquid egg are made, why they keep longer, and what that means if you bake or track your macros.",
     process)

# ---------------------------------------------------------------- about
about = """
  <div class="sky-panel page-head">
    <div class="wrap">
      <h1>We got tired of throwing eggs away</h1>
      <p>[Replace this with the real reason he started. One honest sentence beats a paragraph of mission statement.]</p>
    </div>
%(curve)s
  </div>

  <section>
    <div class="wrap">
      <div class="duo">
        <div class="prose">
          <h3>How it started</h3>
          <p>[Two or three sentences. What he was doing before, what went wrong or what he noticed, and the moment it turned into a business. Keep it specific &mdash; a real detail is worth more than any adjective.]</p>
          <p>[Where the eggs come from, and why those farms. If he visits them, say so.]</p>
        </div>
        <div class="prose">
          <h3>How we work</h3>
          <p>[What happens in a normal week. Batch sizes, how often you pasteurise, how quickly an order goes out.]</p>
          <p>[Anything he refuses to do &mdash; no preservatives, no reselling other people's stock, no breaking the cold chain to save a trip. This is usually the most convincing part of an about page.]</p>
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

  <section>
    <div class="wrap">
      <div class="head">
        %(arc)s
        <h2>Who you'll be talking to</h2>
        <p>[Names and one line each. A small business is allowed to sound like people rather than a company.]</p>
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

  <section class="on-sky">
    <div class="wrap">
      <div class="head"><h2>Before you ask</h2></div>
      <div class="trio">
        <div class="card">
          <h3>Is there a minimum order?</h3>
          <p>[Yes or no, and the number. Say it plainly here rather than making people ask.]</p>
        </div>
        <div class="card">
          <h3>How fast is delivery?</h3>
          <p>[Same day, next day, fixed days of the week &mdash; whatever is true, including the cut-off time for an order.]</p>
        </div>
        <div class="card">
          <h3>Can I see the licence?</h3>
          <p>Our FSSAI licence number is in the footer of every page, and we'll happily send the certificate if you need it on file.</p>
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
