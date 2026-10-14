html_path = r"C:\Users\User\.gemini\antigravity\scratch\sugar-sparkle-website\index.html"
js_path = r"C:\Users\User\.gemini\antigravity\scratch\sugar-sparkle-website\app.js"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Navigation to add "宣傳影片"
old_nav = '''        <a href="#concept" class="hover:text-brandPink transition-colors">品牌定位</a>
        <a href="#budget" class="hover:text-brandPink transition-colors">100萬資金分配</a>'''

new_nav = '''        <a href="#concept" class="hover:text-brandPink transition-colors">品牌定位</a>
        <a href="#video" class="hover:text-brandPink transition-colors flex items-center gap-1 font-bold text-brandPurple">
          <i data-lucide="film" class="w-4 h-4"></i>宣傳短片
        </a>
        <a href="#budget" class="hover:text-brandPink transition-colors">100萬資金分配</a>'''

html = html.replace(old_nav, new_nav)

# Mobile nav
old_m = '''      <a href="#concept" class="block hover:text-brandPink py-1">品牌定位</a>
      <a href="#budget" class="block hover:text-brandPink py-1">100萬資金分配</a>'''

new_m = '''      <a href="#concept" class="block hover:text-brandPink py-1">品牌定位</a>
      <a href="#video" class="block hover:text-brandPink py-1 text-brandPurple font-bold">🎬 形象宣傳短片</a>
      <a href="#budget" class="block hover:text-brandPink py-1">100萬資金分配</a>'''

html = html.replace(old_m, new_m)

# 2. Add Video Section between Section 1 and Section 2
video_section = '''

  <!-- ================= SECTION: BRAND COMMERCIAL VIDEO (形象宣傳短片專區) ================= -->
  <section id="video" class="py-16 md:py-24 bg-gradient-to-b from-pink-50/50 via-white to-pink-50/30 border-y border-pink-100 relative overflow-hidden">
    <!-- Ambient Glow Background -->
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-pink-200/30 rounded-full blur-3xl pointer-events-none -z-10"></div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <!-- Section Header -->
      <div class="text-center max-w-3xl mx-auto mb-12">
        <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-pink-100 text-brandPink text-xs font-extrabold mb-2">
          <i data-lucide="film" class="w-3.5 h-3.5"></i> 品牌形象廣告 · BRAND COMMERCIAL
        </span>
        <h2 class="text-3xl sm:text-4xl font-black text-gray-900 tracking-tight">沉浸式視覺饗宴 · 品牌概念宣傳短片</h2>
        <p class="text-gray-600 mt-3 text-base">將彩虹糖果牆的自選樂趣、盲盒開箱的驚喜心跳，轉化為具備社群病毒擴散力的短影音廣告。</p>
      </div>

      <!-- Main Video Theater Container -->
      <div class="max-w-4xl mx-auto glass-card rounded-3xl p-4 sm:p-6 shadow-2xl border-2 border-pink-200/90 relative group">
        
        <!-- Video Header Bar with Switcher / Customizer -->
        <div class="flex flex-col sm:flex-row items-center justify-between gap-3 pb-4 mb-4 border-b border-gray-100 text-xs">
          <div class="flex items-center gap-2">
            <span class="flex h-2.5 w-2.5 rounded-full bg-red-500 animate-pulse"></span>
            <span class="font-extrabold text-gray-800 text-sm">Sugar &amp; Sparkle 官方概念形象影片 (4K HD)</span>
          </div>
          <!-- Live YouTube Input Tool -->
          <div class="flex items-center gap-2 w-full sm:w-auto">
            <div class="relative flex-1 sm:w-72">
              <input type="text" id="videoUrlInput" placeholder="貼上 YouTube 影片網址更換..." 
                     class="w-full text-xs py-1.5 pl-3 pr-8 rounded-xl border border-gray-200 focus:outline-none focus:border-brandPink bg-gray-50/80">
              <button id="updateVideoBtn" title="點擊切換影片" class="absolute right-2 top-1/2 -translate-y-1/2 text-gray-400 hover:text-brandPink">
                <i data-lucide="arrow-right-circle" class="w-4 h-4"></i>
              </button>
            </div>
          </div>
        </div>

        <!-- 16:9 Responsive Video Player Box -->
        <div class="relative w-full aspect-video rounded-2xl overflow-hidden bg-black shadow-inner border border-pink-100">
          <iframe id="mainPromoVideo" class="w-full h-full" 
                  src="https://www.youtube.com/embed/L_LUpnjgPso?rel=0&modestbranding=1" 
                  title="Sugar & Sparkle 官方品牌概念影片" 
                  frameborder="0" 
                  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
                  allowfullscreen>
          </iframe>
        </div>

        <!-- Video Highlights & Strategy Badges -->
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 pt-6 text-center text-xs">
          <div class="p-3.5 rounded-2xl bg-pink-50/80 border border-pink-100 flex items-center gap-3">
            <div class="w-9 h-9 rounded-xl bg-brandPink text-white flex items-center justify-center shrink-0">
              <i data-lucide="smartphone" class="w-5 h-5"></i>
            </div>
            <div class="text-left">
              <span class="font-bold text-gray-900 block">TikTok &amp; Reels 短影音</span>
              <span class="text-gray-500 text-[11px]">垂直比例拍攝，專攻社群演算法</span>
            </div>
          </div>

          <div class="p-3.5 rounded-2xl bg-blue-50/80 border border-blue-100 flex items-center gap-3">
            <div class="w-9 h-9 rounded-xl bg-brandBlue text-white flex items-center justify-center shrink-0">
              <i data-lucide="sparkles" class="w-5 h-5"></i>
            </div>
            <div class="text-left">
              <span class="font-bold text-gray-900 block">沉浸式開箱體驗</span>
              <span class="text-gray-500 text-[11px]">自選糖果與隱藏版盲盒心跳實錄</span>
            </div>
          </div>

          <div class="p-3.5 rounded-2xl bg-emerald-50/80 border border-emerald-100 flex items-center gap-3">
            <div class="w-9 h-9 rounded-xl bg-emerald-500 text-white flex items-center justify-center shrink-0">
              <i data-lucide="share-2" class="w-5 h-5"></i>
            </div>
            <div class="text-left">
              <span class="font-bold text-gray-900 block">自來客口碑循環</span>
              <span class="text-gray-500 text-[11px]">網紅探店打卡零成本自然流量</span>
            </div>
          </div>
        </div>

      </div>

    </div>
  </section>
'''

target = '  <!-- ================= SECTION 2: 100萬資金分配 (CAPITAL BUDGET) ================= -->'
html = html.replace(target, video_section + '\n\n' + target)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Video section injected into index.html!")

# Update app.js to handle video switcher
with open(js_path, "r", encoding="utf-8") as f:
    js = f.read()

video_js = '''
// 5. Video Player & Switcher Logic
function initVideo() {
  const input = document.getElementById('videoUrlInput');
  const btn = document.getElementById('updateVideoBtn');
  const iframe = document.getElementById('mainPromoVideo');

  function updateVideo() {
    if (!input || !iframe) return;
    const url = input.value.trim();
    if (!url) return;

    // Parse YouTube ID
    let videoId = '';
    const match = url.match(/(?:youtu\\.be\\/|youtube\\.com\\/(?:embed\\/|v\\/|watch\\?v=|watch\\?.+&v=))([\\w-]{11})/);
    if (match && match[1]) {
      videoId = match[1];
      iframe.src = `https://www.youtube.com/embed/${videoId}?autoplay=1&rel=0`;
      input.value = '';
      alert('已成功替換宣傳短片！');
    } else {
      alert('請輸入有效的 YouTube 影片網址（例如：https://www.youtube.com/watch?v=...）');
    }
  }

  if (btn) btn.addEventListener('click', updateVideo);
  if (input) {
    input.addEventListener('keypress', (e) => {
      if (e.key === 'Enter') updateVideo();
    });
  }
}
'''

if 'initVideo()' not in js:
    js = js.replace('  initGallery();', '  initGallery();\n  initVideo();')
    js += '\n' + video_js
    with open(js_path, "w", encoding="utf-8") as f:
        f.write(js)
    print("Video logic added to app.js!")
