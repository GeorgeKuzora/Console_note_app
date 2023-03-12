import os


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
