# Консольное приложение для ведения заметок

## Общая информация

[Страница проекта](https://georgiykuzora.ru/post/console-note-app/)

### Цель проекта

Цель проекта это разработка CLI приложения для создания, изменения, удаления заметок. Заметки должны храниться в простых текстовых файлах в `json` формате.

Работа над приложением включала в себя:

- Использование принципов Объектно-ориентированного программирования.
- Создание unit-тестов.
- Работа в комманде с другими разработчиками.

### Функции приложения

Приложение поддерживает следующие функции:

- Создание заметки.
- Редактирование заметки.
- Удаление заметки.
- Просмотр содержимого всех заметок.
- Просмотр содержимого заметки по её названию.
- Просмотр содержимого заметок по дате их создания.

### Использованные технологии и инструменты

При создании приложения использовались следующие технологии:

- **Python** - язык на котором написано приложение.
- **unittest** - библиотека для созданя тестов.
- **Json** - формат в котором сохраняются заметки.
- **Neovim** - редактор в котором разрабатывался проект.
- **Jira** - инструмент для организации работы команды проекта.

## Работа с приложением

### Запуск приложения

Приложение запускается командой: `python main.py`.

### Доступные комманды

- add - Создать новую заметку
- all - Посмотреть все заметки
- show - Вывести текст заметки на экран введя заголовок заметки
- change - Изменить заметку введя заголовок заметки
- delete - Удалить заметку
- date - Посмотреть заметки в интервале дат создания

## Описание структуры проекта

Проект размещен в двух директориях:

- `src` - исходный код проекта.
- `tests` - исходный код unit-тестов проекта

### Структура кода проекта

Код проекта разбит на модули:

- `lib.py` - модуль с классами отвечающими за основную логику работы с заметками.
- `lib_cli.py` - модуль для представления информации на CLI интерфейсе.
- `lib_file_system.py` - модуль с логикой записи и доступа к файлам заметок на жестком диске.
- `user_exeptions.py` - модуль с пользовательскими классами исключений.
- `main.py` - точка входа в программу.

Модульная структура позволяет заменять компоненты проекта при необходимости. К примеру если необходимо поменять представление данных или изменить формат хранения и доступа к файлам заметок.

### Структура unit-тестов проекта

Unit-тесты проекта размещены в файлах соответствующих структуре исходного кода:

- `test_lib.py` - unit-тесты для классов отвечающих за основную логику работы с заметками.
- `test_lib_cli.py` - unit-тесты для модуля представления CLI интерфейса.
- `test_lib_file_system.py` - unit-тесты для модуля логики записи и доступа к файлам заметок на жестком диске.

### Архитектура приложения

Приложение имеет `MVC` архитектуру.

Model - это модули `lib.py` и `lib_file_system.py`. В них заключена модель работы с заметками и записи/чтения файлов заметок на жестком диске.

View - это модуль `lib_cli.py`. Это предсталвение данных для пользователя в CLI интерфейсе.

Controller - это файл `main.py`. Он отвечает за логику работы программы и взаимодействие между Model и View.

## Дальнейшие планы развития приложения

- Рефакторинг.
- Добавление флагов для запуска комманд из командной строки.
