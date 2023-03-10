import unittest
import os
from lib_file_system import *
from lib import *


class TestFileSystemHandler(unittest.TestCase):

    def setUp(self):
        self.test_fs_stream = ("test json", "20230101010101")
        self.file_name = "data/20230101010101.json"

    def testSaveNote(self):
        FileSystemHandler.saveNote(self.test_fs_stream)
        self.assertTrue(os.access(self.file_name, os.F_OK))
        with open(self.file_name, "r") as file:
            fileContents = file.read()
        self.assertEqual(fileContents, self.test_fs_stream[0])
