import unittest
import os
from lib_file_system import *
from lib import *


class TestFileSystemHandler(unittest.TestCase):
    def setUp(self):
        self.test_id = "20230101010101"
        self.test_file_content = "test note"
        self.file_name = "data/20230101010101.json"
        self.test_write_data = (self.test_file_content, self.test_id)

    def testSaveNote(self):
        FileSystemHandler.saveNote(self.test_write_data)
        self.assertTrue(os.access(self.file_name, os.F_OK))
        with open(self.file_name, "r") as file:
            fileContents = file.read()
        self.assertEqual(fileContents, self.test_file_content)
