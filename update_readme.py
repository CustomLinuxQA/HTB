import os

# Путь к директориям
base_dir = os.getcwd()  # Текущая директория (из которой запускается скрипт)
services_dir = os.path.join(base_dir, "services")
tools_dir = os.path.join(base_dir, "tools")

# Функция для перечисления файлов
def list_files(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

# Получение списков файлов
services_files = list_files(services_dir)
tools_files = list_files(tools_dir)

# Составляем строки с файлами для каждой директории
services_list = ''.join([f'  - `{file}`\n' for file in services_files])
tools_list = ''.join([f'  - `{file}`\n' for file in tools_files])

# Создание содержимого README.md
readme_content = """\
# Hack The Box Notes

Этот репозиторий содержит полезные заметки и подсказки для работы с различными сервисами и инструментами, которые часто встречаются при решении задач на Hack The Box.

## Структура репозитория

- **services/**: Директория с документами, описывающими особенности различных сервисов:
""" + services_list + """

- **tools/**: Директория с документами, посвящёнными использованию различных инструментов:
""" + tools_list + """

## Как использовать

1. Перейдите в нужную директорию (`services` или `tools`).
2. Выберите файл с описанием сервиса или инструмента, который вам нужен.
3. Ознакомьтесь с информацией и используйте её для решения задач.

## Вклад в проект

Если у вас есть полезные заметки или примеры, которые могут быть полезны другим, не стесняйтесь создавать пул-реквесты или открывать issue.

Удачи в Hack The Box! 💻
"""

# Запись содержимого в README.md
with open(os.path.join(base_dir, "README.md"), "w", encoding="utf-8") as readme_file:
    readme_file.write(readme_content)

print("README.md успешно обновлён!")
