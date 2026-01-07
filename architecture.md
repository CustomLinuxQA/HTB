# Obsidian vault: HTB-KB

## 0) Принципы
- 1 машина = 1 папка в /Machines
- Любой новый "кусок знаний" (уязвимость/техника/инструмент) = отдельная заметка в /KB
- В каждой машине: Timeline (что делал) + Evidence (артефакты) + Hypotheses (гипотезы)
- Подсказки из интернета не скрываем: фиксируем как "Hint" с ссылкой и что именно это разблокировало.

---

## 1) Структура папок

HTB-KB/
├─ 00-Inbox/                       # быстрые черновики, потом раскидываешь
├─ 01-Machines/
│  ├─ MonitorsFour/                # пример
│  │  ├─ 00-Overview.md
│  │  ├─ 01-Timeline.md
│  │  ├─ 02-Recon.md
│  │  ├─ 03-Exploitation.md
│  │  ├─ 04-PrivilegeEsc.md
│  │  ├─ 90-Commands.md
│  │  ├─ 99-LessonsLearned.md
│  │  └─ evidence/                 # файлы/скрины/выводы команд (если надо)
│  └─ ...
├─ 02-Playbooks/                   # пошаговые чеклисты по направлениям
│  ├─ Web-Checklist.md
│  ├─ Linux-PrivEsc-Checklist.md
│  ├─ Windows-PrivEsc-Checklist.md
│  ├─ Containers-Docker-Checklist.md
│  └─ Enumeration-Checklist.md
├─ 03-KB/                          # база знаний (уязвимости/паттерны/техники)
│  ├─ Vulns/
│  │  ├─ LFI.md
│  │  ├─ SSRF.md
│  │  ├─ IDOR.md
│  │  ├─ Auth-Bypass.md
│  │  ├─ File-Upload.md
│  │  ├─ Command-Injection.md
│  │  └─ ...
│  ├─ Misconfig/
│  │  ├─ Docker-API-Unauth.md
│  │  ├─ Exposed-Admin-Panels.md
│  │  ├─ Default-Creds.md
│  │  └─ ...
│  ├─ Tech/
│  │  ├─ WSL2.md
│  │  ├─ JWT.md
│  │  ├─ Reverse-Proxy.md
│  │  └─ ...
│  ├─ Tools/
│  │  ├─ Gobuster.md
│  │  ├─ Feroxbuster.md
│  │  ├─ Nmap.md
│  │  ├─ ffuf.md
│  │  └─ ...
│  └─ Patterns/
│     ├─ Enumerate-Params.md
│     ├─ Pivoting-Basics.md
│     └─ ...
├─ 04-References/                  # ссылки и конспекты статей/видео
│  ├─ Docker/
│  ├─ Web/
│  └─ Windows/
├─ 05-Templates/                   # шаблоны заметок
│  ├─ Machine-Overview.md
│  ├─ KB-Vuln.md
│  ├─ KB-Tool.md
│  └─ Hint.md
└─ 99-Index.md                      # стартовая страница / навигация

---

## 2) Теги (минимально нужные)
#htb #machine #recon #web #linux #windows #privesc #container #docker #wsl2
#vuln/lfi #vuln/ssrf #vuln/idor #misconfig/docker-api #pattern/params
#tool/gobuster #tool/feroxbuster #tool/nmap #hint

---

## 3) Шаблон: 01-Machines/<Machine>/00-Overview.md

---
tags: [htb, machine]
difficulty: easy|medium|hard|insane
os: linux|windows|unknown
status: active|done|stuck
ip: 10.10.x.x
---

# <MachineName> — Overview

## Goal
- user.txt
- root.txt

## Entry points (short)
- Web: http://...
- SSH: ...
- Other: ...

## High-level chain (update as you go)
1) Recon: ...
2) Foothold: ...
3) PrivEsc: ...

## Links
- [[01-Timeline]]
- [[02-Recon]]
- [[03-Exploitation]]
- [[04-PrivilegeEsc]]
- [[90-Commands]]
- [[99-LessonsLearned]]

---

## 4) Шаблон: 01-Timeline.md (самое важное для начинающего)

---
tags: [htb, machine, timeline]
---

# Timeline

> Правило: каждая значимая попытка = запись с временем и результатом.

## YYYY-MM-DD
- 10:00 — Nmap: ... (результат: ...)
- 10:20 — Web enum (ferox/gobuster): ... (нашёл: ...)
- 10:45 — Гипотеза: LFI через параметр `page` (почему думаю так)
- 11:10 — Проверка: ... (итог: не подтвердилось)
- 11:30 — Hint (ссылка): ... (что именно подсказка дала)
- 12:00 — Новый путь: Docker API открыт без auth → ...

---

## 5) Шаблон: KB-уязвимость (03-KB/Vulns/<Vuln>.md)

---
tags: [kb, vuln]
---

# <VulnName>

## 1) Что это (1-2 предложения)
...

## 2) Признаки в реальности (индикаторы)
- ...
- ...

## 3) Как проверить (быстро)
- Request/endpoint:
- Payload ideas:
- Ожидаемый результат:

## 4) Типовые обходы/вариации
- ...

## 5) Эксплуатация (аккуратно, по шагам)
1) ...
2) ...

## 6) Защита (чтобы понимать, почему не работает)
- ...

## 7) Связанные заметки
- [[Playbooks/Web-Checklist]]
- [[Patterns/Enumerate-Params]]

## 8) References
- [link1]
- [link2]

---

## 6) Шаблон: KB-инструмент (03-KB/Tools/<Tool>.md)

---
tags: [kb, tool]
---

# <ToolName>

## Зачем
...

## База: 3 команды, которые реально нужны
```bash
# 1) ...
# 2) ...
# 3) ...
