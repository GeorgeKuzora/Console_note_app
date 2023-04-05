from lib import Note, NoteList
from lib_cli import UserInput, ConsolePrinter
from lib_file_system import FileSystemHandler
from src.user_exeptions import InvalidUserInputError


class Controller:
    def __init__(self) -> None:
        pass

    def createNote(self) -> None:
        ConsolePrinter.printNewNoteMessage()
        user_input = UserInput()
        user_input.setTitle()
        user_input.setBody()
        note = Note()
        note.set_title_body(user_input.note_title, user_input.note_body)
        file_name = note.getNoteId()
        file_data = note.getNoteData()
        FileSystemHandler.saveToFile(file_name, file_data)

    def getListOfNotes(self):
        files_content = FileSystemHandler.getContentsList()
        note_list = NoteList()
        note_list.setListData(files_content)
        notes_data = note_list.getListData()
        ConsolePrinter.printListOfNotes(notes_data)

    def getListOfNotesByDate(self):
        ConsolePrinter.printDatesInputMessage()
        user_input = self.setDatesByUser()
        files_content = FileSystemHandler.getContentsList()
        note_list = NoteList()
        note_list.setListData(files_content)
        note_list.setDates(user_input.start_date, user_input.end_date)
        notes_data = note_list.getListData()
        ConsolePrinter.printListOfNotes(notes_data)

    def setDatesByUser(self) -> UserInput:
        try:
            user_input: UserInput = UserInput()
            user_input.setDates()
            return user_input
        except InvalidUserInputError as err:
            print("Дата была введена в неправильном формате", err)
            return self.setDatesByUser()

    def getListNotesByName(self):
        ConsolePrinter.printFindNotesMessage()
        user_input = UserInput()
        user_input.setTitle()
        files_content = FileSystemHandler.getContentsList()
        note_list = NoteList()
        note_list.setListData(files_content)
        notes_data = note_list.getNotesByTitle(user_input.note_title)
        ConsolePrinter.printListOfNotes(notes_data)

    def changeNote(self):
        ConsolePrinter.printFindOriginalNote()
        orig_title_input = UserInput()
        orig_title_input.setTitle()
        files_content = FileSystemHandler.getContentsList()
        note_list = NoteList()
        note_list.setListData(files_content)
        notes_data = note_list.getNotesByTitle(orig_title_input.note_title)
        ConsolePrinter.printChangeNoteMessage()
        user_input = UserInput()
        user_input.setTitle()
        user_input.setBody()
        for nd in notes_data:
            note = Note()
            note.setStorageData(nd)
            note.set_title_body(user_input.note_title, user_input.note_body)
            file_name = note.getNoteId()
            file_data = note.getNoteData()
            FileSystemHandler.saveToFile(file_name, file_data)

    def deleteNote(self):
        ConsolePrinter.printFindNoteForDeletion()
        orig_title_input = UserInput()
        orig_title_input.setTitle()
        files_content = FileSystemHandler.getContentsList()
        note_list = NoteList()
        note_list.setListData(files_content)
        notes_data = note_list.getNotesByTitle(orig_title_input.note_title)
        for nd in notes_data:
            note = Note()
            note.setStorageData(nd)
            file_name = note.getNoteId()
            FileSystemHandler.deleteFile(file_name)
        ConsolePrinter.printDeleteMessage()


class Program:
    def __init__(self) -> None:
        pass

    def getCommandFromStartMenu(self) -> str:
        ConsolePrinter.printHelp()
        command = input("Введите желаемую комманду: ")
        print()
        return command

    def runController(self):
        control = Controller()
        dict_of_methods = {
            "add": control.createNote,
            "all": control.getListOfNotes,
            "show": control.getListNotesByName,
            "change": control.changeNote,
            "delete": control.deleteNote,
            "date": control.getListOfNotesByDate,
        }
        command = self.getCommandFromStartMenu()
        dict_of_methods[command]()


if __name__ == "__main__":
    program = Program()
    program.runController()
