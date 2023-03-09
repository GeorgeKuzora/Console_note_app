import os


class FileSystemHandler():
    def __init__(self) -> None:
        pass

    @staticmethod
    def saveNote(note):
        FileSystemHandler.createFile(note)

    @staticmethod
    def createFile(note_obj):
        file_name = FileSystemHandler.getFileName(note_obj)
        try:
            os.mkdir("data")
        except FileExistsError:
            pass
        finally:
            with open(file_name, 'w', encoding="utf-8") as file:
                file.write(note_obj.note_in_json)

    @staticmethod
    def getFileName(note_obj):
        file_name = "data/" + note_obj.note_id + ".json"
        return file_name
