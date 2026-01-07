---
tags: [htb, privesc, docker, wsl2]
---

# Privilege Escalation

## Стартовая точка
- user: www-data
- environment: Docker container

## Docker API
- Обнаружен Docker API без аутентификации
- Endpoint: 192.168.65.7:2375
- Docker Desktop (Windows + WSL2)

## Эксплуатация
- Создан контейнер с bind mount:
  - /mnt/host/c → C:\ хоста
- Контейнер читает root.txt

## Итог
- Получен доступ к файловой системе Windows host
- root.txt извлечён без shell на хосте
