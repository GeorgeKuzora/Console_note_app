from datetime import datetime
import json


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
    NOTE_DT_FORMAT = "%Y%m%d%H%M%S%f"

    def __init__(self) -> None:
        self.note_title = ""
        self.note_body = ""
        self.note_creation_dt = datetime.now()
        self.note_last_modification_dt = datetime.now()
        self.note_id = self._noteIdFormat()
        self.note_in_json = ""

    def _noteIdFormat(self):
        _note_id = self.note_creation_dt.strftime(self.NOTE_ID_FORMAT)
        return _note_id

    @classmethod
    def createNote(cls):
        new_note = Note()
        new_note.note_title = UserInputPrompt.getClearUserInput("Введите заголовок заметки: ")
        new_note.note_body = UserInputPrompt.getClearUserInput("Введите тело заметки: ")
        new_note.note_in_json = new_note._convertToJson()
        return new_note

    def _convertToJson(self):
       attr_dict = self._convertToDict()
       attr_json = json.dumps(attr_dict)
       return attr_json

    def _convertToDict(self):
        note_as_dict = {}
        note_as_dict.update({"note_title": self.note_title,
                             "note_body": self.note_body,
                             "note_id": self.note_id,
                             "note_creation_dt": self._formatDateTimeToString(
                                                self.note_creation_dt),
                             "note_last_modification_dt": self._formatDateTimeToString(
                                                self.note_last_modification_dt)
                            })
        return note_as_dict

    def _formatDateTimeToString(self, _note_date_time):
        _note_date_time_string = _note_date_time.strftime(self.NOTE_DT_FORMAT)
        return _note_date_time_string
