#### подключение по ftp
ftp -4 (ip addres)
Name: anonymous
Password: <empty>

**ftp** - программа пересылки файлов, позволяет пользователю передавать файлы на другой компьютер сети и получать их из него.

#### скачать файл с сервера
get my-file.txt

Получает **удаленный_файл** и сохраняет его на локальной машине. Если имя локального файла не указано, он получает то же имя, что и на удаленной машине, с учетом изменений, вызванных текущими установками [**case**](https://www.opennet.ru/man.shtml?topic=ftp&category=1&russian=0#case), [**ntrans**](https://www.opennet.ru/man.shtml?topic=ftp&category=1&russian=0#ntrans) и [**nmap**](https://www.opennet.ru/man.shtml?topic=ftp&category=1&russian=0#nmap). При передаче файла используются текущие значения типа, формата, режима и структуры.

#### загрузить файл на сервер
cd uploads
put /home/capitan/my-file.txt