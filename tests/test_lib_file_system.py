import unittest
import os
import json
from lib_file_system import FileSystemHandler as fsh


class TestFileSystemHandler(unittest.TestCase):
    mock_file_content = {
        "note_title": "test title",
        "note_body": "test body",
        "note_id": "20230313194644",
        "note_creation_dt": "20230313194644353411",
        "note_last_modification_dt": "20230313194644353430",
    }

    def setUp(self):
        self.mock_file_name = "20230313194644"
        self.mock_file_content = self.mock_file_content

        self.test_file_name = "data/20230313194644.json"
        self.test_write_data = (self.mock_file_content, self.mock_file_name)

    def testFormatFileName(self):
        formated_file_name = fsh.formatFileName(self.mock_file_name)
        self.assertEqual(formated_file_name[-20:], self.test_file_name[-20:])

    def testSaveToFile(self):
        fsh.saveToFile(self.mock_file_name, self.mock_file_content)
        self.assertTrue(os.access(self.test_file_name, os.F_OK))
        with open(self.test_file_name, "r") as file:
            file_contents = json.load(file)
        self.assertEqual(file_contents, self.mock_file_content)
        MockFileController.deleteFile(self.mock_file_name)

    def testDeleteFile(self):
        MockFileController.createFile(self.mock_file_name)
        fsh.deleteFile(self.mock_file_name)
        self.assertFalse(os.access(self.test_file_name, os.F_OK))

    def testGetContentsList(self):
        files = ("testfile1", "testfile2", "testfile3")
        for file in files:
            MockFileController.createFile(file)
        contents_list = fsh.getContentsList()
        self.assertEqual(len(contents_list), 3)
        for file in files:
            MockFileController.deleteFile(file)


class MockFileController:
    @staticmethod
    def createFile(file_name: str) -> None:
        file_name = "data" + "/" + file_name + ".json"
        try:
            os.mkdir("data")
        except FileExistsError:
            pass
        finally:
            with open(file_name, "w", encoding="utf-8") as file:
                # file.write('{"test key": "test value",}')
                json.dump(TestFileSystemHandler.mock_file_content, file)

    @staticmethod
    def deleteFile(file_name: str) -> None:
        file_name = "data" + "/" + file_name + ".json"
        os.remove(file_name)
