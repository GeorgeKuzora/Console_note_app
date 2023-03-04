import unittest
from lib import *


class TestUserInputPrompt(unittest.TestCase):

    def testPromptUserForString(self):
        test_string = UserInputPrompt.promptUserForString("Input 'test': ")
        self.assertEqual(test_string, "test")

    def testHandleUserInputExeptions(self):
        test_string = UserInputPrompt.handleUserInputExeptions("test")
        self.assertEqual(test_string, "test")
        empty_string = UserInputPrompt.handleUserInputExeptions("")
        self.assertFalse(empty_string)

    def testGetClearUserInput(self):
        test_string = UserInputPrompt.getClearUserInput("Input test: ")
        self.assertEqual(test_string, "test")
        empty_string = UserInputPrompt.getClearUserInput("Press Enter")
        self.assertFalse(empty_string)
