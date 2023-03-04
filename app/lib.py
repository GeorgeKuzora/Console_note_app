from datetime import datetime


class UserInputPrompt():
    @classmethod
    def promptUserForString(cls, message):
        user_string = input(message)
        return user_string

    @classmethod
    def handleUserInputExeptions(cls, raw_user_input):
        try:
            if raw_user_input == "":
                raise ValueError()
        except ValueError:
            return ""
        return raw_user_input

    @classmethod
    def getClearUserInput(cls, message_for_user):
        raw_user_input = cls.promptUserForString(message_for_user)
        clear_user_input = cls.handleUserInputExeptions(raw_user_input)
        return clear_user_input


class Note():
    NOTE_ID_FORMAT = "%Y%m%d%H%M%S"

    def __init__(self) -> None:
        self.note_title = ""
        self.note_body = ""
        self.note_creation_dt = datetime.now()
        self.note_last_modification_dt = datetime.now()
        self.note_id = self._noteIdFormat()

    @classmethod
    def createNote(cls):
        new_note = Note()
        new_note.note_title = UserInputPrompt.getClearUserInput("Введите \
                                                                заголовок заметки: ")
        new_note.note_body = UserInputPrompt.getClearUserInput("Введите тело заметки: ")
        return new_note

    def _noteIdFormat(self):
        _note_id = self.note_creation_dt.strftime(self.NOTE_ID_FORMAT)
        return _note_id
