import os


class FileSystemHandler():

    @staticmethod
    def saveNote(file_system_stream):
        file_name = FileSystemHandler.getFileName(file_system_stream[1])
        try:
            os.mkdir("data")
        except FileExistsError:
            pass
        finally:
            with open(file_name, 'w', encoding="utf-8") as file:
                file.write(file_system_stream[0])

    @staticmethod
    def getFileName(note_id):
        file_name = "data/" + note_id+ ".json"
        return file_name
