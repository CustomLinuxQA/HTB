
#### тип базы данных 
In-memory Database
```
sudo apt-get install redis-tools
```
#### утилита для взаимодействия с сервером Redis
redis-cli

#### флаг для указания имени хоста
-h
redis-cli -h 10.129.150.229 (подключаемся к тачке)

#### команда для получения информации и статистики о сервере Redis
INFO

#### команда для выбора нужной базы данных в Redis
select

#### команда для поиска всех ключей
KEYS *

#### посмотреть значение ключа
get flag (где flag название ключа)
