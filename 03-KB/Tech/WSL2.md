---
tags: [kb, tech, windows, wsl2, docker]
---

# WSL2 (Windows Subsystem for Linux) — attack surface

## Что это
WSL2 — Linux VM внутри Windows, используемая Docker Desktop и разработчиками.

Для атакующего:
> контейнер → WSL2 → Windows host

## Почему это опасно
- Docker Desktop часто:
  - слушает Docker API во внутренней сети
  - не требует аутентификации
- Контейнеры видят внутреннюю подсеть WSL2
- Файловая система Windows примонтирована в Linux

## Типичная цепочка атаки

Web RCE
↓
Docker container
↓
Docker API (internal)
↓
WSL2
↓
Windows host filesystem


## Ключевые признаки
- IP вида `192.168.65.x`
- Docker Desktop на Windows
- Пути:
  - `/mnt/host/c`
  - `/mnt/c`
- Отсутствие firewall между container ↔ WSL2

## Что можно получить
- Файлы Windows (Users, Desktop)
- Credentials
- root.txt без shell на хосте
- Иногда — persistence

## Почему это работает
- WSL2 — VM, но доверенная
- Docker Desktop ломает изоляцию ради удобства
- Безопасность ≠ приоритет dev-окружений

## Когда проверять
- Windows + Docker
- Контейнерный foothold
- Нет обычного Linux PrivEsc

## Связанные заметки
- [[03-KB/Misconfig/Docker-API-Unauth]]
- [[02-Playbooks/Containers-Docker-Checklist]]