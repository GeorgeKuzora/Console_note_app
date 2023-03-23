import unittest
from datetime import datetime
from lib import Note, NoteList


class MockNote(Note):
    def __init__(self) -> None:
        self.note_title = "mock title"
        self.note_body = "mock body"
        self.note_creation_dt = datetime(2023, 1, 1, 0, 0, 0, 0)
        self.note_last_modification_dt = datetime(2023, 1, 1, 0, 0, 0, 0)
        self.note_id = "20230101000000"

    def randomizeData(self) -> None:
        self.note_title = "this is random title"
        self.note_body = "this is random body"
        self.note_creation_dt = datetime(2020, 6, 12, 13, 56, 30, 45632)
        self.note_last_modification_dt = datetime(2021, 11, 20, 8, 28, 45, 74327)
        self.note_id = "20200612135630"


class TestNote(unittest.TestCase):
    def setUp(self) -> None:
        self.test_data = {
            "note_title": "test title",
            "note_body": "test body",
            "note_id": "20230101000000",
            "note_creation_dt": "20230101000000000000",
            "note_last_modification_dt": "20230101000000000000",
        }

    def useTestData(self, mock_note: MockNote) -> None:
        for key in self.test_data:
            if key == "note_creation_dt" or key == "note_last_modification_dt":
                setattr(
                    mock_note,
                    key,
                    datetime.strptime(self.test_data[key], mock_note.NOTE_DT_FORMAT),
                )
            else:
                setattr(mock_note, key, self.test_data[key])

    def testNoteIdFormat(self) -> None:
        mock_note = MockNote()
        formated_note_id = mock_note._noteIdFormat()
        self.assertEqual(formated_note_id, self.test_data["note_id"])

    def testSetTitleBody(self) -> None:
        mock_note = MockNote()
        note_mod_date = mock_note.note_last_modification_dt
        mock_note.setTitleBody(
            self.test_data["note_title"], self.test_data["note_body"]
        )
        self.assertEqual(mock_note.note_title, self.test_data["note_title"])
        self.assertEqual(mock_note.note_body, self.test_data["note_body"])
        self.assertNotEqual(mock_note.note_last_modification_dt, note_mod_date)

    def testSetStorageData(self) -> None:
        mock_note = MockNote()
        mock_note.randomizeData()
        mock_note.setStorageData(self.test_data)
        for key in self.test_data:
            if key == "note_creation_dt" or key == "note_last_modification_dt":
                value = datetime.strftime(
                    getattr(mock_note, key), mock_note.NOTE_DT_FORMAT
                )
            else:
                value = getattr(mock_note, key)
            self.assertEqual(value, self.test_data[key])

    def testGetNoteId(self) -> None:
        mock_note = MockNote()
        self.assertEqual(mock_note.getNoteId(), self.test_data["note_id"])

    def testFormatDateTimeToString(self) -> None:
        mock_note = MockNote()
        dt_str = mock_note._formatDateTimeToString(mock_note.note_creation_dt)
        self.assertEqual(dt_str, self.test_data["note_creation_dt"])

    def testGetNoteData(self) -> None:
        mock_note = MockNote()
        self.useTestData(mock_note)
        data = mock_note.getNoteData()
        self.assertEqual(data, self.test_data)


class TestNoteList(unittest.TestCase):
    def setUp(self) -> None:
        self.test_data_1 = {
            "note_title": "test title",
            "note_body": "test body",
            "note_id": "20230101000000",
            "note_creation_dt": "20230101000000000000",
            "note_last_modification_dt": "20230101000000000000",
        }
        self.test_data_2 = {
            "note_title": "another test title",
            "note_body": "another test body",
            "note_id": "20230109000000",
            "note_creation_dt": "20230109000000000000",
            "note_last_modification_dt": "20230101000000000000",
        }
        self.test_data_list = [self.test_data_1 for i in range(4)]
        self.test_data_list_2 = [self.test_data_2 for i in range(4)]
        self.test_data_list.extend(self.test_data_list_2)
        self.test_start_date = datetime(2023, 1, 2, 0, 0, 0, 0)
        self.test_end_date = datetime(2023, 2, 1, 0, 0, 0, 0)

    def testInit(self) -> None:
        note_list = NoteList()
        self.assertIsInstance(note_list, NoteList)
        self.assertEqual(note_list.note_list, [])
        self.assertEqual(note_list.start_date, datetime(1900, 1, 1, 0, 0, 0, 0))
        self.assertEqual(note_list.end_date, datetime(9999, 1, 1, 0, 0, 0, 0))

    def testSetListData(self):
        note_list = NoteList()
        note_list.setListData(self.test_data_list)
        self.assertEqual(len(note_list.note_list), len(self.test_data_list))
        for n in note_list.note_list:
            self.assertIsInstance(n, Note)

    def testGetListData(self) -> None:
        note_list = NoteList()
        note_list.setListData(self.test_data_list)
        content = note_list.getListData()
        self.assertEqual(content, self.test_data_list)

    def testSetDates(self) -> None:
        note_list = NoteList()
        note_list.setDates(self.test_start_date, self.test_end_date)
        self.assertEqual(note_list.start_date, self.test_start_date)
        self.assertEqual(note_list.end_date, self.test_end_date)

    def testGetListDataWithDatesSet(self):
        note_list = NoteList()
        note_list.setListData(self.test_data_list)
        note_list.setDates(self.test_start_date, self.test_end_date)
        content = note_list.getListData()
        self.assertEqual(len(content), len(self.test_data_list_2))
        self.assertEqual(content, self.test_data_list_2)

    def testGetNotesByTitle(self):
        note_list = NoteList()
        note_list.setListData(self.test_data_list)
        content = note_list.getNotesByTitle(self.test_data_2["note_title"])
        self.assertEqual(len(content), len(self.test_data_list_2))
        self.assertEqual(content, self.test_data_list_2)
