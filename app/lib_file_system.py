import os
from glob import glob
import json


class FileSystemHandler:
    STORAGE_DIR = "data"
    FILE_FORMAT = ".json"
    FILE_NOT_EXISTS_MESSAGE = "File didn't exist"

    @classmethod
    def saveToFile(cls, file_name: str, file_content: dict) -> None:
        file_name = cls.formatFileName(file_name)
        try:
            os.mkdir(cls.STORAGE_DIR)
        except FileExistsError:
            pass
        finally:
            with open(file_name, "w", encoding="utf-8") as file:
                json.dump(file_content, file)

    @classmethod
    def deleteFile(cls, file_name):
        file_name = cls.formatFileName(file_name)
        try:
            os.remove(file_name)
        except:
            print(cls.FILE_NOT_EXISTS_MESSAGE)

    @classmethod
    def formatFileName(cls, file_name: str) -> str:
        file_name = (
            os.getcwd() + "/" + cls.STORAGE_DIR + "/" + file_name + cls.FILE_FORMAT
        )
        return file_name

    @classmethod
    def getContentsList(cls) -> list:
        contents_list = []
        for file_name in glob(os.getcwd() + "/**/*.json"):
            with open(file_name, "r") as file:
                file_contents = json.loads(file.read())
                contents_list.append(file_contents)
        return contents_list
