from generator import create_page, SVGS
from build_menus import menu_section_html

# ----------------- STARTERS -----------------
starters_items = [
    ("65 Fry - Chicken", "₹170", ""), ("65 Fry - Fish", "₹220", ""), ("65 Fry - Prawn", "₹220", ""), ("65 Fry - Kaadai", "₹160", ""),
    ("Chilli - Chicken", "₹200", ""), ("Chilli - Fish", "₹230", ""), ("Chilli - Prawn", "₹250", ""),
    ("Manchurian - Chicken", "₹200", ""), ("Manchurian - Fish", "₹230", ""), ("Manchurian - Prawn", "₹250", ""),
    ("Lollipop 5pcs - Chicken", "₹160", "Chef's Special"), ("Lollipop 5pcs - KFC", "₹200", "Chef's Special"), ("Lollipop 5pcs - Crab", "₹220", "Chef's Special"),
    ("Fish Fry - Nethili", "₹160", ""), ("Fish Fry - Koduva", "₹240", ""), ("Moru Moru Chicken", "₹220", "Chef's Special"),
    ("Crispy Fried Chicken", "₹220", ""), ("Black Pepper Chicken", "₹280", ""), ("Fish Finger (8 pcs)", "₹250", "Chef's Special")
]
south_indian = [("Chicken Pepper Fry", "₹200", ""), ("Prawn Pepper Fry", "₹250", ""), ("Mutton Pepper Fry", "₹280", ""), ("Kaadai Pepper Fry", "₹200", ""), ("Chicken Chukka", "₹200", ""), ("Mutton Chukka", "₹280", "")]
special_starters = [
    ("Dragon Chicken", "₹220", ""), ("Dragon Fish", "₹250", ""), ("Dragon Prawn", "₹280", ""),
    ("Lemon Chicken", "₹220", ""), ("Lemon Fish", "₹250", ""), ("Lemon Prawn", "₹280", ""),
    ("Hot Pepper Chicken", "₹220", ""), ("Hot Pepper Fish", "₹250", ""), ("Hot Pepper Prawn", "₹280", ""),
    ("Salt & Pepper Chicken", "₹220", ""), ("Salt & Pepper Fish", "₹250", ""), ("Salt & Pepper Prawn", "₹280", ""),
    ("Butter Garlic Chicken", "₹220", "Chef's Special"), ("Butter Garlic Prawn", "₹250", "Chef's Special"),
    ("Japan Chicken", "₹220", ""), ("Japan Prawn", "₹250", ""), ("Dragon Paneer", "₹250", "")
]
veg_starters = [
    ("Gobi 65", "₹140", ""), ("Gobi Manchurian", "₹180", ""), ("Gobi Chilli", "₹180", ""),
    ("Mushroom 65", "₹150", ""), ("Mushroom Manchurian", "₹200", ""), ("Mushroom Chilli", "₹200", ""),
    ("Paneer 65", "₹180", ""), ("Paneer Manchurian", "₹220", ""), ("Paneer Chilli", "₹220", ""),
    ("Paneer Pepper Onion", "₹220", ""), ("Paneer Tikka", "₹250", ""), ("Salt & Pepper Mushroom", "₹220", "")
]
starters_content = f"<div class='breadcrumb'><a href='index.html'>Home</a> &nbsp;/&nbsp; Starters</div><section style='padding: 60px 20px;'>" + \
                   menu_section_html("Non-Veg Starters", starters_items, False) + \
                   menu_section_html("South Indian Starters", south_indian, False) + \
                   menu_section_html("Special Starters", special_starters, False) + \
                   menu_section_html("Veg Starters", veg_starters, True) + "</section>"
create_page("starters.html", "Starters Menu | Bhai Biryani Godown Trichy — Chicken 65, Tandoori & More", "Best starters in Trichy at Bhai Biryani Godown. Chicken 65, Dragon Chicken, Fish Fry, Mutton Chukka, Lollipop.", "", starters_content)

# ----------------- FRIED RICE -----------------
rice_items = [("Veg Fried Rice", "₹140", ""), ("Mushroom Fried Rice", "₹150", ""), ("Paneer Fried Rice", "₹150", ""), ("Egg Fried Rice", "₹150", ""), ("Chicken Fried Rice", "₹170", ""), ("Prawn Fried Rice", "₹200", ""), ("Mixed Fried Rice", "₹250", "")]
noodles_items = [("Veg Fried Noodles", "₹140", ""), ("Mushroom Fried Noodles", "₹150", ""), ("Paneer Fried Noodles", "₹150", ""), ("Egg Fried Noodles", "₹150", ""), ("Chicken Fried Noodles", "₹170", ""), ("Prawn Fried Noodles", "₹200", ""), ("Mixed Fried Noodles", "₹250", "")]
schezwan_items = [("Veg", "₹170", ""), ("Mushroom", "₹190", ""), ("Paneer", "₹210", ""), ("Egg", "₹180", ""), ("Chicken", "₹200", ""), ("Prawn", "₹230", ""), ("Mixed", "₹280", "")]
rice_content = f"<div class='breadcrumb'><a href='index.html'>Home</a> &nbsp;/&nbsp; Fried Rice & Noodles</div><section style='padding: 60px 20px;'>" + \
               menu_section_html("Fried Rice", rice_items, False) + \
               menu_section_html("Noodles", noodles_items, False) + \
               menu_section_html("Schezwan / Manchow / Mongolian", schezwan_items, False) + "</section>"
create_page("fried-rice-noodles.html", "Fried Rice & Noodles | Bhai Biryani Godown Trichy", "Wok-tossed chicken, prawn, and veg fried rice and noodles at BBG.", "", rice_content)

# ----------------- TANDOORI & BBQ -----------------
tandoori = [("Tandoori Chicken - Qtr", "₹160", ""), ("Tandoori Chicken - Half", "₹280", ""), ("Tandoori Chicken - Full", "₹520", ""), ("Tikka - Chicken", "₹220", ""), ("Tikka - Fish", "₹250", ""), ("Hariyali Kebab", "₹250", ""), ("Malai Kebab", "₹250", ""), ("Sheek Kebab (Chicken)", "₹250", ""), ("Triple Flavour Kebab", "₹270", "Chef's Special"), ("Tangri Kebab", "₹270", "Chef's Special")]
arabic = [("Arabic Shawaya Grill - Qtr", "₹160", "Chef's Special"), ("Arabic Shawaya Grill - Half", "₹280", ""), ("Arabic Shawaya Grill - Full", "₹520", ""), ("Barbeque (Spicy) - Qtr", "₹160", ""), ("Barbeque (Spicy) - Half", "₹280", ""), ("Barbeque (Spicy) - Full", "₹520", ""), ("Barbeque (Pepper) - Qtr", "₹160", ""), ("Barbeque (Pepper) - Half", "₹280", ""), ("Barbeque (Pepper) - Full", "₹520", ""), ("Al-faham - Qtr", "₹160", ""), ("Al-faham - Half", "₹280", ""), ("Al-faham - Full", "₹520", "")]
tand_content = f"<div class='breadcrumb'><a href='index.html'>Home</a> &nbsp;/&nbsp; Tandoori & Arabic Grill</div><section style='padding: 60px 20px;'><p style='color:var(--color-gold);'>Note: All items come with 2 sauce varieties, french fries, and unlimited Kuboos.</p><br>" + \
               menu_section_html("Tandoori Delights (12PM-4PM & 6PM-11PM)", tandoori, False) + \
               menu_section_html("Arabic Grill & Barbeque (6PM-11PM)", arabic, False) + "</section>"
create_page("tandoori-bbq.html", "Tandoori & Arabic Grill | Bhai Biryani Godown Trichy — Al-Faham, BBQ, Kebabs", "Tandoori chicken, Al-Faham, Shawaya Grill, and BBQ at Bhai Biryani Godown Trichy.", "", tand_content)

# ----------------- GRAVY -----------------
v_gravy = [("Kadai Paneer", "₹220", ""), ("Kadai Veg", "₹200", ""), ("Mushroom Masala", "₹200", ""), ("Gobi Masala", "₹170", ""), ("Mix Veg Curry", "₹200", ""), ("Paneer Butter Masala", "₹220", ""), ("Paneer Tikka Masala", "₹250", "")]
nv_gravy = [("Pepper Gravy - Chicken", "₹200", ""), ("Pepper Gravy - Prawn", "₹260", ""), ("Pepper Gravy - Mutton", "₹280", ""), ("Pepper Gravy - Kaadai", "₹200", ""), ("Masala - Chicken", "₹200", ""), ("Masala - Prawn", "₹260", ""), ("Masala - Mutton", "₹280", ""), ("Masala - Kaadai", "₹200", ""), ("Chettinad Gravy - Chicken", "₹200", ""), ("Chettinad Gravy - Mutton", "₹280", ""), ("Fish Curry / Masala", "₹280", "")]
snv_gravy = [("Kadai Chicken", "₹200", ""), ("Butter Chicken", "₹220", ""), ("Hyderabad Chicken", "₹230", ""), ("Punjabi Chicken", "₹230", ""), ("Chicken Tikka Masala", "₹250", "Chef's Special")]
gravy_content = f"<div class='breadcrumb'><a href='index.html'>Home</a> &nbsp;/&nbsp; Gravies</div><section style='padding: 60px 20px;'>" + \
               menu_section_html("Veg Gravies", v_gravy, True) + \
               menu_section_html("Non-Veg Gravies", nv_gravy, False) + \
               menu_section_html("Special Non-Veg Gravies", snv_gravy, False) + "</section>"
create_page("gravy.html", "Gravies Menu | Bhai Biryani Godown", "Rich curries and masalas at BBG Trichy.", "", gravy_content)

# ----------------- OTHERS -----------------
breads = [("Plain Naan", "₹60", ""), ("Butter Naan", "₹80", ""), ("Garlic Naan", "₹80", ""), ("Plain Kulcha", "₹60", ""), ("Butter Kulcha", "₹80", ""), ("Stuffed Kulcha", "₹100", ""), ("Tandoori Roti", "₹60", ""), ("Butter Roti", "₹70", ""), ("Tandoori Parotta", "₹80", "")]
create_page("breads.html", "Breads | Bhai Biryani Godown", "Soft naans, kulchas, and rotis.", "", f"<div class='breadcrumb'><a href='index.html'>Home</a> &nbsp;/&nbsp; Breads</div><section style='padding: 60px 20px;'>{menu_section_html('Indian Breads', breads, True)}</section>")

pulao_items = [("Veg Pulao", "₹170", ""), ("Paneer Pulao", "₹200", ""), ("Mushroom Pulao", "₹180", ""), ("Cashew Nut Pulao", "₹200", ""), ("Peas Pulao", "₹170", ""), ("Kashmiri Pulao", "₹200", "")]
create_page("pulao.html", "Pulao | Bhai Biryani Godown", "Flavorful pulaos at BBG.", "", f"<div class='breadcrumb'><a href='index.html'>Home</a> &nbsp;/&nbsp; Pulao</div><section style='padding: 60px 20px;'>{menu_section_html('Pulao', pulao_items, True)}</section>")

eggs = [("Boiled Egg", "₹20", ""), ("Kadai Omelette", "₹50", ""), ("Egg Poriyal", "₹50", ""), ("Egg Mass", "₹50", ""), ("Chilli Egg", "₹100", ""), ("Egg Masala", "₹100", "")]
create_page("eggs.html", "Eggs to Try | Bhai Biryani Godown", "Egg dishes at BBG.", "", f"<div class='breadcrumb'><a href='index.html'>Home</a> &nbsp;/&nbsp; Eggs to Try</div><section style='padding: 60px 20px;'>{menu_section_html('Eggs', eggs, False)}</section>")

climax = [("Beeda", "₹20", ""), ("Goli Soda", "₹40", ""), ("Elaneer Payasam", "₹90", ""), ("Mineral Water", "₹20", "")]
create_page("climax.html", "Sweets, Drinks & Desserts | Bhai Biryani Godown", "Refreshments and desserts at BBG.", "", f"<div class='breadcrumb'><a href='index.html'>Home</a> &nbsp;/&nbsp; Sweets & Drinks</div><section style='padding: 60px 20px;'>{menu_section_html('Sweets, Drinks & Desserts', climax, True)}</section>")

print("Generated remaining menus.")
