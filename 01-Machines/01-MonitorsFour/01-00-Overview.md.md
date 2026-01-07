---
tags: [htb, machine, web, docker, windows]
difficulty: easy
os: windows
status: done
ip: 10.10.11.98
---

# MonitorsFour — Overview

## Entry points
- Web: http://monitorsfour.htb
- Subdomain: http://cacti.monitorsfour.htb
- Service: Docker API (internal)

## High-level chain
1) Recon: Web + subdomain enumeration
2) Foothold: Cacti RCE → Docker container
3) PrivEsc: Docker API (2375) → WSL2 → host filesystem

## Flags
- user.txt — container
- root.txt — host (Windows)


## Links
- [[01-01-Timeline]]
- [[01-02-Recon]]
- [[01-03-Exploitation]]
- [[01-04-PrivilegeEsc]]
- [[01-90-Commands]]
- [[01-99-LessonsLearned]]