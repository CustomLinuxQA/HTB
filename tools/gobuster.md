§позволяет одновременно брутфорсить папки и несколько расширений

#### переключатель Gobuster для указания на url, ip, name
-u

#### с помощью перебора каталогов, находим файл php, который предоставит возможность аутентификации в веб-службе
gobuster dir -u 10.129.245.106 -w /usr/share/dirb/wordlists/common.txt -x .php


#### Поиск субдоменов
gobuster vhost -u http://thetoppers.htb -w /usr/share/seclists/Discovery/DNS/subdomains-toplmillion-20000.txt
