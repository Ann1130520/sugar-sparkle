import os

html_path = r"C:\Users\User\.gemini\antigravity\scratch\sugar-sparkle-website\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Navigation Links
old_nav = '''      <!-- Desktop Navigation Links -->
      <nav class="hidden lg:flex items-center gap-7 text-sm font-bold text-gray-700">
        <a href="#concept" class="hover:text-brandPink transition-colors">品牌定位</a>
        <a href="#budget" class="hover:text-brandPink transition-colors">100萬資金分配</a>
        <a href="#products" class="hover:text-brandPink transition-colors">產品矩陣</a>
        <a href="#pnl" class="hover:text-brandPink transition-colors">損益分析</a>'''

new_nav = '''      <!-- Desktop Navigation Links -->
      <nav class="hidden lg:flex items-center gap-7 text-sm font-bold text-gray-700">
        <a href="#concept" class="hover:text-brandPink transition-colors">品牌定位</a>
        <a href="#budget" class="hover:text-brandPink transition-colors">100萬資金分配</a>
        <a href="#products" class="hover:text-brandPink transition-colors">產品矩陣</a>
        <a href="#gallery" class="hover:text-brandPink transition-colors font-extrabold text-brandPink flex items-center gap-1.5 bg-pink-50 px-3 py-1.5 rounded-xl border border-pink-200">
          <i data-lucide="camera" class="w-4 h-4"></i>商品照片區
        </a>
        <a href="#pnl" class="hover:text-brandPink transition-colors">損益分析</a>'''

content = content.replace(old_nav, new_nav)

# Also mobile menu
old_m_nav = '''      <a href="#concept" class="block hover:text-brandPink py-1">品牌定位</a>
      <a href="#budget" class="block hover:text-brandPink py-1">100萬資金分配</a>
      <a href="#products" class="block hover:text-brandPink py-1">產品矩陣</a>
      <a href="#pnl" class="block hover:text-brandPink py-1">損益分析</a>'''

new_m_nav = '''      <a href="#concept" class="block hover:text-brandPink py-1">品牌定位</a>
      <a href="#budget" class="block hover:text-brandPink py-1">100萬資金分配</a>
      <a href="#products" class="block hover:text-brandPink py-1">產品矩陣</a>
      <a href="#gallery" class="block hover:text-brandPink py-1 text-brandPink font-bold">📷 商品照片區</a>
      <a href="#pnl" class="block hover:text-brandPink py-1">損益分析</a>'''

content = content.replace(old_m_nav, new_m_nav)

# 2. Gallery Section HTML
gallery_html = '''

  <!-- ================= SECTION: PRODUCT & STORE GALLERY (商品照片與實景展示區) ================= -->
  <section id="gallery" class="py-16 md:py-24 bg-gradient-to-b from-white via-pink-50/40 to-white border-b border-pink-100">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <!-- Section Header -->
      <div class="text-center max-w-3xl mx-auto mb-12">
        <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-pink-100 text-brandPink text-xs font-extrabold mb-2">
          <i data-lucide="sparkles" class="w-3.5 h-3.5"></i> 實景與商品圖鑑 · PRODUCT GALLERY
        </span>
        <h2 class="text-3xl sm:text-4xl font-black text-gray-900 tracking-tight">門市概念實景與人氣商品特寫</h2>
        <p class="text-gray-600 mt-3 text-base">沉浸式視覺饗宴 — 從色彩繽紛的彩虹重力糖果牆、Z世代搶手潮玩盲盒，到客製派對禮盒。</p>
      </div>

      <!-- Flagship Store Interior Hero Banner -->
      <div class="glass-card rounded-3xl overflow-hidden mb-12 shadow-xl border-2 border-pink-200/80 group">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-0 items-center">
          <div class="lg:col-span-7 overflow-hidden relative max-h-[440px]">
            <img src="assets/images/store_interior.jpg" alt="Sugar & Sparkle Boutique Interior Design" 
                 class="w-full h-full object-cover object-center group-hover:scale-105 transition-transform duration-700">
            <div class="absolute bottom-4 left-4 bg-black/60 backdrop-blur-md text-white text-xs font-bold px-3 py-1.5 rounded-full flex items-center gap-1.5">
              <i data-lucide="eye" class="w-3.5 h-3.5 text-pink-400"></i>
              <span>3D 概念旗艦門市渲染實景</span>
            </div>
          </div>
          <div class="lg:col-span-5 p-8 sm:p-10 space-y-4">
            <div class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-emerald-50 text-emerald-700 font-extrabold text-xs">
              <i data-lucide="check-circle" class="w-3.5 h-3.5"></i> 裝潢預算 NT$ 320,000 完整落地
            </div>
            <h3 class="text-2xl sm:text-3xl font-black text-gray-900">
              彩虹重力自選糖果牆 × 潮流盲盒中島
            </h3>
            <p class="text-sm text-gray-600 leading-relaxed">
              明亮活潑的馬卡龍色調門面，搭配整面落地透明壓克力糖果分裝桶（24桶重力分裝裝置），與正版授權公仔展示發光櫃。顧客一踏入店內即沉浸在甜蜜與探索驚喜的雙重療癒體驗中。
            </p>
            <div class="grid grid-cols-2 gap-3 pt-2 text-xs font-bold">
              <div class="bg-pink-50 p-3 rounded-xl border border-pink-100">
                <span class="text-gray-400 block mb-0.5">自選糖果毛利率</span>
                <span class="text-lg font-black text-brandPink">高達 65%</span>
              </div>
              <div class="bg-blue-50 p-3 rounded-xl border border-blue-100">
                <span class="text-gray-400 block mb-0.5">盲盒平均客單價</span>
                <span class="text-lg font-black text-brandBlue">NT$ 320</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Filter Buttons -->
      <div class="flex flex-wrap items-center justify-center gap-2 sm:gap-3 mb-10">
        <button class="gallery-filter-btn active px-4 py-2 rounded-xl text-xs sm:text-sm font-extrabold transition-all bg-brandPink text-white shadow-md shadow-pink-200" data-filter="all">
          全部商品 (12)
        </button>
        <button class="gallery-filter-btn px-4 py-2 rounded-xl text-xs sm:text-sm font-extrabold transition-all bg-white text-gray-700 border border-gray-200 hover:border-pink-300 hover:text-brandPink" data-filter="candy">
          🍭 秤重自選軟糖 (3)
        </button>
        <button class="gallery-filter-btn px-4 py-2 rounded-xl text-xs sm:text-sm font-extrabold transition-all bg-white text-gray-700 border border-gray-200 hover:border-pink-300 hover:text-brandPink" data-filter="blindbox">
          🧸 潮流盲盒公仔 (3)
        </button>
        <button class="gallery-filter-btn px-4 py-2 rounded-xl text-xs sm:text-sm font-extrabold transition-all bg-white text-gray-700 border border-gray-200 hover:border-pink-300 hover:text-brandPink" data-filter="snack">
          🍫 進口精緻點心 (2)
        </button>
        <button class="gallery-filter-btn px-4 py-2 rounded-xl text-xs sm:text-sm font-extrabold transition-all bg-white text-gray-700 border border-gray-200 hover:border-pink-300 hover:text-brandPink" data-filter="toy">
          🧩 益智文創玩具 (2)
        </button>
        <button class="gallery-filter-btn px-4 py-2 rounded-xl text-xs sm:text-sm font-extrabold transition-all bg-white text-gray-700 border border-gray-200 hover:border-pink-300 hover:text-brandPink" data-filter="party">
          🎁 客製派對禮盒 (2)
        </button>
      </div>

      <!-- Product Cards Grid -->
      <div id="galleryGrid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">

        <!-- Card 1: Rainbow Candies -->
        <div class="gallery-card glass-card rounded-2xl overflow-hidden flex flex-col justify-between group" data-category="candy">
          <div class="relative overflow-hidden aspect-[4/3] bg-pink-50">
            <img src="https://images.unsplash.com/photo-1582058091505-f87a2e55a40f?auto=format&fit=crop&w=800&q=80" 
                 alt="Rainbow Gummy Candy Wall" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
            <span class="absolute top-3 left-3 bg-emerald-500 text-white font-extrabold text-[11px] px-2.5 py-1 rounded-full shadow">毛利 65%</span>
            <span class="absolute top-3 right-3 bg-pink-500 text-white font-extrabold text-[11px] px-2.5 py-1 rounded-full shadow">自選秤重</span>
          </div>
          <div class="p-5 flex-1 flex flex-col justify-between">
            <div>
              <span class="text-xs font-bold text-gray-400 block mb-1">歐美進口系列</span>
              <h4 class="text-base font-black text-gray-900 group-hover:text-brandPink transition-colors">彩虹重力自選軟糖條</h4>
              <p class="text-xs text-gray-500 mt-1 line-clamp-2">德國原裝進口酸味彩虹長條、小熊軟糖、水果爆漿夾心軟糖，香甜微酸。</p>
            </div>
            <div class="mt-4 pt-3 border-t border-gray-100 flex items-center justify-between">
              <div>
                <span class="text-xs text-gray-400 block">建議售價</span>
                <span class="text-base font-black text-brandPink">NT$ 120 <span class="text-xs font-normal text-gray-500">/ 100g</span></span>
              </div>
              <button class="open-product-modal-btn px-3 py-1.5 rounded-xl bg-pink-50 hover:bg-pink-100 text-brandPink font-extrabold text-xs transition-colors flex items-center gap-1"
                      data-title="彩虹重力自選軟糖條" data-category="秤重自選軟糖" data-price="NT$ 120 / 100g" data-cost="NT$ 42 (35%)" data-margin="65.0%" data-share="25.0%"
                      data-desc="透明重力分裝桶陳列，包含德國彩虹酸酸條、小熊軟糖、可樂軟糖與雙層水果夾心。客製化秤重模式體驗感極佳，為店內毛利率最高之現金流核心。"
                      data-img="https://images.unsplash.com/photo-1582058091505-f87a2e55a40f?auto=format&fit=crop&w=800&q=80">
                查看詳情 <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
              </button>
            </div>
          </div>
        </div>

        <!-- Card 2: Lollipops -->
        <div class="gallery-card glass-card rounded-2xl overflow-hidden flex flex-col justify-between group" data-category="candy">
          <div class="relative overflow-hidden aspect-[4/3] bg-pink-50">
            <img src="https://images.unsplash.com/photo-1575224300306-1b8da36134ec?auto=format&fit=crop&w=800&q=80" 
                 alt="Artisan Swirl Lollipops" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
            <span class="absolute top-3 left-3 bg-emerald-500 text-white font-extrabold text-[11px] px-2.5 py-1 rounded-full shadow">毛利 60%</span>
            <span class="absolute top-3 right-3 bg-amber-500 text-white font-extrabold text-[11px] px-2.5 py-1 rounded-full shadow">拍照道具</span>
          </div>
          <div class="p-5 flex-1 flex flex-col justify-between">
            <div>
              <span class="text-xs font-bold text-gray-400 block mb-1">手工藝級硬糖</span>
              <h4 class="text-base font-black text-gray-900 group-hover:text-brandPink transition-colors">巨型復古旋風棒棒糖</h4>
              <p class="text-xs text-gray-500 mt-1 line-clamp-2">鮮豔幾何旋風紋理與經典波普色彩，是小學生放學、情侶拍照最搶手的經典之作。</p>
            </div>
            <div class="mt-4 pt-3 border-t border-gray-100 flex items-center justify-between">
              <div>
                <span class="text-xs text-gray-400 block">建議售價</span>
                <span class="text-base font-black text-brandPink">NT$ 65 - 120 <span class="text-xs font-normal text-gray-500">/ 支</span></span>
              </div>
              <button class="open-product-modal-btn px-3 py-1.5 rounded-xl bg-pink-50 hover:bg-pink-100 text-brandPink font-extrabold text-xs transition-colors flex items-center gap-1"
                      data-title="巨型復古旋風棒棒糖" data-category="手工藝術硬糖" data-price="NT$ 65 - 120 / 支" data-cost="NT$ 26 - 48 (40%)" data-margin="60.0%" data-share="8.0%"
                      data-desc="純手工拉糖工藝，保留傳統經典幾何同心圓螺旋紋理，色彩繽紛吸睛。具備極高拍照上鏡度，常作為IG拍照打卡道具及幼兒園慶生小禮物。"
                      data-img="https://images.unsplash.com/photo-1575224300306-1b8da36134ec?auto=format&fit=crop&w=800&q=80">
                查看詳情 <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
              </button>
            </div>
          </div>
        </div>

        <!-- Card 3: Marshmallows -->
        <div class="gallery-card glass-card rounded-2xl overflow-hidden flex flex-col justify-between group" data-category="candy">
          <div class="relative overflow-hidden aspect-[4/3] bg-pink-50">
            <img src="https://images.unsplash.com/photo-1563729784474-d77dbb933a9e?auto=format&fit=crop&w=800&q=80" 
                 alt="Pastel Marshmallow Clouds" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
            <span class="absolute top-3 left-3 bg-emerald-500 text-white font-extrabold text-[11px] px-2.5 py-1 rounded-full shadow">毛利 58%</span>
            <span class="absolute top-3 right-3 bg-rose-400 text-white font-extrabold text-[11px] px-2.5 py-1 rounded-full shadow">少女心爆棚</span>
          </div>
          <div class="p-5 flex-1 flex flex-col justify-between">
            <div>
              <span class="text-xs font-bold text-gray-400 block mb-1">雲朵甜心系列</span>
              <h4 class="text-base font-black text-gray-900 group-hover:text-brandPink transition-colors">馬卡龍色棉花糖雲朵</h4>
              <p class="text-xs text-gray-500 mt-1 line-clamp-2">蓬鬆綿軟、低糖配方，色彩粉嫩如夢似幻，自帶高顏值伴手禮氣質。</p>
            </div>
            <div class="mt-4 pt-3 border-t border-gray-100 flex items-center justify-between">
              <div>
                <span class="text-xs text-gray-400 block">建議售價</span>
                <span class="text-base font-black text-brandPink">NT$ 85 - 160 <span class="text-xs font-normal text-gray-500">/ 袋</span></span>
              </div>
              <button class="open-product-modal-btn px-3 py-1.5 rounded-xl bg-pink-50 hover:bg-pink-100 text-brandPink font-extrabold text-xs transition-colors flex items-center gap-1"
                      data-title="馬卡龍色棉花糖雲朵" data-category="甜心棉花糖" data-price="NT$ 85 - 160 / 袋" data-cost="NT$ 35 - 67 (42%)" data-margin="58.0%" data-share="7.0%"
                      data-desc="引進粉嫩馬卡龍色系造型棉花糖，口感細緻綿軟、甜度適中。適合與自選糖果袋混合搭配，亦是製作熱可可或派對甜點桌的亮點素材。"
                      data-img="https://images.unsplash.com/photo-1563729784474-d77dbb933a9e?auto=format&fit=crop&w=800&q=80">
                查看詳情 <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
              </button>
            </div>
          </div>
        </div>

        <!-- Card 4: Blind Box -->
        <div class="gallery-card glass-card rounded-2xl overflow-hidden flex flex-col justify-between group" data-category="blindbox">
          <div class="relative overflow-hidden aspect-[4/3] bg-purple-50">
            <img src="https://images.unsplash.com/photo-1607604276583-eef5d076aa5f?auto=format&fit=crop&w=800&q=80" 
                 alt="Designer Vinyl Blind Box Figures" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
            <span class="absolute top-3 left-3 bg-purple-600 text-white font-extrabold text-[11px] px-2.5 py-1 rounded-full shadow">營收佔比 30%</span>
            <span class="absolute top-3 right-3 bg-blue-500 text-white font-extrabold text-[11px] px-2.5 py-1 rounded-full shadow">正版授權</span>
          </div>
          <div class="p-5 flex-1 flex flex-col justify-between">
            <div>
              <span class="text-xs font-bold text-gray-400 block mb-1">潮玩公仔旗艦</span>
              <h4 class="text-base font-black text-gray-900 group-hover:text-brandPurple transition-colors">Z世代正版設計師盲盒</h4>
              <p class="text-xs text-gray-500 mt-1 line-clamp-2">泡泡瑪特、三麗鷗與熱門動漫IP授權盒玩，隱藏款機率帶動收藏熱潮。</p>
            </div>
            <div class="mt-4 pt-3 border-t border-gray-100 flex items-center justify-between">
              <div>
                <span class="text-xs text-gray-400 block">建議售價</span>
                <span class="text-base font-black text-brandPurple">NT$ 320 - 380 <span class="text-xs font-normal text-gray-500">/ 盒</span></span>
              </div>
              <button class="open-product-modal-btn px-3 py-1.5 rounded-xl bg-purple-50 hover:bg-purple-100 text-brandPurple font-extrabold text-xs transition-colors flex items-center gap-1"
                      data-title="Z世代正版設計師盲盒" data-category="潮流盲盒公仔" data-price="NT$ 320 - 380 / 盒" data-cost="NT$ 198 (62%)" data-margin="38.0%" data-share="30.0%"
                      data-desc="店內營收與客單價核心驅動力！精選國內外一線潮玩IP（如三麗鷗家族、泡泡瑪特授權系列、熱門動漫），每套含12款常規+1款限量隱藏版，帶動連續開箱與社群交換。"
                      data-img="https://images.unsplash.com/photo-1607604276583-eef5d076aa5f?auto=format&fit=crop&w=800&q=80">
                查看詳情 <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
              </button>
            </div>
          </div>
        </div>

        <!-- Card 5: Plush Collectibles -->
        <div class="gallery-card glass-card rounded-2xl overflow-hidden flex flex-col justify-between group" data-category="blindbox">
          <div class="relative overflow-hidden aspect-[4/3] bg-purple-50">
            <img src="https://images.unsplash.com/photo-1566576912321-d58ddd7a6088?auto=format&fit=crop&w=800&q=80" 
                 alt="Kawaii Plushies & Collectibles" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
            <span class="absolute top-3 left-3 bg-emerald-500 text-white font-extrabold text-[11px] px-2.5 py-1 rounded-full shadow">毛利 45%</span>
            <span class="absolute top-3 right-3 bg-pink-500 text-white font-extrabold text-[11px] px-2.5 py-1 rounded-full shadow">療癒手感</span>
          </div>
          <div class="p-5 flex-1 flex flex-col justify-between">
            <div>
              <span class="text-xs font-bold text-gray-400 block mb-1">治癒系周邊</span>
              <h4 class="text-base font-black text-gray-900 group-hover:text-brandPurple transition-colors">萌系毛絨玩偶與吊飾</h4>
              <p class="text-xs text-gray-500 mt-1 line-clamp-2">細膩刺繡短絨手感，附精緻登山扣，是學生書包與上班族包包的療癒配飾。</p>
            </div>
            <div class="mt-4 pt-3 border-t border-gray-100 flex items-center justify-between">
              <div>
                <span class="text-xs text-gray-400 block">建議售價</span>
                <span class="text-base font-black text-brandPurple">NT$ 280 - 450 <span class="text-xs font-normal text-gray-500">/ 隻</span></span>
              </div>
              <button class="open-product-modal-btn px-3 py-1.5 rounded-xl bg-purple-50 hover:bg-purple-100 text-brandPurple font-extrabold text-xs transition-colors flex items-center gap-1"
                      data-title="萌系毛絨玩偶與吊飾" data-category="潮流毛絨周邊" data-price="NT$ 280 - 450 / 隻" data-cost="NT$ 154 (55%)" data-margin="45.0%" data-share="8.0%"
                      data-desc="精選日系超柔短絨玩偶，結合軟糯慢回彈內裡。除了經典小熊、兔兔造型，更搭配盲袋盲盒包裝形式販售，兼具拆袋驚喜與高實用性隨身掛飾。"
                      data-img="https://images.unsplash.com/photo-1566576912321-d58ddd7a6088?auto=format&fit=crop&w=800&q=80">
                查看詳情 <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
              </button>
            </div>
          </div>
        </div>

        <!-- Card 6: Gashapon -->
        <div class="gallery-card glass-card rounded-2xl overflow-hidden flex flex-col justify-between group" data-category="blindbox">
          <div class="relative overflow-hidden aspect-[4/3] bg-purple-50">
            <img src="https://images.unsplash.com/photo-1534447677768-be436bb09401?auto=format&fit=crop&w=800&q=80" 
                 alt="Japanese Gashapon Machine Capsules" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
            <span class="absolute top-3 left-3 bg-emerald-500 text-white font-extrabold text-[11px] px-2.5 py-1 rounded-full shadow">毛利 42%</span>
            <span class="absolute top-3 right-3 bg-amber-500 text-white font-extrabold text-[11px] px-2.5 py-1 rounded-full shadow">被動金流</span>
          </div>
          <div class="p-5 flex-1 flex flex-col justify-between">
            <div>
              <span class="text-xs font-bold text-gray-400 block mb-1">轉蛋機專區</span>
              <h4 class="text-base font-black text-gray-900 group-hover:text-brandPurple transition-colors">日本正版扭蛋膠囊盲抽</h4>
              <p class="text-xs text-gray-500 mt-1 line-clamp-2">店門口排列精選轉蛋機台，微縮模型、趣味公仔，無需人力看顧自主營收。</p>
            </div>
            <div class="mt-4 pt-3 border-t border-gray-100 flex items-center justify-between">
              <div>
                <span class="text-xs text-gray-400 block">建議售價</span>
                <span class="text-base font-black text-brandPurple">NT$ 60 - 150 <span class="text-xs font-normal text-gray-500">/ 抽</span></span>
              </div>
              <button class="open-product-modal-btn px-3 py-1.5 rounded-xl bg-purple-50 hover:bg-purple-100 text-brandPurple font-extrabold text-xs transition-colors flex items-center gap-1"
                      data-title="日本正版扭蛋膠囊盲抽" data-category="轉蛋玩具機台" data-price="NT$ 60 - 150 / 抽" data-cost="NT$ 35 - 87 (58%)" data-margin="42.0%" data-share="7.0%"
                      data-desc="設立於店門騎樓與入口處的8台雙層轉蛋機，定期引進BANDAI、TAKARA TOMY等日本正版熱門蛋品。全自動投幣/LinePay掃碼出蛋，提供無人被動收入。"
                      data-img="https://images.unsplash.com/photo-1534447677768-be436bb09401?auto=format&fit=crop&w=800&q=80">
                查看詳情 <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
              </button>
            </div>
          </div>
        </div>

        <!-- Card 7: Chocolates -->
        <div class="gallery-card glass-card rounded-2xl overflow-hidden flex flex-col justify-between group" data-category="snack">
          <div class="relative overflow-hidden aspect-[4/3] bg-blue-50">
            <img src="https://images.unsplash.com/photo-1549007994-cb92caebd54b?auto=format&fit=crop&w=800&q=80" 
                 alt="Artisan Belgian Chocolate Bars" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
            <span class="absolute top-3 left-3 bg-emerald-500 text-white font-extrabold text-[11px] px-2.5 py-1 rounded-full shadow">毛利 50%</span>
            <span class="absolute top-3 right-3 bg-blue-500 text-white font-extrabold text-[11px] px-2.5 py-1 rounded-full shadow">送禮精品</span>
          </div>
          <div class="p-5 flex-1 flex flex-col justify-between">
            <div>
              <span class="text-xs font-bold text-gray-400 block mb-1">精品可可系列</span>
              <h4 class="text-base font-black text-gray-900 group-hover:text-brandBlue transition-colors">手工堅果果乾黑巧克力磚</h4>
              <p class="text-xs text-gray-500 mt-1 line-clamp-2">比利時頂級可可原豆，手工鋪撒烘焙杏仁與草莓果乾，風味層次高雅。</p>
            </div>
            <div class="mt-4 pt-3 border-t border-gray-100 flex items-center justify-between">
              <div>
                <span class="text-xs text-gray-400 block">建議售價</span>
                <span class="text-base font-black text-brandBlue">NT$ 180 - 260 <span class="text-xs font-normal text-gray-500">/ 片</span></span>
              </div>
              <button class="open-product-modal-btn px-3 py-1.5 rounded-xl bg-blue-50 hover:bg-blue-100 text-brandBlue font-extrabold text-xs transition-colors flex items-center gap-1"
                      data-title="手工堅果果乾黑巧克力磚" data-category="精品進口巧克力" data-price="NT$ 180 - 260 / 片" data-cost="NT$ 90 - 130 (50%)" data-margin="50.0%" data-share="10.0%"
                      data-desc="針對重視品味的上班族、高中大學生與情人節客群，選用72%頂級調溫黑巧克力，搭配無防腐劑低溫凍乾果乾。具備高單價、包裝典雅特性。"
                      data-img="https://images.unsplash.com/photo-1549007994-cb92caebd54b?auto=format&fit=crop&w=800&q=80">
                查看詳情 <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
              </button>
            </div>
          </div>
        </div>

        <!-- Card 8: Japanese Treats -->
        <div class="gallery-card glass-card rounded-2xl overflow-hidden flex flex-col justify-between group" data-category="snack">
          <div class="relative overflow-hidden aspect-[4/3] bg-blue-50">
            <img src="https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=800&q=80" 
                 alt="Japanese Matcha & Specialty Biscuits" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
            <span class="absolute top-3 left-3 bg-emerald-500 text-white font-extrabold text-[11px] px-2.5 py-1 rounded-full shadow">毛利 45%</span>
            <span class="absolute top-3 right-3 bg-emerald-600 text-white font-extrabold text-[11px] px-2.5 py-1 rounded-full shadow">日系伴手</span>
          </div>
          <div class="p-5 flex-1 flex flex-col justify-between">
            <div>
              <span class="text-xs font-bold text-gray-400 block mb-1">亞洲特色點心</span>
              <h4 class="text-base font-black text-gray-900 group-hover:text-brandBlue transition-colors">日韓季節限定夾心脆餅</h4>
              <p class="text-xs text-gray-500 mt-1 line-clamp-2">宇治抹茶、草莓季限量版零嘴，包裝精美，免出國就能買到當地限定名產。</p>
            </div>
            <div class="mt-4 pt-3 border-t border-gray-100 flex items-center justify-between">
              <div>
                <span class="text-xs text-gray-400 block">建議售價</span>
                <span class="text-base font-black text-brandBlue">NT$ 150 - 220 <span class="text-xs font-normal text-gray-500">/ 盒</span></span>
              </div>
              <button class="open-product-modal-btn px-3 py-1.5 rounded-xl bg-blue-50 hover:bg-blue-100 text-brandBlue font-extrabold text-xs transition-colors flex items-center gap-1"
                      data-title="日韓季節限定夾心脆餅" data-category="進口特色零食" data-price="NT$ 150 - 220 / 盒" data-cost="NT$ 82 - 121 (55%)" data-margin="45.0%" data-share="10.0%"
                      data-desc="直接自合法進口貿易商批量採購當季最搶手的日韓超商熱門限定品，如Pocky特殊聯名款、日本白巧克力脆餅，提供消費者隨時隨地嘗鮮樂趣。"
                      data-img="https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=800&q=80">
                查看詳情 <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
              </button>
            </div>
          </div>
        </div>

        <!-- Card 9: 3D Wooden Puzzles -->
        <div class="gallery-card glass-card rounded-2xl overflow-hidden flex flex-col justify-between group" data-category="toy">
          <div class="relative overflow-hidden aspect-[4/3] bg-amber-50">
            <img src="https://images.unsplash.com/photo-1587654780291-39c9404d746b?auto=format&fit=crop&w=800&q=80" 
                 alt="3D Wooden Mechanical Puzzles" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
            <span class="absolute top-3 left-3 bg-emerald-500 text-white font-extrabold text-[11px] px-2.5 py-1 rounded-full shadow">毛利 50%</span>
            <span class="absolute top-3 right-3 bg-amber-500 text-white font-extrabold text-[11px] px-2.5 py-1 rounded-full shadow">STEM 益智</span>
          </div>
          <div class="p-5 flex-1 flex flex-col justify-between">
            <div>
              <span class="text-xs font-bold text-gray-400 block mb-1">益智教育精選</span>
              <h4 class="text-base font-black text-gray-900 group-hover:text-amber-600 transition-colors">3D 立體木質機械拼圖</h4>
              <p class="text-xs text-gray-500 mt-1 line-clamp-2">環保實木卡榫設計，無需膠水拼裝復古時鐘、音樂盒與旋轉木馬，寓教於樂。</p>
            </div>
            <div class="mt-4 pt-3 border-t border-gray-100 flex items-center justify-between">
              <div>
                <span class="text-xs text-gray-400 block">建議售價</span>
                <span class="text-base font-black text-amber-600">NT$ 250 - 390 <span class="text-xs font-normal text-gray-500">/ 組</span></span>
              </div>
              <button class="open-product-modal-btn px-3 py-1.5 rounded-xl bg-amber-50 hover:bg-amber-100 text-amber-700 font-extrabold text-xs transition-colors flex items-center gap-1"
                      data-title="3D 立體木質機械拼圖" data-category="益智文創玩具" data-price="NT$ 250 - 390 / 組" data-cost="NT$ 125 - 195 (50%)" data-margin="50.0%" data-share="8.0%"
                      data-desc="天然椴木雷射精密切割，組裝難度涵蓋國小初階到成人進階款。深受注重智力發展的家長青睞，是客單價穩定、退貨率極低的教育型品類。"
                      data-img="https://images.unsplash.com/photo-1587654780291-39c9404d746b?auto=format&fit=crop&w=800&q=80">
                查看詳情 <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
              </button>
            </div>
          </div>
        </div>

        <!-- Card 10: Fidget Toys -->
        <div class="gallery-card glass-card rounded-2xl overflow-hidden flex flex-col justify-between group" data-category="toy">
          <div class="relative overflow-hidden aspect-[4/3] bg-amber-50">
            <img src="https://images.unsplash.com/photo-1591991731833-b4807cf7ef94?auto=format&fit=crop&w=800&q=80" 
                 alt="Fidget Puzzles & Speed Cubes" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
            <span class="absolute top-3 left-3 bg-emerald-500 text-white font-extrabold text-[11px] px-2.5 py-1 rounded-full shadow">毛利 52%</span>
            <span class="absolute top-3 right-3 bg-pink-500 text-white font-extrabold text-[11px] px-2.5 py-1 rounded-full shadow">解壓熱賣</span>
          </div>
          <div class="p-5 flex-1 flex flex-col justify-between">
            <div>
              <span class="text-xs font-bold text-gray-400 block mb-1">隨身舒壓玩具</span>
              <h4 class="text-base font-black text-gray-900 group-hover:text-amber-600 transition-colors">減壓磁力魔方與競技桌遊</h4>
              <p class="text-xs text-gray-500 mt-1 line-clamp-2">磁吸順滑手感、幾何百變形狀，是學生下課互動、考前放鬆的破冰好物。</p>
            </div>
            <div class="mt-4 pt-3 border-t border-gray-100 flex items-center justify-between">
              <div>
                <span class="text-xs text-gray-400 block">建議售價</span>
                <span class="text-base font-black text-amber-600">NT$ 190 - 350 <span class="text-xs font-normal text-gray-500">/ 組</span></span>
              </div>
              <button class="open-product-modal-btn px-3 py-1.5 rounded-xl bg-amber-50 hover:bg-amber-100 text-amber-700 font-extrabold text-xs transition-colors flex items-center gap-1"
                      data-title="減壓磁力魔方與競技桌遊" data-category="文創減壓玩具" data-price="NT$ 190 - 350 / 組" data-cost="NT$ 91 - 168 (48%)" data-margin="52.0%" data-share="7.0%"
                      data-desc="結合靜音磁力卡扣與流暢軸承，設計精巧便攜。適合作為學生書包小配件，亦能於放學後引發同儕間的解題競技熱潮。"
                      data-img="https://images.unsplash.com/photo-1591991731833-b4807cf7ef94?auto=format&fit=crop&w=800&q=80">
                查看詳情 <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
              </button>
            </div>
          </div>
        </div>

        <!-- Card 11: Classroom Party Bags -->
        <div class="gallery-card glass-card rounded-2xl overflow-hidden flex flex-col justify-between group" data-category="party">
          <div class="relative overflow-hidden aspect-[4/3] bg-rose-50">
            <img src="https://images.unsplash.com/photo-1513151233558-d860c5398176?auto=format&fit=crop&w=800&q=80" 
                 alt="Classroom Birthday Goody Bags" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
            <span class="absolute top-3 left-3 bg-emerald-500 text-white font-extrabold text-[11px] px-2.5 py-1 rounded-full shadow">毛利 60%</span>
            <span class="absolute top-3 right-3 bg-rose-500 text-white font-extrabold text-[11px] px-2.5 py-1 rounded-full shadow">校園團訂爆款</span>
          </div>
          <div class="p-5 flex-1 flex flex-col justify-between">
            <div>
              <span class="text-xs font-bold text-gray-400 block mb-1">幼兒園/小學專案</span>
              <h4 class="text-base font-black text-gray-900 group-hover:text-rose-600 transition-colors">幼兒園慶生分享包 (10包起)</h4>
              <p class="text-xs text-gray-500 mt-1 line-clamp-2">客製姓名小吊牌、無防腐劑天然果膠軟糖與迷你益智擦子，家長省心首選。</p>
            </div>
            <div class="mt-4 pt-3 border-t border-gray-100 flex items-center justify-between">
              <div>
                <span class="text-xs text-gray-400 block">建議售價</span>
                <span class="text-base font-black text-rose-600">NT$ 65 - 95 <span class="text-xs font-normal text-gray-500">/ 包</span></span>
              </div>
              <button class="open-product-modal-btn px-3 py-1.5 rounded-xl bg-rose-50 hover:bg-rose-100 text-rose-700 font-extrabold text-xs transition-colors flex items-center gap-1"
                      data-title="幼兒園慶生分享包 (10包起)" data-category="校園客製禮包" data-price="NT$ 65 - 95 / 包" data-cost="NT$ 26 - 38 (40%)" data-margin="60.0%" data-share="5.0%"
                      data-desc="專門針對學校同學慶生設計，內含小熊軟糖、造型餅乾與迷你拼圖，提供客製印製小朋友英文名祝福吊卡。單次採購多為20-35包，是穩定的團體大量訂單來源。"
                      data-img="https://images.unsplash.com/photo-1513151233558-d860c5398176?auto=format&fit=crop&w=800&q=80">
                查看詳情 <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
              </button>
            </div>
          </div>
        </div>

        <!-- Card 12: Deluxe Gift Box -->
        <div class="gallery-card glass-card rounded-2xl overflow-hidden flex flex-col justify-between group" data-category="party">
          <div class="relative overflow-hidden aspect-[4/3] bg-rose-50">
            <img src="https://images.unsplash.com/photo-1549465220-1a8b9238cd48?auto=format&fit=crop&w=800&q=80" 
                 alt="Deluxe Celebration Gift Box" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
            <span class="absolute top-3 left-3 bg-emerald-500 text-white font-extrabold text-[11px] px-2.5 py-1 rounded-full shadow">毛利 65%</span>
            <span class="absolute top-3 right-3 bg-purple-600 text-white font-extrabold text-[11px] px-2.5 py-1 rounded-full shadow">節慶送禮</span>
          </div>
          <div class="p-5 flex-1 flex flex-col justify-between">
            <div>
              <span class="text-xs font-bold text-gray-400 block mb-1">節慶典藏精品</span>
              <h4 class="text-base font-black text-gray-900 group-hover:text-rose-600 transition-colors">奢華燙金客製節慶禮盒</h4>
              <p class="text-xs text-gray-500 mt-1 line-clamp-2">粉嫩燙金厚卡紙盒搭配高磅緞帶，集合限定盲盒、進口巧克力與綜合糖果。</p>
            </div>
            <div class="mt-4 pt-3 border-t border-gray-100 flex items-center justify-between">
              <div>
                <span class="text-xs text-gray-400 block">建議售價</span>
                <span class="text-base font-black text-rose-600">NT$ 450 - 680 <span class="text-xs font-normal text-gray-500">/ 盒</span></span>
              </div>
              <button class="open-product-modal-btn px-3 py-1.5 rounded-xl bg-rose-50 hover:bg-rose-100 text-rose-700 font-extrabold text-xs transition-colors flex items-center gap-1"
                      data-title="奢華燙金客製節慶禮盒" data-category="節慶客製禮盒" data-price="NT$ 450 - 680 / 盒" data-cost="NT$ 157 - 238 (35%)" data-margin="65.0%" data-share="5.0%"
                      data-desc="萬聖節驚喜包、聖誕節倒數禮盒、兒童節企業贈禮的核心主打！禮盒內含精選盲盒公仔1隻 + 進口糖果小罐裝2入 + 品牌手寫卡片，包裝極具高級感。"
                      data-img="https://images.unsplash.com/photo-1549465220-1a8b9238cd48?auto=format&fit=crop&w=800&q=80">
                查看詳情 <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
              </button>
            </div>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- ================= PRODUCT DETAIL MODAL ================= -->
  <div id="productModal" class="fixed inset-0 z-50 hidden bg-black/60 backdrop-blur-sm flex items-center justify-center p-4">
    <div class="glass-card bg-white rounded-3xl max-w-2xl w-full max-h-[90vh] overflow-y-auto p-6 sm:p-8 relative shadow-2xl animate-in fade-in zoom-in duration-200">
      
      <!-- Close Button -->
      <button id="closeProductModalBtn" class="absolute top-4 right-4 w-9 h-9 rounded-full bg-gray-100 hover:bg-gray-200 text-gray-600 flex items-center justify-center transition-colors">
        <i data-lucide="x" class="w-5 h-5"></i>
      </button>

      <div class="grid grid-cols-1 sm:grid-cols-12 gap-6 items-center">
        <!-- Modal Image -->
        <div class="sm:col-span-5 rounded-2xl overflow-hidden shadow-inner bg-pink-50 aspect-square">
          <img id="modalImg" src="" alt="Product Detail" class="w-full h-full object-cover">
        </div>

        <!-- Modal Info -->
        <div class="sm:col-span-7 space-y-3">
          <span id="modalCategory" class="text-xs font-extrabold text-brandPink bg-pink-50 px-2.5 py-1 rounded-md">Category</span>
          <h3 id="modalTitle" class="text-xl sm:text-2xl font-black text-gray-900 leading-snug">Product Title</h3>
          <p id="modalDesc" class="text-xs sm:text-sm text-gray-600 leading-relaxed">Product description text...</p>
          
          <div class="bg-gray-50 p-3.5 rounded-2xl space-y-1.5 text-xs font-semibold">
            <div class="flex justify-between"><span class="text-gray-400">建議售價:</span><span id="modalPrice" class="font-black text-brandPink text-sm">NT$ --</span></div>
            <div class="flex justify-between"><span class="text-gray-400">進貨單位成本:</span><span id="modalCost" class="font-bold text-gray-700">NT$ --</span></div>
            <div class="flex justify-between"><span class="text-gray-400">產品毛利率:</span><span id="modalMargin" class="font-black text-emerald-600">--%</span></div>
            <div class="flex justify-between"><span class="text-gray-400">營收貢獻度:</span><span id="modalShare" class="font-bold text-gray-700">--%</span></div>
          </div>

          <div class="pt-2 flex gap-3">
            <a href="https://docs.google.com/spreadsheets/d/10dj69oe44KHVzqjqfm9YEBhESA_I3HHJ52TpIxMerf4/edit" target="_blank"
               class="flex-1 py-2.5 px-4 rounded-xl bg-brandPink text-white font-extrabold text-xs text-center hover:bg-pink-600 transition-colors flex items-center justify-center gap-1.5">
              <i data-lucide="table" class="w-3.5 h-3.5"></i> 查看完整財務矩陣
            </a>
          </div>
        </div>
      </div>

    </div>
  </div>
'''

target_marker = '  <!-- ================= SECTION 4: OPEX & BREAK-EVEN ANALYSIS ================= -->'

if target_marker in content:
    content = content.replace(target_marker, gallery_html + '\n\n' + target_marker)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully updated index.html with Gallery section!")
else:
    print("Target marker not found!")
