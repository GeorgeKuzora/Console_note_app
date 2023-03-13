import os
import glob


class FileSystemHandler:
    STORAGE_DIR = "data"
    FILE_FORMAT = ".json"

    def __init__(self):
        pass

    @classmethod
    def saveNote(cls, write_data):
        file_name = FileSystemHandler.getFileName(write_data[1])
        try:
            os.mkdir(cls.STORAGE_DIR)
        except FileExistsError:
            pass
        finally:
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(write_data[0])

    @classmethod
    def getFileName(cls, note_id):
        file_name = cls.STORAGE_DIR + "/" + note_id + cls.FILE_FORMAT
        return file_name

    # Записывает в словарь файлы формата json из текущего каталога
    @classmethod
    def createListNote(cls):
        list_note_dict = {}
        i = 0
        print(os.getcwd())
        for file in glob.glob(os.getcwd() + "/**/*.json"):
            list_note_dict.update({i: os.path.basename(file).split(".")[0]})
            i += 1
        return list_note_dict


class FileSystemReader(FileSystemHandler):
    FILE_NOT_EXISTS_MESSAGE = "Note didn't exist"

    def __init__(self, id):
        self.file_id = id
        self.file_name = ""

    @classmethod
    def getJsonById(cls, file_id):
        file = cls.getFileFactory(file_id)
        json_data = file.readFile()
        return json_data

    @classmethod
    def getFileFactory(cls, file_id):
        file_obj = cls(file_id)
        file_obj.file_name = file_obj.getFileName(file_obj.file_id)
        return file_obj

    def readFile(self):
        try:
            return self.getFileContents()
        except FileNotFoundError:
            return self.FILE_NOT_EXISTS_MESSAGE

    def getFileContents(self):
        with open(self.file_name, "r") as file:
            file_contents = file.read()
        return file_contents
