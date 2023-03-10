class CliInputPrompt():

    NOTE_PROMPT = ("note_title", "note_body")

    USER_MESSAGES = {
        NOTE_PROMPT[0]: "Введите заголовок заметки: ",
        NOTE_PROMPT[1]: "Введите содержание заметки: ",
    }

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
