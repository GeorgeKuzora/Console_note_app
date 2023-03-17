import time

class CliInputPrompt():

    NOTE_PROMPT = ("note_title", "note_body")

    USER_MESSAGES = {
        NOTE_PROMPT[0]: "Введите заголовок заметки: ",
        NOTE_PROMPT[1]: "Введите содержание заметки: ",

    }
    
    DATE_SEARCH = ("start_date", "stop_date")

    USER_MESSAGES_DATE = {
        DATE_SEARCH[0]: "Введите начальную дату: ",
        DATE_SEARCH[1]: "Введите конечную дату: ",

    }

    INIT_MSG_CONTENT = [
        "Какое действие вы хотите совершить?",
        "1. Создать новую заметку",
        "2. Посмотреть список заметок по названииям",
        "3. Вывести текст заметки на экран",
        "4. Изменить заметку",
        "5. Удалить заметку",
        "6. Посмотреть заметки в интервале дат создания"
    ]

    USER_CHOICE_MSG = ("Введите номер действия: ",
                       "Введен неправильный номер. Попробуйте еще раз.")

    # не знаю, нужен ли здесь этот метод, обсудим
    def initialActions(cls):
        cls.initialMessage
        cls.userChoice

    #Выводит в консоль вопрос к пользователю, что он хочет
    def initialMessage(cls):
        print("\n".join(cls.INIT_MSG_CONTENT))
    
    # Вызывает метод, соответствующий выбору пользователя.
    # Поскольку методы еще не допилены, не функционирует.
    # Можно проверить, заменив UserChoiceResult на список из 6 элементов.
    def userChoice(cls):
        user_response_int = int(cls.promptUserForString(cls.USER_CHOICE_MSG[0]))
        if user_response_int <= 0 or user_response_int > len(cls.UserChoiceResult):
            print(cls.USER_CHOICE_MSG[1])
            cls.userChoice()
        else:
            return cls.UserChoiceResult()[user_response_int - 1]
# UserChoiceResult - метод создания списка, где будут храниться функции
#                    для исполнения желаний пользователя

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
        date_input_stream = {}
        for i in cls.DATE_SEARCH:
           date_input_stream[i] = cls.promptUserForString(cls.USER_MESSAGES_DATE[i])
        return date_input_stream
    
    # Перевод строки в datetime
    def _formatStringToDateTime(self, user_date_time):
        date_time_from_string = time.strptime(user_date_time, "%Y%m%d")
        return date_time_from_string
