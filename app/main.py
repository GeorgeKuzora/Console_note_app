import lib
import lib_cli
import lib_file_system


def createNoteFromCliInput():
    cli_input_stream = lib_cli.CliInputPrompt.getCliInputStream()
    note_obj = lib.Note.createNote(cli_input_stream)
    file_system_stream = note_obj.getFileSystemStream()
    lib_file_system.FileSystemHandler.saveNote(file_system_stream)


if __name__ == '__main__':
    createNoteFromCliInput()
