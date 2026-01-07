---
tags: [htb, recon, web]
---

# Recon

## Network
- 80/tcp — HTTP
- 5985/tcp — WinRM

## Web
- PHPSESSID → PHP backend
- Пути: /login, /user, /views, /controllers
- Старый admin frontend в /static/admin

## Subdomains
- cacti.monitorsfour.htb (302)
