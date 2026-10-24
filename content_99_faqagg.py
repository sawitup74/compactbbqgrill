_f=[p for p in PAGES if p[0]=="faq"][0]
_agg=""; _all=list(_f[6])
for k,c in CATS.items():
    ps=[p for p in PAGES if p[5]==k and p[6] and p[0]!="faq"]
    if not ps: continue
    _agg+=f'<h2>{c[1]} questions</h2>'
    for p in ps:
        _agg+=f'<h3 style="font-size:1rem;color:var(--muted)">From <a href="/{p[0]}.html">{html.escape(p[1])}</a></h3>'+"".join(f'<p><b>{html.escape(q)}</b><br>{html.escape(a)}</p>' for q,a in p[6])
        _all+=p[6]
page("faq",_f[1],_f[2],_f[3],_f[4]+_agg,"slot",_all)
