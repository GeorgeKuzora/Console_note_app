from datetime import datetime


class Note:
    NOTE_ID_FORMAT = "%Y%m%d%H%M%S"
    NOTE_DT_FORMAT = "%Y%m%d%H%M%S%f"

    def __init__(self) -> None:
        self.note_title = ""
        self.note_body = ""
        self.note_creation_dt = datetime.now()
        self.note_last_modification_dt = datetime.now()
        self.note_id = self._noteIdFormat()

    def _noteIdFormat(self) -> str:
        _note_id = self.note_creation_dt.strftime(self.NOTE_ID_FORMAT)
        return _note_id

    def setTitleBody(self, title: str, body: str) -> None:
        self.note_title = title
        self.note_body = body

    def setStorageData(self, storage_data: dict) -> None:
        for key in storage_data:
            if key == "note_creation_dt" or key == "note_last_modification_dt":
                setattr(
                    self, key, datetime.strptime(storage_data[key], self.NOTE_DT_FORMAT)
                )
            else:
                setattr(self, key, storage_data[key])

    def getNoteId(self) -> str:
        return self.note_id

    def getNoteData(self) -> dict:
        note_as_dict = {}
        note_as_dict.update(
            {
                "note_title": self.note_title,
                "note_body": self.note_body,
                "note_id": self.note_id,
                "note_creation_dt": self._formatDateTimeToString(self.note_creation_dt),
                "note_last_modification_dt": self._formatDateTimeToString(
                    self.note_last_modification_dt
                ),
            }
        )
        return note_as_dict

    def _formatDateTimeToString(self, _note_date_time: datetime) -> str:
        _note_date_time_string = datetime.strftime(_note_date_time, self.NOTE_DT_FORMAT)
        return _note_date_time_string
