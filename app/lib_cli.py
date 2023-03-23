from datetime import datetime


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

    # Выводит в консоль вопрос к пользователю, что он хочет
    @classmethod
    def initialMessage(cls):
        print("\n".join(cls.INIT_MSG_CONTENT))

    # Вызывает метод, соответствующий выбору пользователя.
    # Поскольку методы еще не допилены, не функционирует.
    # Можно проверить, заменив UserChoiceResult на список из 6 элементов.
    @classmethod
    def userChoice(cls):
        user_response_int = int(cls.promptUserForString(cls.USER_CHOICE_MSG[0]))
        if user_response_int <= 0 or user_response_int >= len(cls.INIT_MSG_CONTENT):
            print(cls.USER_CHOICE_MSG[1])
            cls.userChoice()
        else:
            return user_response_int

    # UserChoiceResult - метод создания списка, где будут храниться функции
    # для исполнения желаний пользователя

    @classmethod
    def UserChoiceResult(cls):
        return []

    @classmethod
    def getCliInputStream(cls):
        cli_input_stream = {}
        for np in cls.NOTE_PROMPT:
            cli_input_stream[np] = cls.promptUserForString(cls.USER_MESSAGES[np])
        return cli_input_stream

    @classmethod
    def promptUserForString(cls, message):
        user_string = input(message)
        return user_string

    # Диалог запроса даты поиска
    @classmethod
    def getUserDateForSearch(cls):
        date_input_stream = []
        for i in cls.DATE_SEARCH:
            date_input_stream.append(
                cls._formatStringToDateTime(
                    cls.promptUserForString(cls.USER_MESSAGES_DATE[i])
                )
            )
        return date_input_stream

    # Перевод строки в datetime
    @classmethod
    def _formatStringToDateTime(cls, user_date_time):
        date_time_from_string = datetime.strptime(user_date_time, "%Y/%m/%d")
        return date_time_from_string


def ListOfNoteTitles():
    directory = os.getcwd() + "/data"
    for file in os.listdir(directory):
        with open(f"{directory}/{file}", "r") as current_file:
            file_content = json.loads(current_file.read())
            print(file_content["note_title"])


def PrintBodyOfTheChosenNote():
    directory = os.getcwd() + "/data"
    title_from_user = input("Введите название заметки: ")
    for file in os.listdir(directory):
        with open(f"{directory}/{file}", "r") as current_file:
            dict_from_content = json.loads(current_file.read())
            if title_from_user == dict_from_content["note_title"]:
                result = dict_from_content["note_body"]
                print(f"Текст выбранной заметки: {result}")
                break
