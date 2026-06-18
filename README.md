<div align="center">

# 📸 SnapPDF

A zero-dependency, feature-rich HTML+JS web app that converts photos into a printable **A4 PDF** with waterfall grid layout, drag-and-drop sorting, per-photo rotation, zoom, page navigator, live preview, and drag-to-reorder page groups.

[![CI](https://github.com/jefryprr/snappdf/actions/workflows/ci.yml/badge.svg)](https://github.com/jefryprr/snappdf/actions)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![HTML5](https://img.shields.io/badge/HTML5-zero--dependency-orange.svg)](index.html)
[![GitHub Pages](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-blueviolet.svg)](https://jefryprr.github.io/snappdf/)

</div>

> **🌐 Live Demo: [https://jefryprr.github.io/snappdf/](https://jefryprr.github.io/snappdf/)**
>
> Langsung bisa dipakai — tanpa install, tanpa login. Buka di HP, tablet, atau desktop.

---

## 🌐 Live Demo

Buka langsung di browser: **[https://jefryprr.github.io/snappdf/](https://jefryprr.github.io/snappdf/)**

Deployed via **GitHub Pages** dari branch `main`. Update otomatis setiap push.

---

## ✨ Features

- 🖼️ **Waterfall Grid Layout** — Photos arranged in multi-column waterfall (1–10 columns), not just stacked
- 📐 **A4 Portrait & Landscape** — Automatic column adjustment when switching orientation
- 🔀 **Drag & Drop Reordering** — Sort photos via SortableJS (CDN, zero install)
- ↻ **Per-Photo Rotation** — CW/CCW 90° rotation with canvas transform, persisted per photo
- 🔍 **Zoom Slider** — Adjust preview width from 50–200mm for high-res or long-exposure photos
- 📑 **Page Navigator** — Sidebar with clickable page groups; click page to jump, click photo to focus
- 👀 **Live A4 Preview** — Real-time paginated preview as you configure
- 🔄 **Page Group Reordering** — Drag page groups in sidebar to reorder entire pages
- 📋 **Per-Page Column Override** — Different column count per page
- ↔️ **Photo Transfer** — Move photos between pages via drag in sidebar
- 📏 **Subtle Grid Lines** — Dashed, muted grid in preview (hidden by default)
- 📄 **Custom Filename** — Name your downloaded PDF
- 🎚️ **JPEG Quality Control** — Adjustable quality (50–100)
- 📱 **Mobile Responsive** — Works on phone, tablet, and desktop
- 🔄 **Auto EXIF Rotation** — Photos auto-rotated based on EXIF orientation tag
- 🚫 **Zero Dependencies** — No install, no build step, no backend. Just open `index.html`

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/jefryprr/snappdf.git
cd snappdf

# Open directly in browser (no install needed!)
open index.html        # macOS
xdg-open index.html    # Linux
start index.html       # Windows
```

Or just **double-click `index.html`** in your file explorer.

## 💡 How to Use

1. **Open** `index.html` in any modern browser
2. **Upload** photos (drag & drop or file picker)
3. **Arrange** — drag to reorder, use rotation buttons, adjust zoom
4. **Configure** — set orientation, columns, quality, filename
5. **Preview** — check the live A4 preview with page navigator
6. **Download** — click "Generate PDF" and download

## 🧪 Running Tests

```bash
# Install dev dependencies (optional — for testing the Python scaffold)
pip install -e ".[dev]"
pytest tests/ -v
```

## 📁 Project Structure

```
snappdf/
├── index.html              # Main web app (HTML+JS+CSS, 1877 lines)
├── src/snappdf/            # Python package scaffold
│   ├── __init__.py
│   └── core.py
├── tests/                  # Unit tests (pytest)
│   ├── __init__.py
│   └── test_core.py
├── docs/                   # Documentation
│   └── index.md
├── .github/workflows/      # CI/CD pipelines
│   └── ci.yml
├── .gitignore
├── LICENSE                 # MIT License
├── README.md               # This file
├── CHANGELOG.md            # Version history
├── pyproject.toml          # Build config (Hatchling)
└── requirements.txt        # Runtime dependencies
```

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| PDF Generation | jsPDF (CDN) |
| Drag & Drop | SortableJS (CDN) |
| EXIF Parsing | EXIF.js (CDN) |
| UI | Vanilla HTML + CSS + JavaScript |
| Build | None required |
| Backend | None required |

## 🌐 Deployment — GitHub Pages

App ini bisa diakses publik via **GitHub Pages** tanpa biaya, tanpa backend.

### Cara Mengaktifkan:

1. Buka repo → **Settings** → **Pages**
2. **Source**: Deploy from a branch
3. **Branch**: `main`, folder `/ (root)`
4. Klik **Save**
5. Tunggu ~1 menit → live di `https://jefryprr.github.io/snappdf/`

### Update Otomatis:

Setiap push ke branch `main`, GitHub Pages akan otomatis rebuild. Tidak perlu deploy manual.

---

## 📝 License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.

## 👤 Author

**Jefry Pratama** — [@jefryprr](https://github.com/jefryprr)
