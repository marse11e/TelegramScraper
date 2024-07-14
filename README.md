# Telegram Scraper

Этот проект представляет собой скрипт на Python для сбора участников из мегагрупп Telegram и сохранения их в CSV файл.

## Установка

1. Установите необходимые зависимости, запустив скрипт `setup.py`:

   ```bash
   python3 setup.py
   ```

2. Следуйте инструкциям для ввода идентификатора API, хэша API и номера телефона.

## Использование

1. Запустите основной скрипт для сбора участников:

   ```bash
   python3 group_members.py
   ```

2. Следуйте инструкциям для выбора группы и сбора участников.

## Файлы

- `setup.py`: скрипт для установки зависимостей и настройки конфигурационного файла `config.ini`.
- `group_members.py`: основной скрипт для работы с Telegram API, выбора группы и сбора участников.

## Конфигурация

Для работы необходимо указать API_ID, API_HASH и номер телефона в файле `config.ini`, который создается при первом запуске скрипта `setup.py`.

## Лицензия

Можно использовать, изменять и распространять этот код согласно условиям лицензии, указанной в репозитории [LICENSE](LICENSE).

## Автор

Проект разработан и поддерживается MarselleNaz.
