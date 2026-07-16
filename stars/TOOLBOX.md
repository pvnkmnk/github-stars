# 🧰 Personal Toolbox

> Top 10 picks from each category of my GitHub stars — what I'd actually use and why.
> [pvnkmnk](https://github.com/pvnkmnk) · 2026-06-19

---

## 📡 Homelab Infrastructure — Top 10

### 1. [khuedoan/homelab](https://github.com/khuedoan/homelab) ⭐9,344
**Why I starred this:** The holy grail of homelab automation. One command takes you from bare metal to a fully running stack — DNS, VPN, monitoring, media, the works. It's a learning goldmine even if you don't run it verbatim, because every Ansible playbook and Terraform module is documented and reusable. If I were starting from scratch tomorrow, this is where I'd begin.

### 2. [coollabsio/coolify](https://github.com/coollabsio/coolify) ⭐57,133
**Why I starred this:** Vercel/Heroku/Netlify, but self-hosted. One-click deploys for anything with a Dockerfile — Next.js, Node, Python, databases, you name it. It's the PaaS that makes self-hosting feel like a managed service. Paired with a $20 VPS, this replaces $200/mo in cloud bills.

### 3. [gethomepage/homepage](https://github.com/gethomepage/homepage) ⭐30,704
**Why I starred this:** The dashboard every homelab needs. It auto-discovers your Docker containers via labels, shows live status, integrates with dozens of service APIs (Plex, Sonarr, Pi-hole, etc.), and looks gorgeous doing it. It's the first thing I open every morning to check my lab's pulse.

### 4. [juanfont/headscale](https://github.com/juanfont/headscale) ⭐40,154
**Why I starred this:** Tailscale without the Tailscale servers. Full WireGuard mesh networking that I control end-to-end. Every device in my homelab joins the same private tailnet — my laptop, my servers, my phone. No open ports, no Cloudflare tunnels needed for internal access. It's the networking backbone that makes everything else work securely.

### 5. [glanceapp/glance](https://github.com/glanceapp/glance) ⭐35,221
**Why I starred this:** A single page that aggregates all my feeds — RSS, Reddit, YouTube, Hacker News, weather, stocks, Docker status. It's my information radiator. Minimal, fast, and self-hosted. I use it as my browser's new tab page.

### 6. [ChristianLempa/boilerplates](https://github.com/ChristianLempa/boilerplates) ⭐7,819
**Why I starred this:** A library of production-ready Docker Compose templates for common self-hosted apps — all configured with security best practices, proper networking, and sane defaults. Every time I want to spin up a new service, I check here first to avoid reinventing the wheel.

### 7. [azukaar/Cosmos-Server](https://github.com/azukaar/Cosmos-Server) ⭐5,973
**Why I starred this:** A full home server OS in a single binary. Built-in reverse proxy with auto-SSL, authentication, anti-DDOS, and a marketplace to install apps. It's the "I want it all and I want it secure" option. Great for setting up a server for non-technical family members.

### 8. [IAmStoxe/wirehole](https://github.com/IAmStoxe/wirehole) ⭐4,959
**Why I starred this:** WireGuard + Pi-hole + Unbound in one docker-compose. One `docker compose up` and I have a VPN that blocks ads and malware across every device. I run this on a $5 VPS and it's been rock-solid for years.

### 9. [octelium/octelium](https://github.com/octelium/octelium) ⭐3,892
**Why I starred this:** The Swiss Army knife of secure access — VPN, ZTNA, API gateway, MCP gateway, ngrok alternative, all in one Go binary. It's the most ambitious self-hosted networking project I've seen. If it delivers on half its promises, it replaces 5 separate tools.

### 10. [linkwarden/linkwarden](https://github.com/linkwarden/linkwarden) ⭐18,653
**Why I starred this:** Self-hosted bookmark manager that actually preserves pages — full-text snapshots, screenshots, PDFs. My "read later" list doesn't rot anymore. It's also collaborative, so my whole household can share and organize links. Think Pocket, but I own the data.

---

## 🤖 Agentic Dev Tools — Top 10

### 1. [anomalyco/opencode](https://github.com/anomalyco/opencode) ⭐175,985
**Why I starred this:** The open-source coding agent that I actually use daily. It runs in my terminal, understands my entire codebase, and produces real, working code. It's not a toy — it's a force multiplier. The plugin ecosystem and community are incredible. This is the agent I'd recommend to anyone starting out.

### 2. [anthropics/claude-code](https://github.com/anthropics/claude-code) ⭐133,185
**Why I starred this:** The original coding agent that proved the paradigm. Claude Code showed the world that an agent can understand a million-line codebase and make surgical edits. I star it because it defined the category, and I still reach for it for hard architectural problems.

### 3. [mem0ai/mem0](https://github.com/mem0ai/mem0) ⭐58,853
**Why I starred this:** Universal memory for agents. The missing piece in every agent workflow — persistent, searchable memory that survives sessions. Instead of repeating context every conversation, my agents remember preferences, past decisions, and project state. It's the difference between a smart assistant and a colleague.

### 4. [bytedance/deer-flow](https://github.com/bytedance/deer-flow) ⭐71,473
**Why I starred this:** The long-horizon agent harness. While most coding agents handle a single task, deer-flow manages multi-hour research → code → deploy pipelines with sandboxes, subagents, and memory. It's the closest thing to an autonomous software engineer I've seen. The message gateway pattern is worth studying alone.

### 5. [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) ⭐43,923
**Why I starred this:** Gives my coding agents eyes in the browser. DevTools-level access to any webpage — inspect DOM, monitor network, check console errors, take screenshots, run performance audits. Essential for agents that build or debug web apps. This + OpenCode = a full-stack agent that actually sees what it's doing.

### 6. [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) ⭐51,516
**Why I starred this:** Pre-indexed code knowledge graph that reduces agent token usage by 10x. Instead of reading every file, the agent queries a graph that already knows the code structure. It syncs on file changes automatically and works with every major agent. This is the kind of infrastructure all agents will need.

### 7. [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) ⭐83,103
**Why I starred this:** Session-to-session memory that actually works. It captures everything the agent does, compresses it with AI, and injects relevant context into future sessions. Unlike raw context dumps, it figures out what's relevant. Works across Claude Code, OpenCode, Codex, Gemini, and more.

### 8. [ComposioHQ/composio](https://github.com/ComposioHQ/composio) ⭐28,829
**Why I starred this:** 1,000+ pre-built tool integrations for agents — Gmail, Slack, GitHub, Jira, databases, APIs — with managed auth. Instead of building custom integrations for every tool my agent needs, I connect through Composio. It handles OAuth, rate limiting, and sandboxed execution.

### 9. [aaif-goose/goose](https://github.com/aaif-goose/goose) ⭐49,755
**Why I starred this:** The agent that goes beyond coding. Goose installs packages, runs tests, edits files, and executes commands — it's a full development lifecycle agent written in Rust. I star it for its philosophy: an agent shouldn't just suggest code, it should be able to fully execute.

### 10. [obra/superpowers](https://github.com/obra/superpowers) ⭐232,087
**Why I starred this:** The skills framework that showed agents can be more than prompt engineering. Superpowers treats agent capabilities as composable, reusable building blocks with clear interfaces. It's the Unix philosophy applied to AI: small, focused tools that compose into powerful workflows. My most-starred repo for good reason.

---

## 🎵 Self-Hosted Media — Top 10

### 1. [immich-app/immich](https://github.com/immich-app/immich) ⭐103,674
**Why I starred this:** Google Photos, but I own every byte. Auto-backup from my phone, face recognition, geolocation, shared albums, search — all self-hosted. The development velocity is staggering (releases every few weeks), and the mobile app is genuinely polished. This is the killer app that justifies owning a server.

### 2. [navidrome/navidrome](https://github.com/navidrome/navidrome) ⭐21,790
**Why I starred this:** My personal Spotify. It streams my FLAC collection to any device, is Subsonic-compatible (works with dozens of clients), and the web UI is clean and fast. I've been running it for years and it's never crashed, never corrupted my library, and never complained. The true definition of boring technology done right.

### 3. [beetbox/beets](https://github.com/beetbox/beets) ⭐15,285
**Why I starred this:** The ultimate music librarian. It auto-tags and organizes my entire music collection using MusicBrainz, Discogs, and Beatport. The plugin system is incredible — fetch lyrics, calculate BPM, find duplicate tracks, generate playlists based on acoustic similarity. Without beets, my 50k-track library would be chaos.

### 4. [jeffvli/feishin](https://github.com/jeffvli/feishin) ⭐8,814
**Why I starred this:** The modern, beautiful desktop client that Jellyfin and Navidrome deserve. It looks like a premium streaming app — album art, artist bios, playlist management, gapless playback — but it connects to my self-hosted servers. If you want your self-hosted music to *feel* premium, this is the client.

### 5. [LumePart/Explo](https://github.com/LumePart/Explo) ⭐1,636
**Why I starred this:** Spotify's "Discover Weekly" algorithm, but for my self-hosted music. It analyzes listening history and finds tracks I haven't heard but will probably love. The magic of music discovery without sending data to anyone else. This is the feature that made me stop missing Spotify.

### 6. [metabrainz/picard](https://github.com/metabrainz/picard) ⭐4,954
**Why I starred this:** The gold standard for music tagging. When beets can't figure out a track, Picard can — it uses acoustic fingerprinting (AcoustID) to identify songs even with completely missing metadata. It's saved me countless hours of manual tagging.

### 7. [LizardByte/Sunshine](https://github.com/LizardByte/Sunshine) ⭐38,401
**Why I starred this:** Self-hosted game streaming that actually works at low latency. Pair it with Moonlight on any client device and I can play my gaming PC from my laptop, tablet, or TV. It's the backbone of my home gaming setup — no cloud service needed.

### 8. [geekau/mediastack](https://github.com/geekau/mediastack) ⭐1,782
**Why I starred this:** Pre-configured Docker Compose for the entire *arr stack with security built in — VPN-bound traffic, MFA on remote access, proper network segmentation. It's the template I used to stand up my media server in an afternoon instead of a weekend.

### 9. [KRTirtho/spotube](https://github.com/KRTirtho/spotube) ⭐47,028
**Why I starred this:** A cross-platform music app that uses YouTube Music as its backend — open source, no account needed, works on desktop and mobile. It's the music player I recommend to friends who want to ditch subscriptions but don't want to self-host a full server.

### 10. [clangen/musikcube](https://github.com/clangen/musikcube) ⭐4,784
**Why I starred this:** A terminal-based music player that doubles as a streaming server. It's blazing fast (C++), has a gorgeous ncurses interface, and indexes even my largest libraries in seconds. When I'm SSH'd into my server and want to cue up music, this is what I use. Terminal aesthetics + real functionality.

---

## 🐳 Docker & Container Management — Top 10

### 1. [jesseduffield/lazydocker](https://github.com/jesseduffield/lazydocker) ⭐51,380
**Why I starred this:** The single best Docker TUI ever made. Full control over containers, images, volumes, networks — view logs, restart services, exec into containers, all with vim-keybindings and a beautiful terminal UI. It's the first tool I install on any server. Lazygit + lazydocker = my entire terminal workflow.

### 2. [amir20/dozzle](https://github.com/amir20/dozzle) ⭐13,314
**Why I starred this:** Real-time log viewer for Docker containers with fuzzy search, auto-scroll, and multi-host support. Instead of `docker logs -f` one container at a time, I see all my logs in one browser tab with filtering. It's so lightweight I forget it's running, and so useful I'd never go back.

### 3. [gethomepage/homepage](https://github.com/gethomepage/homepage) ⭐30,704
**Why I starred this:** (Yes, also in Homelab — it's that good.) Docker-native service dashboard. Add a few labels to your compose files and homepage auto-discovers every service, shows status indicators, and creates a beautiful launch page. It's the control center for my Docker fleet.

### 4. [ChrispyBacon-dev/DockFlare](https://github.com/ChrispyBacon-dev/DockFlare) ⭐2,191
**Why I starred this:** Automates Cloudflare Tunnel creation from Docker labels. Add `dockflare.tunnel: myapp` to a container label and it auto-creates a secure tunnel with Let's Encrypt. No more manual Cloudflare configuration. For anyone exposing services through Cloudflare, this is a massive time-saver.

### 5. [marvinvr/docktail](https://github.com/marvinvr/docktail) ⭐767
**Why I starred this:** Expose Docker containers as Tailscale services via labels. Combine Docker + Tailscale without touching Tailscale's config — just add a label and the container joins the tailnet. It's the cleanest integration between my two favorite networking tools.

### 6. [docker/docker-agent](https://github.com/docker/docker-agent) ⭐3,089
**Why I starred this:** Docker's own AI agent builder. It's the official Docker take on agent-native tooling — letting you build, run, and manage AI agents as Docker containers. I star it as a bet on where the industry is heading: agents as containerized workloads managed like any other service.

### 7. [loft-sh/devpod](https://github.com/loft-sh/devpod) ⭐14,972
**Why I starred this:** Codespaces, but open-source and provider-agnostic. Spin up dev environments on any cloud, Kubernetes cluster, or local Docker. It works with any IDE (VS Code, JetBrains, cursor, etc.). I use it for ephemeral dev environments — no more "works on my machine."

### 8. [getarcaneapp/arcane](https://github.com/getarcaneapp/arcane) ⭐5,787
**Why I starred this:** A modern, polished Docker management UI that doesn't feel like it was built in 2015. It's designed for "everyone" — not just ops people. I use it when I want a visual overview of my containers without opening Portainer's sometimes-overwhelming interface.

### 9. [clemcer/LoggiFly](https://github.com/clemcer/LoggiFly) ⭐1,741
**Why I starred this:** Alerting for Docker logs. It watches container logs for patterns (errors, warnings, custom regex) and sends notifications (Discord, Slack, Telegram). Instead of discovering a crashed service days later, I get a ping the moment something goes wrong. Simple, focused, effective.

### 10. [DockSTARTer/DockSTARTer](https://github.com/GhostWriters/DockSTARTer) ⭐2,560
**Why I starred this:** The "I want Docker apps running but don't want to think about it" tool. Interactive TUI that lets you pick from 100+ apps, then generates optimized docker-compose configs with proper networking, permissions, and update strategies. It's how I onboard friends to self-hosting.

---

## 🧠 AI / LLM Tools — Top 10

### 1. [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) ⭐117,150
**Why I starred this:** The engine that made local LLMs practical. Before llama.cpp, running a language model locally required a GPU and patience. Now I run Llama 3, Mistral, and Qwen on my laptop CPU. It's the foundation that everything else — Ollama, LocalAI, LM Studio — is built on. A genuine revolution in a C++ codebase.

### 2. [mudler/LocalAI](https://github.com/mudler/LocalAI) ⭐46,960
**Why I starred this:** The everything-in-one local AI engine. Drop-in OpenAI API replacement that runs LLMs, image generation, audio transcription, text-to-speech, embeddings — all locally, no GPU required. I use it as my personal AI backend for privacy-sensitive projects. It's the self-hoster's answer to the OpenAI API.

### 3. [qdrant/qdrant](https://github.com/qdrant/qdrant) ⭐32,438
**Why I starred this:** The vector database I trust for production workloads. Written in Rust, blisteringly fast, and the API is a joy to use. It powers semantic search, RAG pipelines, and recommendation systems in my projects. The filtering + vector search combination is unmatched.

### 4. [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) ⭐36,752
**Why I starred this:** RAG made simple and actually fast. LightRAG doesn't try to be everything — it does retrieval-augmented generation with a focus on speed and simplicity. Graphs + vectors working together. For projects where I need "search my documents" without a PhD in information retrieval, this is it.

### 5. [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) ⭐10,763
**Why I starred this:** A single OpenAI-compatible endpoint that stacks the free tiers of 16 different LLM providers. Smart routing, automatic failover, ~1.7 billion tokens/month for free. It's my fallback for when I don't want to pay for API calls during development and experimentation.

### 6. [yamadashy/repomix](https://github.com/yamadashy/repomix) ⭐26,381
**Why I starred this:** Packs an entire repository into a single AI-friendly file — respecting .gitignore, with token counting and intelligent formatting. When I need to feed a codebase to ChatGPT or Claude, this is how I do it. Essential for the "understand my project" prompt.

### 7. [dragonflydb/dragonfly](https://github.com/dragonflydb/dragonfly) ⭐30,730
**Why I starred this:** A Redis replacement that's 25x faster on a single node and uses dramatically less memory. Drop-in compatible with the Redis protocol, so all my existing code works. I use it as the fast cache layer in my agent memory stack — sub-millisecond latency with no operational overhead.

### 8. [hiyouga/LlamaFactory](https://github.com/hiyouga/LlamaFactory) ⭐72,279
**Why I starred this:** Fine-tuning made accessible. One tool that supports 100+ models with a unified interface — LoRA, QLoRA, full fine-tuning, RLHF. Before LlamaFactory, fine-tuning a model meant stitching together 5 different libraries. Now it's a single config file and one command.

### 9. [upstash/context7](https://github.com/upstash/context7) ⭐57,625
**Why I starred this:** Always-updated code documentation injected into LLM context. When my coding agent needs to use a library, Context7 provides the actual API reference rather than stale training data. It's the difference between "I think this function exists" and "I know this is the current API."

### 10. [browser-use/browser-harness](https://github.com/browser-use/browser-harness) ⭐15,058
**Why I starred this:** Self-healing browser automation for LLMs. It handles the messy reality of web automation — selectors change, pages load slowly, popups appear — so my agents don't get stuck. If an agent needs to interact with any website reliably, this is the harness that makes it possible.

---

## 🗄️ Databases & Data — Top 10

### 1. [supabase/supabase](https://github.com/supabase/supabase) ⭐104,445
**Why I starred this:** The open-source Firebase that actually delivers. Postgres underneath (so you get real SQL, not a limited query language), plus auth, realtime subscriptions, edge functions, and storage — all self-hostable. It's what I reach for when I need a backend in 10 minutes but refuse to be locked into a proprietary platform. The local dev experience with `supabase start` is genuinely excellent.

### 2. [pocketbase/pocketbase](https://github.com/pocketbase/pocketbase) ⭐55,000
**Why I starred this:** An entire backend in a single Go binary. SQLite database, file storage, auth, admin UI, realtime subscriptions — all in ~20MB. No containers, no config files, no dependency hell. It's the ultimate "I need a database and API right now" tool for side projects and prototypes. The admin dashboard is so good I've shipped it to non-technical clients.

### 3. [nocodb/nocodb](https://github.com/nocodb/nocodb) ⭐58,000
**Why I starred this:** Airtable, but backed by your own database (Postgres, MySQL, SQLite, etc.). Spreadsheet UI that anyone can use, but underneath it's generating real SQL queries. The best feature: you can switch between spreadsheet view and raw SQL at any time. It's the bridge between "I want a spreadsheet" and "I want a real database."

### 4. [appwrite/appwrite](https://github.com/appwrite/appwrite) ⭐52,000
**Why I starred this:** Firebase alternative with a philosophy I respect: self-hosted first, with a cloud option. Database, auth, storage, functions, messaging, and realtime — all with a clean REST API. The console UI is gorgeous and the SDK generation for 15+ languages means I never write boilerplate API clients. It's my go-to for hackathons.

### 5. [mathesar-foundation/mathesar](https://github.com/mathesar-foundation/mathesar) ⭐6,500
**Why I starred this:** A Postgres GUI that doesn't flatten the database into a spreadsheet — it respects the relational model. Foreign keys become links, views are first-class, and the UI actually teaches you database design. It's the tool I'd give to someone who knows Excel but wants to graduate to a real database without learning SQL first. Genuinely thoughtful design.

### 6. [surrealdb/surrealdb](https://github.com/surrealdb/surrealdb) ⭐33,000
**Why I starred this:** The most ambitious database project I follow. Multi-model (document, graph, time-series, vector) in a single engine written in Rust. The SurrealQL language lets you do joins, graph traversals, and vector search in one query. It's not production-ready for everything yet, but it's the database I want to exist in 5 years — and the velocity is real.

### 7. [FerretDB/FerretDB](https://github.com/FerretDB/FerretDB) ⭐10,000
**Why I starred this:** MongoDB wire protocol, backed by Postgres. If you have an app that speaks MongoDB but you want to run it on Postgres (for ACID, for tooling, for licensing), FerretDB translates the wire protocol transparently. It's the escape hatch from document-database lock-in without rewriting your application.

### 8. [undb-xyz/undb](https://github.com/undb-xyz/undb) ⭐6,000
**Why I starred this:** A local-first database-as-spreadsheet that feels like Airtable's minimalist cousin. Built on SQLite and runs entirely in the browser (WASM) — no server needed. I star it because it represents the future: databases that work offline, sync when connected, and don't require infrastructure. The DX is surprisingly smooth.

### 9. [chartdb/chartdb](https://github.com/chartdb/chartdb) ⭐21,000
**Why I starred this:** One-click database diagrams from a connection string. Drop in a Postgres or MySQL URL and it generates a full ERD with relationships, indexes, and exportable DDL. I use it every time I inherit a project with no documentation — it reverse-engineers understanding in seconds. The visual schema diff feature is also incredible for reviewing migrations.

### 10. [vanna-ai/vanna](https://github.com/vanna-ai/vanna) ⭐16,000
**Why I starred this:** Natural language → SQL, trained on your actual schema and query history. Unlike generic text-to-SQL tools, Vanna learns your table conventions, your naming patterns, and common queries over time. Connect it to your database and non-technical teammates can ask "how many users signed up last week" and get accurate results. It's the most practical AI + database tool I've found.

---

## 🔒 Security & Identity — Top 10

### 1. [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) ⭐69,857
**Why I starred this:** The NSA's reverse engineering framework, open-sourced. A full-featured SRE tool with a decompiler, disassembler, debugger, and plugin API — for free. It's the kind of tool that reminds you how much capability exists in government labs. I star it both for practical use (analyzing binaries, understanding malware) and as a piece of software history.

### 2. [crowdsecurity/crowdsec](https://github.com/crowdsecurity/crowdsec) ⭐12,000
**Why I starred this:** Fail2ban redesigned for the modern era. It detects attacks based on behavior analysis (not just log regexes), shares threat intelligence across a global community, and can block attackers at the CDN/bouncer level before they even hit your server. I run it on every public-facing service and it silently blocks ~50 attacks/day without me thinking about it.

### 3. [dani-garcia/vaultwarden](https://github.com/dani-garcia/vaultwarden) ⭐47,000
**Why I starred this:** Bitwarden server rewritten in Rust — memory-efficient enough to run on a Raspberry Pi. Full password manager functionality (passwords, TOTP, passkeys, sharing) without the Bitwarden enterprise pricing. It's the first service I set up on any new server and the one my family actually uses. Security that doesn't feel like a compromise.

### 4. [goauthentik/authentik](https://github.com/goauthentik/authentik) ⭐17,000
**Why I starred this:** Single sign-on that's actually designed for self-hosters. OAuth2, SAML, LDAP, proxy auth, MFA, passwordless — all with a web UI that makes sense. Add `authentik-proxy` in front of any service and it gets authentication without modifying the app. It's the identity layer that ties my entire homelab together.

### 5. [tailscale/tailscale](https://github.com/tailscale/tailscale) ⭐22,000
**Why I starred this:** Zero-config WireGuard mesh networking that Just Works. Install on any device and they all find each other through NAT, firewalls, and CGNAT — no port forwarding, no config files. The MagicDNS, Funnel (public ingress), and ACL system make it so much more than a VPN. It's how I access everything I run, from anywhere, without opening a single port.

### 6. [authelia/authelia](https://github.com/authelia/authelia) ⭐24,000
**Why I starred this:** The authentication middleware that sits in front of your services. It handles 2FA (TOTP, Duo, WebAuthn), password resets, brute-force protection, and access control — all before requests reach your apps. Pair it with any reverse proxy (Traefik, Nginx, Caddy) and every service behind it gets enterprise-grade auth.

### 7. [gravitl/netmaker](https://github.com/gravitl/netmaker) ⭐11,000
**Why I starred this:** WireGuard mesh networks managed through a web UI and API. Unlike Tailscale, it's fully self-hosted with no external dependencies. It handles key exchange, peer discovery, and ingress/egress gateways across clouds and on-prem. I use it for connecting my VPS instances into a private mesh without recurring per-device fees.

### 8. [fail2ban/fail2ban](https://github.com/fail2ban/fail2ban) ⭐14,000
**Why I starred this:** The original brute-force defender — and still essential. It scans logs for authentication failures and temporarily bans IPs via iptables. Simple, reliable, zero dependencies. I star it out of respect: it's been protecting servers for 20 years and still works perfectly. Sometimes the old tools are the right tools.

### 9. [smallstep/certificates](https://github.com/smallstep/certificates) ⭐7,500
**Why I starred this:** Your own internal certificate authority with ACME support. No more self-signed cert warnings internally — every service gets a proper TLS certificate from a CA you control. It integrates with ACME clients (like Caddy and Traefik) so all your internal services get auto-renewed TLS. It's the missing piece in "zero trust internally."

### 10. [lwthiker/curl-impersonate](https://github.com/lwthiker/curl-impersonate) ⭐6,000
**Why I starred this:** Curl, but it impersonates Chrome/Firefox/Safari TLS fingerprints. Many websites block bots based on TLS handshake fingerprinting — this bypasses that by mimicking real browser behavior at the TLS level. Essential for web scraping, API testing, and any automation where sites try to detect non-browser clients.

---

## ⚡ Automation & Workflow — Top 10

### 1. [n8n-io/n8n](https://github.com/n8n-io/n8n) ⭐193,041
**Why I starred this:** The open-source automation platform that I actually enjoy using. 400+ integrations, a visual workflow editor that doesn't feel like a toy, and the ability to write custom JavaScript/TypeScript nodes. Self-hosted means my automation data stays on my server. I use it to connect my homelab services, send notifications, and automate deployment pipelines. It's Zapier for people who know how to code.

### 2. [huginn/huginn](https://github.com/huginn/huginn) ⭐48,000
**Why I starred this:** Build agents that monitor the web and take actions on your behalf. "Email me when a new apartment listing matches my criteria," "Track this product price and buy when it drops," "Monitor RSS feeds and cross-post to Discord." It's a system of programmable agents that watch things 24/7 so I don't have to. The name comes from the Norse raven that flew around the world gathering information — accurate.

### 3. [activepieces/activepieces](https://github.com/activepieces/activepieces) ⭐15,000
**Why I starred this:** The no-code automation platform that competes with Zapier/Make but is fully open-source. It has the cleanest UI of any automation tool I've tried, pieces (connectors) are TypeScript functions, and it supports branching, loops, and error handling naturally. It's what I recommend to less technical friends who want automation without n8n's learning curve.

### 4. [windmill-labs/windmill](https://github.com/windmill-labs/windmill) ⭐13,000
**Why I starred this:** Turn scripts into production APIs and workflows. Write a Python/TypeScript/Go/Bash script, and Windmill gives it a REST API, a UI, cron scheduling, webhook triggers, and approval flows — instantly. It's the fastest path from "I wrote a script" to "this is a production service" I've ever seen. The auto-generated UIs for script parameters feel like magic.

### 5. [Kong/insomnia](https://github.com/Kong/insomnia) ⭐37,000
**Why I starred this:** The API client I prefer over Postman. Open-source, supports REST, GraphQL, gRPC, and WebSocket, and has a design-first approach with OpenAPI spec generation. The environment variable management is cleaner than Postman's, and it doesn't push cloud accounts as aggressively. It's my daily driver for API development and debugging.

### 6. [hoppscotch/hoppscotch](https://github.com/hoppscotch/hoppscotch) ⭐72,000
**Why I starred this:** A beautiful, browser-based API client that requires zero installation. REST, GraphQL, WebSocket, SSE, MQTT — all in one tab. The PWA version works offline, and the self-host option means I can run my own instance. When I'm on a machine where I can't install anything, this is my API workspace.

### 7. [triggerdotdev/trigger.dev](https://github.com/triggerdotdev/trigger.dev) ⭐23,000
**Why I starred this:** Durable, long-running background jobs for Next.js and serverless apps. Instead of 30-second Lambda timeouts, Trigger.dev jobs can run for hours with automatic retries, logging, and observability. It's the answer to "how do I run a 20-minute AI pipeline in a serverless architecture" — write it as a regular async function, and Trigger handles the rest.

### 8. [kestra-io/kestra](https://github.com/kestra-io/kestra) ⭐11,000
**Why I starred this:** Declarative, event-driven orchestration that treats workflows as infrastructure. Define pipelines in YAML (with templating), version-control them in Git, and trigger them from events, schedules, or APIs. It's Airflow without the Python overhead — more like Terraform for workflows. The real-time topology view during execution is beautiful.

### 9. [argoproj/argo-workflows](https://github.com/argoproj/argo-workflows) ⭐16,000
**Why I starred this:** Kubernetes-native workflow engine for compute-intensive pipelines. Each step runs in its own container with resource limits, retries, and artifact passing. It's the Kubernetes way of saying "run this ML training job, then this data processing step, then deploy the model" — all with DAG semantics and a web UI. Production-grade CI/CD and data pipelines.

### 10. [PrefectHQ/prefect](https://github.com/PrefectHQ/prefect) ⭐22,000
**Why I starred this:** Python workflow orchestration that doesn't force you into DAG-shaped thinking. Dynamic, parameterized workflows with automatic retries, caching, and a beautiful UI. Unlike Airflow, it embraces the fact that Python is dynamic — workflows can branch, loop, and adapt at runtime. I use it for data pipelines that need flexibility, not rigidity.

---

## 💻 Developer Resources — Top 10

### 1. [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) ⭐516,951
**Why I starred this:** The ultimate "learn by building" curriculum. Guides for building your own git, redis, docker, database, shell, web server, neural network, and 100+ more — from scratch. It's the antidote to tutorial hell. Every time I want to deeply understand a technology, I find its guide here and build it. This repo has taught me more than any course.

### 2. [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) ⭐369,000
**Why I starred this:** A curated list of free programming books, courses, and resources across every language and topic imaginable. It's the library I send to anyone learning to code — maintained by hundreds of contributors and available in 50+ languages. The fact that this quality of education is freely available is genuinely inspiring.

### 3. [public-apis/public-apis](https://github.com/public-apis/public-apis) ⭐352,000
**Why I starred this:** A collective list of free APIs for development — weather, finance, animals, sports, games, data, everything. When I'm prototyping and need a data source, I browse here instead of signing up for yet another API key. It's saved me from building mock data generators more times than I can count.

### 4. [kamranahmedse/developer-roadmap](https://github.com/kamranahmedse/developer-roadmap) ⭐327,000
**Why I starred this:** Interactive roadmaps for every development career path — frontend, backend, DevOps, AI, blockchain, game dev, and more. It's not a tutorial; it's a "here's what you need to know and in what order" map. I use it when mentoring junior devs and when exploring a new domain myself. The visual clarity is unmatched.

### 5. [jwasham/coding-interview-university](https://github.com/jwasham/coding-interview-university) ⭐326,000
**Why I starred this:** A complete computer science education plan, originally created to prep for Google interviews, now a comprehensive CS curriculum. Data structures, algorithms, system design, networking, OS — all mapped out with resources. I star it as a reference for foundational CS knowledge, not just interview prep. The creator's discipline is humbling.

### 6. [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) ⭐320,000
**Why I starred this:** The best resource on system design I've found. From scaling a web app to designing YouTube, Twitter, or WhatsApp — every major system design topic with diagrams, tradeoff discussions, and Anki flashcards. I revisit it before any architecture decision to sanity-check my thinking. It's made me a better engineer.

### 7. [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) ⭐248,000
**Why I starred this:** Curated tutorials that teach through building real projects — compilers, games, operating systems, databases. The philosophy: you don't learn to code by reading, you learn by building. Each tutorial is tagged with the primary language and difficulty level. It's the syllabus I wish I had when I started programming.

### 8. [sindresorhus/awesome](https://github.com/sindresorhus/awesome) ⭐379,000
**Why I starred this:** The meta-list of curated lists. Want to know the best Go libraries? There's an awesome-go. Best Rust tools? awesome-rust. The awesome list ecosystem is how I discover new tools in any domain — I start here, follow the rabbit hole, and find gems I'd never encounter otherwise.

### 9. [mtdvio/every-programmer-should-know](https://github.com/mtdvio/every-programmer-should-know) ⭐97,000
**Why I starred this:** A collection of technical knowledge every software engineer should know — from data structures to distributed systems, from Unicode to floating point arithmetic. It's not a tutorial; it's a map of the territory. I use it as a self-assessment tool: if I can't explain something on this list, I study it.

### 10. [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) ⭐172,000
**Why I starred this:** A sysadmin's grimoire — commands, one-liners, configs, and hard-won knowledge for Linux, networking, security, and debugging. It's the kind of knowledge that usually lives in personal wikis and .bash_history files. When something breaks at 3 AM and I need the right incantation, this book has often saved me.

---

## ⌨️ Terminal & CLI Tools — Top 10

### 1. [junegunn/fzf](https://github.com/junegunn/fzf) ⭐81,037
**Why I starred this:** The fuzzy finder that changed how I use the terminal. `Ctrl+R` for command history search, `Ctrl+T` to fuzzy-find files, `**<Tab>` to trigger it inline — it's so deeply integrated into my workflow that I feel lost without it. The vim/neovim integration makes it an indispensable part of my editor too. If I could only install one CLI tool on a new machine, it's fzf.

### 2. [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep) ⭐53,000
**Why I starred this:** Recursively search directories with regex, ignoring .gitignore, at incredible speed. It replaced grep, ack, ag, and find-in-files in my workflow overnight. Written in Rust with SIMD acceleration, it searches millions of lines in milliseconds. The `rg` command is muscle memory at this point — I type it without thinking.

### 3. [sharkdp/bat](https://github.com/sharkdp/bat) ⭐55,000
**Why I starred this:** `cat` with wings. Syntax highlighting, line numbers, Git change markers, and automatic paging — all in a single binary. I've aliased `cat=bat` so thoroughly that I flinch when I see plain cat output. The Nord theme it defaults to is gorgeous, and it handles massive files gracefully.

### 4. [sharkdp/fd](https://github.com/sharkdp/fd) ⭐40,000
**Why I starred this:** A simpler, faster `find`. Intuitive syntax (`fd pattern` instead of `find . -name pattern`), respects .gitignore by default, and is blazing fast. I use it dozens of times a day — `fd somefile` and it instantly shows me every match. It's what find should have been.

### 5. [ajeetdsouza/zoxide](https://github.com/ajeetdsouza/zoxide) ⭐33,000
**Why I starred this:** A smarter `cd` that learns your habits. It tracks which directories you visit most and lets you jump to them with partial names — `z proj` takes me to `/home/me/projects/whatever` because it knows. After a week of use, navigating my filesystem feels telepathic. It works with every shell and is absurdly fast.

### 6. [starship/starship](https://github.com/starship/starship) ⭐51,000
**Why I starred this:** The cross-shell prompt that shows exactly what I need — current directory, git branch and status, language version, runtime indicators, command duration. It's fast (Rust), works with any shell, and the default config is tasteful. I use it everywhere and never configure prompts manually anymore.

### 7. [lsd-rs/lsd](https://github.com/lsd-rs/lsd) ⭐16,000
**Why I starred this:** `ls` with Nerd Font icons, colors, and tree view. `lsd -la` shows file permissions with icons, `lsd --tree` visualizes directory structure, and the output is genuinely beautiful. Combined with bat and fd, it completes the holy trinity of Rust-powered terminal replacements.

### 8. [atuinsh/atuin](https://github.com/atuinsh/atuin) ⭐27,000
**Why I starred this:** Shell history synced across machines with full-text search, encrypted storage, and statistics. Every command I've ever typed, searchable, across my laptop, desktop, and servers. The stats feature alone — showing your most-used commands — is weirdly addictive. And unlike shell history files, it's encrypted so I don't worry about sensitive commands leaking.

### 9. [jesseduffield/lazygit](https://github.com/jesseduffield/lazygit) ⭐63,000
**Why I starred this:** Git operations at the speed of thought. Staging individual hunks, resolving merge conflicts, interactive rebasing, cherry-picking — all with vim keybindings in a beautiful TUI. It's so good that I use it even when I know the git CLI commands. The merge conflict resolution interface alone is worth the install.

### 10. [eza-community/eza](https://github.com/eza-community/eza) ⭐19,000
**Why I starred this:** The modern `ls` replacement (formerly exa). Color-coded output, Git-aware file listing with status icons, and hyperlink support in modern terminals. `eza -la --git` is my default `ls` alias — it shows me file permissions, sizes, modification times, and git status all in one clean view. The tree view with `--tree --level=3` is how I explore new codebases.

---

## 📝 Knowledge & PKM — Top 10

### 1. [toeverything/AFFiNE](https://github.com/toeverything/AFFiNE) ⭐69,532
**Why I starred this:** Notion + Miro in one open-source, local-first app. Write docs, draw on a canvas, and link them together — all stored locally with optional sync. The "blocks everywhere" philosophy means a paragraph in a doc can also live on a whiteboard. It's the most ambitious PKM project I follow, and the pace of development is relentless.

### 2. [AppFlowy-IO/AppFlowy](https://github.com/AppFlowy-IO/AppFlowy) ⭐67,000
**Why I starred this:** Notion's open-source doppelganger built in Flutter + Rust. Local-first, privacy-focused, with a Notion-caliber UI. The data lives on your machine in a SQLite database you can query directly. I star it because it proves that polished productivity software can be open-source — you don't have to sacrifice UX for principles.

### 3. [logseq/logseq](https://github.com/logseq/logseq) ⭐42,000
**Why I starred this:** A knowledge graph that treats your notes as a database. Every bullet is a block that can be referenced, linked, and queried. It's outliner + wiki + journal, all stored in plain Markdown/Org files. The query system (Datalog-like syntax) lets you ask "show me all TODOs tagged #urgent from the last week" and get instant results. It's how I organize my thinking.

### 4. [siyuan-note/siyuan](https://github.com/siyuan-note/siyuan) ⭐34,000
**Why I starred this:** A block-based note-taking app that feels like a modern, local-first Notion with Chinese engineering precision. Content blocks can be embedded, referenced, and synchronized across devices (with end-to-end encryption). The block-level reference system is more powerful than bidirectional links — you can compose documents by assembling blocks from anywhere.

### 5. [foambubble/foam](https://github.com/foambubble/foam) ⭐17,000
**Why I starred this:** Roam Research, but as a VS Code extension. Your notes are plain Markdown files in a Git repo, with graph visualization, backlinks, and daily notes. I love that it's not a separate app — it's my editor with PKM superpowers. The Git-backed approach means every note has version history and can be collaboratively edited.

### 6. [dendronhq/dendron](https://github.com/dendronhq/dendron) ⭐7,500
**Why I starred this:** Hierarchical note-taking that scales to 20,000+ notes without becoming a mess. Notes are organized in a hierarchy (like `dev.python.asyncio`) and can be looked up, refactored, and linked with precision. It's the PKM system for people who think in structured taxonomies rather than flat graphs. The lookup system makes finding any note instant.

### 7. [mickael-menu/zk](https://github.com/mickael-menu/zk) ⭐3,500
**Why I starred this:** A plain-text Zettelkasten assistant for the terminal. `zk new` creates a note, `zk list` queries your notes with filters, and `zk graph` visualizes connections. It's the Unix philosophy applied to knowledge management: do one thing well, work with plain text, and compose with other tools. My terminal-native PKM companion.

### 8. [outline/outline](https://github.com/outline/outline) ⭐32,000
**Why I starred this:** The team wiki that actually looks modern. Real-time collaborative editing, Markdown support, nested collections, and a clean reading experience. It's what Confluence should have been. Self-hostable with Slack/OIDC auth, and the search is genuinely fast. I use it for team documentation that doesn't feel like a chore to write.

### 9. [docmost/docmost](https://github.com/docmost/docmost) ⭐14,000
**Why I starred this:** A Notion/Confluence alternative that's self-hosted, real-time collaborative, and built with a modern stack. It has the block editor, comments, and page nesting you'd expect, but runs on Postgres and Redis. Newcomer to the space but the execution is surprisingly polished. I'm watching this one closely.

### 10. [bookstackapp/BookStack](https://github.com/BookStackApp/BookStack) ⭐18,000
**Why I starred this:** Documentation organized like a book — shelves → books → chapters → pages. It's the simplest hierarchy that works for structured documentation. The WYSIWYG editor with Markdown support, diagramming (draw.io integration), and role-based access control make it ideal for internal wikis. It's how I organize documentation that needs a table of contents, not a graph.

---

## 🌐 Web & Design — Top 10

### 1. [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) ⭐93,437
**Why I starred this:** A massive library of UI/UX patterns, components, and design principles distilled from top products. It's like having a senior designer's brain in a repo — "how does Stripe handle empty states," "what's the correct focus ring pattern," "accessibility checklist for modals." I reference it whenever I'm designing a new interface and want to avoid reinventing known patterns.

### 2. [shadcn-ui/ui](https://github.com/shadcn-ui/ui) ⭐85,000
**Why I starred this:** Beautifully designed, accessible React components that you copy-paste into your project (not install as a dependency). This means you own the code, can customize anything, and get React 19/server components support naturally. The design sensibilities are impeccable — it's the component library that makes my projects look professional by default.

### 3. [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss) ⭐90,000
**Why I starred this:** Utility-first CSS that changed how I think about styling. Instead of naming things and fighting specificity, I compose designs from primitives directly in HTML. It's controversial for a reason — you either love it or hate it — but after building dozens of projects with it, the speed and consistency it provides are unmatched. Tailwind v4 with CSS-first configuration is even better.

### 4. [vercel/next.js](https://github.com/vercel/next.js) ⭐135,000
**Why I starred this:** The React framework that makes full-stack development feel coherent. Server components, streaming, file-based routing, image optimization, ISR — it abstracts the hard parts of web development without hiding them. It's what I reach for when I need a production React app fast, and the ecosystem (Vercel, shadcn, tRPC) is incredibly well-integrated.

### 5. [storybookjs/storybook](https://github.com/storybookjs/storybook) ⭐87,000
**Why I starred this:** The workshop for building UI components in isolation. Develop, test, and document components without running the full app. It's essential for design systems — every component has a story that shows its variants, edge cases, and accessibility. When I'm building a component library, Storybook is the first thing I set up.

### 6. [browserless/browserless](https://github.com/browserless/browserless) ⭐11,000
**Why I starred this:** Headless Chrome as a service — with connection pooling, queueing, and error handling. Instead of managing Chrome processes in my scraping/PDF generation/screenshot pipelines, I send requests to browserless and it handles the rest. It's the production-grade headless browser that Puppeteer/Playwright scripts deserve.

### 7. [radix-ui/primitives](https://github.com/radix-ui/primitives) ⭐20,000
**Why I starred this:** Unstyled, accessible React primitives that shadcn/ui builds on top of. Dialog, dropdown, tooltip, tabs — every component handles focus management, keyboard navigation, ARIA attributes, and animation foundations. It's the accessibility layer I trust when building custom design systems. The "unstyled" approach means total visual control with correct behavior.

### 8. [nuejs/nue](https://github.com/nuejs/nue) ⭐10,000
**Why I starred this:** A radical rethink of frontend development — a web framework for UX engineers that prioritizes design over engineering complexity. It uses HTML-based templating with minimal JavaScript and is designed for designers who code. I star it as a bet on a future where web development isn't dominated by JavaScript framework complexity.

### 9. [sveltejs/svelte](https://github.com/sveltejs/svelte) ⭐84,000
**Why I starred this:** The framework that compiles away. No virtual DOM, reactive-by-default, scoped styles, and genuinely less code than React equivalents. It feels like writing HTML with superpowers. Svelte 5 with runes is a paradigm shift in reactive programming, and the DX is so pleasant that I choose it for personal projects whenever possible.

### 10. [sailboatui/sailboatui](https://github.com/sailboatui/sailboatui) ⭐10,000
**Why I starred this:** A Tailwind CSS component library that focuses on developer experience and code quality. Pre-built pages, components, and sections that look custom-made — not like another "generic Tailwind template." When I need to ship a landing page or dashboard quickly and don't want to design from scratch, this is my starting point.

---

## 💬 Communication & Chat — Top 10

### 1. [python-telegram-bot/python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) ⭐29,231
**Why I starred this:** The library that makes Telegram bot development genuinely enjoyable. Clean, Pythonic API with type hints, conversation handlers, job queues, and excellent documentation. I've built notification systems, deployment bots, and media archivers with it — the async/await support means it scales to thousands of users without breaking a sweat.

### 2. [mattermost/mattermost](https://github.com/mattermost/mattermost) ⭐32,000
**Why I starred this:** Self-hosted Slack alternative with real-time messaging, threaded conversations, webhooks, and extensive integrations. Written in Go + React, it runs efficiently and the API is well-documented. It's what I'd deploy for an organization that needs Slack-level features but wants data sovereignty.

### 3. [zulip/zulip](https://github.com/zulip/zulip) ⭐24,000
**Why I starred this:** The chat platform designed around topics (threads) as first-class primitives. Every message belongs to a topic, making async communication actually work — you can catch up on a conversation from yesterday without scrolling through memes. It's open-source, self-hosted, and the design is backed by research. If more companies used Zulip, fewer people would hate chat.

### 4. [matrix-org/synapse](https://github.com/matrix-org/synapse) ⭐5,500
**Why I starred this:** The reference Matrix homeserver. Federated, decentralized chat that lets you talk to anyone on any Matrix server — like email for messaging. I star it because Matrix is the most serious attempt at an open, interoperable messaging protocol, and Synapse is the battle-tested implementation. The bridges to Discord, Slack, Telegram, and IRC make it a universal chat hub.

### 5. [signalapp/Signal-Server](https://github.com/signalapp/Signal-Server) ⭐10,000
**Why I starred this:** The server that powers Signal, the gold standard for private messaging. I star it not because I'd run it (Signal's architecture is deliberately centralized), but because it's a masterclass in cryptographic protocol design. The double ratchet algorithm, sealed sender, and private group system are worth studying for any engineer building secure systems.

### 6. [discord/discord-api-docs](https://github.com/discord/discord-api-docs) ⭐6,500
**Why I starred this:** Discord's API documentation repo, community-maintained and surprisingly comprehensive. When building Discord bots, slash commands, or webhooks, this is the reference. I star it because Discord's API is genuinely well-designed (gateway + REST + interactions) and the docs repo is an example of how to do developer platforms right.

### 7. [RocketChat/Rocket.Chat](https://github.com/RocketChat/Rocket.Chat) ⭐43,000
**Why I starred this:** A self-hosted communication platform with messaging, video calls, file sharing, and integrations. It's Slack + Zoom + Dropbox, self-hosted. The omnichannel customer service features (live chat widget, email, SMS) make it more than just team chat. It's the most feature-complete open-source communication platform available.

### 8. [cinnyapp/cinny](https://github.com/cinnyapp/cinny) ⭐3,000
**Why I starred this:** A beautiful Matrix client that looks and feels like Discord. It makes Matrix actually pleasant to use — clean UI, smooth animations, and a sensible layout. For people intimidated by Element's busy interface, Cinny is the client that makes Matrix feel like a modern chat app. If Matrix is to succeed, it needs clients like this.

### 9. [revoltchat/revolt](https://github.com/revoltchat/revolt) ⭐8,000
**Why I starred this:** A Discord-like chat platform that's fully open-source and self-hostable. It has the polish of Discord — roles, channels, embeds, bots — but with an open protocol and no monetization pressure. It's what Discord would be if it were built by the community for the community. The UI is shockingly good for an open-source project.

### 10. [element-hq/element-web](https://github.com/element-hq/element-web) ⭐13,000
**Why I starred this:** The flagship Matrix client, built by the Matrix creators. It's the most feature-complete Matrix experience — E2EE by default, VoIP, widgets, integrations, and bridges. It's not the prettiest client, but it's the most capable. When I need to prove that Matrix works for real-world use, Element is the reference implementation.

---

## 📄 Documentation & Static Sites — Top 10

### 1. [squidfunk/mkdocs-material](https://github.com/squidfunk/mkdocs-material) ⭐26,960
**Why I starred this:** The theme that makes documentation beautiful. Markdown in, gorgeous responsive docs out — with search, dark mode, code annotations, diagrams, and navigation that just works. I use it for every project's documentation because it's zero-effort beauty. The instant search (client-side, no backend) and the mermaid/diagram support make it feel premium.

### 2. [facebook/docusaurus](https://github.com/facebook/docusaurus) ⭐63,000
**Why I starred this:** Meta's documentation framework that powers React Native, Jest, and thousands of other projects. MDX support, versioning, i18n, and a plugin ecosystem that covers everything from search (Algolia) to analytics. It's the heavy-duty option — when documentation needs to be a product in itself, Docusaurus delivers.

### 3. [withastro/starlight](https://github.com/withastro/starlight) ⭐7,000
**Why I starred this:** Documentation built on Astro, the zero-JS-by-default framework. It's blazing fast because it ships minimal JavaScript, supports MDX, and has built-in navigation, search, and dark mode. For developer docs where performance matters (and your audience is on slow connections), Starlight is the thoughtful choice.

### 4. [just-the-docs/just-the-docs](https://github.com/just-the-docs/just-the-docs) ⭐8,500
**Why I starred this:** A Jekyll theme for documentation that focuses on hierarchy and navigation. No flashy features — just excellent information architecture, responsive layout, and clean typography. When I want docs that are purely about content without framework overhead, this is my pick. It works on GitHub Pages natively, which is a huge plus.

### 5. [docsifyjs/docsify](https://github.com/docsifyjs/docsify) ⭐30,000
**Why I starred this:** Documentation that renders on the fly — no build step, no static HTML generation. Drop your Markdown files, add one HTML file, and you have a documentation site with full-text search and theming. It's the simplest possible path from Markdown → docs site, and the runtime rendering means edits are live instantly.

### 6. [vitepressjs/vitepress](https://github.com/vuejs/vitepress) ⭐15,000
**Why I starred this:** Vue-powered documentation that's essentially VitePress (the Vue team's answer to Docusaurus). It's incredibly fast (Vite-based), supports Vue components in Markdown, and has a clean, minimal aesthetic. For Vue projects it's the obvious choice; for non-Vue projects, it's still competitive with any static docs generator.

### 7. [mdx-js/mdx](https://github.com/mdx-js/mdx) ⭐19,000
**Why I starred this:** Markdown with embedded JSX components. Write documentation that includes live code examples, interactive demos, and custom components — all in .mdx files. It's the format that bridges documentation and storytelling. Every time I write docs that need code examples that actually run, MDX is the format.

### 8. [getgrav/grav](https://github.com/getgrav/grav) ⭐15,000
**Why I starred this:** A flat-file CMS with no database — content is stored as Markdown files in folders, yet you get a full admin panel, themes, plugins, and caching. It's WordPress-level capability with Jekyll-level simplicity. For clients who need a CMS but I refuse to maintain a database, Grav is my secret weapon.

### 9. [retypeapp/retype](https://github.com/retypeapp/retype) ⭐5,500
**Why I starred this:** A static site generator that produces visually impressive documentation from Markdown with zero configuration. Live preview while editing, built-in search, and a polished default theme. It's like mkdocs-material's simpler cousin — less customizable but even faster to set up. Ideal for small-to-medium projects.

### 10. [rust-lang/mdBook](https://github.com/rust-lang/mdBook) ⭐21,000
**Why I starred this:** The documentation tool that Rust uses for The Book. Markdown → a beautiful, searchable online book with inline code testing (you can run code samples). The built-in test runner for code blocks ensures documentation examples never go stale. It's so good that non-Rust projects use it too — I've written internal documentation books with it.

---

## 📱 Mobile & Cross-Platform — Top 10

### 1. [DioxusLabs/dioxus](https://github.com/DioxusLabs/dioxus) ⭐36,425
**Why I starred this:** React-like UI framework in Rust that targets web, desktop, mobile, and TUI — from a single codebase. The ambitious vision is "write once in Rust, render everywhere" with native performance. It's not production-ready for everything yet, but the architecture is elegant and the team ships fast. This is where cross-platform UI could be in 3 years.

### 2. [facebook/react-native](https://github.com/facebook/react-native) ⭐126,000
**Why I starred this:** Write mobile apps in React that compile to truly native UI components — not WebViews. It powers Facebook, Instagram, Discord, Shopify, and thousands more. I star it because it proved that "learn once, write everywhere" is practical for real production apps at scale. The new architecture (Fabric + TurboModules) is a massive improvement.

### 3. [flutter/flutter](https://github.com/flutter/flutter) ⭐172,000
**Why I starred this:** Google's UI toolkit for building natively compiled applications from a single Dart codebase — mobile, web, desktop, embedded. The hot reload is addictive, the widget system is composable, and the Material Design implementation is pixel-perfect. When I need a polished, performant cross-platform app and don't mind Dart, Flutter delivers.

### 4. [expo/expo](https://github.com/expo/expo) ⭐40,000
**Why I starred this:** The React Native framework that removes the pain. Expo handles building, signing, OTA updates, push notifications, and 100+ native modules — so you focus on the app, not the toolchain. It's what makes React Native accessible to web developers. The EAS Build service means I never configure Xcode manually again.

### 5. [tamagui/tamagui](https://github.com/tamagui/tamagui) ⭐13,000
**Why I starred this:** A UI kit and optimizing compiler for React Native + Web. Write components once in Tamagui and they render optimally on both platforms — with the web version compiling to atomic CSS. It solves the hardest problem in cross-platform UI: making apps that feel native everywhere without code duplication. The performance optimization is real engineering, not marketing.

### 6. [nandorojo/solito](https://github.com/nandorojo/solito) ⭐5,000
**Why I starred this:** A navigation library that unifies Next.js and React Navigation into a single API. Write navigation once and it works on web (Next.js file-based routing) and mobile (React Navigation stacks/tabs). For projects using the Expo + Next.js monorepo pattern, this is the missing piece that makes the dream of shared navigation actually work.

### 7. [ionic-team/capacitor](https://github.com/ionic-team/capacitor) ⭐13,000
**Why I starred this:** A cross-platform native runtime for web apps. Write your app with any web framework (React, Vue, Svelte), and Capacitor wraps it in a native container with access to device APIs (camera, filesystem, push notifications, etc.). It's the spiritual successor to Cordova/PhoneGap, with a modern API and better plugin ecosystem.

### 8. [tauri-apps/tauri](https://github.com/tauri-apps/tauri) ⭐98,000
**Why I starred this:** Build desktop apps with web frontends and Rust backends — 10x smaller than Electron. The Rust core handles system APIs, file access, and security, while the web view renders the UI. It's what Electron should have been: secure by default, memory-efficient, and built on Rust. The v2 release with mobile support is the most exciting thing in desktop development.

### 9. [nativewind/nativewind](https://github.com/nativewind/nativewind) ⭐7,000
**Why I starred this:** Tailwind CSS, but for React Native. Write `className="flex-1 bg-black p-4"` and it compiles to NativeWind styles — no `StyleSheet.create()` boilerplate. It makes the mental model of styling identical across web and mobile, which is the dream for full-stack developers. The developer experience is so much faster than StyleSheet.

### 10. [kivy/kivy](https://github.com/kivy/kivy) ⭐19,000
**Why I starred this:** A Python framework for building multi-touch applications that run on Windows, macOS, Linux, Android, and iOS. It's the "I want a GUI in Python and I want it everywhere" option. The KV language for declarative UI is unique and powerful. For Python-first developers who need a GUI, Kivy is the most mature cross-platform option.

---

## 🪟 Windows Tools — Top 10

### 1. [dockur/windows](https://github.com/dockur/windows) ⭐51,727
**Why I starred this:** Run a full Windows VM as a Docker container — with web-based RDP access. It auto-downloads the Windows ISO, configures drivers, and boots into a fully functional Windows desktop accessible from any browser. It's the fastest way to spin up a Windows environment for testing or legacy apps, and it's dramatically simpler than manually setting up a VM.

### 2. [microsoft/PowerToys](https://github.com/microsoft/PowerToys) ⭐122,000
**Why I starred this:** Microsoft's own collection of power-user utilities — FancyZones (window management), PowerRename (batch file renaming), Color Picker, Image Resizer, Keyboard Manager, and 20+ more. It's the first thing I install on any Windows machine. The fact that Microsoft ships this as open-source is genuinely admirable.

### 3. [ventoy/Ventoy](https://github.com/ventoy/Ventoy) ⭐76,000
**Why I starred this:** Create a multi-boot USB drive by simply copying ISO files onto it — no reformatting, no flashing tools. Drag and drop Windows, Linux, and rescue ISOs onto one USB stick and Ventoy boots them all. It's saved me from carrying around a dozen USB drives. Pure utility perfection.

### 4. [valinet/ExplorerPatcher](https://github.com/valinet/ExplorerPatcher) ⭐35,000
**Why I starred this:** Restore the Windows 10 taskbar, Start menu, and File Explorer on Windows 11. Microsoft's forced UI changes drove thousands of power users to this tool — it brings back the functionality that Windows 11 removed while keeping the 11 kernel improvements. It's community-driven defiance against unwanted UI changes.

### 5. [ChrisTitusTech/winutil](https://github.com/ChrisTitusTech/winutil) ⭐35,000
**Why I starred this:** A comprehensive PowerShell utility that automates Windows setup — debloating, driver installation, privacy tweaks, software installation, and system optimization, all from a single TUI. It's the "fresh Windows install in 30 minutes instead of 3 hours" tool. The curated software installer alone saves enormous time.

### 6. [jart/cosmopolitan](https://github.com/jart/cosmopolitan) ⭐20,000
**Why I starred this:** Build C programs that run natively on Linux, macOS, Windows, FreeBSD, OpenBSD, and NetBSD — from a single binary. The "Actually Portable Executable" format is a technical marvel: one file, zero dependencies, runs everywhere. It's the kind of mad-scientist engineering that makes open source magical.

### 7. [microsoft/wslg](https://github.com/microsoft/wslg) ⭐11,000
**Why I starred this:** Run Linux GUI applications natively on Windows through WSL 2 — with GPU acceleration, audio, and seamless integration. You can run GIMP, Nautilus, or any X11/Wayland app and it appears as a native window. It turns Windows into the best Linux desktop (controversial take, but WSLg makes it plausible).

### 8. [quickemu-project/quickemu](https://github.com/quickemu-project/quickemu) ⭐13,000
**Why I starred this:** One-command virtual machines on Linux — `quickget windows 11 && quickemu --vm windows-11.conf` and you have a fully optimized Windows VM with GPU passthrough, USB redirection, and shared folders. It wraps QEMU's complexity into a simple interface. For Linux users who occasionally need Windows, this is the fastest path.

### 9. [winapps-org/winapps](https://github.com/winapps-org/winapps) ⭐9,000
**Why I starred this:** Run individual Windows applications on Linux as if they were native — each app gets its own window via RDP, integrated into your Linux desktop. It's the "I need Outlook and nothing else from Windows" solution. The seamless window integration (rather than a full remote desktop) makes it feel natural.

### 10. [lassekongo83/adw-gtk3](https://github.com/lassekongo83/adw-gtk3) ⭐3,000
**Why I starred this:** A GTK3 theme that matches the modern libadwaita look, making older GTK3 applications look consistent with modern GNOME apps. If you've ever used a Linux desktop where some apps look 10 years older than others, this theme fixes that visual inconsistency. It's a small detail that dramatically improves the desktop experience.

---

## 📦 General Platforms & Suites — Top 10

### 1. [twentyhq/twenty](https://github.com/twentyhq/twenty) ⭐50,379
**Why I starred this:** An open-source Salesforce alternative — CRM, customer data, workflows, and automation in a modern React/GraphQL stack. It's not just a clone; it's a rethinking of what a CRM should look like in 2026, with an extensible data model, GraphQL API, and a beautiful UI. I star it as both a useful tool and a reference architecture for enterprise-grade open-source.

### 2. [plausible/analytics](https://github.com/plausible/analytics) ⭐23,000
**Why I starred this:** Privacy-first, lightweight web analytics that's self-hostable. No cookies, no tracking, GDPR-compliant by default — yet the dashboard tells me everything I actually need (pageviews, sources, countries, devices). It's the analytics I install on every project. The simple setup (`docker compose up`) and clean UI make Google Analytics feel bloated.

### 3. [directus/directus](https://github.com/directus/directus) ⭐33,000
**Why I starred this:** Wrap any SQL database in a REST+GraphQL API with an admin panel — instantly. Connect to an existing database and Directus auto-discovers the schema, builds a CMS interface, and generates APIs. It's the fastest way to put a headless CMS in front of any database. The role-based access control and webhooks make it production-ready.

### 4. [medusajs/medusa](https://github.com/medusajs/medusa) ⭐31,000
**Why I starred this:** Shopify's open-source alternative — headless commerce with a modular architecture. You compose a commerce backend from pluggable modules (cart, orders, payments, fulfillment) and customize everything. For any project that involves selling things online, Medusa is the foundation that doesn't lock me into a platform or payment processor.

### 5. [calcom/cal.com](https://github.com/calcom/cal.com) ⭐42,000
**Why I starred this:** Calendly's open-source competitor, and honestly better. Self-host scheduling infrastructure with team round-robin, routing forms, video integrations, and a white-label option. The API-first design means scheduling can be embedded anywhere. I use it because I'd rather control my scheduling data than hand it to a SaaS company.

### 6. [baptisteArno/typebot.io](https://github.com/baptisteArno/typebot.io) ⭐10,000
**Why I starred this:** Build conversational forms and chatbots with a visual builder — no code, open-source, self-hostable. It's Typeform + Chatbot builder in one tool. I use it for onboarding flows, surveys, and support bots. The logic branching system is powerful enough for complex flows but simple enough that non-technical teammates can build them.

### 7. [Budibase/budibase](https://github.com/Budibase/budibase) ⭐24,000
**Why I starred this:** Build internal tools and business apps visually — connect to databases, APIs, or Google Sheets and drag-and-drop forms, tables, and charts. It's the open-source Retool alternative. When someone says "can you build me a quick CRUD app for tracking X," Budibase is my answer — it turns weeks of work into hours.

### 8. [ToolJet/ToolJet](https://github.com/ToolJet/ToolJet) ⭐36,000
**Why I starred this:** Another open-source low-code platform for internal tools, with a strong focus on extensibility — JavaScript/Python code blocks, custom components, and a marketplace. It connects to 50+ data sources and the UI builder is intuitive. It's the internal tool builder I recommend when Budibase doesn't have the right connector.

### 9. [illacloud/illa-builder](https://github.com/illacloud/illa-builder) ⭐15,000
**Why I starred this:** A Retool-like low-code builder with real-time collaboration and drag-and-drop UI. It's fast (Go backend, React frontend), supports every major database, and has an AI assistant that can generate components from natural language. The collaboration features (multiple builders editing simultaneously) make it ideal for teams.

### 10. [appsmithorg/appsmith](https://github.com/appsmithorg/appsmith) ⭐37,000
**Why I starred this:** The most popular open-source internal tool builder. Connect to any data source, build UIs with drag-and-drop widgets, write JavaScript anywhere, and deploy. It has the largest community and most integrations of any tool in this category. For serious internal tooling that needs to be maintained long-term, Appsmith has the ecosystem to support it.

---

## ❓ Unique & Niche — Top 10

### 1. [remoteintech/remote-jobs](https://github.com/remoteintech/remote-jobs) ⭐40,478
**Why I starred this:** A massive, community-maintained list of companies that hire remotely — with tech stacks, regions, and benefits. It's not a job board; it's a curated directory of "here's who hires remotely and what they use." I star it because it represents the future of work and is genuinely useful when job hunting.

### 2. [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) ⭐240,000
**Why I starred this:** The definitive catalog of self-hosted software — from analytics to wikis, from password managers to pastebins. It's how I discover new services to run in my homelab, and it's the list I send to anyone curious about self-hosting. The categorization and tagging make it easy to find alternatives to any SaaS product.

### 3. [tldr-pages/tldr](https://github.com/tldr-pages/tldr) ⭐56,000
**Why I starred this:** Simplified, community-driven man pages with practical examples. Instead of `man tar` and parsing 5,000 words, `tldr tar` shows the 10 most common use cases with clear examples. It's the documentation format that respects your time. I've contributed pages and it's one of the most satisfying open-source projects to help with.

### 4. [charmbracelet/vhs](https://github.com/charmbracelet/vhs) ⭐18,000
**Why I starred this:** Write terminal GIFs as code. Define a script of what to type, wait for, and screenshot, and VHS renders a perfect terminal recording as a GIF. It's how I create documentation GIFs, bug report demos, and README animations. The declarative approach (write a .tape file) means you can version-control your terminal demos.

### 5. [charmbracelet/glow](https://github.com/charmbracelet/glow) ⭐21,000
**Why I starred this:** Read Markdown files beautifully in the terminal — with syntax highlighting, word wrapping, and navigation. `glow README.md` and you get a paginated, styled view that's better than reading it on GitHub. I use it to read project documentation, TIL notes, and even my own writing. It makes the terminal feel like a reading environment.

### 6. [orhun/git-cliff](https://github.com/orhun/git-cliff) ⭐12,000
**Why I starred this:** Generate changelogs from conventional commits — with templates, grouping, and GitHub/GitLab integration. It reads your git history, categorizes commits (feat, fix, chore), and produces a beautiful, structured CHANGELOG.md. It's the CHANGELOG generator that actually works the way I want — configurable templates, scope grouping, and footer links.

### 7. [asdf-vm/asdf](https://github.com/asdf-vm/asdf) ⭐24,000
**Why I starred this:** Manage all your runtime versions (Node, Python, Go, Rust, Ruby, Terraform, etc.) with one tool. One `.tool-versions` file, one command (`asdf install`), and every project gets the exact versions it needs. It replaced nvm, pyenv, rbenv, and a dozen other version managers in my workflow. The plugin ecosystem covers everything.

### 8. [jdx/mise](https://github.com/jdx/mise) ⭐17,000
**Why I starred this:** The evolution of asdf — same version management concept, but written in Rust (faster), with a task runner, environment variable management, and direnv integration built in. It's asdf + direnv + make, unified. I migrated from asdf to mise and haven't looked back. The `mise.toml` file in every project is a single source of truth for tooling.

### 9. [sharkdp/hyperfine](https://github.com/sharkdp/hyperfine) ⭐26,000
**Why I starred this:** Command-line benchmarking that's scientifically rigorous. Run commands multiple times, automatically detect outliers, calculate statistics, and show progress. `hyperfine 'rg pattern' 'grep -r pattern .'` tells me exactly how much faster ripgrep is. It's the tool that turns "I think this is faster" into "this is 4.7x faster with a 95% confidence interval."

### 10. [simonw/llm](https://github.com/simonw/llm) ⭐8,000
**Why I starred this:** Access LLMs from the command line — OpenAI, Claude, Gemini, local models, anything. `llm "summarize this code" < file.py` or `cat log.txt | llm "find the error"`. It's the Unix pipe for AI: simplest possible interface, composable with everything else. I use it dozens of times a day for quick questions, code explanations, and text transformations. The plugin system means it works with every model I care about.

---

## 🏆 The "If I Could Only Keep 10" List

If I had to rebuild from scratch with only 10 tools from these stars — one per major domain:

| # | Repo | Category | Why |
|---|------|----------|-----|
| 1 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | Agentic Dev | The agent I actually live in |
| 2 | [coollabsio/coolify](https://github.com/coollabsio/coolify) | Homelab | Deploys everything else |
| 3 | [immich-app/immich](https://github.com/immich-app/immich) | Media | The app my family cares about |
| 4 | [jesseduffield/lazydocker](https://github.com/jesseduffield/lazydocker) | Docker | Ops without the pain |
| 5 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | AI/LLM | The engine that runs everything else locally |
| 6 | [junegunn/fzf](https://github.com/junegunn/fzf) | Terminal | Changes how you use the command line — muscle memory |
| 7 | [supabase/supabase](https://github.com/supabase/supabase) | Databases | The open-source backend that makes projects possible |
| 8 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | Automation | Connects everything I run to everything else |
| 9 | [dani-garcia/vaultwarden](https://github.com/dani-garcia/vaultwarden) | Security | My family's digital safety, self-hosted |
| 10 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | Dev Resources | The curriculum that taught me how things actually work |

---

*From [pvnkmnk's stars](https://github.com/pvnkmnk) · Curated with [star-guide pipeline](https://github.com/pvnkmnk/star-guide)*
