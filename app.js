// Sugar & Sparkle Interactive Web Application Logic

document.addEventListener('DOMContentLoaded', () => {
  initCharts();
  initSimulator();
  initNav();
  initGallery();
  initVideo();
});

// 1. Chart.js Visualizations
function initCharts() {
  // A. Capital Allocation Doughnut Chart
  const ctxBudget = document.getElementById('budgetDoughnutChart');
  if (ctxBudget) {
    new Chart(ctxBudget, {
      type: 'doughnut',
      data: {
        labels: [
          '門市裝潢與展示櫃 (32%)',
          '首批進貨庫存 (30%)',
          '營運週轉金 (23%)',
          '租賃押金 (7%)',
          '證照許可與開幕宣傳 (4.5%)',
          'POS與IT設備 (3.5%)'
        ],
        datasets: [{
          data: [320000, 300000, 230000, 70000, 45000, 35000],
          backgroundColor: [
            '#FF5376',
            '#3A86FF',
            '#06D6A0',
            '#FFB703',
            '#9D4EDD',
            '#FB5607'
          ],
          borderWidth: 3,
          borderColor: '#FFFFFF',
          hoverOffset: 8
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            position: 'bottom',
            labels: {
              boxWidth: 14,
              font: { size: 12, family: "'Noto Sans TC', sans-serif" },
              padding: 16
            }
          },
          tooltip: {
            callbacks: {
              label: function(context) {
                const val = context.parsed;
                const pct = ((val / 1000000) * 100).toFixed(1);
                return ` NT$ ${val.toLocaleString()} (${pct}%)`;
              }
            }
          }
        },
        cutout: '68%'
      }
    });
  }

  // B. Product Mix vs Gross Margin Chart
  const ctxProduct = document.getElementById('productMarginChart');
  if (ctxProduct) {
    new Chart(ctxProduct, {
      type: 'bar',
      data: {
        labels: ['秤重自選軟糖', '進口特色零食', '潮玩盲盒公仔', '益智文創玩具', '客製派對禮盒'],
        datasets: [
          {
            label: '營收佔比 (%)',
            data: [25, 20, 30, 15, 10],
            backgroundColor: '#8338EC',
            borderRadius: 8
          },
          {
            label: '毛利率 (%)',
            data: [65, 45, 38, 50, 60],
            backgroundColor: '#06D6A0',
            borderRadius: 8
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          y: {
            beginAtZero: true,
            max: 80,
            ticks: {
              callback: v => v + '%'
            },
            grid: { color: 'rgba(0,0,0,0.04)' }
          },
          x: {
            grid: { display: false }
          }
        },
        plugins: {
          legend: { position: 'top' },
          tooltip: {
            callbacks: {
              label: c => ` ${c.dataset.label}: ${c.parsed.y}%`
            }
          }
        }
      }
    });
  }

  // C. 3-Year Financial Growth Projection Chart
  const ctxForecast = document.getElementById('growthForecastChart');
  if (ctxForecast) {
    new Chart(ctxForecast, {
      type: 'bar',
      data: {
        labels: ['第一年 (穩定基底)', '第二年 (+20% 擴張)', '第三年 (+15% 規模化)'],
        datasets: [
          {
            type: 'bar',
            label: '年度營業額 (NT$ 仟元)',
            data: [4560, 5472, 6293],
            backgroundColor: '#3A86FF',
            borderRadius: 8,
            order: 2
          },
          {
            type: 'bar',
            label: '年度毛利額 (NT$ 仟元)',
            data: [2212, 2681, 3115],
            backgroundColor: '#06D6A0',
            borderRadius: 8,
            order: 3
          },
          {
            type: 'line',
            label: '年度淨利 (NT$ 仟元)',
            data: [952, 1289, 1559],
            borderColor: '#FF5376',
            backgroundColor: '#FF5376',
            borderWidth: 3,
            pointRadius: 6,
            pointHoverRadius: 8,
            order: 1
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          y: {
            beginAtZero: true,
            ticks: {
              callback: v => `NT$ ${v}k`
            },
            grid: { color: 'rgba(0,0,0,0.04)' }
          },
          x: { grid: { display: false } }
        },
        plugins: {
          legend: { position: 'top' }
        }
      }
    });
  }
}

// 2. Interactive Real-Time Financial Simulator
function initSimulator() {
  const atvSlider = document.getElementById('simAtv');
  const atvDisplay = document.getElementById('simAtvVal');
  const custSlider = document.getElementById('simCust');
  const custDisplay = document.getElementById('simCustVal');

  const resRevenue = document.getElementById('simResRevenue');
  const resGross = document.getElementById('simResGross');
  const resNet = document.getElementById('simResNet');
  const resMargin = document.getElementById('simResMargin');
  const resPayback = document.getElementById('simResPayback');
  const bepStatus = document.getElementById('simBepStatus');

  function calculate() {
    if (!atvSlider || !custSlider) return;
    const atv = parseInt(atvSlider.value, 10);
    const dailyCust = parseInt(custSlider.value, 10);

    atvDisplay.innerText = `NT$ ${atv}`;
    custDisplay.innerText = `${dailyCust} 人/日`;

    const monthlyRevenue = atv * dailyCust * 30;
    const blendedMargin = 0.485; // 48.5%
    const monthlyGrossProfit = monthlyRevenue * blendedMargin;
    const fixedCosts = 100000;
    const monthlyNetProfit = monthlyGrossProfit - fixedCosts;
    const netMargin = (monthlyNetProfit / monthlyRevenue) * 100;

    resRevenue.innerText = `NT$ ${Math.round(monthlyRevenue).toLocaleString()}`;
    resGross.innerText = `NT$ ${Math.round(monthlyGrossProfit).toLocaleString()}`;
    
    // Net profit formatting & styling
    if (monthlyNetProfit >= 0) {
      resNet.innerText = `+ NT$ ${Math.round(monthlyNetProfit).toLocaleString()}`;
      resNet.className = "text-2xl font-bold text-emerald-600";
      resMargin.innerText = `${netMargin.toFixed(1)}%`;
      
      const paybackMonths = 1000000 / monthlyNetProfit;
      if (paybackMonths > 0 && paybackMonths < 60) {
        resPayback.innerText = `${paybackMonths.toFixed(1)} 個月`;
      } else {
        resPayback.innerText = `> 5 年`;
      }

      bepStatus.innerHTML = `<span class="inline-flex items-center text-xs font-bold text-emerald-700 bg-emerald-100 px-3 py-1 rounded-full">✓ 獲利營運中 (超越損益平衡點 NT$ 206k)</span>`;
    } else {
      resNet.innerText = `- NT$ ${Math.abs(Math.round(monthlyNetProfit)).toLocaleString()}`;
      resNet.className = "text-2xl font-bold text-rose-600";
      resMargin.innerText = `${netMargin.toFixed(1)}% (虧損)`;
      resPayback.innerText = `未達損益點`;
      bepStatus.innerHTML = `<span class="inline-flex items-center text-xs font-bold text-rose-700 bg-rose-100 px-3 py-1 rounded-full">⚠ 尚未達成損益平衡 (需滿 31人/日)</span>`;
    }
  }

  if (atvSlider && custSlider) {
    atvSlider.addEventListener('input', calculate);
    custSlider.addEventListener('input', calculate);
    calculate();
  }
}

// 3. Navigation Controls
function initNav() {
  const toggleBtn = document.getElementById('mobileMenuBtn');
  const mobileMenu = document.getElementById('mobileMenu');

  if (toggleBtn && mobileMenu) {
    toggleBtn.addEventListener('click', () => {
      mobileMenu.classList.toggle('hidden');
    });
  }
}

// 4. Product Gallery Filter & Modal
function initGallery() {
  const filterBtns = document.querySelectorAll('.gallery-filter-btn');
  const cards = document.querySelectorAll('.gallery-card');

  // Filter functionality
  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => {
        b.classList.remove('active', 'bg-brandPink', 'text-white', 'shadow-md', 'shadow-pink-200');
        b.classList.add('bg-white', 'text-gray-700', 'border', 'border-gray-200');
      });
      btn.classList.add('active', 'bg-brandPink', 'text-white', 'shadow-md', 'shadow-pink-200');
      btn.classList.remove('bg-white', 'text-gray-700', 'border', 'border-gray-200');

      const filter = btn.getAttribute('data-filter');
      cards.forEach(card => {
        const cat = card.getAttribute('data-category');
        if (filter === 'all' || cat === filter) {
          card.style.display = 'flex';
          card.classList.add('animate-in', 'fade-in', 'zoom-in');
        } else {
          card.style.display = 'none';
        }
      });
    });
  });

  // Modal functionality
  const modal = document.getElementById('productModal');
  const closeModalBtn = document.getElementById('closeProductModalBtn');
  const modalImg = document.getElementById('modalImg');
  const modalCategory = document.getElementById('modalCategory');
  const modalTitle = document.getElementById('modalTitle');
  const modalDesc = document.getElementById('modalDesc');
  const modalPrice = document.getElementById('modalPrice');
  const modalCost = document.getElementById('modalCost');
  const modalMargin = document.getElementById('modalMargin');
  const modalShare = document.getElementById('modalShare');

  document.querySelectorAll('.open-product-modal-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      if (!modal) return;
      modalImg.src = btn.getAttribute('data-img');
      modalCategory.innerText = btn.getAttribute('data-category');
      modalTitle.innerText = btn.getAttribute('data-title');
      modalDesc.innerText = btn.getAttribute('data-desc');
      modalPrice.innerText = btn.getAttribute('data-price');
      modalCost.innerText = btn.getAttribute('data-cost');
      modalMargin.innerText = btn.getAttribute('data-margin');
      modalShare.innerText = btn.getAttribute('data-share');

      modal.classList.remove('hidden');
    });
  });

  if (closeModalBtn) {
    closeModalBtn.addEventListener('click', () => {
      modal.classList.add('hidden');
    });
  }

  if (modal) {
    modal.addEventListener('click', (e) => {
      if (e.target === modal) {
        modal.classList.add('hidden');
      }
    });
  }
}



// 5. Video Player & Multi-Category Playlist Logic
function initVideo() {
  const input = document.getElementById('videoUrlInput');
  const btn = document.getElementById('updateVideoBtn');
  const iframe = document.getElementById('mainPromoVideo');
  const currentTitle = document.getElementById('currentVideoTitle');
  const currentTag = document.getElementById('currentVideoTag');
  const playlistItems = document.querySelectorAll('.playlist-item-card');

  function playVideo(videoId, title, tag, autoplay = true) {
    if (!iframe) return;
    const autoParam = autoplay ? '1' : '0';
    iframe.src = `https://www.youtube.com/embed/${videoId}?autoplay=${autoParam}&rel=0&modestbranding=1`;
    if (currentTitle && title) currentTitle.innerText = title;
    if (currentTag && tag) currentTag.innerText = tag;

    // Update active playlist item styling
    playlistItems.forEach(item => {
      const itemVid = item.getAttribute('data-video-id');
      const playBtn = item.querySelector('.play-status-btn');
      if (itemVid === videoId) {
        item.classList.add('ring-2', 'ring-brandPink', 'bg-pink-50/80');
        item.classList.remove('bg-white');
        if (playBtn) playBtn.innerHTML = '<span class="text-brandPink font-black flex items-center gap-1">▶ 播放中</span>';
      } else {
        item.classList.remove('ring-2', 'ring-brandPink', 'bg-pink-50/80');
        item.classList.add('bg-white');
        if (playBtn) playBtn.innerHTML = '<span class="text-gray-400 group-hover:text-brandPink transition-colors flex items-center gap-1">點擊播放</span>';
      }
    });
  }

  playlistItems.forEach(item => {
    item.addEventListener('click', () => {
      const vid = item.getAttribute('data-video-id');
      const title = item.getAttribute('data-title');
      const tag = item.getAttribute('data-tag');
      playVideo(vid, title, tag, true);
      
      // Smooth scroll to theater on mobile
      if (window.innerWidth < 768) {
        const theater = document.getElementById('mainVideoTheater');
        if (theater) theater.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    });
  });

  function updateCustomVideo() {
    if (!input || !iframe) return;
    const url = input.value.trim();
    if (!url) return;

    // Parse YouTube ID
    const match = url.match(/(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?v=|watch\?.+&v=))([\w-]{11})/);
    if (match && match[1]) {
      const videoId = match[1];
      playVideo(videoId, '自訂外部播放影片', '自訂影音', true);
      input.value = '';
    } else {
      alert('請輸入有效的 YouTube 影片網址（例如：https://www.youtube.com/watch?v=...）');
    }
  }

  if (btn) btn.addEventListener('click', updateCustomVideo);
  if (input) {
    input.addEventListener('keypress', (e) => {
      if (e.key === 'Enter') updateCustomVideo();
    });
  }
}
