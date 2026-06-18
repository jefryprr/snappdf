# Changelog

All notable changes to this project will be documented in this file.
Format: [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)

---

## [0.2.0] — 2026-06-20

### Changed
- **README overhaul** — professional English documentation with feature table, architecture section, and contributing guidelines
- **CI pipeline** — replaced minimal check with HTML structure validation, duplicate tag detection, and Markdown linting

### Fixed
- Duplicate `</style>` tag in `index.html`

### Removed
- Misleading Python scaffold (`src/`, `tests/`, `pyproject.toml`) — the app is 100% frontend, these files gave false impression of a Python package
- Redundant `docs/index.md` — was a minimal copy of README

### Added
- GitHub issue templates (bug report, feature request)
- Pull request template
- Contributing section in README

---

## [0.1.0] — 2026-06-20

### Added
- Zero-dependency HTML+JS+CSS web app (no install, no build step)
- A4 PDF generation with waterfall grid layout (1–10 columns)
- Portrait and Landscape orientation
- Drag-and-drop photo reordering via SortableJS
- Per-photo rotation (CW/CCW 90 degrees) with canvas transform
- Zoom slider (50-200mm preview width) for high-res/long-exposure photos
- Page Navigator sidebar (click page to jump, click photo to focus)
- Live A4 preview with multi-page pagination
- Page group reordering (drag page groups in sidebar)
- Per-page column override (different column count per page)
- Photo transfer between pages via drag in sidebar
- Subtle grid lines in preview (dashed, muted)
- Show-on-demand page breaks (hidden by default)
- Custom filename for downloaded PDF
- JPEG quality control (50-100)
- Auto EXIF rotation via orientation tag
- Mobile-responsive layout
- MIT License
- CI/CD workflow with GitHub Actions
