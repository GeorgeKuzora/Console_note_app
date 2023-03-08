import unittest
from datetime import datetime
from lib import *


class TestUserInputPrompt(unittest.TestCase):

    def testPromptUserForString(self):
        test_string = UserInputPrompt.promptUserForString("Input 'test': ")
        self.assertEqual(test_string, "test")

    def testHandleUserInputExeptions(self):
        test_string = UserInputPrompt.handleUserInputExeptions("test")
        self.assertEqual(test_string, "test")
        empty_string = UserInputPrompt.handleUserInputExeptions("")
        self.assertFalse(empty_string)

    def testGetClearUserInput(self):
        test_string = UserInputPrompt.getClearUserInput("Input test: ")
        self.assertEqual(test_string, "test")
        empty_string = UserInputPrompt.getClearUserInput("Press Enter")
        self.assertFalse(empty_string)


class TestNote(unittest.TestCase):

    def setUp(self):
        self.test_datetime = datetime(2023, 1, 1, 1, 1, 1, 1)
        self.test_note = Note()
        self.test_note.note_id = self.test_datetime.strftime(self.test_note.NOTE_ID_FORMAT)
        self.test_note.note_creation_dt = self.test_datetime
        self.test_note.note_last_modification_dt = self.test_datetime
        self.test_note.note_title = "test title"
        self.test_note.note_body = "test body"

    def testNoteIdFormat(self):
        formated_note_id = self.test_note._noteIdFormat()
        self.assertEqual(formated_note_id, self.test_note.note_id)

    def testCreateNote(self):
        time_before_note_created = datetime.now()
        user_test_note = Note.createNoteFacrory()
        # Please input "test title" and "test body" in prompts
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

    def testConvertToJson(self):
        object_attr_json = self.test_note._convertToJson()
        self.assertEqual(type(object_attr_json), type("string"))
