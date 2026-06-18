<div align="center">

# 📸 SnapPDF

**Zero-dependency photo-to-PDF converter — right in your browser.**

Convert photos into printable A4 PDFs with waterfall grid layout, drag-and-drop sorting, per-photo rotation, and live preview.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-blueviolet?style=for-the-badge&logo=github)](https://jefryprr.github.io/snappdf/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![HTML5](https://img.shields.io/badge/Built%20with-HTML5-orange?style=for-the-badge&logo=html5)](index.html)
[![No Dependencies](https://img.shields.io/badge/Dependencies-None-success?style=for-the-badge)](#zero-dependencies)

---

**[🌐 Try it Live](https://jefryprr.github.io/snappdf/)** · No install · No login · Works on phone, tablet & desktop

</div>

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🖼️ **Waterfall Grid** | Multi-column layout (1–10 columns) with automatic pagination |
| 📐 **A4 Portrait & Landscape** | Switch orientation with auto column adjustment |
| 🔀 **Drag & Drop** | Reorder photos via SortableJS (CDN, zero install) |
| ↻ **Per-Photo Rotation** | CW/CCW 90° with canvas transform, persisted per photo |
| 🔍 **Zoom Slider** | Adjust preview width from 50–200mm |
| 📑 **Page Navigator** | Sidebar with clickable page groups |
| 👀 **Live Preview** | Real-time A4 preview as you configure |
| 📋 **Per-Page Columns** | Different column count per page |
| ↔️ **Photo Transfer** | Move photos between pages via sidebar drag |
| 📄 **Custom Filename** | Name your downloaded PDF |
| 🎚️ **JPEG Quality** | Adjustable quality (50–100) |
| 📱 **Mobile Responsive** | Works on phone, tablet, and desktop |
| 🔄 **Auto EXIF Rotation** | Photos auto-rotated based on EXIF orientation |
| 🚫 **Zero Dependencies** | No install, no build step, no backend |

---

## 🚀 Quick Start

```bash
git clone https://github.com/jefryprr/snappdf.git
cd snappdf
start index.html    # Windows
open index.html     # macOS
xdg-open index.html # Linux
```

Or just **double-click `index.html`** in your file explorer.

---

## 📖 How to Use

1. **Open** `index.html` in any modern browser
2. **Upload** photos — drag & drop, file picker, or paste from clipboard
3. **Arrange** — drag to reorder, rotate, adjust zoom
4. **Configure** — orientation, columns, quality, filename
5. **Preview** — check the live A4 preview with page navigator
6. **Download** — click "Generate PDF" and save

---

## 🏗️ Architecture

```
snappdf/
├── index.html              # Complete web app (HTML + CSS + JS)
├── .github/
│   └── workflows/
│       └── ci.yml          # CI pipeline
├── .gitignore
├── CHANGELOG.md
├── LICENSE                 # MIT
└── README.md
```

**Single-file architecture** — the entire app lives in `index.html` for maximum portability. No build tools, no bundlers, no node_modules.

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| PDF Generation | [jsPDF](https://github.com/parallax/jsPDF) (CDN) |
| Drag & Drop | [SortableJS](https://github.com/SortableJS/Sortable) (CDN) |
| EXIF Parsing | [exifr](https://github.com/MikeKovarik/exifr) (CDN) |
| Icons | [Lucide](https://lucide.dev/) (CDN) |
| UI | Vanilla HTML + CSS + JavaScript |
| Fonts | [Inter](https://rsms.me/inter/) (Google Fonts) |

---

## 🌐 Deployment

Deployed via **GitHub Pages** from branch `main`. Every push auto-redeploys.

To enable on your fork:

1. Go to **Settings → Pages**
2. Source: **Deploy from a branch**
3. Branch: `main`, folder: `/ (root)`
4. Save → live at `https://<username>.github.io/snappdf/`

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.

---

<div align="center">

**Built by [Jefry Pratama](https://github.com/jefryprr)**

</div>
