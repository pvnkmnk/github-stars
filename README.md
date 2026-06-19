# ⭐ github-stars

> A curated, annotated guide to [pvnkmnk](https://github.com/pvnkmnk)'s 1,033 GitHub stars — 18 categories, 1,014 curated tools, 6 deep-dives. Auto-updated weekly.

**Live wiki:** → [pvnkmnk.github.io/github-stars](https://pvnkmnk.github.io/github-stars/)

[![Deploy](https://github.com/pvnkmnk/github-stars/actions/workflows/deploy-gh-pages.yml/badge.svg)](https://github.com/pvnkmnk/github-stars/actions/workflows/deploy-gh-pages.yml)
[![Weekly Refresh](https://github.com/pvnkmnk/github-stars/actions/workflows/update-stars.yml/badge.svg)](https://github.com/pvnkmnk/github-stars/actions/workflows/update-stars.yml)

---

## 📂 File Guide

| File | Purpose | Format |
|------|---------|--------|
| **[STAR-GUIDE.md](stars/STAR-GUIDE.md)** | Master reference — all 18 categories with descriptions, cross-references, TOC, Part II Top 10 picks, Part III deep-dives | Markdown tables |
| **[AGENT-GUIDE.md](stars/AGENT-GUIDE.md)** | Token-efficient format for AI agent consumption | Pipe-delimited `EMOJI\|STARS\|FULL_NAME\|LANG\|DESC` |
| **[CHEATSHEET.md](stars/CHEATSHEET.md)** | Compact one-liners — terminal-friendly, fits on screen | Fixed-width aligned |
| **[TOOLBOX.md](stars/TOOLBOX.md)** | Top 10 picks per category with "why I starred" reasoning | Narrative markdown |
| **[DEEP-DIVE.md](stars/DEEP-DIVE.md)** | Specialized topic analysis (proxy, monitoring, backup, secrets, CI/CD, security) | Markdown tables |
| **[GAP-ANALYSIS.md](stars/GAP-ANALYSIS.md)** | Category coverage audit — what's missing from my stars | Narrative markdown |
| **[NOT-CURATED.md](stars/NOT-CURATED.md)** | Inbox for new un-categorized stars — reviewed and curated weekly | Simple link list |
| **[gh-stars-pvnkmnk.csv](stars/gh-stars-pvnkmnk.csv)** | Raw CSV export of all 1,033 stars | CSV |
| **[gh-stars-pvnkmnk.txt](stars/gh-stars-pvnkmnk.txt)** | Formatted text export of all stars | Human-readable text |

---

## 📊 18 Categories

| Category | Tools | Highlights |
|----------|-------|------------|
| 📡 Homelab Infrastructure | 40 | coolify (57k), headscale (40k), homepage (30k) |
| 🤖 Agentic Dev Tools | 109 | opencode (175k), claude-code (133k), superpowers (232k) |
| 🎵 Self-Hosted Media | 131 | immich (103k), navidrome (21k), beets (15k) |
| 🐳 Docker & Container | 26 | lazydocker (51k), dozzle (13k), devpod (14k) |
| 🧠 AI / LLM Tools | 70 | llama.cpp (117k), LocalAI (46k), qdrant (32k) |
| 🗄️ Databases & Storage | 24 | supabase (104k), nocodb (63k), dbeaver (50k) |
| 🔒 Security & Auth | 18 | ghidra (69k), gitleaks (27k), tailscale (32k) |
| ⚡ Automation & Workflows | 24 | n8n (193k), OpenBB (69k), maybe (54k) |
| 💻 Dev Tools & Languages | 44 | freeCodeCamp (419k), build-your-own-x (360k), bun (93k) |
| ⌨️ Terminal, CLI & Shell | 63 | fzf (69k), alacritty (58k), yazi (39k), zellij (33k) |
| 📝 Knowledge & PKM | 81 | joplin (55k), AFFiNE (47k), obsidian ecosystem |
| 🌐 Web & Frontend | 70 | tailwindcss (87k), playwright (77k), hoppscotch (68k) |
| 💬 Chat & Messaging | 14 | python-telegram-bot (29k), signal-cli, mattermost |
| 📄 Docs & Blog | 7 | mkdocs-material (26k), hugo (80k), astro (55k) |
| 📱 Mobile | 38 | ReVanced (28k), Seal (26k), KernelSU (16k) |
| 🪟 Windows | 30 | ExplorerPatcher (32k), Seelen-UI (17k), EverythingToolbar (14k) |
| 📦 Low Signal | 170 | Weak category matches — low-confidence placements, scored < 4 |
| ❓ Unique & Niche | 57 | No keyword match — one-of-a-kind repos, manually reviewed |

---

## 🛠️ Pipeline: How It Works

### Weekly workflow

```bash
# 1. Fetch latest stars into SQLite (~/.cache/gh-stars/stars.db)
gh-stars fetch pvnkmnk

# 2. Run the full curation pipeline
python3 scripts/update_stars.py

# 3. Commit & push updated guides
git add stars/ && git commit -m "chore: weekly star refresh" && git push
```

### What the pipeline does

1. **Fetches** latest stars via [`gh-stars`](https://github.com/prabirshrestha/gh-stars) into a local SQLite database
2. **Detects** new repos not yet in STAR-GUIDE.md or NOT-CURATED.md
3. **Auto-categorizes** using keyword scoring against 16 curated categories (optional: `--auto-curate N`)
4. **Appends** remaining uncategorized repos to NOT-CURATED.md with category suggestions
5. **Regenerates** AGENT-GUIDE.md and CHEATSHEET.md from STAR-GUIDE.md sections
6. **Exports** raw CSV and TXT snapshots

### Key flags

| Flag | Purpose |
|------|---------|
| `--no-fetch` | Skip `gh-stars fetch` (use cached DB) |
| `--fetch-only` | Only fetch, no regeneration |
| `--suggest-only` | Only generate categorization suggestions, no file changes |
| `--auto-curate N` | Auto-insert repos scoring ≥ N with clear category match into STAR-GUIDE (default: 8) |

### CI/CD

Two GitHub Actions workflows power the repo:
- **[update-stars.yml](.github/workflows/update-stars.yml)** — fetches stars, regenerates guides, and pushes to `main` on a weekly schedule
- **[deploy-gh-pages.yml](.github/workflows/deploy-gh-pages.yml)** — deploys `index.html` + `stars/` to `gh-pages` on every push to `main`

---

## 🔍 Quick Search

```bash
# Find repos by keyword
grep -i "postgres" stars/STAR-GUIDE.md stars/CHEATSHEET.md

# Find by category (emoji)
grep "^📡" stars/AGENT-GUIDE.md      # Homelab
grep "^🤖" stars/AGENT-GUIDE.md      # Agentic Dev
grep "^🎵" stars/AGENT-GUIDE.md      # Media
grep "^🧠" stars/AGENT-GUIDE.md      # AI/LLM

# High-star repos only (>10k)
awk -F'|' '$2>10000' stars/AGENT-GUIDE.md

# Count per category
grep -c "^📡" stars/AGENT-GUIDE.md
```

---

## 📖 Deep Dives (STAR-GUIDE Part III)

- 🔀 **Reverse Proxy** — Traefik, Pangolin, SWAG, Wiregate
- 📊 **Monitoring & Observability** — netdata, SigNoz, dozzle, changedetection.io
- 💾 **Backup & Restore** — parsync, msgvault, Olares
- 🔐 **Secrets Management** — gitleaks, Infisical, lockenv
- 🚀 **CI/CD & Automation** — act, terraform, ansible, dokku
- 🛡️ **Security Suite** — VPN, auth, agent security, Ghidra

---

*1,033 stars · 1,014 curated · 18 categories · auto-updated weekly*
