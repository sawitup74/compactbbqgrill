import json,html,sys,os
CDN="https://cdn.shopify.com/s/files/1/0721/8833/0172/files/"
IMG={k:CDN+v for k,v in dict(c07="compact-07.jpg?v=1792382833",c28="compact-28.jpg?v=1792382861",c08="compact-08.jpg?v=1792382834",c13="compact-13.jpg?v=1792382834",both16="both-16.jpg?v=1792382825",both02="both-02.jpg?v=1792382824",pl1="zz_Slot_Grill_Plancha_1.jpg?v=1792382973",pl2="zz_Slot_Grill_Plancha_2.jpg?v=1792382973",balm="seasoning-balm-main.jpg?v=1791978819",full01="full-size-01.jpg?v=1792382862").items()}
SG="https://slotgrill.com"
COMPACT=SG+"/products/slot-grill-compact-carbon-steel-free-shipping"
FULL=SG+"/products/slot-grill-carbon-steel-collapsible-bbq-grill"
GRID=SG+"/products/slot-grill-griddle-plancha"
BALM=SG+"/products/seasoning-balm-for-slot-grill"
THERMO=SG+"/products/slot-grill-instant-read-digital-meat-thermometer"
CONTACT=SG+"/pages/contact"
DOMAIN="https://compactbbqgrill.com"
CSS="""
:root{--ink:#1c1a17;--muted:#5e5a54;--fire:#c2461b;--fire2:#e0702e;--bg:#faf7f2;--card:#fff;--line:#e7e0d6}
*{box-sizing:border-box}body{margin:0;font:17px/1.65 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:var(--ink);background:var(--bg)}
a{color:var(--fire)}img{max-width:100%;height:auto;display:block;border-radius:12px}
header{background:#171512;color:#fff;position:sticky;top:0;z-index:5}
.nav{max-width:1080px;margin:auto;display:flex;align-items:center;justify-content:space-between;padding:.7rem 1rem;gap:1rem}
.brand{color:#fff;text-decoration:none;font-weight:800;letter-spacing:.02em}.brand span{color:var(--fire2)}
.nav nav a{color:#ddd;text-decoration:none;margin-left:1rem;font-size:.95rem}
.btn{display:inline-block;background:var(--fire);color:#fff!important;text-decoration:none;font-weight:700;padding:.8rem 1.2rem;border-radius:10px;margin:.3rem .4rem .3rem 0}
.btn.alt{background:transparent;border:2px solid var(--fire);color:var(--fire)!important}
.hero{max-width:1080px;margin:auto;padding:2rem 1rem;display:grid;grid-template-columns:1.1fr 1fr;gap:2rem;align-items:center}
.hero h1{font-size:clamp(2rem,5vw,3.2rem);line-height:1.05;margin:.2rem 0 1rem}
.kicker{text-transform:uppercase;letter-spacing:.15em;font-size:.78rem;color:var(--fire);font-weight:800}
main{max-width:760px;margin:auto;padding:1rem}main.wide{max-width:1080px}
h1{line-height:1.15}h2{margin-top:2.2rem;line-height:1.2}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:1rem}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;overflow:hidden;text-decoration:none;color:var(--ink);display:flex;flex-direction:column}
.card img{border-radius:0;aspect-ratio:4/3;object-fit:cover}.card div{padding:.9rem 1rem}.card h3{margin:.1rem 0 .3rem;font-size:1.05rem}.card p{margin:0;color:var(--muted);font-size:.92rem}
.product{background:#fff;border:1px solid var(--line);border-radius:16px;padding:1rem;display:grid;grid-template-columns:180px 1fr;gap:1rem;align-items:center;margin:2rem 0}
.product h3{margin:0 0 .3rem}.price{font-weight:800;font-size:1.2rem}.price s{color:var(--muted);font-weight:400;font-size:.95rem;margin-left:.4rem}
table{border-collapse:collapse;width:100%;font-size:.95rem;background:#fff}td,th{border:1px solid var(--line);padding:.5rem;text-align:left;vertical-align:top}th{background:#f3ede4}
.tbl{overflow-x:auto}
blockquote{margin:1rem 0;padding:1rem 1.2rem;background:#fff;border-left:5px solid var(--fire);border-radius:8px}blockquote cite{display:block;margin-top:.4rem;color:var(--muted);font-style:normal;font-size:.9rem}
.stars{color:#e0a100;letter-spacing:.1em}
.note{background:#fff4e8;border:1px solid #f1d2b3;padding:.8rem 1rem;border-radius:10px;font-size:.95rem}
footer{background:#171512;color:#aaa;margin-top:3rem;padding:2rem 1rem;font-size:.9rem}footer .in{max-width:1080px;margin:auto}footer a{color:#ddd}
.crumbs{font-size:.85rem;color:var(--muted);margin:.5rem 0}
@media(max-width:760px){.hero{grid-template-columns:1fr;padding-top:1rem}.nav nav{display:none}.product{grid-template-columns:1fr}body{font-size:16.5px}.btn{display:block;text-align:center}}
"""
def productbox(variant="compact"):
    if variant=="full":
        return f'<div class="product"><img src="{IMG["full01"]}" alt="Slot Grill Full Size carbon steel charcoal grill"><div><h3>Slot Grill Full Size</h3><p>10-gauge carbon steel · about 27.6 lb · 20.5" × 11.25" cooking area · made in Texas</p><p class="price">$139.97<s>$149.97</s></p><a class="btn" href="{FULL}">See the Full Size at SlotGrill.com</a></div></div>'
    return f'<div class="product"><img src="{IMG["c07"]}" alt="Slot Grill Compact 12-gauge carbon steel charcoal grill"><div><h3>Slot Grill Compact</h3><p>12-gauge carbon steel · about 14 lb · 16.25" × 9" cooking area · packs about 1" thick · made in Texas · <span class="stars">★★★★★</span> 4.92 (77 reviews)</p><p class="price">$79.97<s>$89.97</s></p><a class="btn" href="{COMPACT}">Shop the Compact at SlotGrill.com</a><a class="btn alt" href="{GRID}">Add a griddle</a></div></div>'
PAGES=[]  # (slug,title,desc,img,body,cat,faq)
CATS={"howto":("how-to-guides","How-To Guides","Setup, lighting, assembly and the basics of cooking on the Slot Grill Compact."),
"fire":("fire-and-charcoal","Fire &amp; Charcoal Technique","Lighting, heat control, searing, fuel and cooking for a crowd on a small charcoal fire."),
"recipes":("recipes","Recipes","Small-grill recipes sized for the Compact's 16.25 x 9 inch cooking area."),
"trips":("trips-and-occasions","Trips &amp; Occasions","Camping, tailgates, river trips, hunting camp, RV, beach, patio and power-outage cooking."),
"care":("care-and-maintenance","Care &amp; Maintenance","Seasoning, cleaning, storage and rust prevention for raw carbon steel."),
"slot":("about-slot-grill","About Slot Grill","The Compact, the Full Size, owner reviews, how to buy genuine, FAQs and glossary.")}
def page(slug,title,desc,img,body,cat="howto",faq=None):
    global PAGES
    PAGES=[p for p in PAGES if p[0]!=slug]; PAGES.append((slug,title,desc,img,body,cat,faq or []))
def shell(title,desc,slug,inner,wide=False,img=None,faq=None):
    canon=DOMAIN+("/" if slug=="index" else f"/{slug}.html")
    ld={"@context":"https://schema.org","@type":"WebPage" if slug=="index" else "Article","name":title,"headline":title,"url":canon,"image":img or IMG["c07"],"about":{"@type":"Product","name":"Slot Grill Compact","brand":{"@type":"Brand","name":"Slot Grill"},"manufacturer":{"@type":"Organization","name":"Precision Cut Metals LLC"},"url":COMPACT}}
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}"><link rel="canonical" href="{canon}">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:image" content="{img or IMG['c07']}">
<link rel="stylesheet" href="/style.css"><script type="application/ld+json">{json.dumps(ld)}</script>{faqld(faq)}</head><body>
<header><div class="nav"><a class="brand" href="/">Compact<span>BBQ</span>Grill</a><nav><a href="/how-to-guides.html">How-tos</a><a href="/fire-and-charcoal.html">Fire</a><a href="/recipes.html">Recipes</a><a href="/trips-and-occasions.html">Trips</a><a href="/care-and-maintenance.html">Care</a><a href="/faq.html">FAQ</a><a href="/about-slot-grill.html">Slot Grill</a></nav><a class="btn" style="margin:0;padding:.5rem .8rem" href="{COMPACT}">Shop</a></div></header>
<main class="{'wide' if wide else ''}">{inner}</main>
<footer><div class="in"><p><b>CompactBBQGrill</b> is a guide to cooking on small charcoal grills, published by Slot Grill (Precision Cut Metals LLC, Texas). Slot Grill® is a registered trademark of Precision Cut Metals LLC, U.S. Reg. No. 8,180,923.</p><p>Genuine Slot Grills are sold only at <a href="{SG}">SlotGrill.com</a>, the @SlotGrill TikTok Shop and @SlotGrill on the Shop app. Questions? Use the <a href="{CONTACT}">Slot Grill contact form</a>.</p><p><a href="/">Home</a> · <a href="/how-to-guides.html">How-tos</a> · <a href="/fire-and-charcoal.html">Fire &amp; charcoal</a> · <a href="/recipes.html">Recipes</a> · <a href="/trips-and-occasions.html">Trips</a> · <a href="/care-and-maintenance.html">Care</a> · <a href="/faq.html">FAQ</a> · <a href="/glossary.html">Glossary</a> · <a href="/reviews.html">Reviews</a> · <a href="/real-slot-grill.html">Spotting a real Slot Grill</a></p></div></footer></body></html>'''
def faqld(faq):
    if not faq: return ""
    return '<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]})+'</script>'
def faqhtml(faq):
    return ('<h2>Frequently asked questions</h2>'+"".join(f'<h3>{html.escape(q)}</h3><p>{html.escape(a)}</p>' for q,a in faq)) if faq else ""
def related(slug,cat):
    rel=[p for p in PAGES if p[5]==cat and p[0]!=slug and os.path.exists(p[0]+".html")]
    if not rel: return ""
    c=CATS[cat]
    return f'<h2>More in {c[1]}</h2><ul>'+"".join(f'<li><a href="/{p[0]}.html">{html.escape(p[1])}</a></li>' for p in rel)+f'</ul><p><a href="/{c[0]}.html">All {c[1]} →</a></p>'
def article(slug,title,desc,img,body,cat="howto",faq=None):
    c=CATS[cat]
    import re as _re
    wc=lambda b:len(_re.sub("<[^>]+>"," ",b).split())
    for blk in [QUICK,MISTAKES,PACKDOWN,SAFETY,WEATHER,ONROAD]:
        if wc(body)+wc(faqhtml(faq))>=1450 or cat=="slot" or slug=="glossary": break
        if blk[:40] not in body: body+=blk
    inner=f'<p class="crumbs"><a href="/">Home</a> › <a href="/{c[0]}.html">{c[1]}</a> › {html.escape(title)}</p><h1>{html.escape(title)}</h1><img src="{img}" alt="{html.escape(title)} on a Slot Grill Compact">{body}{faqhtml(faq) if slug!='faq' else ''}{productbox()}{related(slug,cat)}<p class="note">All specs and prices are from SlotGrill.com. Always grill outdoors on a stable, non-combustible surface and follow local fire rules.</p>'
    return shell(title,desc,slug,inner,img=img,faq=faq)
def cardgrid(ps): return '<div class="grid">'+"".join(f'<a class="card" href="/{s}.html"><img src="{i}" alt="" loading="lazy"><div><h3>{html.escape(t)}</h3><p>{html.escape(d)}</p></div></a>' for s,t,d,i,*_ in ps)+'</div>'
def write_index(done):
    catsec="".join(f'<h2><a href="/{c[0]}.html" style="color:inherit">{c[1]}</a></h2><p>{c[2]}</p>'+cardgrid([p for p in done if p[5]==k]) for k,c in CATS.items() if any(p[5]==k for p in done))
    cards="".join(f'<a class="card" href="/{s}.html"><img src="{i}" alt="" loading="lazy"><div><h3>{html.escape(t)}</h3><p>{html.escape(d)}</p></div></a>' for s,t,d,i,*_ in done)
    inner=f'''</main><section class="hero"><div><div class="kicker">Small grill. Real steel.</div><h1>Big cooks on a compact charcoal grill</h1><p>How-tos, tailgate and camping setups, and small-grill recipes, all cooked on the Slot Grill Compact: 12-gauge carbon steel, about 14 lb, packs about 1" flat, and sets up by hand in 30–60 seconds. Made in Texas.</p><a class="btn" href="{COMPACT}">Shop the Slot Grill Compact · $79.97</a><a class="btn alt" href="/reviews.html">Read owner reviews</a><p><span class="stars">★★★★★</span> 4.92 average from 77 Compact reviews</p></div><img src="{IMG['c28']}" alt="Slot Grill Compact assembled with charcoal"></section><main class="wide">
{catsec}
<h2>Why we cook on the Compact</h2><div class="tbl"><table><tr><th>Cooking area</th><td>16.25" × 9" (146 sq in)</td></tr><tr><th>Footprint / height</th><td>17.5" × 10.25" · 10.5" tall</td></tr><tr><th>Steel</th><td>12-gauge carbon steel</td></tr><tr><th>Weight</th><td>About 14 lb (16.2 lb with 1 griddle, 18.4 lb with 2)</td></tr><tr><th>Air gap under coal bed</th><td>2⅞"</td></tr><tr><th>Setup</th><td>Tab and slot, no tools, 30–60 seconds</td></tr><tr><th>Fuel</th><td>Charcoal or cooking wood</td></tr><tr><th>Made in</th><td>Texas, USA · free shipping in the lower 48</td></tr></table></div>
{productbox()}{productbox("full")}'''
    open("index.html","w").write(shell("Compact BBQ Grill: Small Charcoal Grill Guides & Recipes","How-tos, tailgate and camping tips, and recipes for small charcoal grills, cooked on the American-made Slot Grill Compact.","index",inner,wide=True))
open("style.css","w").write(CSS)
exec(open("content.py").read())
import glob
for f in sorted(glob.glob("content_*.py")): exec(open(f).read())
done=[]
only=sys.argv[1:]  # build incrementally
for p in PAGES:
    if only and p[0] not in only and not os.path.exists(p[0]+".html"): continue
    open(p[0]+".html","w").write(article(*p)); done.append(p)
for k,c in CATS.items():
    ps=[p for p in done if p[5]==k]
    if not ps: continue
    open(c[0]+".html","w").write(shell(html.unescape(c[1])+" | Compact BBQ Grill",html.unescape(c[2]),c[0],f'<p class="crumbs"><a href="/">Home</a> › {c[1]}</p><h1>{c[1]}</h1><p>{c[2]} Everything here is cooked and tested on the Slot Grill Compact.</p>'+cardgrid(ps)+productbox(),wide=True))
write_index(done)
urls=[DOMAIN+"/"]+[f"{DOMAIN}/{c[0]}.html" for k,c in CATS.items() if any(p[5]==k for p in done)]+[f"{DOMAIN}/{p[0]}.html" for p in done]
open("sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"  <url><loc>{u}</loc><lastmod>2026-10-23</lastmod></url>\n" for u in urls)+"</urlset>\n")
open("robots.txt","w").write(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
print(len(done),"pages")

# --- slotgrill.com link trim v3 (Keith, 2026-10-24) ---
# One working button per page + a few contextual links; other slotgrill.com links become plain text.
# Run with LINKCUT=0 to build the full-link version. Do not remove: the live sites are trimmed.
import linkcut, os
LINKCUT_KEEP={"about-slot-grill": ["SlotGrill.com"], "how-to-season-a-compact-grill": ["Slot Grill Seasoning Balm"], "index": ["Shop the Slot Grill Compact \u00b7 $79.97", "See the Full Size at SlotGrill.com", "SlotGrill.com"], "real-slot-grill": ["SlotGrill.com"], "slot-grill-maker-story": ["SlotGrill.com"]}
linkcut.run(LINKCUT_KEEP, pref='Shop', enabled=os.environ.get("LINKCUT","1")!="0")
