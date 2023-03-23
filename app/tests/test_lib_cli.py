import unittest
from unittest.mock import patch
from lib_cli import UserInput, ConsolePrinter
from datetime import datetime


class TestUserInput(unittest.TestCase):
    test_input = "test input"
    test_date_str = "2023-01-01"

    def setUp(self) -> None:
        self.note_title = "test title"
        self.note_body = "test body"
        self.test_date = datetime(2023, 1, 1, 0, 0, 0, 0)
        self.test_data = {
            "note_title": self.note_title,
            "note_body": self.note_body,
            "start_date": self.test_date,
            "end_date": self.test_date,
        }
        self.test_message = "test message"

    def testInit(self) -> None:
        user_input = UserInput()
        self.assertIsInstance(user_input, UserInput)
        for key in self.test_data.keys():
            attr = getattr(user_input, key)
            self.assertEqual(type(attr), type(self.test_data[key]))

    @patch("builtins.input", return_value=test_input)
    def testSetUserInput(self, mock_input):
        user_input = UserInput()
        result = user_input.setUserInput()
        self.assertEqual(result, self.test_input)

    @patch("lib_cli.UserInput.setUserInput", return_value=test_input)
    def testSetTitle(self, mock_input):
        user_input = UserInput()
        user_input.setTitle()
        self.assertEqual(user_input.note_title, self.test_input)

    @patch("lib_cli.UserInput.setUserInput", return_value=test_date_str)
    def testSetDates(self, mock_input):
        user_input = UserInput()
        user_input.setDates()
        self.assertEqual(user_input.start_date, self.test_date)
        self.assertEqual(user_input.end_date, self.test_date)
