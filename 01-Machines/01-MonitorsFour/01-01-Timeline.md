---
tags: [htb, timeline]
---

# Timeline

## Recon
- Nmap: 80, 5985
- Web enum: feroxbuster
- Subdomain найден через ffuf: cacti.monitorsfour.htb

## Web analysis
- PHP приложение за Nginx
- Endpoint /user возвращает JSON
- Ошибка: Missing token parameter

## IDOR
- token=0 возвращает всех пользователей
- Утечка MD5 хешей паролей

## Foothold
- MD5 crack → marcus:wonderful1
- Логин в Cacti
- Эксплойт CVE-2025-24367 → reverse shell
- Доступ в Docker container

## PrivEsc
- Найден Docker API на 192.168.65.7:2375
- Создан контейнер с bind mount хоста
- Прочитан root.txt с Windows host
