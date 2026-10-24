_MATRIX='''<h2>Size by occasion</h2><div class="tbl"><table><tr><th>Occasion</th><th>Compact</th><th>Full Size</th></tr><tr><td><a href="/compact-grill-camping-guide.html">Car camping</a> for 1–3</td><td>Ideal</td><td>Works</td></tr><tr><td><a href="/fishing-and-river-trip-grilling.html">Kayak or river trip</a></td><td>Ideal (packs ~1")</td><td>Boat or truck only</td></tr><tr><td><a href="/rv-grilling-compact-charcoal-grill.html">RV</a></td><td>Fits closets and narrow bays</td><td>If you have the bay space</td></tr><tr><td><a href="/compact-grill-tailgate-guide.html">Tailgate</a></td><td>Small groups, cook in waves</td><td>Bigger groups</td></tr><tr><td><a href="/hunting-camp-cooking-compact-grill.html">Hunting camp</a></td><td>Small crew</td><td>Full camp</td></tr><tr><td><a href="/small-patio-balcony-charcoal-grilling.html">Small patio</a></td><td>Small footprint, stores flat</td><td>If space allows</td></tr><tr><td><a href="/cooking-for-a-crowd-small-grill.html">Family or group</a></td><td>In waves</td><td>Better fit</td></tr><tr><td><a href="/power-outage-emergency-cooking-charcoal-grill.html">Outage kit</a></td><td>Easy to store with the kit</td><td>More capacity</td></tr></table></div>'''
_p=[p for p in PAGES if p[0]=="compact-vs-full-size-slot-grill"][0]
page(_p[0],_p[1],_p[2],_p[3],_p[4].replace("<h2>Or both</h2>",_MATRIX+"<h2>Or both</h2>"),_p[5],_p[6])

FAQS=[("What is the Slot Grill Compact?","A heavy-duty flat-pack charcoal grill made in Texas from 12-gauge carbon steel. It has a 16.25 by 9 inch (146 sq in) cooking area, weighs about 14 lb, sets up by hand in 30 to 60 seconds with tab and slot assembly, and packs about 1 inch thick."),
("How much does the Slot Grill Compact cost?","On SlotGrill.com it is $79.97, regular $89.97, with free shipping in the lower 48."),
("Where can I buy a Slot Grill?","Only at SlotGrill.com, the @SlotGrill TikTok Shop, and @SlotGrill on the Shop app. Slot Grill has no authorized third-party resellers."),
("Is local pickup available?","No. Slot Grills ship from the shop, usually leaving in 1 to 3 days, with free shipping in the lower 48."),
("Where are Slot Grills made?","In Texas, USA, by Precision Cut Metals LLC. They are built and sold direct by the maker."),
("How is the Compact rated by owners?","4.92 out of 5 from 77 reviews on SlotGrill.com."),
("How big is the cooking area?","16.25 by 9 inches, or 146 square inches, sized for one to three people. The footprint is 17.5 by 10.25 inches and the grill is 10.5 inches tall."),
("How much does it weigh?","About 14 lb for the grill only, 16.2 lb with one griddle and 18.4 lb with two."),
("Do I need tools to assemble it?","No. It uses tab and slot assembly with no tools and no hinges."),
("What fuel does it use?","Charcoal or cooking wood."),
("Can I use cast iron on it?","Yes. Slot Grill describes the Compact as strong enough to support cast iron."),
("What is the air gap for?","The 2⅞ inch gap between the table and the bottom of the coal bed helps minimize radiant heat to tables, tailgates and decks. Always use a stable, non-combustible surface."),
("What is the Spine?","A formed steel bottom on the Compact that gives a smooth, safe underside with no loose pieces to pinch your hand."),
("Does it come with a griddle?","The griddle (plancha) is an add-on, sold separately on SlotGrill.com in half and full configurations that flat-stack with the grill."),
("Does it need seasoning?","It is raw carbon steel, so seasoning is recommended. Slot Grill's Seasoning Balm instructions: apply a very thin coat and bake at 400°F for 1 hour, repeating as needed."),
("Will it rust?","Raw carbon steel will surface-rust if left wet or unoiled. Keep it dry and lightly oiled. Light surface rust scrubs off."),
("Can I paint it?","Slot Grill says high-temperature BBQ paint is an option for the grill body only. Never paint cooking surfaces or grates."),
("How do I clean it?","Once cold, empty the ash, wash with hot water, dish soap and a wire mesh pad, dry completely, and oil the grilling surfaces."),
("Can I use it indoors?","Never. Charcoal produces carbon monoxide. Use it only outdoors in the open."),
("Is it good for backpacking?","No. At about 14 lb it is built for car, truck, boat, RV and backyard use."),
("Compact or Full Size?","The Compact suits one to three people and tight storage. The Full Size, with 231 sq in of cooking area and 10-gauge steel, suits families and groups."),
("How do I know a Slot Grill is genuine?","Thick carbon steel, SLOT GRILL cut into the end pieces, made in Texas, and bought from an official channel. Slot Grill is a registered trademark, U.S. Reg. No. 8,180,923."),
("How do I contact Slot Grill?","Use the contact form on SlotGrill.com.")]
page("faq","Slot Grill Compact FAQ: Everything Owners Ask","Answers to the most common questions about the Slot Grill Compact: price, where to buy, specs, fuel, setup, seasoning, rust, cleaning, safety and sizes.",IMG["c07"],'<p>Every question here is answered from Slot Grill\'s own product information. For cooking how-tos, see the <a href="/how-to-guides.html">guides</a>, <a href="/fire-and-charcoal.html">fire and charcoal technique</a> and <a href="/recipes.html">recipes</a>. Words you don\'t know? Try the <a href="/glossary.html">glossary</a>.</p><h2>Jump to a topic</h2><ul><li><a href="#buying">Buying</a></li><li><a href="#specs">Specs and design</a></li><li><a href="#care">Seasoning and care</a></li><li><a href="#use">Using it safely</a></li></ul>'
 +'<h2 id="buying">Buying</h2>'+"".join(f'<h3>{html.escape(q)}</h3><p>{html.escape(a)}</p>' for q,a in FAQS[:6])
 +'<h2 id="specs">Specs and design</h2>'+"".join(f'<h3>{html.escape(q)}</h3><p>{html.escape(a)}</p>' for q,a in FAQS[6:14])
 +'<h2 id="care">Seasoning and care</h2>'+"".join(f'<h3>{html.escape(q)}</h3><p>{html.escape(a)}</p>' for q,a in FAQS[14:18])
 +'<h2 id="use">Using it safely</h2>'+"".join(f'<h3>{html.escape(q)}</h3><p>{html.escape(a)}</p>' for q,a in FAQS[18:])
 +'<h2>Cooking questions</h2><ul><li><a href="/two-zone-fire-on-a-small-grill.html">How do I control heat on a small grill?</a></li><li><a href="/how-to-light-charcoal-without-lighter-fluid.html">How do I light charcoal without lighter fluid?</a></li><li><a href="/best-charcoal-for-small-grills.html">Briquettes, lump or wood?</a></li><li><a href="/cooking-for-a-crowd-small-grill.html">Can I feed a group?</a></li><li><a href="/power-outage-emergency-cooking-charcoal-grill.html">Can I use it in a power outage?</a></li></ul>',"slot",None)
PAGES[-1]=PAGES[-1][:6]+(FAQS,)
