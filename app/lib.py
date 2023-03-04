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
