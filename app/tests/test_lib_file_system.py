import unittest
import os
import json
from lib_file_system import *
from lib import *


class TestFileSystemHandler(unittest.TestCase):
    def setUp(self):
        self.test_id = "20230101010101"
        self.test_file_content = """{"note_title": "test title",
                                     "note_body": "test body",
                                     "note_id": "20230313194644",
                                     "note_creation_dt": "20230313194644353411",
                                     "note_last_modification_dt": "20230313194644353430"}"""
        self.test_dict = json.loads(self.test_file_content)
        self.file_name = "data/20230101010101.json"
        self.test_write_data = (self.test_file_content, self.test_id)

    def testSaveNote(self):
        FileSystemHandler.saveNote(self.test_write_data)
        self.assertTrue(os.access(self.file_name, os.F_OK))
        with open(self.file_name, "r") as file:
            fileContents = file.read()
        self.assertEqual(fileContents, self.test_file_content)

    def testCreateListNote(self):
        file_list = FileSystemHandler.createListNote()
        file_list_values = file_list.values()
        self.assertEqual(type(file_list), type({"thisis": "dict"}))
        self.assertTrue(len(file_list_values) != 0)


class TestFileSystemReader(unittest.TestCase):
    def setUp(self):
        self.test_id = "20230101010102"
        self.test_file_content = """{"note_title": "test title",
                                     "note_body": "test body",
                                     "note_id": "20230313194644",
                                     "note_creation_dt": "20230313194644353411",
                                     "note_last_modification_dt": "20230313194644353430"}"""
        self.test_dict = json.loads(self.test_file_content)
        self.test_file_name = "data/20230101010102.json"
        self.test_file_obj = FileSystemReader(self.test_id)
        self.test_file_obj.file_name = self.test_file_name
        self.test_corupted_id = "323424"
        self.test_corupted_file_name = "data/323424.json"
        self.test_corupted_file = FileSystemReader(self.test_corupted_id)
        self.test_corupted_file.file_name = self.test_corupted_file_name
        with open(self.test_file_name, "w") as file:
            file.write(self.test_file_content)

    def testGetJsonById(self):
        file_data = FileSystemReader.getJsonById(self.test_id)
        self.assertEqual(file_data, self.test_file_content)

    def testGetFileFactory(self):
        file_obj = FileSystemReader.getFileFactory(self.test_id)
        self.assertEqual(type(file_obj), type(FileSystemReader(self.test_id)))
        self.assertEqual(file_obj.file_name, self.test_file_name)

    def testReadFile(self):
        file_data = self.test_file_obj.readFile()
        self.assertEqual(file_data, self.test_file_content)

    def testReadFileNotRead(self):
        file_data = self.test_corupted_file.readFile()
        self.assertEqual(file_data, self.test_corupted_file.FILE_NOT_EXISTS_MESSAGE)

    def testGetFileContents(self):
        file_data = self.test_file_obj.getFileContents()
        self.assertEqual(file_data, self.test_file_content)

    def testGetJsonByNoteTitle(self):
        file_data = FileSystemReader.getJsonByNoteTitle(self.test_dict["note_title"])
        self.assertEqual(type(file_data), type("string"))
