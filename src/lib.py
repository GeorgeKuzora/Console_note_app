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

    def set_title_body(self, title: str, body: str) -> None:
        self.note_title = title
        self.note_body = body
        self.note_last_modification_dt = datetime.now()

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


class NoteList:
    INIT_START_DATE = datetime(1900, 1, 1, 0, 0, 0, 0)
    INIT_END_DATE = datetime(9999, 1, 1, 0, 0, 0, 0)

    def __init__(self) -> None:
        self.note_list = []
        self.start_date = self.INIT_START_DATE
        self.end_date = self.INIT_END_DATE

    def setListData(self, list_data: list) -> None:
        for ld in list_data:
            note = Note()
            note.setStorageData(ld)
            self.note_list.append(note)

    def getListData(self) -> list:
        list_data = []
        for n in self.note_list:
            if (
                n.note_creation_dt >= self.start_date
                and n.note_creation_dt <= self.end_date
            ):
                list_data.append(n.getNoteData())
        return list_data

    def setDates(self, start_date: datetime, end_date: datetime) -> None:
        self.start_date = start_date
        self.end_date = end_date

    def getNotesByTitle(self, title: str) -> list:
        list_data = []
        for n in self.note_list:
            if title in n.note_title:
                list_data.append(n.getNoteData())
        return list_data
