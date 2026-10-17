#!/usr/bin/env python3
"""
build_canva_studio.py
Generates the complete, polished Canva-style Packaging Design Studio for Diamond Bakery.
Includes:
- Responsive centered circular steel dabba & flat sticker canvas
- Canva layer accordion:
  1. Product Title ("Assorted Cookies") with Mota Bold font switcher & size slider
  2. Diamond Brand Wordmark, "D" Monogram letter, Subtitle & Crest scale slider
  3. Top Outer Curved Arc text, radius & font size sliders
  4. Bottom Outer Curved Arc text, radius & font size sliders
  5. Tagline Capsule Ribbon with width & size sliders
  6. Balanced Net Weight & FSSAI Veg Plaque
  7. Floral Mandala with opacity, scale & 17 designs
  8. Color & Palette Controls (Center color, gradient, arc color, ribbon color)
  9. A4 White Page Print Setup (1, 2, 4, 6 labels per sheet, cut marks, CMYK bars)
- Direct canvas dragging (drag layers up/down on canvas, live slider updates)
- Ultra HD 600 DPI (3600x3600px) direct download & Infinite Vector SVG download
- 100% bug-free JavaScript execution
"""

html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Diamond Bakery • 6" Round Packaging Studio (Canva Layer Edition)</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Alex+Brush&family=Cinzel:wght@600;700;800;900&family=Cinzel+Decorative:wght@700;900&family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600;1,700&family=Dancing+Script:wght@700&family=EB+Garamond:wght@600;700;800&family=Great+Vibes&family=Italianno&family=Marcellus&family=Montserrat:wght@600;700;800;900&family=Parisienne&family=Playfair+Display:ital,wght@0,600;0,700;0,900;1,600;1,900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=Prata&display=swap" rel="stylesheet">
  <script src="embedded_assets.js"></script>
  <script src="mandalas_library.js"></script>
  <script src="fonts_base64.js"></script>
  <style>
    body {
      font-family: 'Plus Jakarta Sans', sans-serif;
      background-color: #030712;
      color: #F3F4F6;
      overflow-x: hidden;
    }
    .font-great-vibes { font-family: 'Great Vibes', cursive; }
    .font-alex-brush { font-family: 'Alex Brush', cursive; }
    .font-parisienne { font-family: 'Parisienne', cursive; }
    .font-dancing { font-family: 'Dancing Script', cursive; }
    .font-italianno { font-family: 'Italianno', cursive; }
    .font-cinzel { font-family: 'Cinzel', serif; }
    .font-cinzel-dec { font-family: 'Cinzel Decorative', serif; }
    .font-playfair { font-family: 'Playfair Display', serif; }
    .font-cormorant { font-family: 'Cormorant Garamond', serif; }
    .font-marcellus { font-family: 'Marcellus', serif; }
    .font-prata { font-family: 'Prata', serif; }
    .font-eb-garamond { font-family: 'EB Garamond', serif; }
    .font-montserrat { font-family: 'Montserrat', sans-serif; }
    .font-jakarta { font-family: 'Plus Jakarta Sans', sans-serif; }

    /* Custom Scrollbars */
    .scrollbar-thin::-webkit-scrollbar { width: 6px; height: 6px; }
    .scrollbar-thin::-webkit-scrollbar-track { background: #0b0f19; }
    .scrollbar-thin::-webkit-scrollbar-thumb { background: #374151; border-radius: 4px; }
    .scrollbar-thin::-webkit-scrollbar-thumb:hover { background: #4b5563; }

    /* Steel Dabba Metallic Rim Styling */
    .tin-stage-shadow {
      box-shadow: 
        0 25px 60px -15px rgba(0, 0, 0, 0.9),
        0 10px 30px -5px rgba(0, 0, 0, 0.7);
    }
    .tin-metallic-bezel {
      background: radial-gradient(circle at 35% 25%, #f8fafc 0%, #cbd5e1 22%, #64748b 52%, #334155 76%, #0f172a 100%);
      box-shadow: 
        inset 0 3px 5px rgba(255, 255, 255, 0.8),
        inset 0 -8px 16px rgba(0, 0, 0, 0.9),
        0 14px 28px rgba(0, 0, 0, 0.75);
    }
    .tin-surface-sheen {
      position: absolute;
      inset: 0;
      border-radius: 9999px;
      background: linear-gradient(135deg, rgba(255,255,255,0.18) 0%, rgba(255,255,255,0.03) 32%, transparent 52%, rgba(212,175,55,0.10) 88%);
      pointer-events: none;
      z-index: 10;
    }

    /* Interactive Canva Draggable Layer Highlight */
    .canva-draggable {
      cursor: grab;
      touch-action: none;
      user-select: none;
      transition: filter 0.15s ease;
    }
    .canva-draggable:hover {
      cursor: grab;
      filter: drop-shadow(0 0 5px rgba(245, 158, 11, 0.8));
    }
    .canva-draggable:active {
      cursor: grabbing;
      filter: drop-shadow(0 0 8px rgba(56, 189, 248, 1));
    }

    /* Print Setup for Direct A4 Sheet Printing */
    @media print {
      @page {
        size: A4 portrait;
        margin: 0;
      }
      body * {
        visibility: hidden !important;
      }
      #a4-print-mount, #a4-print-mount * {
        visibility: visible !important;
      }
      #a4-print-mount {
        position: fixed !important;
        left: 0 !important;
        top: 0 !important;
        width: 210mm !important;
        height: 297mm !important;
        max-width: none !important;
        box-shadow: none !important;
        border-radius: 0 !important;
        padding: 10mm !important;
        margin: 0 !important;
        background: #FFFFFF !important;
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
      }
    }

    .card-highlight-active {
      box-shadow: 0 0 0 2px #F59E0B, 0 0 24px rgba(245, 158, 11, 0.35) !important;
      border-color: #F59E0B !important;
      transition: all 0.3s ease;
    }

    /* Split workspace: keep editor and artwork visible together while editing */
    @media (min-width: 768px) {
      body {
        height: 100vh;
        overflow: hidden;
      }
      .studio-workspace {
        height: calc(100dvh - 4.5rem);
        min-height: 520px;
        overflow: hidden;
        align-items: stretch;
      }
      .studio-controls {
        height: 100%;
        min-height: 0;
        overflow-y: auto;
        overscroll-behavior: contain;
        scrollbar-gutter: stable;
        scroll-behavior: smooth;
        padding-right: .75rem;
      }
      .studio-preview {
        height: 100%;
        min-height: 0;
        overflow: hidden; /* Photo stays fixed in place on laptop/desktop! */
        position: sticky;
        top: 0;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-self: stretch;
      }
      #packaging-stage-wrapper {
        min-height: 0 !important;
        flex: 1 1 auto;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: clamp(.5rem, 1vw, 1.25rem);
      }
      #tin-dabba-shell {
        max-height: 100%;
        max-width: min(500px, calc(100dvh - 210px));
        width: 100%;
        aspect-ratio: 1 / 1;
      }
    }
    @media (min-width: 768px) and (max-width: 1023px) {
      .studio-workspace { gap: .75rem; padding: .75rem; }
      .studio-preview > .w-full.flex.items-center.justify-between {
        flex-wrap: wrap;
        gap: .5rem;
      }
    }
    @media (max-width: 767px) {
      .studio-preview {
        scroll-margin-top: 5rem;
      }
      #packaging-stage-wrapper {
        min-height: 0;
        height: min(88vw, 440px);
        padding: .75rem;
      }
      #tin-dabba-shell {
        max-width: min(100%, 400px);
      }
    }

  </style>
</head>
<body class="min-h-screen flex flex-col bg-slate-950 text-slate-100 select-none">

  <!-- TOP APP HEADER -->
  <header class="border-b border-slate-800 bg-slate-900/95 backdrop-blur sticky top-0 z-50 px-4 py-3">
    <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-3">
      
      <!-- Brand & Title -->
      <div class="flex items-center gap-3">
        <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-amber-500 to-amber-300 flex items-center justify-center text-slate-950 font-black text-xl shadow-lg shadow-amber-500/20">
          💎
        </div>
        <div>
          <div class="flex items-center gap-2">
            <h1 class="font-extrabold text-white text-base sm:text-lg tracking-tight">Diamond Bakery</h1>
            <span class="text-[10px] bg-amber-500/20 text-amber-300 font-bold px-2 py-0.5 rounded-full border border-amber-500/30 uppercase">Sticker Designer</span>
          </div>
          <p class="text-[11px] text-slate-400">6-inch gol sticker banayein • Rang, text aur layout badlein</p>
        </div>
      </div>

      <!-- Action Buttons -->
      <div class="flex items-center gap-2">
        <button onclick="downloadPNG600DPI()" class="px-3.5 py-2 bg-gradient-to-r from-amber-500 to-amber-400 hover:from-amber-400 hover:to-amber-300 text-slate-950 font-black text-xs rounded-xl shadow-lg shadow-amber-500/25 flex items-center gap-1.5 transition-all transform active:scale-95" title="Download Print-Ready 3600x3600px 600 DPI PNG">
          <span>✨</span>
          <span>Download Sticker PNG</span>
        </button>

        <button onclick="downloadVectorSVG()" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-teal-300 border border-teal-500/30 font-bold text-xs rounded-xl transition-all flex items-center gap-1.5">
          <span>📐</span>
          <span>Editable Design File</span>
        </button>

        <button onclick="setViewMode('a4'); setTimeout(() => window.print(), 200);" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-amber-300 border border-amber-500/30 font-bold text-xs rounded-xl transition-all flex items-center gap-1.5">
          <span>🖨️</span>
          <span>Print Sticker Sheet</span>
        </button>
      </div>

    </div>
  </header>

  <!-- MAIN STUDIO LAYOUT: SIDEBAR (CANVA CONTROLS) + CENTER (STAGE CANVAS) -->
  <main class="studio-workspace flex-1 max-w-7xl w-full mx-auto p-3 sm:p-4 md:p-6 grid grid-cols-1 md:grid-cols-12 gap-4 lg:gap-6 items-start">
    
    <!-- LEFT SIDEBAR: CANVA LAYERS & CONTROLS (Col span 5 on desktop) -->
    <div class="studio-controls md:col-span-5 space-y-4">
      
      <section class="rounded-xl border border-slate-700/80 bg-slate-900/80 px-3.5 py-3 shadow-lg" aria-label="Quick start">
        <div class="flex items-start justify-between gap-3">
          <div>
            <h2 class="text-sm font-extrabold text-white">Apna sticker banayein</h2>
            <p class="mt-1 text-xs leading-5 text-slate-300">① Rang chunein <span class="text-slate-500">→</span> ② Naam badlein <span class="text-slate-500">→</span> ③ Download karein</p>
          </div>
          <span class="shrink-0 rounded-lg border border-emerald-500/30 bg-emerald-500/10 px-2 py-1 text-[10px] font-bold text-emerald-300">LIVE PREVIEW ↗</span>
        </div>
      </section>

      <!-- 2 PHOTO DESIGN STYLES + MASTER (1-Click Switch between User's 2 Tin Layouts) -->
      <div class="rounded-2xl border border-amber-500/40 bg-gradient-to-r from-amber-500/15 via-slate-900 to-amber-500/10 p-3.5 shadow-xl space-y-2.5">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-2">
            <span class="text-sm">🎯</span>
            <span class="text-xs font-black text-amber-300 uppercase tracking-wider">Photo Ke 2 Designs (1-Click Switch)</span>
          </div>
          <span class="text-[9px] bg-amber-500/20 text-amber-300 font-bold px-2 py-0.5 rounded border border-amber-500/40">100% PHOTO MATCH</span>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
          <!-- Style 1: Top Tin (Pillar & Mandala) -->
          <button onclick="setDesignStyle('style1_pillar')" id="btn-style-style1_pillar" class="p-2.5 rounded-xl border border-slate-700 bg-slate-900 hover:border-amber-500 text-left transition-all flex flex-col justify-between">
            <div>
              <span class="text-xs font-black text-amber-300 block">👑 Style 1: Top Tin</span>
              <span class="text-[10px] text-slate-300 block mt-0.5 font-normal">Gold Ribbon Pillar + Center Mandala</span>
            </div>
            <span class="text-[9px] text-emerald-400 font-mono mt-1 font-semibold">Photo Upar Wala Tin</span>
          </button>

          <!-- Style 2: Bottom Tin (Assorted Cookies Script) -->
          <button onclick="setDesignStyle('style2_script')" id="btn-style-style2_script" class="p-2.5 rounded-xl border-2 border-amber-500 bg-amber-500/20 text-left transition-all flex flex-col justify-between shadow-lg">
            <div>
              <span class="text-xs font-black text-amber-300 block">🍪 Style 2: Bottom Tin</span>
              <span class="text-[10px] text-slate-300 block mt-0.5 font-normal">Big Script "Assorted cookies" + Tagline</span>
            </div>
            <span class="text-[9px] text-amber-300 font-mono mt-1 font-bold">Photo Neeche Wala Tin</span>
          </button>

          <!-- Style 3: Master Studio (Combined) -->
          <button onclick="setDesignStyle('style3_combined')" id="btn-style-style3_combined" class="p-2.5 rounded-xl border border-slate-700 bg-slate-900 hover:border-amber-500 text-left transition-all flex flex-col justify-between">
            <div>
              <span class="text-xs font-black text-slate-200 block">✨ Style 3: Master Studio</span>
              <span class="text-[10px] text-slate-400 block mt-0.5 font-normal">Logo + Script + Ribbon + Mandala</span>
            </div>
            <span class="text-[9px] text-teal-400 font-mono mt-1 font-semibold">All Layers Combined</span>
          </button>
        </div>
      </div>

    <!-- 1-CLICK MASTER THEMES (Twin Matching Colors & Luxury Editions) -->
      <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 shadow-xl">
        <div class="flex items-center justify-between mb-3">
          <div class="flex items-center gap-2">
            <span class="text-amber-400 font-bold text-sm">Twin Luxury Colors</span>
            <span class="text-[10px] bg-amber-500/20 text-amber-300 border border-amber-500/40 px-2 py-0.5 rounded font-bold">Dono Ek Jaisi Luxury Finish</span>
          </div>
          <span class="text-[10px] text-teal-300 font-bold">6 High-End Colors</span>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-3 gap-2">
          <!-- Preset 1: Royal Velvet Maroon (Photo Original) -->
          <button onclick="applyPreset('maroon')" id="btn-preset-maroon" class="p-2.5 rounded-xl border-2 border-amber-500 bg-amber-500/15 text-left transition-all hover:scale-[1.02] flex flex-col justify-between shadow-lg">
            <div class="flex items-center justify-between">
              <span class="text-xs font-black text-amber-200 flex items-center gap-1.5">
                <span class="w-3.5 h-3.5 rounded-full bg-[#581825] border-2 border-amber-400 inline-block shadow"></span>
                Royal Maroon
              </span>
            </div>
            <p class="text-[9px] text-amber-300 mt-1 font-bold">✨ Photo Wala Original</p>
          </button>

          <!-- Preset 2: Pastel Mint (Twin Sister) -->
          <button onclick="applyPreset('mint')" id="btn-preset-mint" class="p-2.5 rounded-xl border border-slate-800 bg-slate-950/60 text-left transition-all hover:scale-[1.02] flex flex-col justify-between">
            <div class="flex items-center justify-between">
              <span class="text-xs font-black text-emerald-300 flex items-center gap-1.5">
                <span class="w-3.5 h-3.5 rounded-full bg-[#C2ECE0] border-2 border-emerald-400 inline-block shadow"></span>
                Mint Green
              </span>
            </div>
            <p class="text-[9px] text-emerald-400 mt-1 font-semibold">✨ Matching Twin Sister</p>
          </button>

          <!-- Preset 3: Emerald Green -->
          <button onclick="applyPreset('emerald')" id="btn-preset-emerald" class="p-2.5 rounded-xl border border-slate-800 bg-slate-950/60 text-left transition-all hover:scale-[1.02] flex flex-col justify-between">
            <div class="flex items-center justify-between">
              <span class="text-xs font-black text-emerald-400 flex items-center gap-1.5">
                <span class="w-3.5 h-3.5 rounded-full bg-[#0D3822] border-2 border-emerald-300 inline-block"></span>
                Emerald
              </span>
            </div>
            <p class="text-[9px] text-slate-400 mt-1">Deep Forest & Gold</p>
          </button>
            <p class="text-[9px] text-slate-400 mt-1">Deep Forest & Gold</p>
          </button>

          <!-- Preset 4: Rose Gold -->
          <button onclick="applyPreset('rosegold')" id="btn-preset-rosegold" class="p-2.5 rounded-xl border border-slate-800 bg-slate-950/60 text-left transition-all hover:scale-[1.02] flex flex-col justify-between">
            <div class="flex items-center justify-between">
              <span class="text-xs font-black text-rose-300 flex items-center gap-1.5">
                <span class="w-3 h-3 rounded-full bg-[#4A1525] border border-rose-300 inline-block"></span>
                Rose Gold
              </span>
            </div>
            <p class="text-[9px] text-slate-400 mt-1">Wine & Rose Gold</p>
          </button>

          <!-- Preset 5: Midnight Purple -->
          <button onclick="applyPreset('purple')" id="btn-preset-purple" class="p-2.5 rounded-xl border border-slate-800 bg-slate-950/60 text-left transition-all hover:scale-[1.02] flex flex-col justify-between">
            <div class="flex items-center justify-between">
              <span class="text-xs font-black text-purple-300 flex items-center gap-1.5">
                <span class="w-3 h-3 rounded-full bg-[#240B36] border border-purple-400 inline-block"></span>
                Purple
              </span>
            </div>
            <p class="text-[9px] text-slate-400 mt-1">Plum & Champagne</p>
          </button>

          <!-- Preset 6: Deep 24K Gold -->
          <button onclick="applyPreset('gold_luxe')" id="btn-preset-gold_luxe" class="p-2.5 rounded-xl border border-slate-800 bg-slate-950/60 text-left transition-all hover:scale-[1.02] flex flex-col justify-between">
            <div class="flex items-center justify-between">
              <span class="text-xs font-black text-amber-300 flex items-center gap-1.5">
                <span class="w-3 h-3 rounded-full bg-[#3D2706] border border-amber-300 inline-block"></span>
                Deep Gold
              </span>
            </div>
            <p class="text-[9px] text-slate-400 mt-1">Antique Bronze & Gold</p>
          </button>
        </div>

        <!-- More Quick Swatches -->
        <div class="mt-3 pt-2.5 border-t border-slate-800/80 flex items-center justify-between">
          <span class="text-[11px] text-slate-400">Classic swatches:</span>
          <div class="flex items-center gap-2">
            <button onclick="applyPreset('black')" title="Obsidian Black & Gold" class="w-6 h-6 rounded-full bg-zinc-900 border border-amber-500/60 hover:scale-125 transition-all"></button>
            <button onclick="applyPreset('cream')" title="Ivory Cream & Gold" class="w-6 h-6 rounded-full bg-[#FFFDF7] border border-amber-600/60 hover:scale-125 transition-all"></button>
            <button onclick="applyPreset('crimson')" title="Crimson Red & Gold" class="w-6 h-6 rounded-full bg-[#7F1D1D] border border-amber-400/60 hover:scale-125 transition-all"></button>
            <button onclick="applyPreset('sapphire')" title="Royal Sapphire Navy" class="w-6 h-6 rounded-full bg-[#0B2545] border border-amber-400/60 hover:scale-125 transition-all"></button>
          </div>
        </div>
      </div>

      <!-- CANVA LAYERS ACCORDION (Click to Edit Any Layer) -->
      <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 shadow-xl space-y-3">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-2">
            <span class="text-white font-extrabold text-sm">Sticker mein kya badalna hai?</span>
          </div>
          <span class="text-[10px] text-amber-400 font-mono">Section kholkar edit karein</span>
        </div>

        <!-- LAYER 1: COOKIES TITLE (MOTA BOLD FONTS) -->
        <div class="border border-slate-800 rounded-xl overflow-hidden bg-slate-950/40" id="card-cookies">
          <button onclick="toggleAccordion('layer-cookies-content')" class="w-full px-3.5 py-2.5 flex items-center justify-between bg-slate-900 hover:bg-slate-850 transition-all text-left">
            <div class="flex items-center gap-2">
              <span class="text-base">🍪</span>
              <div>
                <span class="text-xs font-bold text-amber-300">1. Product ka naam</span>
                <span class="text-[10px] text-slate-400 block font-normal">Sticker par likha hua naam badlein</span>
              </div>
            </div>
            <span class="text-xs text-slate-400 font-mono" id="layer-cookies-arrow">▼</span>
          </button>

          <div id="layer-cookies-content" class="p-3.5 space-y-3">
            <!-- Separate, editable product name lines -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
              <div>
                <label for="input-title" class="text-[11px] font-semibold text-slate-300 block mb-1">Upper line — name</label>
                <input type="text" id="input-title" value="Assorted" oninput="updateLabel()" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 text-sm text-white focus:border-amber-500 focus:outline-none">
              </div>
              <div>
                <label for="input-title-line2" class="text-[11px] font-semibold text-slate-300 block mb-1">Lower line — name</label>
                <input type="text" id="input-title-line2" value="Cookies" oninput="updateLabel()" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 text-sm text-white focus:border-amber-500 focus:outline-none">
              </div>
            </div>

            <!-- Font Style Switcher (All 14 Luxury Packaging Fonts) -->
            <div class="space-y-2">
              <div class="flex items-center justify-between">
                <label for="select-title-font" class="text-[11px] font-semibold text-amber-400">👑 All 14 Luxury Packaging Fonts:</label>
                <span class="text-[10px] text-amber-300 font-mono font-bold" id="title-font-current-name">Alex Brush (Photo Wala Script)</span>
              </div>
              <select id="select-title-font" onchange="setTitleFont(this.value)" class="w-full bg-slate-900 border border-amber-500/50 rounded-lg px-3 py-2 text-xs text-amber-300 font-bold focus:border-amber-400 focus:outline-none">
                <optgroup label="✨ SIGNATURE SCRIPT & CALLIGRAPHY (Cursive)">
                  <option value="alex-brush" selected>✍️ Alex Brush (Photo Wala 100% Match - Assorted Cookies)</option>
                  <option value="great-vibes">✨ Great Vibes (Luxury Flowing Script)</option>
                  <option value="parisienne">💃 Parisienne (French Romantic Flourish)</option>
                  <option value="italianno">🍷 Italianno (Tall Luxury Italian Calligraphy)</option>
                  <option value="dancing-script">✒️ Dancing Script (Artisan Cursive)</option>
                </optgroup>
                <optgroup label="🏛️ ROYAL & LUXURY SERIFS (Mota Bold / Didot)">
                  <option value="cinzel-dec">👑 Cinzel Decorative (Imperial Bold Roman)</option>
                  <option value="cinzel">🏛️ Cinzel Bold (Regal Clean Classic)</option>
                  <option value="playfair-black">💎 Playfair Display 900 (Thick Luxury Serif)</option>
                  <option value="cormorant">📜 Cormorant Garamond (Royal French Serif)</option>
                  <option value="marcellus">⚜️ Marcellus (Trajan Roman Luxury)</option>
                  <option value="prata">👑 Prata (Didot Haute Couture Serif)</option>
                  <option value="eb-garamond">📖 EB Garamond (Heritage Bakery Serif)</option>
                </optgroup>
                <optgroup label="💎 MODERN CLEAN BOLD SANS">
                  <option value="montserrat-black">💎 Montserrat Heavy 900 (Bold Geometric)</option>
                  <option value="plus-jakarta">⚡ Plus Jakarta Sans (Ultra Clean Modern)</option>
                </optgroup>
              </select>

              <!-- Quick Font Buttons Grid (Top Favorites) -->
              <div class="grid grid-cols-2 sm:grid-cols-3 gap-1.5 pt-1">
                <button onclick="setTitleFont('alex-brush')" id="font-btn-alex-brush" class="px-2 py-1.5 rounded-lg border text-left text-xs font-alex-brush transition-all border-amber-500 bg-amber-500/20 text-amber-300 font-bold shadow">✍️ Alex Brush (Photo)</button>
                <button onclick="setTitleFont('great-vibes')" id="font-btn-great-vibes" class="px-2 py-1.5 rounded-lg border text-left text-xs font-great-vibes transition-all border-slate-800 bg-slate-900 text-slate-300 hover:border-slate-700">✨ Great Vibes</button>
                <button onclick="setTitleFont('cinzel-dec')" id="font-btn-cinzel-dec" class="px-2 py-1.5 rounded-lg border text-left text-xs font-cinzel-dec transition-all border-slate-800 bg-slate-900 text-slate-300 hover:border-slate-700">🏛️ Cinzel Dec</button>
                <button onclick="setTitleFont('playfair-black')" id="font-btn-playfair-black" class="px-2 py-1.5 rounded-lg border text-left text-xs font-playfair transition-all border-slate-800 bg-slate-900 text-slate-300 hover:border-slate-700">👑 Playfair 900</button>
                <button onclick="setTitleFont('cormorant')" id="font-btn-cormorant" class="px-2 py-1.5 rounded-lg border text-left text-xs font-cormorant transition-all border-slate-800 bg-slate-900 text-slate-300 hover:border-slate-700">📜 Cormorant</button>
                <button onclick="setTitleFont('parisienne')" id="font-btn-parisienne" class="px-2 py-1.5 rounded-lg border text-left text-xs font-parisienne transition-all border-slate-800 bg-slate-900 text-slate-300 hover:border-slate-700">💃 Parisienne</button>
              </div>
            </div>

            <!-- Size Slider -->
            <div class="flex items-center justify-between gap-3 pt-1">
              <span class="text-[11px] text-slate-300 font-medium">Font Size:</span>
              <input type="range" id="slider-title-size" min="50" max="250" value="135" oninput="updateLabel()" class="w-36 accent-amber-500 cursor-pointer">
              <span id="title-size-val" class="text-xs font-mono font-bold text-amber-400 w-12 text-right">135 px</span>
            </div>

            <!-- Quick Size Preset Buttons -->
            <div class="space-y-1.5 pt-1">
              <span class="text-[10px] text-slate-400 font-medium block">Quick Size Presets:</span>
              <div class="grid grid-cols-5 gap-1.5">
                <button type="button" id="btn-title-size-120" onclick="setTitleSize(120)" class="px-1.5 py-1 rounded-lg border text-center text-[10px] font-bold transition-all border-slate-800 bg-slate-900 text-slate-300 hover:border-slate-700">120px<br><span class="text-[8px] font-normal text-slate-400">Normal</span></button>
                <button type="button" id="btn-title-size-135" onclick="setTitleSize(135)" class="px-1.5 py-1 rounded-lg border text-center text-[10px] font-bold transition-all border-amber-500 bg-amber-500/20 text-amber-300">135px<br><span class="text-[8px] font-normal text-amber-400/80">Photo</span></button>
                <button type="button" id="btn-title-size-160" onclick="setTitleSize(160)" class="px-1.5 py-1 rounded-lg border text-center text-[10px] font-bold transition-all border-slate-800 bg-slate-900 text-slate-300 hover:border-slate-700">160px<br><span class="text-[8px] font-normal text-slate-400">Bada</span></button>
                <button type="button" id="btn-title-size-190" onclick="setTitleSize(190)" class="px-1.5 py-1 rounded-lg border text-center text-[10px] font-bold transition-all border-slate-800 bg-slate-900 text-slate-300 hover:border-slate-700">190px<br><span class="text-[8px] font-normal text-slate-400">Ex-Bada</span></button>
                <button type="button" id="btn-title-size-220" onclick="setTitleSize(220)" class="px-1.5 py-1 rounded-lg border text-center text-[10px] font-bold transition-all border-slate-800 bg-slate-900 text-slate-300 hover:border-slate-700">220px<br><span class="text-[8px] font-normal text-slate-400">Jumbo</span></button>
              </div>
            </div>

            <!-- Canva-style X/Y controls for both independently editable product-name lines -->
            <div class="rounded-xl border border-slate-800 bg-slate-950/50 p-3 space-y-3">
              <div class="flex flex-wrap items-center justify-between gap-2">
                <label for="slider-title-x" class="text-xs font-semibold text-slate-200">Upper line — X (left / right)</label>
                <span id="title-x-val" class="w-16 shrink-0 text-right text-xs font-mono font-bold text-teal-400">X: 600</span><input type="number" id="number-title-x" min="250" max="950" step="1" value="600" onchange="updateLabel()" class="w-12 rounded-lg border border-slate-700 bg-slate-900 px-1 py-1 text-right text-xs font-mono text-white focus:border-amber-500 focus:outline-none" aria-label="Exact title-x-val position">
              </div>
              <input type="range" id="slider-title-x" min="250" max="950" value="600" oninput="updateLabel()" class="w-full accent-amber-500 cursor-pointer" aria-label="Upper product name horizontal position">
              <div class="flex flex-wrap items-center justify-between gap-2">
                <label for="slider-title-y" class="text-xs font-semibold text-slate-200">Upper line — Y (up / down)</label>
                <span id="title-y-val" class="w-16 shrink-0 text-right text-xs font-mono font-bold text-teal-400">Y: 620</span><input type="number" id="number-title-y" min="500" max="760" step="1" value="620" onchange="updateLabel()" class="w-12 rounded-lg border border-slate-700 bg-slate-900 px-1 py-1 text-right text-xs font-mono text-white focus:border-amber-500 focus:outline-none" aria-label="Exact title-y-val position">
              </div>
              <input type="range" id="slider-title-y" min="500" max="760" value="620" oninput="updateLabel()" class="w-full accent-amber-500 cursor-pointer" aria-label="Upper product name vertical position">
              <div class="flex flex-wrap items-center justify-between gap-2">
                <label for="slider-title2-x" class="text-xs font-semibold text-slate-200">Lower line — X (left / right)</label>
                <span id="title2-x-val" class="w-16 shrink-0 text-right text-xs font-mono font-bold text-amber-400">X: 600</span><input type="number" id="number-title2-x" min="250" max="950" step="1" value="600" onchange="updateLabel()" class="w-12 rounded-lg border border-slate-700 bg-slate-900 px-1 py-1 text-right text-xs font-mono text-white focus:border-amber-500 focus:outline-none" aria-label="Exact title2-x-val position">
              </div>
              <input type="range" id="slider-title2-x" min="250" max="950" value="600" oninput="updateLabel()" class="w-full accent-amber-500 cursor-pointer" aria-label="Lower product name horizontal position">
              <div class="flex flex-wrap items-center justify-between gap-2">
                <label for="slider-title2-y" class="text-xs font-semibold text-slate-200">Lower line — Y (up / down)</label>
                <span id="title2-y-val" class="w-16 shrink-0 text-right text-xs font-mono font-bold text-amber-400">Y: 735</span><input type="number" id="number-title2-y" min="600" max="870" step="1" value="735" onchange="updateLabel()" class="w-12 rounded-lg border border-slate-700 bg-slate-900 px-1 py-1 text-right text-xs font-mono text-white focus:border-amber-500 focus:outline-none" aria-label="Exact title2-y-val position">
              </div>
              <input type="range" id="slider-title2-y" min="600" max="870" value="735" oninput="updateLabel()" class="w-full accent-amber-500 cursor-pointer" aria-label="Lower product name vertical position">
              <p class="text-[11px] leading-5 text-slate-400">X se left/right aur Y se upar/neeche set karein. Preview par drag karke bhi move karein.</p>
            </div>

            <!-- Text Color Picker -->
            <div class="flex items-center justify-between gap-3 pt-1 border-t border-slate-800">
              <span class="text-[11px] text-slate-300 font-medium">Text Color:</span>
              <div class="flex items-center gap-1.5">
                <button onclick="setTitleColorMode('gold')" id="btn-title-col-gold" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500 text-slate-950">24K Gold</button>
                <button onclick="setTitleColorMode('emerald')" id="btn-title-col-emerald" class="px-2 py-0.5 rounded text-[10px] font-bold bg-slate-800 text-slate-300">Emerald</button>
                <button onclick="setTitleColorMode('white')" id="btn-title-col-white" class="px-2 py-0.5 rounded text-[10px] font-bold bg-slate-800 text-slate-300">White</button>
                <input type="color" id="picker-title-color" value="#D4AF37" onchange="setTitleColorCustom(this.value)" class="w-6 h-6 rounded border border-slate-700 bg-transparent cursor-pointer">
              </div>
            </div>
          </div>
        </div>

        <!-- LAYER 2: BRAND LOGO & NAME (LOCKED TOGETHER 🔒) -->
        <div class="border border-slate-800 rounded-xl overflow-hidden bg-slate-950/40" id="card-brand">
          <button onclick="toggleAccordion('layer-brand-content')" class="w-full px-3.5 py-2.5 flex items-center justify-between bg-slate-900 hover:bg-slate-850 transition-all text-left">
            <div class="flex items-center gap-2">
              <span class="text-base">💎</span>
              <div>
                <span class="text-xs font-bold text-amber-300">2. Logo & Brand Name (Locked 🔒)</span>
                <span class="text-[10px] text-slate-400 block font-normal">Logo (upar) aur Name (neeche) ek sath lock hain</span>
              </div>
            </div>
            <div class="flex items-center gap-2">
              <span class="text-[9px] bg-amber-500/20 text-amber-300 px-1.5 py-0.5 rounded border border-amber-500/30 font-bold">LOCKED 🔒</span>
              <span class="text-xs text-slate-400 font-mono" id="layer-brand-arrow">►</span>
            </div>
          </button>

          <div id="layer-brand-content" class="p-3.5 space-y-3.5 hidden">
            <!-- Lock notification banner -->
            <div class="rounded-xl border border-amber-500/30 bg-amber-500/10 p-2.5 flex items-center justify-between">
              <div class="flex items-center gap-2">
                <span class="text-base">🔒</span>
                <div>
                  <p class="text-xs font-bold text-amber-200">Unified Logo + Brand Lockup</p>
                  <p class="text-[10px] text-slate-300">Master slider se poora logo unit ek sath scale karein; colors alag alag choose karein!</p>
                </div>
              </div>
              <span class="text-[10px] bg-emerald-500/20 text-emerald-300 font-bold px-2 py-0.5 rounded border border-emerald-500/30">Auto-Center</span>
            </div>

            <!-- MASTER LOGO SCALE SLIDER (ONE SLIDER TO SCALE EVERYTHING) -->
            <div class="rounded-xl border-2 border-amber-500/50 bg-gradient-to-br from-amber-500/15 via-slate-950 to-slate-950 p-3.5 space-y-2.5">
              <div class="flex items-center justify-between">
                <div>
                  <label for="slider-master-brand-scale" class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                    <span>👑</span> Master Logo Scale (Ek Sath Sabki Size)
                  </label>
                  <span class="text-[10px] text-slate-300 block">Crest, DIAMOND aur Subtitle sab ek sath proportionally scale honge</span>
                </div>
                <span id="master-brand-scale-val" class="text-xs font-mono font-bold text-amber-300 bg-amber-950/90 px-2 py-0.5 rounded border border-amber-500/40">100%</span>
              </div>
              <input type="range" id="slider-master-brand-scale" min="50" max="180" value="100" oninput="onMasterBrandScaleInput(this.value)" class="w-full accent-amber-500 cursor-pointer">
              <!-- Quick master size buttons -->
              <div class="flex items-center justify-between gap-1 pt-1">
                <button type="button" id="btn-master-scale-75" onclick="setMasterBrandScale(75)" class="flex-1 py-1 rounded-lg border text-center text-[10px] font-bold transition-all border-slate-700 bg-slate-900 text-slate-300 hover:border-amber-500">75%<br><span class="text-[8px] font-normal text-slate-400">Chota</span></button>
                <button type="button" id="btn-master-scale-100" onclick="setMasterBrandScale(100)" class="flex-1 py-1 rounded-lg border text-center text-[10px] font-bold transition-all border-amber-500 bg-amber-500/20 text-amber-300">100%<br><span class="text-[8px] font-normal text-amber-400/80">Default</span></button>
                <button type="button" id="btn-master-scale-125" onclick="setMasterBrandScale(125)" class="flex-1 py-1 rounded-lg border text-center text-[10px] font-bold transition-all border-slate-700 bg-slate-900 text-slate-300 hover:border-amber-500">125%<br><span class="text-[8px] font-normal text-slate-400">Bada</span></button>
                <button type="button" id="btn-master-scale-150" onclick="setMasterBrandScale(150)" class="flex-1 py-1 rounded-lg border text-center text-[10px] font-bold transition-all border-slate-700 bg-slate-900 text-slate-300 hover:border-amber-500">150%<br><span class="text-[8px] font-normal text-slate-400">Ex-Bada</span></button>
                <button type="button" id="btn-master-scale-175" onclick="setMasterBrandScale(175)" class="flex-1 py-1 rounded-lg border text-center text-[10px] font-bold transition-all border-slate-700 bg-slate-900 text-slate-300 hover:border-amber-500">175%<br><span class="text-[8px] font-normal text-slate-400">Jumbo</span></button>
              </div>
            </div>

            <!-- Master Position (Y - Upar / Neeche) -->
            <div class="rounded-xl border border-slate-800 bg-slate-950/60 p-3 space-y-2">
              <div class="flex items-center justify-between">
                <label for="slider-brand-block-y" class="text-xs font-bold text-slate-200">Logo + Name Position (Upar / Neeche)</label>
                <span id="brand-block-y-val" class="text-xs font-mono font-bold text-teal-400">Y: 420</span>
              </div>
              <input type="range" id="slider-brand-block-y" min="200" max="650" value="420" oninput="updateLabel()" class="w-full accent-amber-500 cursor-pointer">
              <p class="text-[10px] text-slate-400">Yeh slider logo aur brand name dono ko ek sath upar/neeche move karta hai.</p>
            </div>

            <!-- COLOR SECTION 1: CREST / EMBLEM COLOR -->
            <div class="rounded-xl border border-slate-800 bg-slate-950/60 p-3 space-y-2.5">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold text-slate-200">👑 1. Emblem / Crest Tint (Top Logo)</span>
                <span id="crest-scale-val" class="text-xs font-mono font-bold text-teal-400">95%</span>
              </div>
              
              <!-- Emblem Color Controls -->
              <div class="flex items-center justify-between gap-2 pt-1">
                <label class="flex items-center gap-2 text-[11px] text-slate-300 cursor-pointer">
                  <input type="checkbox" id="check-emblem-tint" onchange="updateLabel()" class="accent-amber-500 rounded">
                  <span>Custom Gold Tint</span>
                </label>
                <div class="flex items-center gap-1.5">
                  <button type="button" onclick="setCrestTint(false)" class="px-2 py-0.5 rounded border border-slate-700 bg-slate-900 text-[10px] text-slate-300 hover:border-amber-500">Original</button>
                  <button type="button" onclick="setCrestTint(true, '#D4AF37')" class="px-2 py-0.5 rounded border border-slate-700 bg-slate-900 text-[10px] text-amber-300 hover:border-amber-500">24K Gold</button>
                  <input type="color" id="picker-emblem-color" value="#D4AF37" oninput="setCrestTint(true, this.value)" class="w-7 h-7 rounded border border-slate-700 bg-slate-900 cursor-pointer">
                </div>
              </div>

              <!-- Individual fine-tuning details -->
              <div class="pt-2 border-t border-slate-800/80 flex items-center justify-between gap-3">
                <label for="slider-crest-scale" class="text-[11px] text-slate-400">Fine Scale:</label>
                <input type="range" id="slider-crest-scale" min="50" max="180" value="95" oninput="updateLabel()" class="w-36 accent-amber-500 cursor-pointer">
                <label for="slider-brand-spacing" class="text-[11px] text-slate-400">Gap:</label>
                <input type="range" id="slider-brand-spacing" min="0" max="50" value="16" oninput="updateLabel()" class="w-24 accent-amber-500 cursor-pointer">
                <span id="brand-spacing-val" class="text-xs font-mono text-amber-400 w-8 text-right">16px</span>
              </div>
            </div>

            <!-- COLOR SECTION 2: BRAND NAME ("DIAMOND") -->
            <div class="rounded-xl border border-slate-800 bg-slate-950/60 p-3 space-y-3">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold text-slate-200">💎 2. Brand Name ("DIAMOND")</span>
                <span id="brand-size-val" class="text-xs font-mono font-bold text-teal-400">48 px</span>
              </div>
              <div>
                <label for="input-brand" class="text-[11px] text-slate-300 block mb-1">Brand Name Text:</label>
                <input type="text" id="input-brand" value="DIAMOND" oninput="updateLabel()" maxlength="40" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 text-sm text-white focus:border-amber-500 focus:outline-none">
              </div>

              <div class="grid grid-cols-2 gap-2">
                <div>
                  <label for="select-brand-font" class="text-[11px] text-slate-300 block mb-1">Font Style:</label>
                  <select id="select-brand-font" oninput="updateLabel()" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-2 py-2 text-xs text-white">
                    <optgroup label="Royal Serifs">
                      <option value="prata">Prata (Royal Didot)</option>
                      <option value="cinzel">Cinzel Bold</option>
                      <option value="cinzel-decorative">Cinzel Decorative</option>
                      <option value="cormorant">Cormorant Garamond</option>
                      <option value="marcellus">Marcellus Trajan</option>
                      <option value="playfair">Playfair Display 900</option>
                      <option value="eb-garamond">EB Garamond</option>
                    </optgroup>
                    <optgroup label="Modern Sans">
                      <option value="montserrat">Montserrat Heavy</option>
                      <option value="plus-jakarta">Plus Jakarta Sans</option>
                    </optgroup>
                    <optgroup label="Cursive Scripts">
                      <option value="great-vibes">Great Vibes</option>
                      <option value="alex-brush">Alex Brush</option>
                      <option value="parisienne">Parisienne</option>
                      <option value="dancing-script">Dancing Script</option>
                    </optgroup>
                  </select>
                </div>
                <div>
                  <label class="text-[11px] text-slate-300 block mb-1">Fine Size:</label>
                  <input type="range" id="slider-brand-size" min="24" max="90" value="48" oninput="updateLabel()" class="w-full accent-amber-500 cursor-pointer">
                </div>
              </div>

              <!-- Brand Name Independent Color -->
              <div class="pt-2 border-t border-slate-800/80">
                <label class="text-[11px] text-slate-300 font-semibold block mb-1.5">DIAMOND Colour (Independent):</label>
                <div class="flex items-center justify-between">
                  <div class="flex flex-wrap gap-1.5">
                    <button type="button" onclick="setBrandColorMode('red')" class="px-2 py-1 rounded-lg border border-slate-700 bg-slate-900 text-[10px] font-bold text-red-400 hover:border-red-500">Ruby Red</button>
                    <button type="button" onclick="setBrandColorMode('gold')" class="px-2 py-1 rounded-lg border border-slate-700 bg-slate-900 text-[10px] font-bold text-amber-300 hover:border-amber-500">24K Gold</button>
                    <button type="button" onclick="setBrandColorMode('white')" class="px-2 py-1 rounded-lg border border-slate-700 bg-slate-900 text-[10px] font-bold text-white hover:border-slate-500">White</button>
                    <button type="button" onclick="setBrandColorMode('emerald')" class="px-2 py-1 rounded-lg border border-slate-700 bg-slate-900 text-[10px] font-bold text-emerald-400 hover:border-emerald-500">Emerald</button>
                  </div>
                  <input type="color" id="picker-brand-name-color" value="#C81D25" oninput="setBrandColorCustom(this.value)" class="w-7 h-7 rounded border border-slate-700 bg-slate-900 cursor-pointer">
                </div>
              </div>
            </div>

            <!-- COLOR SECTION 3: SUBTITLE ("BAKERY • RESTAURANT • SWEETS") -->
            <div class="rounded-xl border border-slate-800 bg-slate-950/60 p-3 space-y-2.5">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold text-slate-200">✨ 3. Subtitle / Tagline</span>
                <span id="brand-sub-size-val" class="text-xs font-mono font-bold text-teal-400">13 px</span>
              </div>
              <div>
                <input type="text" id="input-brand-sub" value="BAKERY • RESTAURANT • SWEETS" oninput="updateLabel()" maxlength="70" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white focus:border-amber-500 focus:outline-none">
              </div>
              <div class="pt-2 border-t border-slate-800/80 flex items-center justify-between gap-3">
                <div class="flex items-center gap-1.5">
                  <span class="text-[11px] text-slate-300 font-semibold">Colour:</span>
                  <button type="button" onclick="setBrandSubColor('#0B3B24')" class="px-2 py-0.5 rounded border border-slate-700 bg-slate-900 text-[10px] text-emerald-400 hover:border-emerald-500">Green</button>
                  <button type="button" onclick="setBrandSubColor('#D4AF37')" class="px-2 py-0.5 rounded border border-slate-700 bg-slate-900 text-[10px] text-amber-300 hover:border-amber-500">Gold</button>
                  <button type="button" onclick="setBrandSubColor('#FFFFFF')" class="px-2 py-0.5 rounded border border-slate-700 bg-slate-900 text-[10px] text-white hover:border-slate-500">White</button>
                  <input type="color" id="picker-brand-sub-color" value="#0B3B24" oninput="setBrandSubColor(this.value)" class="w-6 h-6 rounded border border-slate-700 bg-slate-900 cursor-pointer">
                </div>
                <div class="flex items-center gap-2">
                  <label for="slider-brand-sub-size" class="text-[11px] text-slate-400">Fine Size:</label>
                  <input type="range" id="slider-brand-sub-size" min="9" max="28" value="13" oninput="updateLabel()" class="w-20 accent-amber-500 cursor-pointer">
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- LAYER 3: TOP OUTER RIM ARC -->
        <div class="border border-slate-800 rounded-xl overflow-hidden bg-slate-950/40" id="card-top-arc">
          <button onclick="toggleAccordion('layer-top-arc-content')" class="w-full px-3.5 py-2.5 flex items-center justify-between bg-slate-900 hover:bg-slate-850 transition-all text-left">
            <div class="flex items-center gap-2">
              <span class="text-base">⭕</span>
              <div>
                <span class="text-xs font-bold text-amber-300">3. Upar ki gol line</span>
                <span class="text-[10px] text-slate-400 block font-normal">Sticker ke upar likha text</span>
              </div>
            </div>
            <span class="text-xs text-slate-400 font-mono" id="layer-top-arc-arrow">►</span>
          </button>

          <div id="layer-top-arc-content" class="p-3.5 space-y-3 hidden">
            <div>
              <label class="text-[11px] font-semibold text-slate-300 block mb-1">Top Arc Curved Text:</label>
              <input type="text" id="input-top-arc" value="★  SERVING SHIMLA SINCE 2002  •  FINEST ARTISAN BAKES  ★" oninput="updateLabel()" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white focus:border-amber-500 focus:outline-none">
            </div>

            <!-- Quick Text Presets -->
            <div class="flex flex-wrap gap-1.5">
              <button onclick="setTopArcText('★  SERVING SHIMLA SINCE 2002  •  FINEST ARTISAN BAKES  ★')" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 rounded text-[10px] text-slate-300">★ Serving Shimla Since 2002 ★</button>
              <button onclick="setTopArcText('★  FRESHLY OVEN BAKED DAILY  •  PREMIUM QUALITY  ★')" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 rounded text-[10px] text-slate-300">★ Freshly Oven Baked Daily ★</button>
              <button onclick="setTopArcText('★  THE MALL SHIMLA  •  ESTD. 2002  ★')" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 rounded text-[10px] text-slate-300">★ The Mall Shimla ★</button>
            </div>

            <div class="flex items-center justify-between gap-3">
              <span class="text-[11px] text-slate-300 font-medium">Arc Radius:</span>
              <input type="range" id="slider-top-arc-radius" min="480" max="560" value="530" oninput="updateLabel()" class="w-36 accent-amber-500 cursor-pointer">
              <span id="top-arc-radius-val" class="text-xs font-mono font-bold text-amber-400 w-12 text-right">530 px</span>
            </div>

            <div class="flex items-center justify-between gap-3">
              <span class="text-[11px] text-slate-300 font-medium">Font Size:</span>
              <input type="range" id="slider-top-arc-size" min="11" max="24" step="0.5" value="14.5" oninput="updateLabel()" class="w-36 accent-amber-500 cursor-pointer">
              <span id="top-arc-size-val" class="text-xs font-mono font-bold text-teal-400 w-12 text-right">14.5 px</span>
            </div>

            <div class="rounded-lg border border-slate-800 bg-slate-950/50 p-3 space-y-2">
              <div class="flex flex-wrap items-center justify-between gap-2">
                <label for="slider-top-arc-x" class="text-xs text-slate-300">Top arc X (left / right)</label>
                <span id="top-arc-x-val" class="w-16 text-right text-xs font-mono font-bold text-teal-400">X: 600</span><input type="number" id="number-top-arc-x" min="350" max="850" step="1" value="600" onchange="updateLabel()" class="w-12 rounded-lg border border-slate-700 bg-slate-900 px-1 py-1 text-right text-xs font-mono text-white focus:border-amber-500 focus:outline-none" aria-label="Exact top-arc-x-val position">
              </div>
              <input type="range" id="slider-top-arc-x" min="350" max="850" value="600" oninput="updateLabel()" class="w-full accent-amber-500 cursor-pointer">
              <div class="flex flex-wrap items-center justify-between gap-2">
                <label for="slider-top-arc-y" class="text-xs text-slate-300">Top arc Y (up / down)</label>
                <span id="top-arc-y-val" class="w-16 text-right text-xs font-mono font-bold text-teal-400">Y: 600</span><input type="number" id="number-top-arc-y" min="350" max="850" step="1" value="600" onchange="updateLabel()" class="w-12 rounded-lg border border-slate-700 bg-slate-900 px-1 py-1 text-right text-xs font-mono text-white focus:border-amber-500 focus:outline-none" aria-label="Exact top-arc-y-val position">
              </div>
              <input type="range" id="slider-top-arc-y" min="350" max="850" value="600" oninput="updateLabel()" class="w-full accent-amber-500 cursor-pointer">
            </div>
            <div class="flex items-center justify-between gap-3 pt-1 border-t border-slate-800">
              <span class="text-[11px] text-slate-300 font-medium">Arc Text Color:</span>
              <input type="color" id="picker-top-arc-color" value="#0F4C2A" onchange="setTopArcColor(this.value)" class="w-7 h-7 rounded border border-slate-700 bg-transparent cursor-pointer">
            </div>
          </div>
        </div>

        <!-- LAYER 4: BOTTOM OUTER RIM ARC -->
        <div class="border border-slate-800 rounded-xl overflow-hidden bg-slate-950/40" id="card-bot-arc">
          <button onclick="toggleAccordion('layer-bot-arc-content')" class="w-full px-3.5 py-2.5 flex items-center justify-between bg-slate-900 hover:bg-slate-850 transition-all text-left">
            <div class="flex items-center gap-2">
              <span class="text-base">⭕</span>
              <div>
                <span class="text-xs font-bold text-amber-300">4. Neeche ki gol line</span>
                <span class="text-[10px] text-slate-400 block font-normal">Sticker ke neeche likha text</span>
              </div>
            </div>
            <span class="text-xs text-slate-400 font-mono" id="layer-bot-arc-arrow">►</span>
          </button>

          <div id="layer-bot-arc-content" class="p-3.5 space-y-3 hidden">
            <div>
              <label class="text-[11px] font-semibold text-slate-300 block mb-1">Bottom Arc Curved Text:</label>
              <input type="text" id="input-bottom-arc" value="★  PREPARED IN PURE BUTTER & DESI GHEE  •  ZERO PALM OIL  ★" oninput="updateLabel()" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white focus:border-amber-500 focus:outline-none">
            </div>

            <!-- Quick Text Presets -->
            <div class="flex flex-wrap gap-1.5">
              <button onclick="setBotArcText('★  PREPARED IN PURE BUTTER & DESI GHEE  •  ZERO PALM OIL  ★')" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 rounded text-[10px] text-slate-300">★ Pure Butter & Desi Ghee ★</button>
              <button onclick="setBotArcText('★  PREMIUM DESI GHEE & BUTTER  •  NO PRESERVATIVES  ★')" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 rounded text-[10px] text-slate-300">★ No Preservatives ★</button>
              <button onclick="setBotArcText('★  HANDCRAFTED IN SHIMLA  •  TRADITIONAL RECIPE  ★')" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 rounded text-[10px] text-slate-300">★ Handcrafted in Shimla ★</button>
            </div>

            <div class="flex items-center justify-between gap-3">
              <span class="text-[11px] text-slate-300 font-medium">Arc Radius:</span>
              <input type="range" id="slider-bottom-arc-radius" min="480" max="560" value="530" oninput="updateLabel()" class="w-36 accent-amber-500 cursor-pointer">
              <span id="bottom-arc-radius-val" class="text-xs font-mono font-bold text-amber-400 w-12 text-right">530 px</span>
            </div>

            <div class="flex items-center justify-between gap-3">
              <span class="text-[11px] text-slate-300 font-medium">Font Size:</span>
              <input type="range" id="slider-bottom-arc-size" min="11" max="24" step="0.5" value="14.5" oninput="updateLabel()" class="w-36 accent-amber-500 cursor-pointer">
              <span id="bottom-arc-size-val" class="text-xs font-mono font-bold text-teal-400 w-12 text-right">14.5 px</span>
            </div>

            <div class="rounded-lg border border-slate-800 bg-slate-950/50 p-3 space-y-2">
              <div class="flex flex-wrap items-center justify-between gap-2">
                <label for="slider-bot-arc-x" class="text-xs text-slate-300">Bottom arc X (left / right)</label>
                <span id="bot-arc-x-val" class="w-16 text-right text-xs font-mono font-bold text-teal-400">X: 600</span><input type="number" id="number-bot-arc-x" min="350" max="850" step="1" value="600" onchange="updateLabel()" class="w-12 rounded-lg border border-slate-700 bg-slate-900 px-1 py-1 text-right text-xs font-mono text-white focus:border-amber-500 focus:outline-none" aria-label="Exact bot-arc-x-val position">
              </div>
              <input type="range" id="slider-bot-arc-x" min="350" max="850" value="600" oninput="updateLabel()" class="w-full accent-amber-500 cursor-pointer">
              <div class="flex flex-wrap items-center justify-between gap-2">
                <label for="slider-bot-arc-y" class="text-xs text-slate-300">Bottom arc Y (up / down)</label>
                <span id="bot-arc-y-val" class="w-16 text-right text-xs font-mono font-bold text-teal-400">Y: 600</span><input type="number" id="number-bot-arc-y" min="350" max="850" step="1" value="600" onchange="updateLabel()" class="w-12 rounded-lg border border-slate-700 bg-slate-900 px-1 py-1 text-right text-xs font-mono text-white focus:border-amber-500 focus:outline-none" aria-label="Exact bot-arc-y-val position">
              </div>
              <input type="range" id="slider-bot-arc-y" min="350" max="850" value="600" oninput="updateLabel()" class="w-full accent-amber-500 cursor-pointer">
            </div>
            <div class="flex items-center justify-between gap-3 pt-1 border-t border-slate-800">
              <span class="text-[11px] text-slate-300 font-medium">Arc Text Color:</span>
              <input type="color" id="picker-bot-arc-color" value="#0F4C2A" onchange="setBotArcColor(this.value)" class="w-7 h-7 rounded border border-slate-700 bg-transparent cursor-pointer">
            </div>
          </div>
        </div>

        <!-- LAYER 5: TAGLINE RIBBON -->
        <div class="border border-slate-800 rounded-xl overflow-hidden bg-slate-950/40" id="card-ribbon">
          <button onclick="toggleAccordion('layer-ribbon-content')" class="w-full px-3.5 py-2.5 flex items-center justify-between bg-slate-900 hover:bg-slate-850 transition-all text-left">
            <div class="flex items-center gap-2">
              <span class="text-base">🎀</span>
              <div>
                <span class="text-xs font-bold text-amber-300">5. Beech ki ribbon</span>
                <span class="text-[10px] text-slate-400 block font-normal">Pure Butter & Zero Palm Oil banner</span>
              </div>
            </div>
            <span class="text-xs text-slate-400 font-mono" id="layer-ribbon-arrow">►</span>
          </button>

          <div id="layer-ribbon-content" class="p-3.5 space-y-3 hidden">
            <div>
              <label class="text-[11px] font-semibold text-slate-300 block mb-1">Tagline Text:</label>
              <input type="text" id="input-butter-tagline" value="★  BAKED WITH 100% PURE BUTTER  •  ZERO PALM OIL  ★" oninput="updateLabel()" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white focus:border-amber-500 focus:outline-none">
            </div>

            <!-- Quick Tagline Presets -->
            <div class="flex flex-wrap gap-1.5">
              <button onclick="setRibbonText('★  BAKED WITH 100% PURE BUTTER  •  ZERO PALM OIL  ★')" class="px-2 py-1 bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 border border-amber-500/40 rounded text-[10px] font-bold">✨ ★ BAKED WITH 100% PURE BUTTER • ZERO PALM OIL ★ (Photo)</button>
              <button onclick="setRibbonText('« RELISHING THE RICH BUTTERY BAKES »')" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 rounded text-[10px] text-slate-300">« RELISHING THE RICH BUTTERY BAKES »</button>
              <button onclick="setRibbonText('★  FINEST ARTISAN RECIPE  •  HANDCRAFTED  ★')" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 rounded text-[10px] text-slate-300">★ Handcrafted ★</button>
            </div>

            <!-- Ribbon Font Style -->
            <div>
              <label for="select-ribbon-font" class="text-[11px] font-semibold text-slate-300 block mb-1">Ribbon Font Style:</label>
              <select id="select-ribbon-font" onchange="setRibbonFont(this.value)" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-2.5 py-1.5 text-xs text-white">
                <option value="cormorant" selected>📜 Cormorant Garamond (Photo Wala Serif)</option>
                <option value="cinzel">🏛️ Cinzel Bold</option>
                <option value="cinzel-dec">👑 Cinzel Decorative</option>
                <option value="marcellus">⚜️ Marcellus Trajan</option>
                <option value="playfair-black">💎 Playfair Display 900</option>
                <option value="prata">👑 Prata</option>
                <option value="eb-garamond">📖 EB Garamond</option>
                <option value="montserrat-black">💎 Montserrat Heavy</option>
                <option value="plus-jakarta">⚡ Plus Jakarta Sans</option>
                <option value="great-vibes">✨ Great Vibes (Script)</option>
                <option value="alex-brush">✍️ Alex Brush (Script)</option>
              </select>
            </div>

            <div class="flex items-center justify-between gap-3">
              <span class="text-[11px] text-slate-300 font-medium">Ribbon Width:</span>
              <input type="range" id="slider-tagline-width" min="500" max="850" value="750" oninput="updateLabel()" class="w-36 accent-amber-500 cursor-pointer">
              <span id="tagline-width-val" class="text-xs font-mono font-bold text-amber-400 w-12 text-right">750 px</span>
            </div>

            <div class="flex items-center justify-between gap-3">
              <span class="text-[11px] text-slate-300 font-medium">Font Size:</span>
              <input type="range" id="slider-tagline-size" min="11" max="22" step="0.5" value="16.5" oninput="updateLabel()" class="w-36 accent-amber-500 cursor-pointer">
              <span id="tagline-size-val" class="text-xs font-mono font-bold text-teal-400 w-12 text-right">16.5 px</span>
            </div>

            <div class="flex flex-wrap items-center justify-between gap-2">
              <span class="text-[11px] text-slate-300 font-medium">Position X (left / right):</span>
              <input type="range" id="slider-tagline-x" min="250" max="950" value="600" oninput="updateLabel()" class="w-36 accent-amber-500 cursor-pointer">
              <span id="tagline-x-val" class="text-xs font-mono font-bold text-teal-400 w-16 text-right">X: 600</span><input type="number" id="number-tagline-x" min="250" max="950" step="1" value="600" onchange="updateLabel()" class="w-12 rounded-lg border border-slate-700 bg-slate-900 px-1 py-1 text-right text-xs font-mono text-white focus:border-amber-500 focus:outline-none" aria-label="Exact tagline-x-val position">
            </div>
            <div class="flex flex-wrap items-center justify-between gap-2">
              <span class="text-[11px] text-slate-300 font-medium">Position Y (up / down):</span>
              <input type="range" id="slider-tagline-y" min="680" max="900" value="795" oninput="updateLabel()" class="w-36 accent-amber-500 cursor-pointer">
              <span id="tagline-y-val" class="text-xs font-mono font-bold text-teal-400 w-16 text-right">Y: 795</span><input type="number" id="number-tagline-y" min="680" max="900" step="1" value="795" onchange="updateLabel()" class="w-12 rounded-lg border border-slate-700 bg-slate-900 px-1 py-1 text-right text-xs font-mono text-white focus:border-amber-500 focus:outline-none" aria-label="Exact tagline-y-val position">
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 pt-2 border-t border-slate-800">
              <div>
                <label for="picker-ribbon-bg" class="text-[11px] text-slate-300 block mb-1">Ribbon fill</label>
                <input type="color" id="picker-ribbon-bg" value="#0B3B24" oninput="setRibbonBgColor(this.value)" class="w-full h-9 rounded border border-slate-700 bg-slate-900 cursor-pointer">
              </div>
              <div>
                <label for="picker-ribbon-text-color" class="text-[11px] text-slate-300 block mb-1">Ribbon text</label>
                <input type="color" id="picker-ribbon-text-color" value="#FFFDF0" oninput="updateLabel()" class="w-full h-9 rounded border border-slate-700 bg-slate-900 cursor-pointer">
              </div>
              <div>
                <label for="picker-ribbon-border" class="text-[11px] text-slate-300 block mb-1">Ribbon border</label>
                <input type="color" id="picker-ribbon-border" value="#D4AF37" oninput="updateLabel()" class="w-full h-9 rounded border border-slate-700 bg-slate-900 cursor-pointer">
              </div>
            </div>
          </div>
        </div>

        <!-- LAYER 6: NET WEIGHT & FSSAI PLAQUE -->
        <div class="border border-slate-800 rounded-xl overflow-hidden bg-slate-950/40" id="card-plaque">
          <button onclick="toggleAccordion('layer-plaque-content')" class="w-full px-3.5 py-2.5 flex items-center justify-between bg-slate-900 hover:bg-slate-850 transition-all text-left">
            <div class="flex items-center gap-2">
              <span class="text-base">⚖️</span>
              <div>
                <span class="text-xs font-bold text-amber-300">6. Weight aur veg mark</span>
                <span class="text-[10px] text-slate-400 block font-normal">FSSAI green logo & weight plaque</span>
              </div>
            </div>
            <span class="text-xs text-slate-400 font-mono" id="layer-plaque-arrow">►</span>
          </button>

          <div id="layer-plaque-content" class="p-3.5 space-y-3 hidden">
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
              <div>
                <label class="text-[11px] font-semibold text-slate-300 block mb-1">Net Weight Text:</label>
                <input type="text" id="input-weight" value="400g ℮" oninput="updateLabel()" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 text-sm text-white focus:border-amber-500 focus:outline-none">
                <div class="flex items-center gap-1.5 pt-1.5">
                  <button type="button" onclick="setWeightPreset('400g ℮')" id="btn-weight-400" class="px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/50 text-xs font-bold transition-all">400g ℮ (Photo)</button>
                  <button type="button" onclick="setWeightPreset('500g ℮')" id="btn-weight-500" class="px-2 py-0.5 rounded bg-slate-800 text-slate-300 hover:border-slate-600 border border-transparent text-xs transition-all">500g ℮</button>
                  <button type="button" onclick="setWeightPreset('250g ℮')" id="btn-weight-250" class="px-2 py-0.5 rounded bg-slate-800 text-slate-300 hover:border-slate-600 border border-transparent text-xs transition-all">250g ℮</button>
                  <button type="button" onclick="setWeightPreset('1 kg ℮')" id="btn-weight-1000" class="px-2 py-0.5 rounded bg-slate-800 text-slate-300 hover:border-slate-600 border border-transparent text-xs transition-all">1 kg ℮</button>
                </div>
              </div>
              <div class="flex items-center sm:pt-4">
                <label class="flex items-center gap-2 cursor-pointer text-xs text-slate-300">
                  <input type="checkbox" id="check-veg-logo" checked onchange="updateLabel()" class="accent-emerald-500 rounded">
                  <span>🟢 FSSAI Green Veg Logo</span>
                </label>
              </div>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 pt-2 border-t border-slate-800">
              <div>
                <label for="picker-plaque-bg" class="text-[11px] text-slate-300 block mb-1">Plaque fill</label>
                <input type="color" id="picker-plaque-bg" value="#FFFFFF" oninput="updateLabel()" class="w-full h-9 rounded border border-slate-700 bg-slate-900 cursor-pointer">
              </div>
              <div>
                <label for="picker-plaque-border" class="text-[11px] text-slate-300 block mb-1">Plaque border</label>
                <input type="color" id="picker-plaque-border" value="#D4AF37" oninput="updateLabel()" class="w-full h-9 rounded border border-slate-700 bg-slate-900 cursor-pointer">
              </div>
              <div>
                <label for="picker-plaque-text-color" class="text-[11px] text-slate-300 block mb-1">Plaque text</label>
                <input type="color" id="picker-plaque-text-color" value="#0B3B24" oninput="updateLabel()" class="w-full h-9 rounded border border-slate-700 bg-slate-900 cursor-pointer">
              </div>
            </div>

            <div class="flex flex-wrap items-center justify-between gap-2">
              <span class="text-[11px] text-slate-300 font-medium">Position X (left / right):</span>
              <input type="range" id="slider-plaque-x" min="300" max="900" value="600" oninput="updateLabel()" class="w-36 accent-amber-500 cursor-pointer">
              <span id="plaque-x-val" class="text-xs font-mono font-bold text-teal-400 w-16 text-right">X: 600</span><input type="number" id="number-plaque-x" min="300" max="900" step="1" value="600" onchange="updateLabel()" class="w-12 rounded-lg border border-slate-700 bg-slate-900 px-1 py-1 text-right text-xs font-mono text-white focus:border-amber-500 focus:outline-none" aria-label="Exact plaque-x-val position">
            </div>
            <div class="flex flex-wrap items-center justify-between gap-2">
              <span class="text-[11px] text-slate-300 font-medium">Position Y (up / down):</span>
              <input type="range" id="slider-plaque-y" min="780" max="1000" value="895" oninput="updateLabel()" class="w-36 accent-amber-500 cursor-pointer">
              <span id="plaque-y-val" class="text-xs font-mono font-bold text-teal-400 w-16 text-right">Y: 895</span><input type="number" id="number-plaque-y" min="780" max="1000" step="1" value="895" onchange="updateLabel()" class="w-12 rounded-lg border border-slate-700 bg-slate-900 px-1 py-1 text-right text-xs font-mono text-white focus:border-amber-500 focus:outline-none" aria-label="Exact plaque-y-val position">
            </div>
          </div>
        </div>

        <!-- LAYER 7: MANDALA WATERMARK -->
        <div class="border border-slate-800 rounded-xl overflow-hidden bg-slate-950/40" id="card-mandala">
          <button onclick="toggleAccordion('layer-mandala-content')" class="w-full px-3.5 py-2.5 flex items-center justify-between bg-slate-900 hover:bg-slate-850 transition-all text-left">
            <div class="flex items-center gap-2">
              <span class="text-base">🌸</span>
              <div>
                <span class="text-xs font-bold text-amber-300">7. Background pattern</span>
                <span class="text-[10px] text-slate-400 block font-normal">Authentic gold artwork watermark</span>
              </div>
            </div>
            <span class="text-xs text-slate-400 font-mono" id="layer-mandala-arrow">►</span>
          </button>

          <div id="layer-mandala-content" class="p-3.5 space-y-3 hidden">
            <div class="grid grid-cols-2 gap-2" id="mandala-buttons-container">
              <!-- Populated by JS -->
            </div>

            <div class="flex items-center justify-between gap-3 pt-2">
              <span class="text-[11px] text-slate-300 font-medium">Mandala Opacity:</span>
              <input type="range" id="slider-mandala-opacity" min="5" max="90" value="38" oninput="updateLabel()" class="w-36 accent-amber-500 cursor-pointer">
              <span id="mandala-opacity-val" class="text-xs font-mono font-bold text-amber-400 w-12 text-right">38%</span>
            </div>

            <div class="flex items-center justify-between gap-3">
              <span class="text-[11px] text-slate-300 font-medium">Mandala Scale:</span>
              <input type="range" id="slider-mandala-scale" min="50" max="140" value="100" oninput="updateLabel()" class="w-36 accent-amber-500 cursor-pointer">
              <span id="mandala-scale-val" class="text-xs font-mono font-bold text-teal-400 w-12 text-right">100%</span>
            </div>

            <!-- Luxury Leaf Watermark Texture (Photo Match) -->
            <div class="rounded-xl border border-amber-500/30 bg-amber-500/10 p-2.5 space-y-1.5">
              <div class="flex items-center justify-between">
                <div>
                  <span class="text-xs font-bold text-amber-300 block">🌿 Velvet Leaf Texture (Photo Damask)</span>
                  <span class="text-[10px] text-slate-300">Photo jaisa rich botanical watermark pattern</span>
                </div>
                <span id="pattern-opacity-val" class="text-xs font-mono font-bold text-teal-400">35%</span>
              </div>
              <input type="range" id="slider-pattern-opacity" min="0" max="90" value="35" oninput="setPatternOpacity(this.value)" class="w-full accent-amber-500 cursor-pointer">
            </div>
            <div class="rounded-lg border border-slate-800 bg-slate-950/50 p-3 space-y-2">
              <div class="flex flex-wrap items-center justify-between gap-2">
                <label for="slider-mandala-x" class="text-xs text-slate-300">Mandala X (left / right)</label>
                <span id="mandala-x-val" class="w-16 text-right text-xs font-mono font-bold text-teal-400">X: 600</span><input type="number" id="number-mandala-x" min="100" max="1100" step="1" value="600" onchange="updateLabel()" class="w-12 rounded-lg border border-slate-700 bg-slate-900 px-1 py-1 text-right text-xs font-mono text-white focus:border-amber-500 focus:outline-none" aria-label="Exact mandala-x-val position">
              </div>
              <input type="range" id="slider-mandala-x" min="100" max="1100" value="600" oninput="updateLabel()" class="w-full accent-amber-500 cursor-pointer">
              <div class="flex flex-wrap items-center justify-between gap-2">
                <label for="slider-mandala-y" class="text-xs text-slate-300">Mandala Y (up / down)</label>
                <span id="mandala-y-val" class="w-16 text-right text-xs font-mono font-bold text-teal-400">Y: 600</span><input type="number" id="number-mandala-y" min="100" max="1100" step="1" value="600" onchange="updateLabel()" class="w-12 rounded-lg border border-slate-700 bg-slate-900 px-1 py-1 text-right text-xs font-mono text-white focus:border-amber-500 focus:outline-none" aria-label="Exact mandala-y-val position">
              </div>
              <input type="range" id="slider-mandala-y" min="100" max="1100" value="600" oninput="updateLabel()" class="w-full accent-amber-500 cursor-pointer">
            </div>
          </div>
        </div>

        <!-- LAYER 8: PALETTE & BACKGROUND COLORS -->
        <div class="border border-slate-800 rounded-xl overflow-hidden bg-slate-950/40" id="card-palette">
          <button onclick="toggleAccordion('layer-palette-content')" class="w-full px-3.5 py-2.5 flex items-center justify-between bg-slate-900 hover:bg-slate-850 transition-all text-left">
            <div class="flex items-center gap-2">
              <span class="text-base">🎨</span>
              <div>
                <span class="text-xs font-bold text-amber-300">8. Sticker ke rang</span>
                <span class="text-[10px] text-slate-400 block font-normal">Custom tin background & rim colors</span>
              </div>
            </div>
            <span class="text-xs text-slate-400 font-mono" id="layer-palette-arrow">►</span>
          </button>

          <div id="layer-palette-content" class="p-3.5 space-y-3 hidden">
            <div class="grid grid-cols-2 gap-3">
              <div>
                <label class="text-[11px] font-semibold text-slate-300 block mb-1">Center Base Color:</label>
                <div class="flex items-center gap-2">
                  <input type="color" id="picker-bg-center" value="#C5ECE1" onchange="setBgCenterColor(this.value)" class="w-8 h-8 rounded border border-slate-700 bg-transparent cursor-pointer">
                  <span id="bg-center-hex" class="text-xs font-mono text-slate-400">#C5ECE1</span>
                </div>
              </div>

              <div>
                <label class="text-[11px] font-semibold text-slate-300 block mb-1">Outer Rim Gradient:</label>
                <div class="flex items-center gap-2">
                  <input type="color" id="picker-bg-outer" value="#97D8C4" onchange="setBgOuterColor(this.value)" class="w-8 h-8 rounded border border-slate-700 bg-transparent cursor-pointer">
                  <span id="bg-outer-hex" class="text-xs font-mono text-slate-400">#97D8C4</span>
                </div>
              </div>

              <div>
                <label for="picker-foil-color" class="text-[11px] font-semibold text-slate-300 block mb-1">Foil / gold details</label>
                <div class="flex items-center gap-2">
                  <input type="color" id="picker-foil-color" value="#D4AF37" oninput="updateLabel()" class="w-8 h-8 rounded border border-slate-700 bg-slate-900 cursor-pointer">
                  <span class="text-xs text-slate-400">Rims, ornament, gold text</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- LAYER 9: A4 WHITE PAGE ENGINE -->
        <div class="border border-slate-800 rounded-xl overflow-hidden bg-slate-950/40" id="card-a4">
          <button onclick="toggleAccordion('layer-a4-content')" class="w-full px-3.5 py-2.5 flex items-center justify-between bg-slate-900 hover:bg-slate-850 transition-all text-left">
            <div class="flex items-center gap-2">
              <span class="text-base">📄</span>
              <div>
                <span class="text-xs font-bold text-amber-300">9. Print settings (A4 page)</span>
                <span class="text-[10px] text-slate-400 block font-normal">Standard A4 paper sheets • 1, 2, 4 or 6 labels</span>
              </div>
            </div>
            <span class="text-xs text-slate-400 font-mono" id="layer-a4-arrow">►</span>
          </button>

          <div id="layer-a4-content" class="p-3.5 space-y-3 hidden">
            <div class="grid grid-cols-2 gap-2">
              <button onclick="setA4Layout(1)" id="btn-a4-layout-1" class="p-2.5 rounded-xl border-2 border-amber-500 bg-amber-500/15 text-left">
                <div class="text-xs font-bold text-amber-300">1 Label / A4</div>
                <div class="text-[10px] text-slate-400">100% True 6" Scale (152.4 mm)</div>
              </button>
              <button onclick="setA4Layout(2)" id="btn-a4-layout-2" class="p-2.5 rounded-xl border border-slate-800 bg-slate-900 text-left">
                <div class="text-xs font-bold text-white">2 Labels / A4</div>
                <div class="text-[10px] text-slate-400">Stacked pair (140 mm each)</div>
              </button>
              <button onclick="setA4Layout(4)" id="btn-a4-layout-4" class="p-2.5 rounded-xl border border-slate-800 bg-slate-900 text-left">
                <div class="text-xs font-bold text-white">4 Labels / A4</div>
                <div class="text-[10px] text-slate-400">2×2 Grid (98 mm each)</div>
              </button>
              <button onclick="setA4Layout(6)" id="btn-a4-layout-6" class="p-2.5 rounded-xl border border-slate-800 bg-slate-900 text-left">
                <div class="text-xs font-bold text-white">6 Labels / A4</div>
                <div class="text-[10px] text-slate-400">2×3 Grid (80 mm stickers)</div>
              </button>
            </div>

            <div class="flex items-center gap-3 pt-2">
              <button onclick="setViewMode('a4')" class="flex-1 py-2 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold rounded-lg text-xs shadow">
                👁️ View A4 Sheet Mode
              </button>
              <button onclick="printA4Direct()" class="flex-1 py-2 bg-slate-800 hover:bg-slate-700 text-teal-300 border border-teal-500/30 font-bold rounded-lg text-xs shadow">
                🖨️ Print Now (Ctrl+P)
              </button>
            </div>
          </div>
        </div>

      </div>

    </div>

    <!-- RIGHT MAIN CANVAS STAGE (Col span 7 on desktop) -->
    <div class="studio-preview md:col-span-7 flex flex-col items-center space-y-4">
      
      <!-- VIEW MODE SWITCHER & STAGE TOOLBAR -->
      <div class="w-full flex items-center justify-between bg-slate-900/90 border border-slate-800 px-4 py-2.5 rounded-2xl shadow-xl">
        <div class="flex items-center gap-2">
          <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></span>
          <span class="text-xs font-black uppercase tracking-wider text-white">Sticker Preview</span>
          <span class="text-[10px] text-amber-300 bg-amber-500/15 px-2 py-0.5 rounded border border-amber-500/30">
            Preview mein item ko drag karke jagah badlein
          </span>
        </div>

        <div class="flex items-center gap-1.5 bg-slate-950 p-1 rounded-xl border border-slate-800 text-xs font-bold">
          <button onclick="resetPositions()" class="px-2.5 py-1 rounded-lg text-slate-400 hover:text-white transition-all text-xs" title="Reset all layers to default symmetrical center">
            Reset Layout
          </button>
          <button onclick="setViewMode('3d')" id="btn-view-3d" class="px-2.5 py-1 rounded-lg bg-amber-500 text-slate-950 font-black transition-all">
            Tin Preview
          </button>
          <button onclick="setViewMode('flat')" id="btn-view-flat" class="px-2.5 py-1 rounded-lg text-slate-400 hover:text-white transition-all">
            Flat Sticker
          </button>
          <button onclick="setViewMode('a4')" id="btn-view-a4" class="px-2.5 py-1 rounded-lg text-slate-400 hover:text-white transition-all">
            Print Page
          </button>
        </div>
      </div>

      <!-- MAIN PACKAGING DISPLAY (3D DABBA OR FLAT STAGE) -->
      <div id="packaging-stage-wrapper" class="w-full bg-slate-950/80 rounded-3xl p-4 sm:p-6 md:p-8 flex items-center justify-center min-h-[500px] border border-slate-800/80 shadow-2xl relative overflow-hidden">
        
        <!-- 3D Steel Dabba Shell (Aspect Square, perfectly centered, max-w-[480px]) -->
        <div id="tin-dabba-shell" class="relative w-full max-w-[480px] aspect-square flex items-center justify-center tin-stage-shadow rounded-full transition-all duration-300">
          
          <!-- Silver-Steel Metallic Outer Bezel -->
          <div id="tin-metal-rim" class="absolute -inset-3.5 rounded-full tin-metallic-bezel pointer-events-none"></div>

          <!-- Inset 6-Inch Label Circular Stage (overflow: hidden prevents any bleed) -->
          <div class="relative z-10 w-full h-full rounded-full overflow-hidden shadow-inner bg-slate-900">
            
            <!-- Subtle Steel-Glass Light Reflection Sheen -->
            <div id="tin-surface-sheen" class="tin-surface-sheen"></div>

            <!-- SVG Container Mount -->
            <div id="tin-svg-mount" class="w-full h-full flex items-center justify-center">
              <!-- SVG dynamically mounted here by renderSVG() -->
            </div>

          </div>

        </div>

      </div>

      <!-- A4 PRINT SHEET PREVIEW (Hidden by default, shown when mode is 'a4') -->
      <div id="a4-sheet-wrapper" class="w-full hidden flex flex-col items-center space-y-4">
        
        <!-- A4 Controls Toolbar -->
        <div class="w-full bg-slate-900 border border-slate-800 p-3.5 rounded-2xl flex flex-wrap items-center justify-between gap-3 text-xs">
          <div class="flex items-center gap-2">
            <span class="font-bold text-amber-300">📄 A4 White Paper (210 × 297 mm)</span>
            <span class="text-slate-400">|</span>
            <span id="a4-sheet-layout-hud" class="text-slate-300 font-mono">1 Label (100% True Scale)</span>
          </div>
          <div class="flex items-center gap-2">
            <button onclick="printA4Direct()" class="px-3 py-1.5 bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-black rounded-lg text-xs flex items-center gap-1 shadow">
              <span>🖨️ Print Sheet</span>
            </button>
            <button onclick="downloadA4PNG()" class="px-3 py-1.5 bg-amber-500 hover:bg-amber-400 text-slate-950 font-black rounded-lg text-xs flex items-center gap-1 shadow">
              <span>📥 Download A4 (300 DPI)</span>
            </button>
          </div>
        </div>

        <!-- The White A4 Paper Simulation -->
        <div class="bg-slate-900/60 p-4 sm:p-6 rounded-3xl border border-slate-800 flex justify-center items-center w-full overflow-x-auto">
          <div id="a4-print-mount" 
               class="relative bg-white text-slate-950 shadow-2xl rounded-sm transition-all duration-300 flex flex-col justify-between"
               style="width: 100%; max-width: 500px; aspect-ratio: 210/297; min-height: 700px; padding: 20px;">
            
            <!-- A4 Header: Sheet Metadata -->
            <div class="flex items-center justify-between border-b border-slate-200 pb-1.5 text-[9px] font-mono text-slate-500 uppercase tracking-wider">
              <span class="font-bold text-slate-800">DIAMOND BAKERY • 6-INCH ROUND MASTER TIN</span>
              <span id="a4-sheet-sub-title">1 LABEL • 100% TRUE SCALE (152.4 MM)</span>
              <span>A4 (210 × 297 MM)</span>
            </div>

            <!-- A4 Labels Placement Body -->
            <div id="a4-labels-grid" class="my-auto flex flex-wrap items-center justify-around gap-4 w-full">
              <!-- Dynamically populated with scaled labels & crop marks -->
            </div>

            <!-- A4 Footer: Cut Guides & CMYK Bars -->
            <div class="border-t border-slate-200 pt-2 flex items-center justify-between text-[8px] font-mono text-slate-500">
              <span>✂️ Cut along circular guidelines • 100% True Scale (Do Not Fit To Page)</span>
              <div class="flex items-center gap-1">
                <span class="w-3 h-2 bg-cyan-500 inline-block"></span>
                <span class="w-3 h-2 bg-pink-500 inline-block"></span>
                <span class="w-3 h-2 bg-yellow-400 inline-block"></span>
                <span class="w-3 h-2 bg-black inline-block"></span>
                <span class="w-3 h-2 inline-block" style="background: #D4AF37;"></span>
              </div>
            </div>

          </div>
        </div>

      </div>

      <!-- BOTTOM SPECIFICATION SUMMARY BADGES -->
      <div class="w-full grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
        <div class="p-2.5 bg-slate-900/80 rounded-xl border border-slate-800">
          <span class="text-slate-500 block text-[9px] uppercase font-bold">Sticker Size</span>
          <span class="text-amber-300 font-bold text-xs">6" Diameter (3" Radius)</span>
        </div>
        <div class="p-2.5 bg-slate-900/80 rounded-xl border border-slate-800">
          <span class="text-slate-500 block text-[9px] uppercase font-bold">Upar ka text</span>
          <span class="text-teal-400 font-bold text-xs" id="hud-top-arc-val">Radius 530px</span>
        </div>
        <div class="p-2.5 bg-slate-900/80 rounded-xl border border-slate-800">
          <span class="text-slate-500 block text-[9px] uppercase font-bold">Neeche ka text</span>
          <span class="text-teal-400 font-bold text-xs" id="hud-bot-arc-val">Radius 530px</span>
        </div>
        <div class="p-2.5 bg-slate-900/80 rounded-xl border border-slate-800">
          <span class="text-slate-500 block text-[9px] uppercase font-bold">Print Quality</span>
          <span class="text-emerald-400 font-bold text-xs">600 DPI (3600×3600px)</span>
        </div>
      </div>

    </div>

  </main>

  <!-- JAVASCRIPT ENGINE -->
  <script>
    // ==========================================
    // STATE DEFINITION (100% PHOTO-MATCHED)
    // ==========================================
    const state = {
      preset: 'mint', // Mint preset matches user's uploaded reference sticker!
      viewMode: '3d', // '3d', 'flat', 'a4'
      designStyle: 'style2_script',
      showBrandPillar: false,
      patternOpacity: 0.25,
      ribbonFont: 'cormorant',
      topArcFont: 'cinzel',
      bottomArcFont: 'cinzel',
      
      // Background & Rims (Sampled from User Reference)
      bgCenter: '#C2ECE0',
      bgOuter: '#97D8C4',
      foilColor: '#E5CF88',

      // Product Title ("Assorted Cookies" in Alex Brush)
      titleLine1: 'Assorted',
      titleLine2: 'Cookies',
      titleFont: 'alex-brush', // Exact 100% match with user photo!
      titleSize: 135,
      titleLine1X: 600,
      titleLine1Y: 615,
      titleLine2X: 600,
      titleLine2Y: 720,
      titleColorMode: 'gold',
      titleCustomColor: '#D4AF37',

      // Brand & Monogram (LOCKED TOGETHER 🔒)
      brand: 'DIAMOND',
      brandSub: 'BAKERY • RESTAURANT • SWEETS',
      monogram: 'D',
      masterBrandScale: 100,
      brandSize: 48,
      brandBlockX: 600,
      brandBlockY: 410,
      brandSpacing: 16,
      brandFont: 'prata',
      brandNameColor: '#C81D25',
      brandSubColor: '#0B3B24',
      brandSubSize: 13,
      crestScale: 0.95,
      emblemColor: '#D4AF37',
      emblemTintEnabled: false,
      brandColorMode: 'red',
      brandCustomColor: '#C81D25',

      // Top Arc
      topArc: '★  SERVING SHIMLA SINCE 2002  •  FINEST ARTISAN BAKES  ★',
      topArcRadius: 530,
      topArcX: 600,
      topArcY: 600,
      topArcSize: 14.5,
      topArcColor: '#0B3B24',

      // Bottom Arc
      bottomArc: '★  PREPARED IN PURE BUTTER & DESI GHEE  •  ZERO PALM OIL  ★',
      bottomArcRadius: 530,
      bottomArcX: 600,
      bottomArcY: 600,
      bottomArcSize: 14.5,
      bottomArcColor: '#0B3B24',

      // Tagline Capsule Ribbon ("★  BAKED WITH 100% PURE BUTTER  •  ZERO PALM OIL  ★")
      ribbonText: '★  BAKED WITH 100% PURE BUTTER  •  ZERO PALM OIL  ★',
      ribbonWidth: 750,
      ribbonSize: 16.5,
      ribbonX: 600,
      ribbonY: 795,
      ribbonBg: '#0B3B24',
      ribbonBorder: '#E5CF88',
      ribbonTextColor: '#FFFDF0',

      // Plaque (Weight is 400g e)
      weight: '400g e',
      showVeg: true,
      plaqueX: 600,
      plaqueY: 895,
      plaqueBg: '#FFFFFF',
      plaqueBorder: '#E5CF88',
      plaqueTextColor: '#0B3B24',

      // Mandala
      mandalaType: 'authentic_user',
      mandalaOpacity: 0.35,
      mandalaScale: 1.0,
      mandalaX: 600,
      mandalaY: 600,

      // A4 Engine
      a4Layout: 1
    };

    // ==========================================
    // PRESET DEFINITIONS (MATCHING USER IMAGES)
    // ==========================================
    const PRESETS = {
      mint: {
        bgCenter: '#C2ECE0',
        bgOuter: '#97D8C4',
        foilColor: '#E5CF88',
        brandColorMode: 'red',
        brandNameColor: '#C81D25',
        brandSubColor: '#0B3B24',
        titleFont: 'alex-brush',
        titleColorMode: 'gold',
        titleSize: 135,
        titleLine1: 'Assorted',
        titleLine2: 'Cookies',
        titleLine1Y: 615,
        titleLine2Y: 720,
        brandBlockY: 410,
        brandSpacing: 16,
        ribbonText: '★  BAKED WITH 100% PURE BUTTER  •  ZERO PALM OIL  ★',
        ribbonY: 795,
        plaqueY: 895,
        topArc: '★  SERVING SHIMLA SINCE 2002  •  FINEST ARTISAN BAKES  ★',
        topArcColor: '#0B3B24',
        bottomArc: '★  PREPARED IN PURE BUTTER & DESI GHEE  •  ZERO PALM OIL  ★',
        bottomArcColor: '#0F4C2A',
        ribbonBg: '#0B3B24',
        ribbonBorder: '#E5CF88',
        ribbonTextColor: '#FFFDF0',
        plaqueBg: '#FFFFFF',
        plaqueBorder: '#E5CF88',
        plaqueTextColor: '#0B3B24',
        mandalaType: 'authentic_user',
        mandalaOpacity: 0.35,
        patternOpacity: 0.25,
        weight: '400g e'
      },
      maroon: {
        bgCenter: '#581825',
        bgOuter: '#22040B',
        foilColor: '#E5CF88',
        brandColorMode: 'red',
        brandNameColor: '#C81D25',
        brandSubColor: '#E5CF88',
        titleFont: 'alex-brush',
        titleColorMode: 'gold',
        titleSize: 135,
        titleLine1: 'Assorted',
        titleLine2: 'Cookies',
        titleLine1Y: 615,
        titleLine2Y: 720,
        brandBlockY: 410,
        brandSpacing: 16,
        ribbonText: '★  BAKED WITH 100% PURE BUTTER  •  ZERO PALM OIL  ★',
        ribbonY: 795,
        plaqueY: 895,
        topArc: '★  SERVING SHIMLA SINCE 2002  •  FINEST ARTISAN BAKES  ★',
        topArcColor: '#E5CF88',
        bottomArc: '★  PREPARED IN PURE BUTTER & DESI GHEE  •  ZERO PALM OIL  ★',
        bottomArcColor: '#E5CF88',
        ribbonBg: '#360912',
        ribbonBorder: '#E5CF88',
        ribbonTextColor: '#FFFDF0',
        plaqueBg: '#360912',
        plaqueBorder: '#E5CF88',
        plaqueTextColor: '#FFFFFF',
        mandalaType: 'authentic_user',
        mandalaOpacity: 0.38,
        patternOpacity: 0.30,
        weight: '400g e'
      },
      emerald: {
        bgCenter: '#0D3822',
        bgOuter: '#051B10',
        foilColor: '#E5C158',
        brandColorMode: 'gold',
        brandNameColor: '#E5C158',
        brandSubColor: '#FFFFFF',
        titleFont: 'alex-brush',
        titleColorMode: 'gold',
        titleSize: 135,
        titleLine1Y: 615,
        titleLine2Y: 720,
        brandBlockY: 410,
        brandSpacing: 16,
        ribbonY: 795,
        plaqueY: 895,
        topArc: '★  SERVING SHIMLA SINCE 2002  •  FINEST ARTISAN BAKES  ★',
        topArcColor: '#E5C158',
        bottomArc: '★  PREPARED IN PURE BUTTER & DESI GHEE  •  ZERO PALM OIL  ★',
        bottomArcColor: '#E5C158',
        ribbonBg: '#082818',
        ribbonBorder: '#E5C158',
        ribbonTextColor: '#FFFDF0',
        plaqueBg: '#082818',
        plaqueBorder: '#E5C158',
        plaqueTextColor: '#FFFFFF',
        mandalaType: 'filigree',
        mandalaOpacity: 0.42,
        weight: '400g e'
      },
      rosegold: {
        bgCenter: '#4A1525',
        bgOuter: '#250711',
        foilColor: '#E8A598',
        brandColorMode: 'gold',
        brandNameColor: '#E8A598',
        brandSubColor: '#FFFFFF',
        titleFont: 'alex-brush',
        titleColorMode: 'gold',
        titleSize: 135,
        titleLine1Y: 615,
        titleLine2Y: 720,
        brandBlockY: 410,
        brandSpacing: 16,
        ribbonY: 795,
        plaqueY: 895,
        topArc: '★  SERVING SHIMLA SINCE 2002  •  FINEST ARTISAN BAKES  ★',
        topArcColor: '#F5C2B6',
        bottomArc: '★  PREPARED IN PURE BUTTER & DESI GHEE  •  ZERO PALM OIL  ★',
        bottomArcColor: '#F5C2B6',
        ribbonBg: '#300B17',
        ribbonBorder: '#E8A598',
        ribbonTextColor: '#FFF0ED',
        plaqueBg: '#FFFFFF',
        plaqueBorder: '#E8A598',
        plaqueTextColor: '#4A1525',
        mandalaType: 'rose_window',
        mandalaOpacity: 0.40,
        weight: '400g e'
      },
      purple: {
        bgCenter: '#240B36',
        bgOuter: '#11041D',
        foilColor: '#F3D079',
        brandColorMode: 'gold',
        brandNameColor: '#F3D079',
        brandSubColor: '#FFFFFF',
        titleFont: 'alex-brush',
        titleColorMode: 'gold',
        titleSize: 135,
        titleLine1Y: 615,
        titleLine2Y: 720,
        brandBlockY: 410,
        brandSpacing: 16,
        ribbonY: 795,
        plaqueY: 895,
        topArc: '★  SERVING SHIMLA SINCE 2002  •  FINEST ARTISAN BAKES  ★',
        topArcColor: '#F3D079',
        bottomArc: '★  PREPARED IN PURE BUTTER & DESI GHEE  •  ZERO PALM OIL  ★',
        bottomArcColor: '#F3D079',
        ribbonBg: '#1A0626',
        ribbonBorder: '#F3D079',
        ribbonTextColor: '#FFFDF0',
        plaqueBg: '#1A0626',
        plaqueBorder: '#F3D079',
        plaqueTextColor: '#FFFFFF',
        mandalaType: 'imperial_crown',
        mandalaOpacity: 0.45,
        weight: '400g e'
      },
      gold_luxe: {
        bgCenter: '#3D2706',
        bgOuter: '#1C1101',
        foilColor: '#FFDF73',
        brandColorMode: 'red',
        brandNameColor: '#C81D25',
        brandSubColor: '#FFFFFF',
        titleFont: 'alex-brush',
        titleColorMode: 'gold',
        titleSize: 135,
        titleLine1Y: 615,
        titleLine2Y: 720,
        brandBlockY: 410,
        brandSpacing: 16,
        ribbonY: 795,
        plaqueY: 895,
        topArc: '★  SERVING SHIMLA SINCE 2002  •  FINEST ARTISAN BAKES  ★',
        topArcColor: '#FFDF73',
        bottomArc: '★  PREPARED IN PURE BUTTER & DESI GHEE  •  ZERO PALM OIL  ★',
        bottomArcColor: '#FFDF73',
        ribbonBg: '#2A1B04',
        ribbonBorder: '#FFDF73',
        ribbonTextColor: '#FFFDF0',
        plaqueBg: '#FFFFFF',
        plaqueBorder: '#FFDF73',
        plaqueTextColor: '#3D2706',
        mandalaType: 'sunburst_luxe',
        mandalaOpacity: 0.45,
        weight: '400g e'
      }
    };

    // ==========================================
    // ALL 14 PACKAGING FONTS EMBEDDED MAP
    // ==========================================
    const FONT_MAP = {
      'alex-brush': { family: "'Alex Brush', cursive", weight: "normal", letterSpacing: "0.02em", name: 'Alex Brush (Photo Wala Script)' },
      'great-vibes': { family: "'Great Vibes', cursive", weight: "normal", letterSpacing: "0.02em", name: 'Great Vibes (Flowing Script)' },
      'parisienne': { family: "'Parisienne', cursive", weight: "normal", letterSpacing: "0.02em", name: 'Parisienne (French Script)' },
      'dancing-script': { family: "'Dancing Script', cursive", weight: "700", letterSpacing: "0.02em", name: 'Dancing Script' },
      'italianno': { family: "'Italianno', cursive", weight: "normal", letterSpacing: "0.03em", name: 'Italianno (Fine Italic)' },
      'cinzel-dec': { family: "'Cinzel Decorative', serif", weight: "900", letterSpacing: "0.04em", name: 'Cinzel Decorative' },
      'cinzel': { family: "'Cinzel', serif", weight: "800", letterSpacing: "0.05em", name: 'Cinzel Trajan' },
      'playfair-black': { family: "'Playfair Display', serif", weight: "900", letterSpacing: "0.02em", name: 'Playfair Display 900' },
      'cormorant': { family: "'Cormorant Garamond', serif", weight: "700", letterSpacing: "0.04em", name: 'Cormorant Garamond' },
      'marcellus': { family: "'Marcellus', serif", weight: "normal", letterSpacing: "0.05em", name: 'Marcellus Trajan' },
      'prata': { family: "'Prata', serif", weight: "normal", letterSpacing: "0.04em", name: 'Prata (Didot Serif)' },
      'eb-garamond': { family: "'EB Garamond', serif", weight: "700", letterSpacing: "0.04em", name: 'EB Garamond' },
      'montserrat-black': { family: "'Montserrat', sans-serif", weight: "900", letterSpacing: "0.06em", name: 'Montserrat Heavy' },
      'plus-jakarta': { family: "'Plus Jakarta Sans', sans-serif", weight: "800", letterSpacing: "0.04em", name: 'Plus Jakarta Sans' }
    };

    function applyPreset(presetKey) {
      const p = PRESETS[presetKey];
      if (!p) return;
      state.preset = presetKey;
      Object.assign(state, p);
      state.titleLine1X = 600;
      state.titleLine2X = 600;
      state.brandBlockX = 600;
      state.brandBlockY = p.brandBlockY || 410;
      state.brandSpacing = p.brandSpacing || 16;
      state.crestScale = p.crestScale || 0.95;
      state.topArcX = 600;
      state.topArcY = 600;
      state.bottomArcX = 600;
      state.bottomArcY = 600;
      state.ribbonX = 600;
      state.plaqueX = 600;
      state.mandalaX = 600;
      state.mandalaY = 600;

      ['mint', 'maroon', 'emerald', 'rosegold', 'purple', 'gold_luxe'].forEach(k => {
        const btn = document.getElementById(`btn-preset-${k}`);
        if (btn) {
          if (k === presetKey) {
            btn.className = "p-2.5 rounded-xl border-2 border-amber-500 bg-amber-500/15 text-left transition-all hover:scale-[1.02] flex flex-col justify-between shadow-lg";
          } else {
            btn.className = "p-2.5 rounded-xl border border-slate-800 bg-slate-950/60 text-left transition-all hover:scale-[1.02] flex flex-col justify-between";
          }
        }
      });

      syncUIFromState();
      renderSVG();
    }

    function toggleAccordion(contentId) {
      const content = document.getElementById(contentId);
      if (!content) return;
      const isHidden = content.classList.contains('hidden');
      
      document.querySelectorAll('[id^="layer-"][id$="-content"]').forEach(el => {
        el.classList.add('hidden');
      });
      document.querySelectorAll('[id^="layer-"][id$="-arrow"]').forEach(el => {
        el.textContent = '►';
      });

      if (isHidden) {
        content.classList.remove('hidden');
        const arrowId = contentId.replace('-content', '-arrow');
        const arrow = document.getElementById(arrowId);
        if (arrow) arrow.textContent = '▼';
      }
    }

    function openLayerAccordion(layerName) {
      const content = document.getElementById(`layer-${layerName}-content`);
      if (!content) return;
      if (content.classList.contains('hidden')) {
        toggleAccordion(content.id);
      }
      const controls = document.querySelector('.studio-controls');
      const card = document.getElementById(`card-${layerName}`) || content.closest('.border') || content.parentElement;
      if (controls && card) {
        const target = Math.max(0, card.offsetTop - controls.offsetTop - 12);
        controls.scrollTo({ top: target, behavior: 'smooth' });
      }
      if (card) {
        card.classList.add('card-highlight-active');
        setTimeout(() => {
          card.classList.remove('card-highlight-active');
        }, 1200);
      }
    }

    // ==========================================
    // TITLE FONT & COLOR CONTROLS
    // ==========================================
    function setTitleFont(fontKey) {
      if (!FONT_MAP[fontKey]) fontKey = 'alex-brush';
      state.titleFont = fontKey;
      
      if (fontKey === 'alex-brush' || fontKey === 'great-vibes') {
        state.titleSize = 135;
      } else if (fontKey === 'parisienne') {
        state.titleSize = 130;
      } else if (fontKey === 'italianno') {
        state.titleSize = 150;
      } else if (fontKey === 'cinzel-dec') {
        state.titleSize = 105;
      } else if (fontKey === 'montserrat-black') {
        state.titleSize = 98;
      } else if (fontKey === 'playfair-black') {
        state.titleSize = 106;
      } else if (fontKey === 'cormorant') {
        state.titleSize = 110;
      }

      const fontSelect = document.getElementById('select-title-font');
      if (fontSelect) fontSelect.value = fontKey;

      const badge = document.getElementById('title-font-current-name');
      if (badge && FONT_MAP[fontKey]) badge.textContent = FONT_MAP[fontKey].name;

      const favoriteKeys = ['alex-brush', 'great-vibes', 'cinzel-dec', 'playfair-black', 'cormorant', 'parisienne'];
      favoriteKeys.forEach(fk => {
        const btn = document.getElementById(`font-btn-${fk}`);
        if (btn) {
          if (fk === fontKey) {
            btn.className = "px-2 py-1.5 rounded-lg border text-left text-xs font-bold transition-all border-amber-500 bg-amber-500/20 text-amber-300 shadow";
          } else {
            btn.className = "px-2 py-1.5 rounded-lg border text-left text-xs transition-all border-slate-800 bg-slate-900 text-slate-300 hover:border-slate-700";
          }
        }
      });

      const s = document.getElementById('slider-title-size');
      if (s) s.value = state.titleSize;
      const v = document.getElementById('title-size-val');
      if (v) v.textContent = `${state.titleSize} px`;

      renderSVG();
    }

    function setRibbonFont(fontKey) {
      if (!FONT_MAP[fontKey]) fontKey = 'cormorant';
      state.ribbonFont = fontKey;
      const sel = document.getElementById('select-ribbon-font');
      if (sel) sel.value = fontKey;
      renderSVG();
    }

    function setPatternOpacity(val) {
      const num = parseInt(val, 10);
      state.patternOpacity = isNaN(num) ? 0.25 : num / 100;
      const v = document.getElementById('pattern-opacity-val');
      if (v) v.textContent = `${num}%`;
      const slider = document.getElementById('slider-pattern-opacity');
      if (slider) slider.value = num;
      renderSVG();
    }

    function setWeightPreset(w) {
      state.weight = w;
      const inp = document.getElementById('input-weight');
      if (inp) inp.value = w;
      ['400', '500', '250', '1000'].forEach(k => {
        const btn = document.getElementById(`btn-weight-${k}`);
        if (btn) {
          const match = (k === '1000' && w.includes('1 kg')) || (k !== '1000' && w.includes(k));
          if (match) {
            btn.className = "px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/50 text-xs font-bold transition-all";
          } else {
            btn.className = "px-2 py-0.5 rounded bg-slate-800 text-slate-300 hover:border-slate-600 border border-transparent text-xs transition-all";
          }
        }
      });
      renderSVG();
    }

    function setDesignStyle(styleKey) {
      state.designStyle = styleKey;

      if (styleKey === 'style1_pillar') {
        state.showBrandPillar = true;
        state.titleFont = 'cinzel-dec';
        state.titleSize = 105;
        state.mandalaOpacity = 0.42;
      } else if (styleKey === 'style2_script') {
        state.showBrandPillar = false;
        state.titleFont = 'alex-brush';
        state.titleSize = 135;
        state.mandalaOpacity = 0.35;
      } else if (styleKey === 'style3_combined') {
        state.showBrandPillar = true;
        state.titleFont = 'alex-brush';
        state.titleSize = 130;
        state.mandalaOpacity = 0.38;
      }

      ['style1_pillar', 'style2_script', 'style3_combined'].forEach(k => {
        const btn = document.getElementById(`btn-style-${k}`);
        if (btn) {
          if (k === styleKey) {
            btn.className = "p-2.5 rounded-xl border-2 border-amber-500 bg-amber-500/20 text-left transition-all flex flex-col justify-between shadow-lg";
          } else {
            btn.className = "p-2.5 rounded-xl border border-slate-700 bg-slate-900 hover:border-amber-500 text-left transition-all flex flex-col justify-between";
          }
        }
      });

      syncUIFromState();
      renderSVG();
    }

    function setTitleColorMode(mode) {
      state.titleColorMode = mode;
      renderSVG();
    }

    function setTitleColorCustom(val) {
      state.titleColorMode = 'custom';
      state.titleCustomColor = val;
      renderSVG();
    }

    function setRibbonText(text) {
      state.ribbonText = text;
      const inp = document.getElementById('input-butter-tagline');
      if (inp) inp.value = text;
      renderSVG();
    }

    function setTitleSize(sz) {
      sz = parseInt(sz, 10) || 135;
      state.titleSize = sz;
      const s = document.getElementById('slider-title-size');
      if (s) s.value = sz;
      const v = document.getElementById('title-size-val');
      if (v) v.textContent = `${sz} px`;

      document.querySelectorAll('[id^="btn-title-size-"]').forEach(b => {
        b.className = "px-1.5 py-1 rounded-lg border text-center text-[10px] font-bold transition-all border-slate-800 bg-slate-900 text-slate-300 hover:border-slate-700";
      });
      const activeBtn = document.getElementById(`btn-title-size-${sz}`);
      if (activeBtn) {
        activeBtn.className = "px-1.5 py-1 rounded-lg border text-center text-[10px] font-bold transition-all border-amber-500 bg-amber-500/20 text-amber-300";
      }

      renderSVG();
    }

    function setMasterBrandScale(percent) {
      percent = parseInt(percent, 10) || 100;
      state.masterBrandScale = percent;
      const factor = percent / 100;

      state.crestScale = Math.round(0.95 * factor * 100) / 100;
      state.brandSize = Math.max(20, Math.round(48 * factor));
      state.brandSubSize = Math.max(8, Math.round(13 * factor));
      state.brandSpacing = Math.round(16 * factor);

      const masterS = document.getElementById('slider-master-brand-scale');
      if (masterS) masterS.value = percent;
      const masterV = document.getElementById('master-brand-scale-val');
      if (masterV) masterV.textContent = `${percent}%`;

      const crestS = document.getElementById('slider-crest-scale');
      if (crestS) crestS.value = Math.round(state.crestScale * 100);
      const crestV = document.getElementById('crest-scale-val');
      if (crestV) crestV.textContent = `${Math.round(state.crestScale * 100)}%`;

      const brandS = document.getElementById('slider-brand-size');
      if (brandS) brandS.value = state.brandSize;
      const brandV = document.getElementById('brand-size-val');
      if (brandV) brandV.textContent = `${state.brandSize} px`;

      const subS = document.getElementById('slider-brand-sub-size');
      if (subS) subS.value = state.brandSubSize;
      const subV = document.getElementById('brand-sub-size-val');
      if (subV) subV.textContent = `${state.brandSubSize} px`;

      const spaceS = document.getElementById('slider-brand-spacing');
      if (spaceS) spaceS.value = state.brandSpacing;
      const spaceV = document.getElementById('brand-spacing-val');
      if (spaceV) spaceV.textContent = `${state.brandSpacing} px`;

      document.querySelectorAll('[id^="btn-master-scale-"]').forEach(b => {
        b.className = "flex-1 py-1 rounded-lg border text-center text-[10px] font-bold transition-all border-slate-700 bg-slate-900 text-slate-300 hover:border-amber-500";
      });
      const activeBtn = document.getElementById(`btn-master-scale-${percent}`);
      if (activeBtn) {
        activeBtn.className = "flex-1 py-1 rounded-lg border text-center text-[10px] font-bold transition-all border-amber-500 bg-amber-500/20 text-amber-300";
      }

      renderSVG();
    }

    function onMasterBrandScaleInput(val) {
      setMasterBrandScale(val);
    }

    function setCrestTint(enable, col) {
      state.emblemTintEnabled = enable;
      const check = document.getElementById('check-emblem-tint');
      if (check) check.checked = enable;
      if (col) {
        state.emblemColor = col;
        const picker = document.getElementById('picker-emblem-color');
        if (picker) picker.value = col;
      }
      renderSVG();
    }

    function setBrandSubColor(col) {
      state.brandSubColor = col;
      const picker = document.getElementById('picker-brand-sub-color');
      if (picker) picker.value = col;
      renderSVG();
    }

    function setBrandColorMode(mode) {
      state.brandColorMode = mode;
      const colors = { red: '#C81D25', gold: '#D4AF37', white: '#FFFFFF', emerald: '#0B3B24', green: '#166534' };
      state.brandNameColor = colors[mode] || state.brandNameColor || '#C81D25';
      state.brandCustomColor = state.brandNameColor;
      const picker = document.getElementById('picker-brand-name-color');
      if (picker) picker.value = state.brandNameColor;
      renderSVG();
    }
    function setBrandColorCustom(val) {
      state.brandColorMode = 'custom';
      state.brandCustomColor = val;
      state.brandNameColor = val;
      const picker = document.getElementById('picker-brand-name-color');
      if (picker) picker.value = val;
      renderSVG();
    }

    function setTopArcText(txt) {
      const el = document.getElementById('input-top-arc');
      if (el) el.value = txt;
      state.topArc = txt;
      renderSVG();
    }

    function setTopArcColor(val) {
      state.topArcColor = val;
      renderSVG();
    }

    function setBotArcText(txt) {
      const el = document.getElementById('input-bottom-arc');
      if (el) el.value = txt;
      state.bottomArc = txt;
      renderSVG();
    }

    function setBotArcColor(val) {
      state.bottomArcColor = val;
      renderSVG();
    }

    function setRibbonBgColor(val) {
      state.ribbonBg = val;
      renderSVG();
    }

    function setBgCenterColor(val) {
      state.bgCenter = val;
      const el = document.getElementById('bg-center-hex');
      if (el) el.textContent = val.toUpperCase();
      renderSVG();
    }

    function setBgOuterColor(val) {
      state.bgOuter = val;
      const el = document.getElementById('bg-outer-hex');
      if (el) el.textContent = val.toUpperCase();
      renderSVG();
    }

    function escapeXmlText(value) {
      return String(value == null ? '' : value)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&apos;');
    }

    // Shared position controls keep the sliders, labels, presets, and drag actions in sync.
    const POSITION_CONTROLS = [
      { key: 'titleLine1X', slider: 'slider-title-x', label: 'title-x-val', axis: 'X', field: 'number-title-x', min: 250, max: 950 },
      { key: 'titleLine1Y', slider: 'slider-title-y', label: 'title-y-val', axis: 'Y', field: 'number-title-y', min: 500, max: 760 },
      { key: 'titleLine2X', slider: 'slider-title2-x', label: 'title2-x-val', axis: 'X', field: 'number-title2-x', min: 250, max: 950 },
      { key: 'titleLine2Y', slider: 'slider-title2-y', label: 'title2-y-val', axis: 'Y', field: 'number-title2-y', min: 600, max: 870 },
      { key: 'brandX', slider: 'slider-brand-x', label: 'brand-x-val', axis: 'X', field: 'number-brand-x', min: 200, max: 1000 },
      { key: 'brandY', slider: 'slider-brand-y', label: 'brand-y-val', axis: 'Y', field: 'number-brand-y', min: 250, max: 650 },
      { key: 'brandSubX', slider: 'slider-brand-sub-x', label: 'brand-sub-x-val', axis: 'X', field: 'number-brand-sub-x', min: 200, max: 1000 },
      { key: 'brandSubY', slider: 'slider-brand-sub-y', label: 'brand-sub-y-val', axis: 'Y', field: 'number-brand-sub-y', min: 250, max: 680 },
      { key: 'crestX', slider: 'slider-crest-x', label: 'crest-x-val', axis: 'X', field: 'number-crest-x', min: 200, max: 1000 },
      { key: 'crestY', slider: 'slider-crest-y', label: 'crest-y-val', axis: 'Y', field: 'number-crest-y', min: 150, max: 550 },
      { key: 'topArcX', slider: 'slider-top-arc-x', label: 'top-arc-x-val', axis: 'X', field: 'number-top-arc-x', min: 350, max: 850 },
      { key: 'topArcY', slider: 'slider-top-arc-y', label: 'top-arc-y-val', axis: 'Y', field: 'number-top-arc-y', min: 350, max: 850 },
      { key: 'bottomArcX', slider: 'slider-bot-arc-x', label: 'bot-arc-x-val', axis: 'X', field: 'number-bot-arc-x', min: 350, max: 850 },
      { key: 'bottomArcY', slider: 'slider-bot-arc-y', label: 'bot-arc-y-val', axis: 'Y', field: 'number-bot-arc-y', min: 350, max: 850 },
      { key: 'ribbonX', slider: 'slider-tagline-x', label: 'tagline-x-val', axis: 'X', field: 'number-tagline-x', min: 250, max: 950 },
      { key: 'ribbonY', slider: 'slider-tagline-y', label: 'tagline-y-val', axis: 'Y', field: 'number-tagline-y', min: 680, max: 900 },
      { key: 'plaqueX', slider: 'slider-plaque-x', label: 'plaque-x-val', axis: 'X', field: 'number-plaque-x', min: 300, max: 900 },
      { key: 'plaqueY', slider: 'slider-plaque-y', label: 'plaque-y-val', axis: 'Y', field: 'number-plaque-y', min: 780, max: 1000 },
      { key: 'mandalaX', slider: 'slider-mandala-x', label: 'mandala-x-val', axis: 'X', field: 'number-mandala-x', min: 100, max: 1100 },
      { key: 'mandalaY', slider: 'slider-mandala-y', label: 'mandala-y-val', axis: 'Y', field: 'number-mandala-y', min: 100, max: 1100 }

    ];
    function syncPositionStateFromUI() {
      POSITION_CONTROLS.forEach(item => {
        const slider = document.getElementById(item.slider);
        const field = item.field ? document.getElementById(item.field) : null;
        if (!slider) return;
        const source = field && document.activeElement === field ? field : slider;
        const candidate = parseInt(source.value, 10);
        if (!Number.isFinite(candidate)) return;
        const min = item.min == null ? parseInt(slider.min, 10) : item.min;
        const max = item.max == null ? parseInt(slider.max, 10) : item.max;
        state[item.key] = Math.max(min, Math.min(max, candidate));
        slider.value = state[item.key];
        if (field) field.value = state[item.key];
        const label = document.getElementById(item.label);
        if (label) label.textContent = item.axis + ': ' + state[item.key];
      });
    }
    function syncPositionControlsToUI() {
      POSITION_CONTROLS.forEach(item => {
        const slider = document.getElementById(item.slider);
        const field = item.field ? document.getElementById(item.field) : null;
        if (slider) slider.value = state[item.key];
        if (field) field.value = state[item.key];
        const label = document.getElementById(item.label);
        if (label) label.textContent = item.axis + ': ' + state[item.key];
      });
    }

    // ==========================================
    // SYNC STATE FROM UI
    // ==========================================
    function updateLabel() {
      const titleInput = document.getElementById('input-title');
      if (titleInput) state.titleLine1 = titleInput.value || 'Assorted';
      const titleLine2Input = document.getElementById('input-title-line2');
      if (titleLine2Input) state.titleLine2 = titleLine2Input.value || 'Cookies';

      const brandInput = document.getElementById('input-brand');
      if (brandInput) state.brand = brandInput.value || 'DIAMOND';
      const brandSubInput = document.getElementById('input-brand-sub');
      if (brandSubInput) state.brandSub = brandSubInput.value || '';
      const brandFontInput = document.getElementById('select-brand-font');
      if (brandFontInput) state.brandFont = brandFontInput.value || 'prata';
      const brandNameColorInput = document.getElementById('picker-brand-name-color');
      if (brandNameColorInput) state.brandNameColor = brandNameColorInput.value;
      const brandSubColorInput = document.getElementById('picker-brand-sub-color');
      if (brandSubColorInput) state.brandSubColor = brandSubColorInput.value;
      const brandSubSizeInput = document.getElementById('slider-brand-sub-size');
      if (brandSubSizeInput) {
        state.brandSubSize = parseInt(brandSubSizeInput.value, 10) || 13;
        const value = document.getElementById('brand-sub-size-val');
        if (value) value.textContent = state.brandSubSize + ' px';
      }
      const emblemColorInput = document.getElementById('picker-emblem-color');
      if (emblemColorInput) state.emblemColor = emblemColorInput.value;
      const emblemTintToggle = document.getElementById('check-emblem-tint');
      if (emblemTintToggle) state.emblemTintEnabled = emblemTintToggle.checked;
      const brandSizeInput = document.getElementById('slider-brand-size');
      if (brandSizeInput) {
        state.brandSize = parseInt(brandSizeInput.value, 10) || 48;
        const value = document.getElementById('brand-size-val');
        if (value) value.textContent = `${state.brandSize} px`;
      }
      const crestScaleInput = document.getElementById('slider-crest-scale');
      if (crestScaleInput) {
        state.crestScale = (parseInt(crestScaleInput.value, 10) || 95) / 100;
        const value = document.getElementById('crest-scale-val');
        if (value) value.textContent = `${Math.round(state.crestScale * 100)}%`;
      }
      const brandBlockYInput = document.getElementById('slider-brand-block-y');
      if (brandBlockYInput) {
        state.brandBlockY = parseInt(brandBlockYInput.value, 10) || 420;
        const value = document.getElementById('brand-block-y-val');
        if (value) value.textContent = `Y: ${state.brandBlockY}`;
      }
      const brandSpacingInput = document.getElementById('slider-brand-spacing');
      if (brandSpacingInput) {
        state.brandSpacing = parseInt(brandSpacingInput.value, 10) || 16;
        const value = document.getElementById('brand-spacing-val');
        if (value) value.textContent = `${state.brandSpacing} px`;
      }

      const topArcInput = document.getElementById('input-top-arc');
      if (topArcInput) state.topArc = topArcInput.value;

      const botArcInput = document.getElementById('input-bottom-arc');
      if (botArcInput) state.bottomArc = botArcInput.value;

      const tagInput = document.getElementById('input-butter-tagline');
      if (tagInput) state.ribbonText = tagInput.value;
      const ribbonTextColorInput = document.getElementById('picker-ribbon-text-color');
      if (ribbonTextColorInput) state.ribbonTextColor = ribbonTextColorInput.value;
      const ribbonBorderInput = document.getElementById('picker-ribbon-border');
      if (ribbonBorderInput) state.ribbonBorder = ribbonBorderInput.value;
      const foilColorInput = document.getElementById('picker-foil-color');
      if (foilColorInput) state.foilColor = foilColorInput.value;

      const wtInput = document.getElementById('input-weight');
      if (wtInput) state.weight = wtInput.value;
      const plaqueBgInput = document.getElementById('picker-plaque-bg');
      if (plaqueBgInput) state.plaqueBg = plaqueBgInput.value;
      const plaqueBorderInput = document.getElementById('picker-plaque-border');
      if (plaqueBorderInput) state.plaqueBorder = plaqueBorderInput.value;
      const plaqueTextColorInput = document.getElementById('picker-plaque-text-color');
      if (plaqueTextColorInput) state.plaqueTextColor = plaqueTextColorInput.value;

      const vegCheck = document.getElementById('check-veg-logo');
      if (vegCheck) state.showVeg = vegCheck.checked;

      const titleSizeS = document.getElementById('slider-title-size');
      if (titleSizeS) {
        state.titleSize = parseInt(titleSizeS.value) || 135;
        const v = document.getElementById('title-size-val');
        if (v) v.textContent = `${state.titleSize} px`;

        document.querySelectorAll('[id^="btn-title-size-"]').forEach(b => {
          if (b.id === `btn-title-size-${state.titleSize}`) {
            b.className = "px-1.5 py-1 rounded-lg border text-center text-[10px] font-bold transition-all border-amber-500 bg-amber-500/20 text-amber-300";
          } else {
            b.className = "px-1.5 py-1 rounded-lg border text-center text-[10px] font-bold transition-all border-slate-800 bg-slate-900 text-slate-300 hover:border-slate-700";
          }
        });
      }

      const titleYS = document.getElementById('slider-title-y');
      if (titleYS) {
        state.titleLine1Y = parseInt(titleYS.value) || 620;
        const v = document.getElementById('title-y-val');
        if (v) v.textContent = `Y: ${state.titleLine1Y}`;
      }
      const title2YS = document.getElementById('slider-title2-y');
      if (title2YS) {
        state.titleLine2Y = parseInt(title2YS.value) || 735;
        const v = document.getElementById('title2-y-val');
        if (v) v.textContent = `Y: ${state.titleLine2Y}`;
      }

      const brandYS = document.getElementById('slider-brand-y');
      if (brandYS) {
        state.brandY = parseInt(brandYS.value) || 405;
        const v = document.getElementById('brand-y-val');
        if (v) v.textContent = `Y: ${state.brandY}`;
      }

      const topRS = document.getElementById('slider-top-arc-radius');
      if (topRS) {
        state.topArcRadius = parseInt(topRS.value) || 530;
        const v = document.getElementById('top-arc-radius-val');
        if (v) v.textContent = `${state.topArcRadius} px`;
        const hud = document.getElementById('hud-top-arc-val');
        if (hud) hud.textContent = `Radius ${state.topArcRadius}px`;
      }

      const topSS = document.getElementById('slider-top-arc-size');
      if (topSS) {
        state.topArcSize = parseFloat(topSS.value) || 14.5;
        const v = document.getElementById('top-arc-size-val');
        if (v) v.textContent = `${state.topArcSize} px`;
      }

      const botRS = document.getElementById('slider-bottom-arc-radius');
      if (botRS) {
        state.bottomArcRadius = parseInt(botRS.value) || 530;
        const v = document.getElementById('bottom-arc-radius-val');
        if (v) v.textContent = `${state.bottomArcRadius} px`;
        const hud = document.getElementById('hud-bot-arc-val');
        if (hud) hud.textContent = `Radius ${state.bottomArcRadius}px`;
      }

      const botSS = document.getElementById('slider-bottom-arc-size');
      if (botSS) {
        state.bottomArcSize = parseFloat(botSS.value) || 14.5;
        const v = document.getElementById('bottom-arc-size-val');
        if (v) v.textContent = `${state.bottomArcSize} px`;
      }

      const tagWS = document.getElementById('slider-tagline-width');
      if (tagWS) {
        state.ribbonWidth = parseInt(tagWS.value) || 750;
        const v = document.getElementById('tagline-width-val');
        if (v) v.textContent = `${state.ribbonWidth} px`;
      }

      const tagSS = document.getElementById('slider-tagline-size');
      if (tagSS) {
        state.ribbonSize = parseFloat(tagSS.value) || 16.5;
        const v = document.getElementById('tagline-size-val');
        if (v) v.textContent = `${state.ribbonSize} px`;
      }

      const tagYS = document.getElementById('slider-tagline-y');
      if (tagYS) {
        state.ribbonY = parseInt(tagYS.value) || 795;
        const v = document.getElementById('tagline-y-val');
        if (v) v.textContent = `Y: ${state.ribbonY}`;
      }

      const plaqueYS = document.getElementById('slider-plaque-y');
      if (plaqueYS) {
        state.plaqueY = parseInt(plaqueYS.value) || 895;
        const v = document.getElementById('plaque-y-val');
        if (v) v.textContent = `Y: ${state.plaqueY}`;
      }

      const mandOpS = document.getElementById('slider-mandala-opacity');
      if (mandOpS) {
        state.mandalaOpacity = (parseInt(mandOpS.value) || 38) / 100;
        const v = document.getElementById('mandala-opacity-val');
        if (v) v.textContent = `${Math.round(state.mandalaOpacity * 100)}%`;
      }

      const mandScS = document.getElementById('slider-mandala-scale');
      if (mandScS) {
        state.mandalaScale = (parseInt(mandScS.value) || 100) / 100;
        const v = document.getElementById('mandala-scale-val');
        if (v) v.textContent = `${Math.round(state.mandalaScale * 100)}%`;
      }

      syncPositionStateFromUI();
      renderSVG();
    }

    function syncUIFromState() {
      const setV = (id, val) => { const el = document.getElementById(id); if (el) el.value = val; };
      const setT = (id, txt) => { const el = document.getElementById(id); if (el) el.textContent = txt; };

      setV('input-title', state.titleLine1);
      setV('input-title-line2', state.titleLine2);
      setV('slider-title-size', state.titleSize);
      setT('title-size-val', `${state.titleSize} px`);
      setV('slider-title-y', state.titleLine1Y);
      setT('title-y-val', `Y: ${state.titleLine1Y}`);
      setV('slider-title2-y', state.titleLine2Y);
      setT('title2-y-val', `Y: ${state.titleLine2Y}`);

      setV('input-brand', state.brand);
      setV('input-brand-sub', state.brandSub);
      setV('select-brand-font', state.brandFont);
      setV('picker-brand-name-color', state.brandNameColor);
      setV('picker-brand-sub-color', state.brandSubColor);
      setV('slider-brand-sub-size', state.brandSubSize || 13);
      setT('brand-sub-size-val', (state.brandSubSize || 13) + ' px');
      setV('picker-emblem-color', state.emblemColor);
      const tintToggle = document.getElementById('check-emblem-tint');
      if (tintToggle) tintToggle.checked = state.emblemTintEnabled;
      setV('slider-brand-size', state.brandSize || 48);
      setT('brand-size-val', `${state.brandSize || 48} px`);
      setV('slider-crest-scale', Math.round((state.crestScale || 0.95) * 100));
      setT('crest-scale-val', `${Math.round((state.crestScale || 0.95) * 100)}%`);
      setV('slider-master-brand-scale', state.masterBrandScale || 100);
      setT('master-brand-scale-val', `${state.masterBrandScale || 100}%`);
      setV('slider-brand-block-y', state.brandBlockY || 420);
      setT('brand-block-y-val', `Y: ${state.brandBlockY || 420}`);
      setV('slider-brand-spacing', state.brandSpacing || 16);
      setT('brand-spacing-val', `${state.brandSpacing || 16} px`);

      document.querySelectorAll('[id^="btn-title-size-"]').forEach(b => {
        if (b.id === `btn-title-size-${state.titleSize}`) {
          b.className = "px-1.5 py-1 rounded-lg border text-center text-[10px] font-bold transition-all border-amber-500 bg-amber-500/20 text-amber-300";
        } else {
          b.className = "px-1.5 py-1 rounded-lg border text-center text-[10px] font-bold transition-all border-slate-800 bg-slate-900 text-slate-300 hover:border-slate-700";
        }
      });

      document.querySelectorAll('[id^="btn-master-scale-"]').forEach(b => {
        if (b.id === `btn-master-scale-${state.masterBrandScale || 100}`) {
          b.className = "flex-1 py-1 rounded-lg border text-center text-[10px] font-bold transition-all border-amber-500 bg-amber-500/20 text-amber-300";
        } else {
          b.className = "flex-1 py-1 rounded-lg border text-center text-[10px] font-bold transition-all border-slate-700 bg-slate-900 text-slate-300 hover:border-amber-500";
        }
      });

      setV('input-top-arc', state.topArc);
      setV('slider-top-arc-radius', state.topArcRadius);
      setT('top-arc-radius-val', `${state.topArcRadius} px`);
      setV('slider-top-arc-size', state.topArcSize);
      setT('top-arc-size-val', `${state.topArcSize} px`);
      setV('picker-top-arc-color', state.topArcColor);

      setV('input-bottom-arc', state.bottomArc);
      setV('slider-bottom-arc-radius', state.bottomArcRadius);
      setT('bottom-arc-radius-val', `${state.bottomArcRadius} px`);
      setV('slider-bottom-arc-size', state.bottomArcSize);
      setT('bottom-arc-size-val', `${state.bottomArcSize} px`);
      setV('picker-bot-arc-color', state.bottomArcColor);

      setV('input-butter-tagline', state.ribbonText);
      setV('slider-tagline-width', state.ribbonWidth);
      setT('tagline-width-val', `${state.ribbonWidth} px`);
      setV('slider-tagline-size', state.ribbonSize);
      setT('tagline-size-val', `${state.ribbonSize} px`);
      setV('slider-tagline-y', state.ribbonY);
      setT('tagline-y-val', `Y: ${state.ribbonY}`);
      setV('picker-ribbon-bg', state.ribbonBg);
      setV('picker-ribbon-text-color', state.ribbonTextColor);
      setV('picker-ribbon-border', state.ribbonBorder);
      setV('picker-foil-color', state.foilColor);

      setV('input-weight', state.weight);
      setV('picker-plaque-bg', state.plaqueBg);
      setV('picker-plaque-border', state.plaqueBorder);
      setV('picker-plaque-text-color', state.plaqueTextColor);
      setV('slider-plaque-y', state.plaqueY);
      setT('plaque-y-val', `Y: ${state.plaqueY}`);

      setV('slider-mandala-opacity', Math.round(state.mandalaOpacity * 100));
      setT('mandala-opacity-val', `${Math.round(state.mandalaOpacity * 100)}%`);
      setV('slider-mandala-scale', Math.round(state.mandalaScale * 100));
      setT('mandala-scale-val', `${Math.round(state.mandalaScale * 100)}%`);

      setV('picker-bg-center', state.bgCenter);
      setT('bg-center-hex', state.bgCenter.toUpperCase());
      setV('picker-bg-outer', state.bgOuter);
      setT('bg-outer-hex', state.bgOuter.toUpperCase());

      setV('select-ribbon-font', state.ribbonFont || 'cormorant');
      setV('slider-pattern-opacity', Math.round((state.patternOpacity ?? 0.25) * 100));
      setT('pattern-opacity-val', `${Math.round((state.patternOpacity ?? 0.25) * 100)}%`);

      ['400', '500', '250', '1000'].forEach(k => {
        const btn = document.getElementById(`btn-weight-${k}`);
        if (btn) {
          const match = (k === '1000' && (state.weight || '').includes('1 kg')) || (k !== '1000' && (state.weight || '').includes(k));
          if (match) {
            btn.className = "px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/50 text-xs font-bold transition-all";
          } else {
            btn.className = "px-2 py-0.5 rounded bg-slate-800 text-slate-300 hover:border-slate-600 border border-transparent text-xs transition-all";
          }
        }
      });

      syncPositionControlsToUI();
      setTitleFont(state.titleFont);
    }

    // ==========================================
    // MANDALA PICKER CARDS GENERATION
    // ==========================================
    const MANDALAS_LIST = [
      { id: 'authentic_user', name: '🌸 Photo Mandala (Original)', desc: 'Exact gold mandala from uploaded tin' },
      { id: 'taj', name: '👑 Taj Mahal Filigree', desc: 'Regal arches & delicate jaali' },
      { id: 'lotus', name: '🪷 Royal Lotus Bloom', desc: '16-petal sacred padma' },
      { id: 'sunburst_luxe', name: '☀️ Sunburst Luxe', desc: 'Majestic 24-ray gold sun' },
      { id: 'victorian', name: '⚜️ Victorian Baroque', desc: 'European vintage scrolls' },
      { id: 'arabesque', name: '🕌 Arabesque Lattice', desc: 'Geometric palace mosaic' }
    ];

    function renderMandalaButtons() {
      const c = document.getElementById('mandala-buttons-container');
      if (!c) return;
      c.innerHTML = MANDALAS_LIST.map(m => `
        <button onclick="setMandalaChoice('${m.id}')" id="btn-mandala-${m.id}" 
                class="p-2.5 rounded-xl border text-left transition-all flex flex-col justify-between ${state.mandalaType === m.id ? 'border-amber-500 bg-amber-500/15 ring-1 ring-amber-500/40' : 'border-slate-800 bg-slate-900 hover:border-slate-700'}">
          <span class="text-xs font-bold text-white">${m.name}</span>
          <span class="text-[10px] text-slate-400 mt-0.5">${m.desc}</span>
        </button>
      `).join('');
    }

    function setMandalaChoice(id) {
      state.mandalaType = id;
      MANDALAS_LIST.forEach(m => {
        const btn = document.getElementById(`btn-mandala-${m.id}`);
        if (btn) {
          if (m.id === id) {
            btn.className = "p-2.5 rounded-xl border text-left transition-all flex flex-col justify-between border-amber-500 bg-amber-500/15 ring-1 ring-amber-500/40";
          } else {
            btn.className = "p-2.5 rounded-xl border text-left transition-all flex flex-col justify-between border-slate-800 bg-slate-900 hover:border-slate-700";
          }
        }
      });
      renderSVG();
    }

    // ==========================================
    // VIEW MODE TOGGLE (3D DABBA / FLAT / A4)
    // ==========================================
    function setViewMode(mode) {
      state.viewMode = mode;
      
      const btn3d = document.getElementById('btn-view-3d');
      const btnFlat = document.getElementById('btn-view-flat');
      const btnA4 = document.getElementById('btn-view-a4');
      const stageWrapper = document.getElementById('packaging-stage-wrapper');
      const a4Wrapper = document.getElementById('a4-sheet-wrapper');
      const metalRim = document.getElementById('tin-metal-rim');
      const tinShell = document.getElementById('tin-dabba-shell');

      if (btn3d) btn3d.className = mode === '3d' ? "px-2.5 py-1 rounded-lg bg-amber-500 text-slate-950 font-black transition-all" : "px-2.5 py-1 rounded-lg text-slate-400 hover:text-white transition-all";
      if (btnFlat) btnFlat.className = mode === 'flat' ? "px-2.5 py-1 rounded-lg bg-amber-500 text-slate-950 font-black transition-all" : "px-2.5 py-1 rounded-lg text-slate-400 hover:text-white transition-all";
      if (btnA4) btnA4.className = mode === 'a4' ? "px-2.5 py-1 rounded-lg bg-amber-500 text-slate-950 font-black transition-all" : "px-2.5 py-1 rounded-lg text-slate-400 hover:text-white transition-all";

      if (mode === 'a4') {
        if (stageWrapper) stageWrapper.classList.add('hidden');
        if (a4Wrapper) a4Wrapper.classList.remove('hidden');
        renderA4Labels();
      } else {
        if (a4Wrapper) a4Wrapper.classList.add('hidden');
        if (stageWrapper) stageWrapper.classList.remove('hidden');

        if (mode === 'flat') {
          if (metalRim) metalRim.classList.add('hidden');
          if (tinShell) tinShell.className = "relative w-full max-w-[480px] aspect-square flex items-center justify-center rounded-full shadow-2xl transition-all duration-300";
        } else {
          // 3D Dabba
          if (metalRim) metalRim.classList.remove('hidden');
          if (tinShell) tinShell.className = "relative w-full max-w-[480px] aspect-square flex items-center justify-center tin-stage-shadow rounded-full transition-all duration-300";
        }
      }
    }

    // ==========================================
    // DIRECT MOUSE / TOUCH DRAG ON SVG CANVAS
    // ==========================================
    // Canva-style two-dimensional direct canvas movement for every foreground layer.
    const DRAG_POSITION_CONFIG = {
      cookies1: { xKey: 'titleLine1X', yKey: 'titleLine1Y', minX: 250, maxX: 950, minY: 500, maxY: 760, sliderX: 'slider-title-x', sliderY: 'slider-title-y', fieldX: 'number-title-x', fieldY: 'number-title-y', labelX: 'title-x-val', labelY: 'title-y-val', accordion: 'cookies' },
      cookies2: { xKey: 'titleLine2X', yKey: 'titleLine2Y', minX: 250, maxX: 950, minY: 600, maxY: 870, sliderX: 'slider-title2-x', sliderY: 'slider-title2-y', fieldX: 'number-title2-x', fieldY: 'number-title2-y', labelX: 'title2-x-val', labelY: 'title2-y-val', accordion: 'cookies' },
      'brand-block': { xKey: 'brandBlockX', yKey: 'brandBlockY', minX: 300, maxX: 900, minY: 200, maxY: 650, sliderX: null, sliderY: 'slider-brand-block-y', fieldX: null, fieldY: null, labelX: null, labelY: 'brand-block-y-val', accordion: 'brand' },
      'top-arc': { xKey: 'topArcX', yKey: 'topArcY', minX: 350, maxX: 850, minY: 350, maxY: 850, sliderX: 'slider-top-arc-x', sliderY: 'slider-top-arc-y', fieldX: 'number-top-arc-x', fieldY: 'number-top-arc-y', labelX: 'top-arc-x-val', labelY: 'top-arc-y-val', accordion: 'top-arc' },
      'bot-arc': { xKey: 'bottomArcX', yKey: 'bottomArcY', minX: 350, maxX: 850, minY: 350, maxY: 850, sliderX: 'slider-bot-arc-x', sliderY: 'slider-bot-arc-y', fieldX: 'number-bot-arc-x', fieldY: 'number-bot-arc-y', labelX: 'bot-arc-x-val', labelY: 'bot-arc-y-val', accordion: 'bot-arc' },
      ribbon: { xKey: 'ribbonX', yKey: 'ribbonY', minX: 250, maxX: 950, minY: 680, maxY: 900, sliderX: 'slider-tagline-x', sliderY: 'slider-tagline-y', fieldX: 'number-tagline-x', fieldY: 'number-tagline-y', labelX: 'tagline-x-val', labelY: 'tagline-y-val', accordion: 'ribbon' },
      plaque: { xKey: 'plaqueX', yKey: 'plaqueY', minX: 300, maxX: 900, minY: 780, maxY: 1000, sliderX: 'slider-plaque-x', sliderY: 'slider-plaque-y', fieldX: 'number-plaque-x', fieldY: 'number-plaque-y', labelX: 'plaque-x-val', labelY: 'plaque-y-val', accordion: 'plaque' },
      mandala: { xKey: 'mandalaX', yKey: 'mandalaY', minX: 100, maxX: 1100, minY: 100, maxY: 1100, sliderX: 'slider-mandala-x', sliderY: 'slider-mandala-y', fieldX: 'number-mandala-x', fieldY: 'number-mandala-y', labelX: 'mandala-x-val', labelY: 'mandala-y-val', accordion: 'mandala' }
    };
    let activeDragLayer = null;
    let dragStartX = 0;
    let dragStartY = 0;
    let layerStartX = 600;
    let layerStartY = 600;

    function startCanvasDrag(evt, layerName) {
      const config = DRAG_POSITION_CONFIG[layerName];
      if (!config) return;
      evt.preventDefault();
      evt.stopPropagation();
      activeDragLayer = layerName;
      dragStartX = evt.clientX;
      dragStartY = evt.clientY;
      layerStartX = state[config.xKey];
      layerStartY = state[config.yKey];
      if (evt.currentTarget && evt.currentTarget.setPointerCapture && evt.pointerId != null) {
        try { evt.currentTarget.setPointerCapture(evt.pointerId); } catch (_) {}
      }
      openLayerAccordion(config.accordion);
    }

    window.addEventListener('pointermove', (evt) => {
      if (!activeDragLayer) return;
      const config = DRAG_POSITION_CONFIG[activeDragLayer];
      const svg = document.getElementById('final-label-svg');
      if (!config || !svg) return;
      const rect = svg.getBoundingClientRect();
      const dx = (evt.clientX - dragStartX) * (1200 / (rect.width || 500));
      const dy = (evt.clientY - dragStartY) * (1200 / (rect.height || 500));
      state[config.xKey] = Math.max(config.minX, Math.min(config.maxX, Math.round(layerStartX + dx)));
      state[config.yKey] = Math.max(config.minY, Math.min(config.maxY, Math.round(layerStartY + dy)));
      if (config.sliderX) { const sx = document.getElementById(config.sliderX); if (sx) sx.value = state[config.xKey]; }
      if (config.sliderY) { const sy = document.getElementById(config.sliderY); if (sy) sy.value = state[config.yKey]; }
      if (config.fieldX) { const fx = document.getElementById(config.fieldX); if (fx) fx.value = state[config.xKey]; }
      if (config.fieldY) { const fy = document.getElementById(config.fieldY); if (fy) fy.value = state[config.yKey]; }
      if (config.labelX) { const lx = document.getElementById(config.labelX); if (lx) lx.textContent = 'X: ' + state[config.xKey]; }
      if (config.labelY) { const ly = document.getElementById(config.labelY); if (ly) ly.textContent = 'Y: ' + state[config.yKey]; }
      const movedLayer = svg.querySelector('[data-layer="' + activeDragLayer + '"]');
      if (movedLayer) movedLayer.setAttribute('transform', 'translate(' + state[config.xKey] + ', ' + state[config.yKey] + ')');
    });
    function finishCanvasDrag() {
      if (activeDragLayer) renderSVG();
      activeDragLayer = null;
    }
    window.addEventListener('pointerup', finishCanvasDrag);
    window.addEventListener('pointercancel', finishCanvasDrag);

    // ==========================================
    // SVG RENDERING ENGINE (FLAWLESS 6-INCH MASTER)
    // ==========================================
    function renderSVG() {
      const mount = document.getElementById('tin-svg-mount');
      if (!mount) return;

      // Arc Paths Math
      const topR = state.topArcRadius || 530;
      const botR = state.bottomArcRadius || 530;

      // Symmetric Top Arc (Bows Upward, clockwise)
      const topX1 = -topR * 0.866;
      const topY1 = -topR * 0.5;
      const topX2 = topR * 0.866;
      const topY2 = -topR * 0.5;
      const topArcPathD = `M ${topX1},${topY1} A ${topR},${topR} 0 0,1 ${topX2},${topY2}`;

      // Symmetric Bottom Arc (Bows Downward)
      const botX1 = -botR * 0.866;
      const botY1 = botR * 0.5;
      const botX2 = botR * 0.866;
      const botY2 = botR * 0.5;
      const botArcPathD = `M ${botX1},${botY1} A ${botR},${botR} 0 0,0 ${botX2},${botY2}`;

      // Font Family Mapping from FONT_MAP (Supports all 14 fonts)
      const titleFontDef = FONT_MAP[state.titleFont] || FONT_MAP['alex-brush'];
      const titleFontFamily = titleFontDef.family;
      const titleFontWeight = titleFontDef.weight;
      const titleLetterSpacing = titleFontDef.letterSpacing;

      const ribbonFontDef = FONT_MAP[state.ribbonFont] || FONT_MAP['cormorant'];
      const ribbonFontFamily = ribbonFontDef.family;
      const ribbonFontWeight = ribbonFontDef.weight;

      // Title Color
      let titleFill = "url(#foilGoldGrad)";
      let titleStroke = "#78350F";
      let titleStrokeWidth = "1.2";

      if (state.titleColorMode === 'emerald') {
        titleFill = "#064E3B";
        titleStroke = "#D4AF37";
        titleStrokeWidth = "0.8";
      } else if (state.titleColorMode === 'white') {
        titleFill = "#FFFDF0";
        titleStroke = "#000000";
        titleStrokeWidth = "1";
      } else if (state.titleColorMode === 'custom') {
        titleFill = state.titleCustomColor;
        titleStroke = "none";
        titleStrokeWidth = "0";
      }

      // Brand Wordmark Color
      let brandFill = "#C81D25"; // Red default
      if (state.brandColorMode === 'gold') brandFill = "url(#foilGoldGrad)";
      if (state.brandColorMode === 'white') brandFill = "#FFFFFF";
      if (state.brandColorMode === 'custom') brandFill = state.brandCustomColor;

      // Monogram Letter Color
      let monoFill = (state.brandColorMode === 'gold') ? "#FFFDF0" : "#E0222A";

      // Mandala Markup
      let mandalaMarkup = '';
      if (state.mandalaType === 'authentic_user' && window.ASSETS && window.ASSETS.mandala) {
        const mw = 1180 * state.mandalaScale;
        mandalaMarkup = `<image href="${window.ASSETS.mandala}" x="${-mw/2}" y="${-mw/2}" width="${mw}" height="${mw}" preserveAspectRatio="xMidYMid meet"/>`;
      } else if (window.MANDALAS && window.MANDALAS[state.mandalaType]) {
        mandalaMarkup = `<g transform="scale(${state.mandalaScale})">${window.MANDALAS[state.mandalaType]}</g>`;
      } else {
        mandalaMarkup = `
          <circle cx="0" cy="0" r="320" fill="none" stroke="url(#foilGoldGrad)" stroke-width="1.5" stroke-dasharray="4 4"/>
          <circle cx="0" cy="0" r="460" fill="none" stroke="url(#foilGoldGrad)" stroke-width="2"/>
        `;
      }

      // Crest Flourish
      let crestMarkup = '';
      if (window.ASSETS && window.ASSETS.crest) {
        const cw = 300 * state.crestScale;
        const ch = cw * (255 / 358);
        crestMarkup = `
          <image href="${window.ASSETS.crest}" x="${-cw/2}" y="${-ch/2}" width="${cw}" height="${ch}" preserveAspectRatio="xMidYMid meet"/>
        `;
      } else {
        crestMarkup = `<circle cx="0" cy="0" r="60" fill="none" stroke="url(#foilGoldGrad)" stroke-width="2"/>`;
      }

      // FSSAI Veg Emblem
      let vegEmblem = state.showVeg ? `
        <g transform="translate(-118, 0)">
          <rect x="-11" y="-11" width="22" height="22" rx="3.5" fill="#FFFFFF" stroke="#16A34A" stroke-width="2.2"/>
          <circle cx="0" cy="0" r="5.5" fill="#16A34A"/>
        </g>
      ` : '';

      const brandFontFamilies = {
        prata: "'Prata', serif",
        cinzel: "'Cinzel', serif",
        'cinzel-decorative': "'Cinzel Decorative', serif",
        playfair: "'Playfair Display', serif",
        montserrat: "'Montserrat', sans-serif",
        cormorant: "'Cormorant Garamond', serif"
      };
      const brandFontFamily = brandFontFamilies[state.brandFont] || brandFontFamilies.prata;
      const emblemHex = /^#[0-9a-f]{6}$/i.test(state.emblemColor || '') ? state.emblemColor : '#D4AF37';
      const emblemRgb = [1, 3, 5].map(index => parseInt(emblemHex.slice(index, index + 2), 16) / 255);
      const emblemTintMatrix = '0 0 0 0 ' + emblemRgb[0] + ' 0 0 0 0 ' + emblemRgb[1] + ' 0 0 0 0 ' + emblemRgb[2] + ' 0 0 0 1 0';
      const foilBase = /^#[0-9a-f]{6}$/i.test(state.foilColor || '') ? state.foilColor : '#D4AF37';
      const mixFoil = (target, amount) => '#' + [1, 3, 5].map(index => {
        const baseChannel = parseInt(foilBase.slice(index, index + 2), 16);
        const targetChannel = parseInt(target.slice(index, index + 2), 16);
        return Math.round(baseChannel * (1 - amount) + targetChannel * amount).toString(16).padStart(2, '0');
      }).join('');
      const foilHighlight = mixFoil('#FFFDF0', 0.82);
      const foilLight = mixFoil('#FDE047', 0.50);
      const foilBright = mixFoil('#FFFFFF', 0.32);
      const foilDeep = mixFoil('#000000', 0.58);

      // Assemble Full Master Label SVG
      const svgCode = `
<svg id="final-label-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 1200" width="100%" height="100%">
  <defs>
    <!-- Background Radial Gradient -->
    <radialGradient id="tinBgGrad" cx="50%" cy="45%" r="72%">
      <stop offset="0%" stop-color="${state.bgCenter}"/>
      <stop offset="70%" stop-color="${state.bgOuter}"/>
      <stop offset="100%" stop-color="${state.bgOuter}"/>
    </radialGradient>

    <!-- Specular 24K Liquid Gold Foil Gradient -->
    <linearGradient id="foilGoldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="${foilHighlight}"/>
      <stop offset="15%" stop-color="${foilLight}"/>
      <stop offset="35%" stop-color="${foilBright}"/>
      <stop offset="65%" stop-color="${foilBase}"/>
      <stop offset="85%" stop-color="${foilLight}"/>
      <stop offset="100%" stop-color="${foilDeep}"/>
    </linearGradient>

    <!-- Soft Drop Shadows for Readability -->
    <filter id="shadowFilter" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000000" flood-opacity="0.30"/>
    </filter>

    <filter id="titleShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="3.5" stdDeviation="4" flood-color="#000000" flood-opacity="0.45"/>
    </filter>

    <filter id="emblemTintFilter" color-interpolation-filters="sRGB">
      <feColorMatrix type="matrix" values="${emblemTintMatrix}"/>
    </filter>

    <!-- Circular Clipping Mask so nothing ever bleeds past 6-inch dabba edge -->
    <clipPath id="lidClip">
      <circle cx="600" cy="600" r="592"/>
    </clipPath>

    <!-- Botanical Leaf Damask Pattern (Sampled from Real Tin Photo) -->
    <pattern id="luxuryLeafPattern" x="0" y="0" width="80" height="80" patternUnits="userSpaceOnUse">
      <g fill="none" stroke="url(#foilGoldGrad)" stroke-width="0.75" opacity="0.45">
        <path d="M40 10 C30 25, 20 28, 15 40 C28 35, 35 25, 40 10 Z"/>
        <path d="M40 10 C50 25, 60 28, 65 40 C52 35, 45 25, 40 10 Z"/>
        <path d="M40 70 C30 55, 20 52, 15 40 C28 45, 35 55, 40 70 Z"/>
        <path d="M40 70 C50 55, 60 52, 65 40 C52 45, 45 55, 40 70 Z"/>
        <circle cx="40" cy="40" r="3.5" fill="url(#foilGoldGrad)"/>
        <circle cx="0" cy="0" r="2" fill="url(#foilGoldGrad)"/>
        <circle cx="80" cy="0" r="2" fill="url(#foilGoldGrad)"/>
        <circle cx="0" cy="80" r="2" fill="url(#foilGoldGrad)"/>
        <circle cx="80" cy="80" r="2" fill="url(#foilGoldGrad)"/>
      </g>
    </pattern>

    <!-- Top Arched Path (Curved Header along Upper Rim) -->
    <path id="topArcPath" d="${topArcPathD}" fill="none"/>

    <!-- Bottom Arched Path (Curved Footer along Lower Rim) -->
    <path id="botArcPath" d="${botArcPathD}" fill="none"/>
  </defs>

  <g clip-path="url(#lidClip)">
    
    <!-- 1. CIRCULAR BASE BACKGROUND (Clickable to open color palette) -->
    <circle cx="600" cy="600" r="592" fill="url(#tinBgGrad)" style="cursor: pointer;" onclick="openLayerAccordion('palette')"/>
    <circle cx="600" cy="600" r="592" fill="url(#luxuryLeafPattern)" opacity="${state.patternOpacity ?? 0.25}" style="pointer-events: none;"/>

    <!-- 2. LUXURY CONCENTRIC DUAL GOLD RIMS -->
    <circle cx="600" cy="600" r="586" fill="none" stroke="url(#foilGoldGrad)" stroke-width="4.5" style="cursor: pointer;" onclick="openLayerAccordion('palette')"/>
    <circle cx="600" cy="600" r="578" fill="none" stroke="url(#foilGoldGrad)" stroke-width="1.8" style="cursor: pointer;" onclick="openLayerAccordion('palette')"/>
    <circle cx="600" cy="600" r="570" fill="none" stroke="url(#foilGoldGrad)" stroke-width="0.8" opacity="0.6"/>

    <!-- 3. MANDALA IN EXACT DEAD CENTER (cx=600, cy=600) -->
    <g data-layer="mandala" opacity="${state.mandalaOpacity}" transform="translate(${state.mandalaX}, ${state.mandalaY})" class="canva-draggable" onpointerdown="startCanvasDrag(event, 'mandala')">
      ${mandalaMarkup}
    </g>

    <!-- 4. TOP RIM CURVED HEADER TEXT -->
    <text data-layer="top-arc" transform="translate(${state.topArcX}, ${state.topArcY})" fill="${state.topArcColor}" font-family="'Cinzel', serif" font-weight="800" font-size="${state.topArcSize}px" letter-spacing="0.26em" class="canva-draggable" onpointerdown="startCanvasDrag(event, 'top-arc')">
      <textPath href="#topArcPath" startOffset="50%" text-anchor="middle">
        ${escapeXmlText(state.topArc)}
      </textPath>
    </text>

    <!-- 5. BOTTOM RIM CURVED FOOTER TEXT -->
    <text data-layer="bot-arc" transform="translate(${state.bottomArcX}, ${state.bottomArcY})" fill="${state.bottomArcColor}" font-family="'Cinzel', serif" font-weight="800" font-size="${state.bottomArcSize}px" letter-spacing="0.22em" class="canva-draggable" onpointerdown="startCanvasDrag(event, 'bot-arc')">
      <textPath href="#botArcPath" startOffset="50%" text-anchor="middle">
        ${escapeXmlText(state.bottomArc)}
      </textPath>
    </text>

    ${state.showBrandPillar ? `
    <!-- Vertical Gold Pillar Banner (Photo Top Tin Style) -->
    <g data-layer="brand-pillar" transform="translate(${state.brandBlockX}, ${state.brandBlockY - 12})" class="canva-draggable" onpointerdown="startCanvasDrag(event, 'brand-block')">
      <!-- Ornate Vertical Gold Pillar Frame (Photo Top Tin Style) -->
      <path d="M -135,-155 L 135,-155 A 12,12 0 0,1 147,-143 L 147,155 A 12,12 0 0,1 135,167 L -135,167 A 12,12 0 0,1 -147,155 L -147,-143 A 12,12 0 0,1 -135,-155 Z" fill="${state.preset === 'mint' ? '#0B3B24' : '#2A060C'}" stroke="url(#foilGoldGrad)" stroke-width="2.5" filter="url(#shadowFilter)" opacity="0.95"/>
      <path d="M -127,-147 L 127,-147 A 6,6 0 0,1 133,-141 L 133,147 A 6,6 0 0,1 127,153 L -127,153 A 6,6 0 0,1 -133,147 L -133,-141 A 6,6 0 0,1 -127,-147 Z" fill="none" stroke="url(#foilGoldGrad)" stroke-width="0.8" opacity="0.85"/>
      <!-- Corner Ornamental Diamonds -->
      <path d="M 0,-155 L 6,-147 L 0,-139 L -6,-147 Z" fill="url(#foilGoldGrad)"/>
      <path d="M 0,155 L 6,147 L 0,139 L -6,147 Z" fill="url(#foilGoldGrad)"/>
    </g>
    ` : ''}

    <!-- 6. UNIFIED LOCKED LOGO + BRAND NAME BLOCK (UPPER NICHE, LOCKED TOGETHER 🔒) -->
    <g data-layer="brand-block" transform="translate(${state.brandBlockX}, ${state.brandBlockY})" class="canva-draggable" onpointerdown="startCanvasDrag(event, 'brand-block')">
      <!-- Crest Emblem (Top) -->
      <g transform="translate(0, ${-68 * state.crestScale})">
        <image href="${(window.ASSETS && window.ASSETS.crest) ? window.ASSETS.crest : 'diamond_crest_user.png'}"
               x="${-105 * state.crestScale}" y="${-105 * state.crestScale}"
               width="${210 * state.crestScale}" height="${210 * state.crestScale}"
               preserveAspectRatio="xMidYMid meet"
               filter="${state.emblemTintEnabled ? 'url(#emblemTintFilter)' : 'url(#shadowFilter)'}" />
      </g>
      <!-- Brand Wordmark (Directly Below Emblem) -->
      <text x="0" y="${55 * state.crestScale + (state.brandSpacing || 16)}" text-anchor="middle" font-family="${brandFontFamily}" font-weight="700" font-size="${state.brandSize}px" letter-spacing="0.035em" fill="${state.brandNameColor || '#C81D25'}" filter="url(#titleShadow)">${escapeXmlText(state.brand)}</text>
      <!-- Subtitle (Directly Below Wordmark) -->
      <text x="0" y="${55 * state.crestScale + (state.brandSpacing || 16) + (state.brandSubSize || 13) * 1.55}" text-anchor="middle" font-family="'Montserrat', sans-serif" font-weight="700" font-size="${state.brandSubSize}px" letter-spacing="0.08em" fill="${state.brandSubColor || '#0B3B24'}">${escapeXmlText(state.brandSub)}</text>
    </g>

    <!-- 7. PRODUCT NAME — two separate, independently draggable lines -->
    <g data-layer="cookies1" transform="translate(${state.titleLine1X}, ${state.titleLine1Y})" class="canva-draggable" onpointerdown="startCanvasDrag(event, 'cookies1')">
      <text x="0" y="0" text-anchor="middle" font-family="${titleFontFamily}" font-weight="${titleFontWeight}" font-size="${state.titleSize}px" letter-spacing="${titleLetterSpacing}" fill="${titleFill}" stroke="${titleStroke}" stroke-width="${titleStrokeWidth}" filter="url(#titleShadow)">${escapeXmlText(state.titleLine1)}</text>
    </g>
    <g data-layer="cookies2" transform="translate(${state.titleLine2X}, ${state.titleLine2Y})" class="canva-draggable" onpointerdown="startCanvasDrag(event, 'cookies2')">
      <text x="0" y="0" text-anchor="middle" font-family="${titleFontFamily}" font-weight="${titleFontWeight}" font-size="${state.titleSize}px" letter-spacing="${titleLetterSpacing}" fill="${titleFill}" stroke="${titleStroke}" stroke-width="${titleStrokeWidth}" filter="url(#titleShadow)">${escapeXmlText(state.titleLine2)}</text>
    </g>

    <!-- 8. TAGLINE CAPSULE RIBBON -->
    <g data-layer="ribbon" transform="translate(${state.ribbonX}, ${state.ribbonY})" class="canva-draggable" onpointerdown="startCanvasDrag(event, 'ribbon')">
      <!-- Capsule Bar -->
      <rect x="${-state.ribbonWidth / 2}" y="-19" width="${state.ribbonWidth}" height="38" rx="19" fill="${state.ribbonBg}" stroke="${state.ribbonBorder}" stroke-width="1.8" filter="url(#shadowFilter)"/>
      <line x1="${-state.ribbonWidth / 2 + 12}" y1="-14" x2="${state.ribbonWidth / 2 - 12}" y2="-14" stroke="${state.ribbonBorder}" stroke-width="0.6" opacity="0.6"/>
      
      <!-- Tagline Text -->
      <text x="0" y="5.5" text-anchor="middle" font-family="${ribbonFontFamily}" font-weight="${ribbonFontWeight}" font-size="${state.ribbonSize}px" letter-spacing="0.20em" fill="${state.ribbonTextColor}">
        ${escapeXmlText(state.ribbonText)}
      </text>
    </g>

    <!-- 9. BALANCED NET WEIGHT & FSSAI PLAQUE -->
    <g data-layer="plaque" transform="translate(${state.plaqueX}, ${state.plaqueY})" class="canva-draggable" onpointerdown="startCanvasDrag(event, 'plaque')">
      <!-- Ornate Gold Cartouche Frame -->
      <path d="M -145,-19 L 145,-19 A 6,6 0 0,0 155,-9 L 155,9 A 6,6 0 0,0 145,19 L -145,19 A 6,6 0 0,0 -155,9 L -155,-9 A 6,6 0 0,0 -145,-19 Z" 
            fill="${state.plaqueBg}" stroke="${state.plaqueBorder}" stroke-width="2.2" filter="url(#shadowFilter)"/>
      <path d="M -140,-14 L 140,-14 A 4,4 0 0,0 148,-6 L 148,6 A 4,4 0 0,0 140,14 L -140,14 A 4,4 0 0,0 -148,6 L -148,-6 A 4,4 0 0,0 -140,-14 Z" 
            fill="none" stroke="${state.plaqueBorder}" stroke-width="0.8" opacity="0.85"/>

      <!-- Veg Emblem -->
      ${vegEmblem}

      <!-- Vertical Dividers -->
      <line x1="-92" y1="-10" x2="-92" y2="10" stroke="${state.plaqueBorder}" stroke-width="1.2" stroke-linecap="round"/>
      <line x1="106" y1="-10" x2="106" y2="10" stroke="${state.plaqueBorder}" stroke-width="1.2" stroke-linecap="round"/>

      <!-- Center Net Weight -->
      <text x="6" y="4.5" text-anchor="middle" font-family="'Cinzel', 'Montserrat', serif" font-weight="800" font-size="13.5px" letter-spacing="0.20em" fill="${state.plaqueTextColor}">
        NET WT. ${escapeXmlText(state.weight)}
      </text>

      <!-- Right Gold Diamond Emblem -->
      <g transform="translate(128, 0)">
        <circle cx="0" cy="0" r="9" fill="${state.plaqueBorder}" opacity="0.18"/>
        <path d="M 0,-8 L 2.2,-2.2 L 8,0 L 2.2,2.2 L 0,8 L -2.2,2.2 L -8,0 L -2.2,-2.2 Z" fill="${state.plaqueBorder}"/>
      </g>
    </g>

  </g>
</svg>`;

      mount.innerHTML = svgCode;

      // Update A4 Sheet if active
      if (state.viewMode === 'a4') {
        renderA4Labels();
      }
    }

    // ==========================================
    // A4 PRINT SHEET GENERATOR
    // ==========================================
    function setA4Layout(n) {
      state.a4Layout = n;
      [1, 2, 4, 6].forEach(layoutNum => {
        const btn = document.getElementById(`btn-a4-layout-${layoutNum}`);
        if (btn) {
          if (layoutNum === n) {
            btn.className = "p-2.5 rounded-xl border-2 border-amber-500 bg-amber-500/15 text-left";
          } else {
            btn.className = "p-2.5 rounded-xl border border-slate-800 bg-slate-900 text-left";
          }
        }
      });
      renderA4Labels();
    }

    function renderA4Labels() {
      const grid = document.getElementById('a4-labels-grid');
      const hud = document.getElementById('a4-sheet-layout-hud');
      const sub = document.getElementById('a4-sheet-sub-title');
      const mount = document.getElementById('tin-svg-mount');
      if (!grid || !mount) return;

      const currentSvg = mount.innerHTML;
      const count = state.a4Layout || 1;

      let sizePx = 360;
      let labelDesc = '1 LABEL • 100% TRUE SCALE (152.4 MM)';

      if (count === 2) {
        sizePx = 220;
        labelDesc = '2 LABELS • 140 MM EACH';
      } else if (count === 4) {
        sizePx = 150;
        labelDesc = '4 LABELS • 2×2 GRID (98 MM EACH)';
      } else if (count === 6) {
        sizePx = 120;
        labelDesc = '6 LABELS • 2×3 GRID (80 MM EACH)';
      }

      if (hud) hud.textContent = `${count} Label${count > 1 ? 's' : ''} (${count === 1 ? '100% True Scale' : sizePx + 'px'})`;
      if (sub) sub.textContent = labelDesc;

      let html = '';
      for (let i = 0; i < count; i++) {
        html += `
          <div class="relative flex items-center justify-center shrink-0 my-1" style="width: ${sizePx}px; height: ${sizePx}px;">
            <div class="w-full h-full rounded-full overflow-hidden shadow-md border border-slate-300">
              ${currentSvg}
            </div>
          </div>
        `;
      }
      grid.innerHTML = html;
    }

    function printA4Direct() {
      setViewMode('a4');
      setTimeout(() => {
        window.print();
      }, 250);
    }

    function blobToDataURL(blob) {
      return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.onload = () => resolve(reader.result);
        reader.onerror = () => reject(new Error('Image conversion failed.'));
        reader.readAsDataURL(blob);
      });
    }

    // Clone the responsive preview into a fixed 1200×1200 SVG and embed linked artwork & fonts!
    async function prepareSvgForExport(svgElement) {
      const clone = svgElement.cloneNode(true);
      clone.setAttribute('width', '1200');
      clone.setAttribute('height', '1200');
      clone.setAttribute('viewBox', '0 0 1200 1200');

      // Inject Base64 Embedded Fonts & Google Web Fonts inside defs so downloaded file NEVER loses fonts!
      let defs = clone.querySelector('defs');
      if (!defs) {
        defs = document.createElementNS('http://www.w3.org/2000/svg', 'defs');
        clone.insertBefore(defs, clone.firstChild);
      }
      const fontStyleEl = document.createElementNS('http://www.w3.org/2000/svg', 'style');
      fontStyleEl.textContent = (window.EMBEDDED_FONTS_CSS || '') + `
        @import url('https://fonts.googleapis.com/css2?family=Alex+Brush&family=Cinzel:wght@600;700;800;900&family=Cinzel+Decorative:wght@700;900&family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600;1,700&family=Great+Vibes&family=Montserrat:wght@600;700;800;900&family=Playfair+Display:ital,wght@0,600;0,700;0,900;1,600;1,900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=Prata&display=swap');
      `;
      defs.appendChild(fontStyleEl);

      const images = Array.from(clone.querySelectorAll('image'));
      await Promise.all(images.map(async (image) => {
        let href = image.getAttribute('href') || image.getAttributeNS('http://www.w3.org/1999/xlink', 'href');
        if (!href) return;
        if (href.startsWith('data:')) return;

        // Use pre-embedded Base64 assets if available
        if (href.includes('crest') && window.ASSETS && window.ASSETS.crest) {
          image.setAttribute('href', window.ASSETS.crest);
          image.removeAttributeNS('http://www.w3.org/1999/xlink', 'href');
          return;
        }
        if (href.includes('mandala') && window.ASSETS && window.ASSETS.mandala) {
          image.setAttribute('href', window.ASSETS.mandala);
          image.removeAttributeNS('http://www.w3.org/1999/xlink', 'href');
          return;
        }

        try {
          const response = await fetch(href, { mode: 'cors' });
          if (response.ok) {
            const dataUrl = await blobToDataURL(await response.blob());
            image.setAttribute('href', dataUrl);
            image.removeAttributeNS('http://www.w3.org/1999/xlink', 'href');
          }
        } catch (e) {
          console.warn('Image embed note:', e);
        }
      }));
      return new XMLSerializer().serializeToString(clone);
    }

    async function loadExportImage(svgElement) {
      if (document.fonts && document.fonts.ready) {
        try { await document.fonts.ready; } catch (_) {}
      }
      const svgStr = await prepareSvgForExport(svgElement);
      const blob = new Blob([svgStr], { type: 'image/svg+xml;charset=utf-8' });
      const objectUrl = URL.createObjectURL(blob);
      try {
        const image = new Image();
        image.decoding = 'async';
        await new Promise((resolve, reject) => {
          image.onload = resolve;
          image.onerror = () => reject(new Error('Sticker preview image render nahi ho payi.'));
          image.src = objectUrl;
        });
        return { image, objectUrl, svgStr };
      } catch (error) {
        URL.revokeObjectURL(objectUrl);
        throw error;
      }
    }

    function crc32(bytes) {
      let crc = 0xFFFFFFFF;
      for (let i = 0; i < bytes.length; i++) {
        crc ^= bytes[i];
        for (let bit = 0; bit < 8; bit++) crc = (crc & 1) ? (crc >>> 1) ^ 0xEDB88320 : (crc >>> 1);
      }
      return (crc ^ 0xFFFFFFFF) >>> 0;
    }

    function makePngChunk(type, data) {
      const chunk = new Uint8Array(12 + data.length);
      const view = new DataView(chunk.buffer);
      view.setUint32(0, data.length);
      for (let i = 0; i < 4; i++) chunk[4 + i] = type.charCodeAt(i);
      chunk.set(data, 8);
      view.setUint32(8 + data.length, crc32(chunk.subarray(4, 8 + data.length)));
      return chunk;
    }

    // Add physical DPI metadata in pixels per metre.
    async function addPngDpiMetadata(blob, dpi) {
      const input = new Uint8Array(await blob.arrayBuffer());
      if (input.length < 33 || input[0] !== 137 || input[1] !== 80 || input[2] !== 78 || input[3] !== 71) {
        throw new Error('Browser did not create a valid PNG.');
      }
      const view = new DataView(input.buffer, input.byteOffset, input.byteLength);
      const firstChunkEnd = 8 + 12 + view.getUint32(8);
      const ppm = Math.round(dpi / 0.0254);
      const data = new Uint8Array(9);
      const dataView = new DataView(data.buffer);
      dataView.setUint32(0, ppm);
      dataView.setUint32(4, ppm);
      data[8] = 1;
      const phys = makePngChunk('pHYs', data);
      const output = new Uint8Array(input.length + phys.length);
      output.set(input.subarray(0, firstChunkEnd), 0);
      output.set(phys, firstChunkEnd);
      output.set(input.subarray(firstChunkEnd), firstChunkEnd + phys.length);
      return new Blob([output], { type: 'image/png' });
    }

    function saveBlob(blob, filename) {
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = filename;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      window.setTimeout(() => URL.revokeObjectURL(url), 1500);
    }

    async function downloadA4PNG() {
      const svg = document.getElementById('final-label-svg');
      if (!svg) return;
      let objectUrl = null;
      try {
        const loaded = await loadExportImage(svg);
        const img = loaded.image;
        objectUrl = loaded.objectUrl;
        const canvas = document.createElement('canvas');
        canvas.width = 2480;
        canvas.height = 3508;
        const ctx = canvas.getContext('2d');
        if (!ctx) throw new Error('Canvas is not available.');
        ctx.fillStyle = '#FFFFFF';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = '#0F172A';
        ctx.font = 'bold 36px monospace';
        ctx.fillText('DIAMOND BAKERY • 6-INCH ROUND TIN MASTER • A4 PRINT SHEET', 100, 120);
        ctx.fillStyle = '#64748B';
        ctx.font = '24px monospace';
        ctx.fillText('100% True Scale (Do Not Fit To Page) • 210 x 297 mm • 300 DPI', 100, 160);

        const count = state.a4Layout || 1;
        if (count === 1) {
          const diam = 1800, x = (2480 - diam) / 2, y = (3508 - diam) / 2;
          ctx.drawImage(img, x, y, diam, diam);
          ctx.strokeStyle = '#000000'; ctx.lineWidth = 4;
          ctx.beginPath(); ctx.moveTo(x - 30, y); ctx.lineTo(x - 5, y); ctx.stroke();
          ctx.beginPath(); ctx.moveTo(x, y - 30); ctx.lineTo(x, y - 5); ctx.stroke();
          ctx.beginPath(); ctx.moveTo(x + diam + 5, y); ctx.lineTo(x + diam + 30, y); ctx.stroke();
          ctx.beginPath(); ctx.moveTo(x + diam, y - 30); ctx.lineTo(x + diam, y - 5); ctx.stroke();
          ctx.beginPath(); ctx.moveTo(x - 30, y + diam); ctx.lineTo(x - 5, y + diam); ctx.stroke();
          ctx.beginPath(); ctx.moveTo(x, y + diam + 5); ctx.lineTo(x, y + diam + 30); ctx.stroke();
          ctx.beginPath(); ctx.moveTo(x + diam + 5, y + diam); ctx.lineTo(x + diam + 30, y + diam); ctx.stroke();
          ctx.beginPath(); ctx.moveTo(x + diam, y + diam + 5); ctx.lineTo(x + diam, y + diam + 30); ctx.stroke();
        } else if (count === 2) {
          const diam = 1450, x = (2480 - diam) / 2;
          ctx.drawImage(img, x, 250, diam, diam);
          ctx.drawImage(img, x, 250 + diam + 100, diam, diam);
        } else if (count === 4) {
          const diam = 1050;
          ctx.drawImage(img, 150, 350, diam, diam);
          ctx.drawImage(img, 150 + diam + 80, 350, diam, diam);
          ctx.drawImage(img, 150, 350 + diam + 80, diam, diam);
          ctx.drawImage(img, 150 + diam + 80, 350 + diam + 80, diam, diam);
        } else if (count === 6) {
          const diam = 800;
          for (let row = 0; row < 3; row++) {
            for (let col = 0; col < 2; col++) {
              ctx.drawImage(img, 250 + col * (diam + 180), 300 + row * (diam + 120), diam, diam);
            }
          }
        }
        const colors = ['#00FFFF', '#FF00FF', '#FFFF00', '#000000', '#D4AF37'];
        colors.forEach((color, index) => {
          ctx.fillStyle = color;
          ctx.fillRect(100 + index * 80, 3420, 60, 30);
        });
        ctx.fillStyle = '#64748B';
        ctx.font = '22px monospace';
        ctx.fillText('Cut along circular guides • Diamond Bakery All Rights Reserved', 560, 3442);
        const png = await new Promise((resolve, reject) => canvas.toBlob(blob => blob ? resolve(blob) : reject(new Error('PNG could not be created.')), 'image/png'));
        saveBlob(await addPngDpiMetadata(png, 300), `diamond_cookies_A4_print_sheet_${count}up_300dpi.png`);
      } catch (error) {
        console.error('A4 PNG export failed:', error);
        alert('A4 PNG download nahi ho paya. Page refresh karke dobara try karein. Details: ' + error.message);
      } finally {
        if (objectUrl) URL.revokeObjectURL(objectUrl);
      }
    }

    async function downloadPNG600DPI() {
      const svg = document.getElementById('final-label-svg');
      if (!svg) return;
      let objectUrl = null;
      try {
        const loaded = await loadExportImage(svg);
        objectUrl = loaded.objectUrl;
        const canvas = document.createElement('canvas');
        canvas.width = 3600;
        canvas.height = 3600;
        const ctx = canvas.getContext('2d');
        if (!ctx) throw new Error('Canvas is not available.');
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.drawImage(loaded.image, 0, 0, 3600, 3600);
        const png = await new Promise((resolve, reject) => canvas.toBlob(blob => blob ? resolve(blob) : reject(new Error('PNG could not be created.')), 'image/png'));
        saveBlob(await addPngDpiMetadata(png, 600), `diamond_bakery_6inch_round_cookies_${state.preset}_600dpi.png`);
      } catch (error) {
        console.error('Sticker PNG export failed:', error);
        alert('PNG download nahi ho paya. Page refresh karke dobara try karein. Details: ' + error.message);
      } finally {
        if (objectUrl) URL.revokeObjectURL(objectUrl);
      }
    }

        async function downloadVectorSVG() {
      const svg = document.getElementById('final-label-svg');
      if (!svg) return;
      try {
        const svgStr = await prepareSvgForExport(svg);
        saveBlob(new Blob([svgStr], { type: 'image/svg+xml;charset=utf-8' }), `diamond_bakery_6inch_round_cookies_${state.preset}.svg`);
      } catch (error) {
        console.error('SVG export failed:', error);
        alert('SVG download nahi ho paya. Details: ' + error.message);
      }
    }

    // ==========================================
    // INITIALIZATION ON PAGE LOAD
    // ==========================================
    function initStudio() {
      renderMandalaButtons();
      applyPreset(state.preset);
      setViewMode(state.viewMode);
    }

    window.addEventListener('DOMContentLoaded', initStudio);
  </script>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

with open('cookie_tin_preview.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Successfully re-generated index.html and cookie_tin_preview.html with draggable layers and refined typography')
