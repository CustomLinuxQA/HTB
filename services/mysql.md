#### запуск 
mysql -u root -h 10.129.166.152

где после ключа -u идет имя пользователя
чтобы отобразить все что находится внутри таблицы используют ключ *

#### список баз данных
show databases;

#### перейти в базу данных htb
use htb;

#### вывод таблиц
show tables;

#### выбор таблицы config
SELECT * from config;

#### комментирование строки в MySQL
(#)


каждый запрос в mysql должен закачиваться знаком ;
работает на порту 3306
