from datetime import datetime
import json


class Note():
    NOTE_ID_FORMAT = "%Y%m%d%H%M%S"
    NOTE_DT_FORMAT = "%Y%m%d%H%M%S%f"
    NOTE_INPUT_STREAM_FORMAT = ("note_title", "note_body")

    def __init__(self) -> None:
        self.note_title = ""
        self.note_body = ""
        self.note_creation_dt = datetime.now()
        self.note_last_modification_dt = datetime.now()
        self.note_id = self._noteIdFormat()

    def _noteIdFormat(self):
        _note_id = self.note_creation_dt.strftime(self.NOTE_ID_FORMAT)
        return _note_id

    @classmethod
    def createNote(cls, input_stream):
        new_note = Note()
        new_note.note_title = input_stream[cls.NOTE_INPUT_STREAM_FORMAT[0]]
        new_note.note_body = input_stream[cls.NOTE_INPUT_STREAM_FORMAT[1]]
        return new_note

    def getFileSystemStream(self):
        return self._convertToJson(), self._noteIdFormat()

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
