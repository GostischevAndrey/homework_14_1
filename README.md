# Введение в ООП

## Описание проекта
В этом домашнем задании мы начинаем с описания основных сущностей и инициализации объектов.
## Зависимости проекта:
* python = "^3.13"
* flake8 = "^7.1.1"
* black = "^24.10.0"
* isort = "^5.13.2"
* mypy = "^1.14.1"
* pytest = "^8.3.4"
## Модули
1. `utils.py` - утилиты \ чтения файла JSON
2. `category.py` - класс Category 
3. `product.py` - класс Product
4. `main.py` - проверка функций
## Функции, которые мы будем использовать:
* `load_from_json_file` - Загружает данные из файла products.json, находящегося в папке data
* `create_objects_from_json` - Реализует подгрузку данных по категориям и товарам из файла JSON
## Инструкция по установке
1. Чтобы скачать репозиторий:
```commandline
https://github.com/GostischevAndrey/homework_classes
```
2. Установите зависимости
```commandline
poetry shell
```
## Тестирование 
Проект протестирован Pytest

Чтобы запустить тесты с оценкой покрытия выполните команду
```commandline
poetry run pytest --cov
```
Чтобы сгенерировать отчет о покрытии в HTML-формате, где src — пакет c модулями, которые тестируем. 
Отчет будет сгенерирован в папке htmlcov и храниться в файле с названием index.html
.
```commandline
pytest --cov=src --cov-report=html
```
## Команда проекта:
* Гостищев Андрей — Back-End developer
## Контакт для связи с командой разработки:
* pise4kan8@gmail.com
## Источники
Программа создана при поддержке онлайн-школы - SkyPro - skypro@skyeng.ru