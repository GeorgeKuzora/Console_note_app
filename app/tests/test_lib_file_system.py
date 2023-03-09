import unittest
import os
from lib_file_system import *
from lib import *


class TestFileSystemHandler(unittest.TestCase):

    def setUp(self):
        self.test_datetime = datetime(2023, 1, 1, 1, 1, 1, 1)
        self.test_note = Note()
        self.test_note.note_id = self.test_datetime.strftime(self.test_note.NOTE_ID_FORMAT)
        self.test_note.note_creation_dt = self.test_datetime
        self.test_note.note_last_modification_dt = self.test_datetime
        self.test_note.note_title = "test title"
        self.test_note.note_body = "test body"
        self.test_note.note_in_json = self.test_note._convertToJson()
        self.file_name = "data/20230101010101.json"

    def testSaveNote(self):
        FileSystemHandler.saveNote(self.test_note)
        self.assertTrue(os.access(self.file_name, os.F_OK))
        with open(self.file_name, "r") as file:
            fileContents = file.read()
        self.assertEqual(fileContents, self.test_note.note_in_json)
