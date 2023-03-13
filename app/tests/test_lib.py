import unittest
from datetime import datetime
from lib import *


class TestNote(unittest.TestCase):

    def setUp(self):
        self.test_datetime = datetime(2023, 1, 1, 1, 1, 1, 1)
        self.test_note = Note()
        self.test_id_string = self.test_datetime.strftime(self.test_note.NOTE_ID_FORMAT)
        self.test_datetime_string = self.test_datetime.strftime(self.test_note.NOTE_DT_FORMAT)
        self.test_note.note_id = self.test_id_string
        self.test_note.note_creation_dt = self.test_datetime
        self.test_note.note_last_modification_dt = self.test_datetime
        self.test_note.note_title = "test title"
        self.test_note.note_body = "test body"
        self.test_input_stream = {Note.NOTE_INPUT_STREAM_FORMAT[0]:"test title",
                                  Note.NOTE_INPUT_STREAM_FORMAT[1]:"test body"}

    def testNoteIdFormat(self):
        formated_note_id = self.test_note._noteIdFormat()
        self.assertEqual(formated_note_id, self.test_note.note_id)

    def testFormatDateTimeToString(self):
        formated_note_dt = self.test_note._formatDateTimeToString(
            self.test_note.note_creation_dt)
        self.assertEqual(formated_note_dt, self.test_datetime_string)

    def testConvertToDict(self):
        object_attr = self.test_note._convertToDict()
        self.assertEqual(type(object_attr), type({"thisis":"dict"}))

    def testGetFileSystemStream(self):
        object_attr = self.test_note.getFileSystemStream()
        self.assertEqual(type(object_attr[0]), type("string"))
        self.assertEqual(type(object_attr[1]), type("string"))

    def testCreateNote(self):
        time_before_note_created = datetime.now()
        user_test_note = Note.createNote(self.test_input_stream)
        time_after_note_created = datetime.now()
        id_from_note_cd = user_test_note.note_creation_dt.strftime(
                                                    user_test_note.NOTE_ID_FORMAT)
        self.assertEqual(user_test_note.note_title, "test title")
        self.assertEqual(user_test_note.note_body, "test body")
        self.assertTrue(user_test_note.note_creation_dt >= time_before_note_created \
                        and user_test_note.note_creation_dt <= time_after_note_created)
        self.assertTrue(user_test_note.note_last_modification_dt \
                        >= time_before_note_created \
                        and user_test_note.note_last_modification_dt <= time_after_note_created)
        self.assertTrue(user_test_note.note_id == id_from_note_cd)

