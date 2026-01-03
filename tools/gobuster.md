# Gobuster — быстрый перебор веб-ресурсов

## Что это за тулза

**Gobuster** — CLI-инструмент для перебора (bruteforce) веб-ресурсов:
- виртуальных хостов (vhost / subdomain),
- путей (directories),
- файлов.

---

## Из чего состоит URL

Пример URL:

http://monitorsfour.htb/login.php
│      │                │
│      │                └─ путь / файл
│      └─ host (имя сервера)
└─ протокол

---

## Что мы можем искать с помощью Gobuster

### 1. Хосты (vhost / subdomain)

Например, сервер с IP `10.10.11.98` может обслуживать несколько сайтов:

10.10.11.98
 ├─ monitorsfour.htb
 ├─ admin.monitorsfour.htb
 └─ api.monitorsfour.htb

---

### 2. Пути (directories)

Поиск скрытых или неочевидных директорий:

/login  
/dashboard  
/api/users  

---

### 3. Файлы

Поиск файлов, которые могут содержать логику или чувствительные данные:

/login.php  
/index.html  
/config.json  

---

## Основные режимы и ключи Gobuster

| Что ты хочешь сделать    | Ключ gobuster |
| ------------------------ | ------------- |
| Перебирать пути          | `dir`         |
| Перебирать хосты (сайты) | `vhost`       |
| Указать домен            | `--domain`    |
| Список вариантов         | `-w`          |
| Потоки                   | `-t`          |

---

## Примеры использования

### Перебор виртуальных хостов (vhost)

gobuster vhost -u http://monitorsfour.htb \
  -w /usr/share/dirb/wordlists/common.txt \
  --domain monitorsfour.htb \
  -t 50

Что происходит:
- значения из wordlist подставляются как поддомены
- отправляются HTTP-запросы с разными Host
- ищутся отличающиеся ответы сервера

---

### Перебор директорий и файлов (dir)

gobuster dir -u http://monitorsfour.htb \
  -w /usr/share/dirb/wordlists/common.txt \
  -t 50

Что происходит:
- перебираются пути вида `/admin`, `/login`, `/api`
- анализируются HTTP-коды и размеры ответов

---

## Короткие советы

- Для `vhost` почти всегда нужен `--domain`
- Увеличивай `-t`, если сервер стабильный
- Используй разные wordlist’ы под разные цели (API, PHP, admin)
- Обращай внимание не только на `200`, но и на `301 / 302`
- Размер ответа (`Content-Length`) часто важнее кода

---

## Итог

Gobuster — базовый и обязательный инструмент для:
- первичного ресёрча цели
- поиска скрытых эндпоинтов
- обнаружения виртуальных хостов и админок

Обычно запускается одним из первых.


#### Поиск субдоменов
gobuster vhost -u http://thetoppers.htb -w /usr/share/seclists/Discovery/DNS/subdomains-toplmillion-20000.txt
