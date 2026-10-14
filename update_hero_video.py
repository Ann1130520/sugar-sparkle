html_path = r"C:\Users\User\.gemini\antigravity\scratch\sugar-sparkle-website\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update iframe src to real candy shop commercial video JLl_D7Ls97g
html = html.replace('src="https://www.youtube.com/embed/L_LUpnjgPso?rel=0&modestbranding=1"',
                    'src="https://www.youtube.com/embed/JLl_D7Ls97g?rel=0&modestbranding=1"')

# 2. Add Hero Watch Video Button right in the Hero CTA area
hero_old_cta = '''          <!-- Hero CTAs -->
          <div class="flex flex-col sm:flex-row items-center justify-center lg:justify-start gap-4 pt-4">
            <a href="#simulator" class="btn-candy-primary w-full sm:w-auto px-8 py-4 rounded-2xl font-black text-center text-sm sm:text-base flex items-center justify-center gap-2 shadow-lg">
              <i data-lucide="calculator" class="w-5 h-5"></i>
              <span>線上即時財務試算器</span>
            </a>
            <a href="#budget" class="btn-candy-secondary w-full sm:w-auto px-8 py-4 rounded-2xl font-black text-center text-sm sm:text-base flex items-center justify-center gap-2 shadow-lg">
              <i data-lucide="pie-chart" class="w-5 h-5"></i>
              <span>瀏覽資本與營運模型</span>
            </a>
          </div>'''

hero_new_cta = '''          <!-- Hero CTAs -->
          <div class="flex flex-col sm:flex-row flex-wrap items-center justify-center lg:justify-start gap-3.5 pt-4">
            <a href="#video" class="w-full sm:w-auto px-8 py-4 rounded-2xl font-black text-center text-sm sm:text-base flex items-center justify-center gap-2 text-white bg-gradient-to-r from-purple-600 via-pink-500 to-rose-500 shadow-xl shadow-pink-300 hover:scale-105 transition-all">
              <i data-lucide="play-circle" class="w-5 h-5 text-yellow-300 animate-pulse"></i>
              <span>▶ 觀看品牌宣傳短片</span>
            </a>
            <a href="#simulator" class="btn-candy-primary w-full sm:w-auto px-7 py-4 rounded-2xl font-black text-center text-sm sm:text-base flex items-center justify-center gap-2 shadow-lg">
              <i data-lucide="calculator" class="w-5 h-5"></i>
              <span>即時財務試算器</span>
            </a>
            <a href="#gallery" class="btn-candy-secondary w-full sm:w-auto px-7 py-4 rounded-2xl font-black text-center text-sm sm:text-base flex items-center justify-center gap-2 shadow-lg">
              <i data-lucide="camera" class="w-5 h-5"></i>
              <span>商品照片圖鑑</span>
            </a>
          </div>'''

html = html.replace(hero_old_cta, hero_new_cta)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated Hero CTAs and video src in index.html!")
