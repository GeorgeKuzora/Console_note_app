import os
from glob import glob



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
    def delNote(cls, note_id):   
        file_name = cls.getFileName(note_id)
        if os.path.isfile(file_name):
            os.remove(file_name)
        else:
            FileSystemReader.FILE_NOT_EXISTS_MESSAGE


    @classmethod
    def getFileName(cls, note_id):
        file_name = cls.STORAGE_DIR + "/" + note_id + cls.FILE_FORMAT
        return file_name

    # Записывает в словарь файлы формата json из текущего каталога
    @classmethod
    def createListNote(cls):
        list_note_dict = {}
        i = 0   
        for file in glob("*.json"):
            list_note_dict.update({i: os.path.basename(file).split(".")[0]})
            i += 1
        return list_note_dict
    
    # Создает словарь из времени создания и имени файла, сортирует и записывает в новый список
    @classmethod
    def createListNoteWithDate(cls):
        list_note = createListNote()
        list_note_date = {}
        for i in range(0, len(list_note)):
            list_note_date.update({list_note[i]: os.path.getmtime(os.getcwd() + "\\" + list_note[i] + ".json")})
       
        sorted_values = sorted(list_note_date.values())
        sort_list_note = {}
        for i in sorted_values:
            for k in list_note_date.keys():
                if list_note_date[k] == i:
                    sort_list_note[k] = list_note_date[k]
                    break

        return sort_list_note
    
   

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

    # Получение json из файла на основе title заметки
    @classmethod
    def getJsonByNoteTitle(cls, title: str):
        for file in glob("*.json"):
            json_data = file.getFileContents()
            if json_data.find(title) != -1:
                return  json_data                
            else:
                continue
        return cls.FILE_NOT_EXISTS_MESSAGE
 
