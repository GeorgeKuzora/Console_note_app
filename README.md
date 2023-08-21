# Консольное приложение для ведения заметок

## Общая информация

### Цель проекта

Целью проекта было создание CLI приложения для создания, изменения, удаления заметок.

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

## Далнейшие планы развития приложения

- Рефакторинг
- Добавление флагов для запуска комманд из командной строки
