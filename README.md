<div align="center">

# 📸 SnapPDF

A lightweight, **frontend-only** photo-to-PDF converter with waterfall layout, drag-and-drop sorting, and EXIF-aware rotation — no server, no Python, no install. Just open `index.html`.

[![CI](https://github.com/jefryprr/snappdf/actions/workflows/ci.yml/badge.svg)](https://github.com/jefryprr/snappdf/actions)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![HTML5](https://img.shields.io/badge/HTML5-frontend%20only-orange.svg)](index.html)

</div>

---

## ✨ Features

- 🖼️ **Waterfall Layout** — Multi-column photo grid (1–10 columns), not just stacked vertically
- 📐 **A4 Portrait & Landscape** — Automatic column adjustment when switching orientation
- 🔀 **Drag & Drop Sort** — Reorder photos by dragging (SortableJS)
- 🔄 **EXIF-Aware Rotation** — Auto-rotate based on EXIF data, plus manual CW/CCW buttons
- 🏷️ **Custom Captions** — Add/edit captions below each photo in the PDF
- 🎚️ **JPEG Quality Control** — Adjustable quality (10–100) to balance clarity vs file size
- 📄 **Multi-Page Support** — Automatically paginates when photos exceed one page
- 📋 **Clipboard Paste** — Paste images directly from clipboard
- 🗑️ **Per-Photo Management** — Delete/restore individual photos without re-uploading
- 👀 **Gallery Preview** — See waterfall layout before generating PDF
- 🌙 **Dark/Light Theme** — Responsive design with theme toggle
- 🚀 **Zero Dependencies** — Runs entirely in the browser, no server needed

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/jefryprr/snappdf.git
cd snappdf

# Open in browser (that's it!)
start index.html          # Windows
open index.html           # macOS
xdg-open index.html       # Linux
```

Or just **[open directly in your browser](index.html)** — no install required.

## 🌐 Deploy

### GitHub Pages

1. Go to repo **Settings** → **Pages**
2. Source: `Deploy from a branch` → `main` → `/ (root)`
3. Your site will be live at `https://jefryprr.github.io/snappdf/`

### Netlify / Vercel

Just drag & drop the `index.html` file — no build step needed.

## 💡 Usage

1. **Upload** — Drag & drop or browse for JPG/JPEG/PNG files
2. **Sort** — Drag to reorder, or use sort buttons (A→Z, Z→A, EXIF date)
3. **Configure** — Set orientation, columns, JPEG quality, and captions
4. **Preview** — Check the gallery preview to see waterfall layout
5. **Generate** — Click "Generate PDF" and download

## 🧪 Running Tests (Python Package)

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install in editable mode
pip install -e ".[dev]"

# Run tests
pytest tests/ -v
```

## 📁 Project Structure

```
snappdf/
├── index.html              # Main web app (1779 lines, frontend-only)
├── src/snappdf/            # Python package scaffold
│   ├── __init__.py
│   └── core.py
├── tests/                  # Unit tests (pytest)
│   ├── __init__.py
│   └── test_core.py
├── docs/
│   └── index.md            # Documentation
├── .github/workflows/
│   └── ci.yml              # GitHub Actions CI
├── .gitignore
├── LICENSE                 # MIT License
├── README.md               # This file
├── CHANGELOG.md            # Version history
├── pyproject.toml          # Build config (Hatchling)
└── requirements.txt        # Dev dependencies
```

## 🛠️ Tech Stack (Frontend)

| Technology | Purpose |
|------------|---------|
| **HTML5 / CSS3 / JS** | Core app (zero framework) |
| **SortableJS** | Drag & drop photo reordering |
| **jsPDF** | Client-side PDF generation |
| **exifr** | EXIF metadata extraction (rotation, date) |
| **Lucide** | Icon set |
| **Inter** | Typography (Google Fonts) |

## 📝 License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.

## 👤 Author

**Jefry Pratama** — [@jefryprr](https://github.com/jefryprr)
