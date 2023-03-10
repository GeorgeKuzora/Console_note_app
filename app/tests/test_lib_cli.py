import unittest
from lib_cli import *


class TestCliInput(unittest.TestCase):

    def testGetCliInputStream(self):
        print("In the next prompts input: 'title' 'body'")
        test_cli_input_stream = CliInputPrompt.getCliInputStream()
        self.assertTrue(type(test_cli_input_stream) == type({"thisis": "dict"}))
        self.assertTrue('title' in test_cli_input_stream.values()
                        and 'body' in test_cli_input_stream.values())
