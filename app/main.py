from lib import Note
from lib_cli import CliInputPrompt, PrintBodyOfTheChosenNote, ListOfNoteTitles
from lib_file_system import FileSystemHandler, FileSystemReader


def createNoteFromCliInput():
    cli_input_stream = CliInputPrompt.getCliInputStream()
    note_obj = Note.createNote(cli_input_stream)
    file_system_stream = note_obj.getFileSystemStream()
    FileSystemHandler.saveNote(file_system_stream)


def getNoteByName():
    PrintBodyOfTheChosenNote()


def getListOfNotes():
    ListOfNoteTitles()


def getListOfNotesByDates():
    all_notes_names = FileSystemHandler.createListNote()
    all_notes = []
    for name in all_notes_names:
        note_json = FileSystemReader.getJsonById(name)
        all_notes.append(Note.createNoteFromJson(note_data=note_json))
    start_end_date = CliInputPrompt.getUserDateForSearch()
    note_list = []
    for note in all_notes:
        if (
            note.note_creation_dt >= start_end_date[0]
            and note.note_creation_dt <= start_end_date[1]
        ):
            note_list.append(note)
            print(note.note_title, end="\n\n")


def changeNote():
    all_notes_names = FileSystemHandler.createListNote()
    data_from_all_notes = []
    for name in all_notes_names:
        data_from_all_notes.append(FileSystemReader.getJsonById(name))
    note_title = CliInputPrompt.promptUserForString(
        CliInputPrompt.USER_MESSAGES[CliInputPrompt.NOTE_PROMPT[0]]
    )
    note = None
    for data in data_from_all_notes:
        if data["note_title"] == note_title:
            note = Note.createNoteFromJson(data)
            break
    if note != None:
        input_stream = CliInputPrompt.getCliInputStream()
        note.changeNote(input_stream)
        file_stream = note.getFileSystemStream()
        FileSystemHandler.saveNote(file_stream)


def deleteNote():
    all_notes_names = FileSystemHandler.createListNote()
    data_from_all_notes = []
    for name in all_notes_names:
        data_from_all_notes.append(FileSystemReader.getJsonById(name))
    note_title = CliInputPrompt.promptUserForString(
        CliInputPrompt.USER_MESSAGES[CliInputPrompt.NOTE_PROMPT[0]]
    )
    note = None
    for data in data_from_all_notes:
        if data["note_title"] == note_title:
            note = Note.createNoteFromJson(data)
            break
    if note != None:
        FileSystemHandler.delNote(note_id=note.note_id)


def actionChooser(num_of_action):
    fuction_loader = [
        createNoteFromCliInput,
        getListOfNotes,
        getNoteByName,
        changeNote,
        deleteNote,
        getListOfNotesByDates,
    ]
    return fuction_loader[num_of_action - 1]


if __name__ == "__main__":
    num_of_func = CliInputPrompt.initialActions()
    actionChooser(num_of_func)()
