# 🔍 Deep-Dive: Specialized Tools from My Stars

> Reverse Proxy · Monitoring · Backup · Secrets · CI/CD
> [pvnkmnk](https://github.com/pvnkmnk) · 2026-06-18

---

## 🔀 Reverse Proxy

*Routing traffic, SSL termination, tunneling, and secure access.*

| Repo | ⭐ | Lang | Why I starred |
|------|-----|------|---------------|
| [traefik/traefik](https://github.com/traefik/traefik) | 63,675 | Go | **The gold standard.** Cloud-native reverse proxy that auto-discovers Docker containers and Kubernetes services. Auto-SSL via Let's Encrypt, middleware chaining, dashboard, metrics. This is what runs my entire homelab's ingress. |
| [fosrl/pangolin](https://github.com/fosrl/pangolin) | 21,286 | TypeScript | **Identity-aware VPN + reverse proxy hybrid.** WireGuard-based remote access that combines VPN tunneling with reverse proxy logic. Gives you access to internal services without opening ports — identity-based, not IP-based. |
| [linuxserver/docker-swag](https://github.com/linuxserver/docker-swag) | 3,680 | Dockerfile | **Nginx + Certbot + fail2ban in one container.** The easiest way to get production-grade reverse proxy with auto-SSL and intrusion prevention. Perfect for homelabs that need the simplicity of one container. |
| [yusing/godoxy](https://github.com/yusing/godoxy) | 3,330 | Go | **High-performance reverse proxy built for self-hosters.** Container-aware, auto-discovers services via Docker labels, built-in dashboard, health checks. Like Traefik but simpler and purpose-built for home servers. |
| [ChrispyBacon-dev/DockFlare](https://github.com/ChrispyBacon-dev/DockFlare) | 2,191 | Python | **Cloudflare Tunnels via Docker labels.** Add `dockflare.tunnel: myapp` to a container and it auto-creates a secure Cloudflare Tunnel with SSL. Zero manual Cloudflare config. |
| [IAmStoxe/wirehole](https://github.com/IAmStoxe/wirehole) | 4,959 | — | **WireGuard + Pi-hole + Unbound in one compose.** Full VPN with ad blocking and DNS privacy. Not a proxy per se, but the most elegant way to secure all your traffic. |
| [Gouryella/drip](https://github.com/Gouryella/drip) | 667 | Go | **Self-hosted tunneling without third-party servers.** Expose localhost securely with unlimited bandwidth. No Cloudflare, no ngrok — just your own relay. |
| [gosuda/portal-tunnel](https://github.com/gosuda/portal-tunnel) | 259 | Go | **Agentic web tunnel.** Publishes localhost services through self-hostable trustless relays with x402 payments support. Built for the agent-native world. |
| [NOXCIS/Wiregate](https://github.com/NOXCIS/Wiregate) | 611 | Vue | **AmneziaWG + WireGuard VPN with Web UI.** Plus TOR + DnsCrypt + Pi-hole + AdGuard. The kitchen-sink VPN solution with a management UI. |
| [alangrainger/immich-public-proxy](https://github.com/alangrainger/immich-public-proxy) | 1,976 | JavaScript | **Secure Immich photo sharing.** Share photos publicly without exposing your Immich instance. Purpose-built reverse proxy for a specific app — a pattern worth copying. |

### Recommendation Stack
- **Production:** Traefik (edge router) + DockFlare (Cloudflare tunnels for external)
- **Home lab:** Godoxy or SWAG (simpler, one-container)
- **Remote access:** Pangolin (identity-aware) or drip (raw tunnel)

---

## 📊 Monitoring & Observability

*Logs, metrics, dashboards, alerts, and uptime tracking.*

### Full-Stack Observability
| Repo | ⭐ | Lang | Why I starred |
|------|-----|------|---------------|
| [netdata/netdata](https://github.com/netdata/netdata) | 79,294 | C | **Instant real-time monitoring for everything.** One command installs an agent that auto-discovers every service, collects thousands of metrics per second, and gives you drag-and-drop dashboards. Zero configuration. The best first monitoring tool for any server. |
| [SigNoz/signoz](https://github.com/SigNoz/signoz) | 27,378 | TypeScript | **Open-source DataDog alternative.** OpenTelemetry-native: logs, traces, and metrics in one platform. When you outgrow netdata and need distributed tracing across services, this is it. |

### Logs & Alerts
| Repo | ⭐ | Lang | Why I starred |
|------|-----|------|---------------|
| [amir20/dozzle](https://github.com/amir20/dozzle) | 13,314 | Go | **Realtime Docker log viewer.** Fuzzy search, auto-scroll, multi-host support. Instead of `docker logs -f` per container, all logs in one browser tab. So light you forget it's there. |
| [clemcer/LoggiFly](https://github.com/clemcer/LoggiFly) | 1,741 | Python | **Alert on Docker log patterns.** Watches container logs for errors/warnings, sends Discord/Slack/Telegram pings. The "you'll know something's wrong before your users do" tool. |
| [komari-monitor/komari](https://github.com/komari-monitor/komari) | 5,036 | Go | **Simple server monitor.** Lightweight health checks and status dashboard. No Prometheus complexity — just "is it up?" for when that's all you need. |

### Dashboards & Status Pages
| Repo | ⭐ | Lang | Why I starred |
|------|-----|------|---------------|
| [glanceapp/glance](https://github.com/glanceapp/glance) | 35,221 | Go | **Single-page feed aggregator.** RSS, Reddit, YouTube, HN, weather, stocks, Docker status — all in one self-hosted page. Your information radiator. |
| [MauriceNino/dashdot](https://github.com/MauriceNino/dashdot) | 3,468 | TypeScript | **Modern, beautiful server dashboard.** CPU, RAM, storage, network — presented gorgeously. Perfect for a TV-mounted status display. |
| [AnthonyGress/lab-dash](https://github.com/AnthonyGress/lab-dash) | 457 | TypeScript | **Dashboard for homelab apps and services.** Manage and monitor everything from one interface. |
| [mostafa-wahied/portracker](https://github.com/mostafa-wahied/portracker) | 2,197 | JavaScript | **Real-time port monitoring and discovery.** See what's listening on what port, catch unexpected services, track changes. |

### Change Detection
| Repo | ⭐ | Lang | Why I starred |
|------|-----|------|---------------|
| [dgtlmoon/changedetection.io](https://github.com/dgtlmoon/changedetection.io) | 32,052 | Python | **Track website changes.** Price drops, restock alerts, content changes, defacement monitoring. Replace a dozen "is it in stock?" browser tabs with one self-hosted tool. |
| [firecrawl/open-scouts](https://github.com/firecrawl/open-scouts) | 1,283 | TypeScript | **AI-powered web monitoring.** Automated scouts that search the web and email alerts. Next-gen change detection with LLM intelligence. |

### Remote & Agent Monitoring
| Repo | ⭐ | Lang | Why I starred |
|------|-----|------|---------------|
| [Ylianst/MeshCentral](https://github.com/Ylianst/MeshCentral) | 6,735 | HTML | **Complete remote monitoring and management.** Web-based RMM with agent install, remote desktop, and device management. Think TeamViewer but self-hosted and with a full fleet management dashboard. |
| [builderz-labs/mission-control](https://github.com/builderz-labs/mission-control) | 5,353 | TypeScript | **AI agent orchestration dashboard.** Monitor agent spend, dispatch tasks, run multi-agent workflows. The observability layer for your AI workforce. |
| [agentseal/agentseal](https://github.com/getagentseal/agentseal) | 287 | Python | **Security monitoring for AI agents.** Scan for dangerous skills/MCP configs, monitor for supply chain attacks, audit MCP servers. The security observability layer for the agent era. |

### Recommendation Stack
- **Quick start:** netdata (auto-everything) + dozzle (logs)
- **Growing:** + glance (dashboards) + changedetection.io (web monitoring)
- **Production:** SigNoz (full APM) + LoggiFly (alerting) + MeshCentral (remote management)

---

## 💾 Backup & Restore

*Data protection, sync, snapshots, and disaster recovery.*

| Repo | ⭐ | Lang | Why I starred |
|------|-----|------|---------------|
| [tmux-plugins/tmux-resurrect](https://github.com/tmux-plugins/tmux-resurrect) | 12,857 | Shell | **Save and restore tmux sessions across restarts.** Not file backup per se, but this has saved my development state more times than any backup tool. Full layout, panes, running programs — all restored. |
| [remotely-save/remotely-save](https://github.com/remotely-save/remotely-save) | 7,673 | TypeScript | **Obsidian sync using your own storage.** S3, Dropbox, OneDrive, WebDAV — pick your backend, own your data. The bridge between local-first notes and multi-device access. |
| [beclab/Olares](https://github.com/beclab/Olares) | 4,858 | Go | **Self-hosted private cloud OS.** Includes backup/snapshot capabilities as part of a full home server platform. Think of it as the "appliance" approach — everything in one box. |
| [AlpinDale/parsync](https://github.com/AlpinDale/parsync) | 606 | Rust | **Parallel rsync with resume over SSH.** When you need to move large amounts of data fast and reliably. The tool you reach for when rsync is too slow and you want checkpoint/resume. |
| [kenn-io/msgvault](https://github.com/kenn-io/msgvault) | 1,832 | Go | **Archive and search lifetime email/chat history.** Powered by DuckDB for offline, full-text search across your entire message history. A different kind of backup — preserving communication history. |
| [timvw/tmux-assistant-resurrect](https://github.com/timvw/tmux-assistant-resurrect) | 55 | Shell | **Persist and restore AI coding sessions across tmux restarts.** Claude Code, OpenCode, Codex CLI, Pi — saves agent context so you can pick up where you left off. |
| [DoliCloud/SellYourSaas](https://github.com/DoliCloud/SellYourSaas) | 286 | PHP | **SaaS management with built-in backup.** Automated deployment, customer management, billing — and automated backup/supervision. |

### Gaps in My Stars
> **What I'm missing:** I don't have the classic backup tools starred — borg, restic, duplicati, kopia, velero. These are all excellent but I apparently discover them when I need them rather than starring them. If I were building a backup strategy from my stars, I'd pair parsync (for bulk sync) with a proper snapshot tool from outside my stars list (e.g., borgbackup for deduplicated encrypted backups).

---

## 🔐 Secrets Management

*Protecting credentials, API keys, environment variables, and sensitive config.*

| Repo | ⭐ | Lang | Why I starred |
|------|-----|------|---------------|
| [gitleaks/gitleaks](https://github.com/gitleaks/gitleaks) | 27,767 | Go | **Find secrets before you commit them.** Pre-commit hook + CI scanning that catches API keys, tokens, passwords before they hit your repo. The first line of defense — and it's caught me more times than I'd like to admit. |
| [onecli/onecli](https://github.com/onecli/onecli) | 2,392 | TypeScript | **Open-source credential gateway with built-in vault.** Give AI agents access to services without exposing raw keys. The agent-native approach to credential management. |
| [Infisical/agent-vault](https://github.com/Infisical/agent-vault) | 1,694 | Go | **HTTP credential proxy and vault for AI agents.** Designed specifically for Claude Code, OpenClaw, Hermes, and custom agent harnesses. Agents request credentials via a proxy — never see the raw keys. |
| [botiverse/agent-vault](https://github.com/botiverse/agent-vault) | 414 | TypeScript | **Keep secrets hidden from AI agents.** A vault purpose-built for the agent era. Different philosophy from Infisical but same problem: agents shouldn't have raw access to secrets. |
| [illarion/lockenv](https://github.com/illarion/lockenv) | 282 | Go | **Simple encrypted vault for .env files.** Like git-crypt or sops but dramatically simpler. Password-based encryption for .env and infrastructure secrets. Perfect for small teams and IaC workflows. |
| [hashicorp/terraform](https://github.com/hashicorp/terraform) | 48,735 | Go | **Infrastructure as Code with secrets handling.** Terraform's state management and variable system is the de facto standard for managing infrastructure secrets declaratively. |

### Recommendation Stack
- **Pre-commit:** gitleaks (catch secrets before they leak)
- **Agent secrets:** Infisical/agent-vault or onecli (agent-native credential proxy)
- **Config secrets:** lockenv (encrypt .env files) or sops (more features)
- **Infrastructure:** Terraform + Terraform MCP Server (IaC with secret management)

---

## 🚀 CI/CD & Automation

*Pipelines, infrastructure as code, deployment automation.*

### Infrastructure as Code
| Repo | ⭐ | Lang | Why I starred |
|------|-----|------|---------------|
| [ansible/ansible](https://github.com/ansible/ansible) | 68,985 | Python | **The universal automation language.** SSH-based, agentless, with modules for everything. I use it to provision servers, configure services, and enforce desired state. The lingua franca of homelab automation. |
| [hashicorp/terraform](https://github.com/hashicorp/terraform) | 48,735 | Go | **Declarative infrastructure as code.** Provision cloud resources, DNS records, even homelab VMs. Combined with Ansible, this forms the complete "provision + configure" pipeline. |
| [hashicorp/terraform-mcp-server](https://github.com/hashicorp/terraform-mcp-server) | 1,439 | Go | **Terraform for AI agents.** MCP server that lets coding agents interact with Terraform — plan, apply, validate. Agents can now manage infrastructure. |

### CI/CD Runners
| Repo | ⭐ | Lang | Why I starred |
|------|-----|------|---------------|
| [nektos/act](https://github.com/nektos/act) | 70,821 | Go | **Run GitHub Actions locally.** Test workflows before pushing, iterate fast without committing. The development loop for Actions — run `act` instead of `git push && wait`. |
| [semaphoreui/semaphore](https://github.com/semaphoreui/semaphore) | 13,769 | Go | **Modern UI for Ansible, Terraform, and other DevOps tools.** Visual pipeline builder, scheduled runs, access control. Turns Ansible from a CLI tool into a team platform. |
| [docker/docker-agent](https://github.com/docker/docker-agent) | 3,089 | Go | **AI Agent Builder by Docker.** Agents as containerized workloads in your CI/CD pipeline. Build → test → deploy with AI-native tooling from Docker themselves. |

### Deployment Platforms
| Repo | ⭐ | Lang | Why I starred |
|------|-----|------|---------------|
| [dokku/dokku](https://github.com/dokku/dokku) | 31,947 | Shell | **Heroku-style `git push` deploys on your own server.** The simplest PaaS workflow: `git push dokku main` and your app is live with SSL. My go-to for deploying side projects without Kubernetes complexity. |
| [psviderski/uncloud](https://github.com/psviderski/uncloud) | 5,237 | Go | **Lightweight Docker orchestration.** Bridges the gap between `docker-compose` and full Kubernetes. Perfect for the homelab that needs more than compose but less than K8s. |
| [sdogruyol/cryload](https://github.com/sdogruyol/cryload) | 211 | Crystal | **HTTP load testing with CI/CD-friendly output.** Machine-readable JSON reports that plug into pipeline quality gates. Modern ab/wrk alternative. |
| [DaKheera47/job-ops](https://github.com/DaKheera47/job-ops) | 3,355 | TypeScript | **DevOps principles for job hunting.** A creative application of CI/CD patterns to a non-engineering problem. Track, analyze, and automate your job search pipeline. |

### AI Agent Orchestration (as CI/CD)
| Repo | ⭐ | Lang | Why I starred |
|------|-----|------|---------------|
| [openclaw/lobster](https://github.com/openclaw/lobster) | 1,230 | TypeScript | **Workflow shell for AI agents.** Turns skills and tools into composable pipelines. The CI/CD metaphor applied to agent task orchestration. |
| [caliber-ai-org/ai-setup](https://github.com/caliber-ai-org/ai-setup) | 1,141 | TypeScript | **Continuously sync AI setups with one command.** Codebase-tailored agent skills, MCP configs, and config files. CI/CD for your agent development environment. |

### Recommendation Stack
- **IaC:** Terraform (provision) + Ansible (configure)
- **CI Runner:** act (local Actions testing) + semaphore (Ansible/Terraform pipeline UI)
- **Deploy:** dokku (simple apps) or uncloud (orchestrated containers)
- **Agent-native:** Terraform MCP Server + lobster (agent pipelines)

---

## 📋 Quick Reference: Tools I'm Actually Using

| Layer | Tool | Role |
|-------|------|------|
| **Ingress** | Traefik + DockFlare | Reverse proxy + Cloudflare tunnels |
| **Monitor** | netdata + dozzle | Metrics + logs |
| **Backup** | (borg/restic — need to add) | Offsite encrypted snapshots |
| **Secrets** | gitleaks + lockenv | Pre-commit scanning + .env encryption |
| **CI/CD** | act + terraform + dokku | Workflow testing + IaC + deployment |

---

*From [pvnkmnk's stars](https://github.com/pvnkmnk) via [star-guide pipeline](https://github.com/pvnkmnk/star-guide)*
