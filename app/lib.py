import os
import glob
from tkinter.tix import ListNoteBook

class UserInputPrompt():
    @classmethod
    def promptUserForString(cls, message):
        user_string = input(message)
        return user_string

    @classmethod
    def handleUserInputExeptions(cls, raw_user_input):
        try:
            if raw_user_input == "":
                raise ValueError()
        except ValueError:
            return ""
        return raw_user_input

    @classmethod
    def getClearUserInput(cls, message_for_user):
        raw_user_input = cls.promptUserForString(message_for_user)
        clear_user_input = cls.handleUserInputExeptions(raw_user_input)
        return clear_user_input
    
   # Записывает в словарь файлы формата json из текущего каталога
    @classmethod
    def createListNote(cls):
        list_note_dict = {}
        i = 0
        for file in glob.glob(os.getcwd() + '**/*.json'):
             list_note_dict.update({i:os.path.basename(file).split('.')[0]})
             i += 1
        return list_note_dict