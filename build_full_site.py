import json
import os

html_path = r"C:\Users\User\.gemini\antigravity\scratch\sugar-sparkle-website\index.html"
products_json = r"C:\Users\User\.gemini\antigravity\scratch\sugar-sparkle-website\products_data.json"

with open(products_json, "r", encoding="utf-8") as f:
    products = json.load(f)

# Build product cards HTML
cards_html = []
for p in products:
    card = f'''
        <!-- Card: {p["title"]} -->
        <div class="gallery-card glass-card rounded-2xl overflow-hidden flex flex-col justify-between group" data-category="{p["category"]}">
          <div class="relative overflow-hidden aspect-[4/3] bg-pink-50">
            <img src="{p["img"]}" alt="{p["title"]}" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
            <span class="absolute top-3 left-3 {p["tag_color"]} text-white font-extrabold text-[11px] px-2.5 py-1 rounded-full shadow">{p["tag"]}</span>
            <span class="absolute top-3 right-3 {p["sub_color"]} text-white font-extrabold text-[11px] px-2.5 py-1 rounded-full shadow">{p["sub_tag"]}</span>
          </div>
          <div class="p-5 flex-1 flex flex-col justify-between">
            <div>
              <span class="text-xs font-bold text-gray-400 block mb-1">{p["category_name"]}</span>
              <h4 class="text-base font-black text-gray-900 group-hover:text-brandPink transition-colors">{p["title"]}</h4>
              <p class="text-xs text-gray-500 mt-1 line-clamp-2">{p["desc"]}</p>
            </div>
            <div class="mt-4 pt-3 border-t border-gray-100 flex items-center justify-between">
              <div>
                <span class="text-xs text-gray-400 block">建議售價</span>
                <span class="text-base font-black text-brandPink">{p["price"]}</span>
              </div>
              <button class="open-product-modal-btn px-3 py-1.5 rounded-xl bg-pink-50 hover:bg-pink-100 text-brandPink font-extrabold text-xs transition-colors flex items-center gap-1"
                      data-title="{p["title"]}" data-category="{p["category_name"]}" data-price="{p["price"]}" data-cost="{p["cost"]}" data-margin="{p["margin"]}" data-share="{p["share"]}"
                      data-desc="{p["desc"]}"
                      data-img="{p["img"]}">
                查看詳情 <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
              </button>
            </div>
          </div>
        </div>
'''
    cards_html.append(card)

cards_joined = "\n".join(cards_html)

# Mascot section HTML
mascot_section = '''
  <!-- ================= SECTION: OFFICIAL BRAND MASCOT (品牌吉祥物專區) ================= -->
  <section id="mascot" class="py-16 md:py-24 bg-gradient-to-r from-pink-100/70 via-purple-50/60 to-blue-100/70 border-b border-pink-200 relative overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-12">
        <span class="inline-flex items-center gap-1.5 px-3.5 py-1 rounded-full bg-brandPink text-white text-xs font-black shadow-md mb-2">
          <i data-lucide="heart" class="w-3.5 h-3.5"></i> 官方品牌雙吉祥物 · OFFICIAL BRAND MASCOTS
        </span>
        <h2 class="text-3xl sm:text-4xl font-black text-gray-900 tracking-tight">認識我們的微笑大使：萌糖熊 &amp; 閃閃星</h2>
        <p class="text-gray-600 mt-3 text-base">為品牌注入高辨識度IP靈魂！結合潮玩盲盒文化與療癒陪伴經濟，打造專屬周邊延伸價值。</p>
      </div>

      <!-- Mascot Spotlight Box -->
      <div class="glass-card rounded-3xl p-6 sm:p-10 shadow-2xl border-2 border-pink-200/90 mb-12">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
          
          <!-- Mascot 3D Illustration Column -->
          <div class="lg:col-span-6 flex justify-center">
            <div class="relative w-full max-w-md rounded-3xl overflow-hidden shadow-2xl border-4 border-white bg-white group">
              <img src="assets/images/mascot.jpg" alt="Sugar Bear and Sparkle Star" class="w-full h-auto object-cover group-hover:scale-105 transition-transform duration-500">
              <div class="absolute bottom-3 left-3 right-3 bg-black/60 backdrop-blur-md rounded-2xl p-3 text-white flex items-center justify-between text-xs font-bold">
                <span class="flex items-center gap-1.5"><i data-lucide="sparkles" class="w-4 h-4 text-yellow-300"></i> 萌糖熊 Sugar Bear &amp; 閃閃星</span>
                <span class="bg-brandPink px-2.5 py-0.5 rounded-full text-[10px] font-black uppercase">Official IP</span>
              </div>
            </div>
          </div>

          <!-- Mascot Profile & Bio Column -->
          <div class="lg:col-span-6 space-y-6">
            
            <!-- Character 1 Bio -->
            <div class="p-5 rounded-2xl bg-white/90 border border-pink-100 shadow-sm space-y-2">
              <div class="flex items-center justify-between">
                <h3 class="text-xl font-black text-gray-900 flex items-center gap-2">
                  <span class="text-2xl">🐻</span> 萌糖熊 Sugar Bear
                </h3>
                <span class="text-xs font-black bg-pink-100 text-brandPink px-2.5 py-1 rounded-full">首席微笑官 (CSO)</span>
              </div>
              <p class="text-xs sm:text-sm text-gray-600 leading-relaxed">
                一隻毛茸茸的蜂蜜焦糖小熊，頭戴象徵甜蜜皇冠的粉紅小王冠、胸前繫著薄荷綠領結。最愛抱著特大號彩虹棒棒糖與剛拆封的潮玩盲盒，熱情邀請每位踏入店裡的大朋友小朋友找回童心。
              </p>
            </div>

            <!-- Character 2 Bio -->
            <div class="p-5 rounded-2xl bg-white/90 border border-yellow-100 shadow-sm space-y-2">
              <div class="flex items-center justify-between">
                <h3 class="text-xl font-black text-gray-900 flex items-center gap-2">
                  <span class="text-2xl">⭐</span> 閃閃星 Sparkle Star
                </h3>
                <span class="text-xs font-black bg-amber-100 text-amber-800 px-2.5 py-1 rounded-full">幸運魔法使</span>
              </div>
              <p class="text-xs sm:text-sm text-gray-600 leading-relaxed">
                總是伴隨在萌糖熊身旁的金色精靈星星，能施展神奇的幸運星塵。相傳只要在店內幸運轉盤轉動前向閃閃星許願，抽中隱藏版盲盒公仔的機率就會翻倍！
              </p>
            </div>

            <!-- Mascot Merch Pills -->
            <div class="space-y-2">
              <span class="text-xs font-extrabold text-gray-500 uppercase tracking-wider block">門市限定吉祥物周邊開發計畫</span>
              <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs text-center font-bold">
                <div class="bg-pink-50 p-2.5 rounded-xl border border-pink-100 text-gray-800">
                  <span class="text-brandPink block text-sm mb-0.5">🧸</span> 100% 植絨公仔
                </div>
                <div class="bg-amber-50 p-2.5 rounded-xl border border-amber-100 text-gray-800">
                  <span class="text-amber-600 block text-sm mb-0.5">💡</span> 發光觸控拍拍燈
                </div>
                <div class="bg-blue-50 p-2.5 rounded-xl border border-blue-100 text-gray-800">
                  <span class="text-brandBlue block text-sm mb-0.5">👜</span> 雙面刺繡帆布袋
                </div>
                <div class="bg-purple-50 p-2.5 rounded-xl border border-purple-100 text-gray-800">
                  <span class="text-purple-600 block text-sm mb-0.5">🍭</span> 棒棒糖超柔抱枕
                </div>
              </div>
            </div>

          </div>

        </div>
      </div>

    </div>
  </section>
'''

# New Filter Buttons
new_filter_buttons = '''
      <!-- Filter Buttons (8 Categories + All) -->
      <div class="flex flex-wrap items-center justify-center gap-2 sm:gap-2.5 mb-10">
        <button class="gallery-filter-btn active px-3.5 py-2 rounded-xl text-xs sm:text-sm font-extrabold transition-all bg-brandPink text-white shadow-md shadow-pink-200" data-filter="all">
          全部精選 (21)
        </button>
        <button class="gallery-filter-btn px-3.5 py-2 rounded-xl text-xs sm:text-sm font-extrabold transition-all bg-white text-gray-700 border border-gray-200 hover:border-pink-300 hover:text-brandPink" data-filter="gummy">
          🍭 歐美彩虹軟糖 (3)
        </button>
        <button class="gallery-filter-btn px-3.5 py-2 rounded-xl text-xs sm:text-sm font-extrabold transition-all bg-white text-gray-700 border border-gray-200 hover:border-pink-300 hover:text-brandPink" data-filter="nostalgia">
          🍬 懷舊柑仔店 (3)
        </button>
        <button class="gallery-filter-btn px-3.5 py-2 rounded-xl text-xs sm:text-sm font-extrabold transition-all bg-white text-gray-700 border border-gray-200 hover:border-pink-300 hover:text-brandPink" data-filter="blindbox">
          🧸 Z世代潮玩盲盒 (3)
        </button>
        <button class="gallery-filter-btn px-3.5 py-2 rounded-xl text-xs sm:text-sm font-extrabold transition-all bg-white text-gray-700 border border-gray-200 hover:border-pink-300 hover:text-brandPink" data-filter="stem">
          🤖 益智模型玩具 (3)
        </button>
        <button class="gallery-filter-btn px-3.5 py-2 rounded-xl text-xs sm:text-sm font-extrabold transition-all bg-white text-gray-700 border border-gray-200 hover:border-pink-300 hover:text-brandPink" data-filter="chocolate">
          🍫 精品可可生巧 (3)
        </button>
        <button class="gallery-filter-btn px-3.5 py-2 rounded-xl text-xs sm:text-sm font-extrabold transition-all bg-white text-gray-700 border border-gray-200 hover:border-pink-300 hover:text-brandPink" data-filter="diy">
          🍡 日韓手作食玩 (2)
        </button>
        <button class="gallery-filter-btn px-3.5 py-2 rounded-xl text-xs sm:text-sm font-extrabold transition-all bg-white text-gray-700 border border-gray-200 hover:border-pink-300 hover:text-brandPink" data-filter="party">
          🎁 校園派對禮盒 (2)
        </button>
        <button class="gallery-filter-btn px-3.5 py-2 rounded-xl text-xs sm:text-sm font-extrabold transition-all bg-white text-gray-700 border border-gray-200 hover:border-pink-300 hover:text-brandPink" data-filter="refreshment">
          🎰 扭蛋與彩虹飲 (2)
        </button>
      </div>
'''

# Update index.html
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Add mascot to nav
old_nav_anchor = '<a href="#gallery"'
new_nav_with_mascot = '<a href="#mascot" class="hover:text-brandPink transition-colors flex items-center gap-1 font-bold text-gray-700"><span class="text-base">🐻</span>吉祥物</a>\n        <a href="#gallery"'
if '#mascot' not in html:
    html = html.replace(old_nav_anchor, new_nav_with_mascot)

# Insert Mascot section before #gallery
if 'id="mascot"' not in html:
    html = html.replace('  <!-- ================= SECTION: PRODUCT & STORE GALLERY', mascot_section + '\n\n  <!-- ================= SECTION: PRODUCT & STORE GALLERY')

# Replace the grid inside gallery
grid_start = '<div id="galleryGrid"'
grid_end = '<!-- ================= PRODUCT DETAIL MODAL ================= -->'

# Replace filter buttons
# Locate from filter buttons to modal
import re
filter_pattern = r'<!-- Filter Buttons -->[\s\S]*?<div id="galleryGrid"'
html = re.sub(filter_pattern, new_filter_buttons + '\n      <div id="galleryGrid"', html)

# Replace cards inside galleryGrid
cards_pattern = r'<div id="galleryGrid"[^>]*>[\s\S]*?</div>\s*</div>\s*</section>'
new_grid_html = f'''<div id="galleryGrid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
{cards_joined}
      </div>
    </div>
  </section>'''

html = re.sub(cards_pattern, new_grid_html, html)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("index.html fully updated with Mascot and 21 Diverse Products!")
