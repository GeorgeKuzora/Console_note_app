from datetime import datetime
from lib import Note


class UserInput:
    USER_MESSAGES = {
        "title": "Введите заголовок заметки: ",
        "body": "Введите текст заметки: ",
        "start": "Введите начальную дату: ",
        "end": "Введите конечную дату: ",
    }
    DATETIME_FORMAT = "%Y-%m-%d"

    def __init__(self) -> None:
        self.note_title = ""
        self.note_body = ""
        self.start_date = datetime(1900, 1, 1, 0, 0, 0, 0)
        self.end_date = datetime(9999, 1, 1, 0, 0, 0, 0)

    def setUserInput(self, message: str = "") -> str:
        user_str = input(message)
        return user_str

    def setTitle(self) -> None:
        self.note_title = self.setUserInput(self.USER_MESSAGES["title"])

    def setBody(self) -> None:
        self.note_body = self.setUserInput(self.USER_MESSAGES["body"])

    def setDates(self) -> None:
        start = self.setUserInput(self.USER_MESSAGES["start"])
        end = self.setUserInput(self.USER_MESSAGES["end"])
        self.start_date = self.convertToDatetime(start)
        self.end_date = self.convertToDatetime(end)

    def convertToDatetime(self, str_date: str) -> datetime:
        date = datetime.strptime(str_date, self.DATETIME_FORMAT)
        return date


class ConsolePrinter:
    DATETIME_FORMAT = "%Y-%m-%d"

    @classmethod
    def printNewNoteMessage(cls) -> None:
        print("Ввод заголовка и текста новой заметки")

    @classmethod
    def printChangeNoteMessage(cls) -> None:
        print("Ввод заголовка и текста редактируемой заметки")

    @classmethod
    def printDatesInputMessage(cls) -> None:
        print("Ввод начальной и конечной даты в формате год-месяц-день")

    @classmethod
    def printFindNotesMessage(cls) -> None:
        print("Ввод названия заметки для поиска")

    @classmethod
    def printFindOriginalNote(cls) -> None:
        print("Ввод названия заметки для изменения")

    @classmethod
    def printFindNoteForDeletion(cls) -> None:
        print("Ввод названия заметки для удаления")

    @classmethod
    def printDeleteMessage(cls):
        print("Заметки были удалены")

    @classmethod
    def printListOfNotes(cls, ListOfNotes: list[dict]) -> None:
        print("---")
        for n in ListOfNotes:
            cls.printNote(n)
            print("---")

    @classmethod
    def printNote(cls, note: dict) -> None:
        print(note["note_title"])
        print()
        print(note["note_body"])
        print()
        print(f"Заметка создана: {cls.formatDatetime(note['note_creation_dt'])}")
        print(
            f"Заметка отредактирована: {cls.formatDatetime(note['note_last_modification_dt'])}"
        )

    @classmethod
    def formatDatetime(cls, date_str: str) -> str:
        date = datetime.strptime(date_str, Note.NOTE_DT_FORMAT)
        date = date.strftime(cls.DATETIME_FORMAT)
        return date

    @classmethod
    def printHelp(cls):
        print(
            """
Доступные команды:
    add - Создать новую заметку
    all - Посмотреть все заметки
    show - Вывести текст заметки на экран введя заголовок заметки
    change - Изменить заметку введя заголовок заметки
    delete - Удалить заметку
    date - Посмотреть заметки в интервале дат создания
"""
        )
