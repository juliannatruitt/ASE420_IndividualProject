import unittest
from src.Priority import Priority
from src.Connection import CreateConnection
from io import StringIO
import sys


class TestPriority(unittest.TestCase):
    connection = CreateConnection()

    def test_string_returns_date(self):
        priority = Priority(self.connection)

        captured_output = StringIO()
        sys.stdout = captured_output

        priority.print_top_table()

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip()
        output_we_want = "Time most spend doing tasks in the tag: FRIENDS -->  2 days, 22:00:00 hours"

        self.assertEqual(output, output_we_want)


if __name__ == '__main__':
    unittest.main()


'''
------------------------------------------------------------------------
OUTPUT (using --> 'python -m unittest test.test_priority' in terminal)
------------------------------------------------------------------------

Ran 1 test in 0.007s

OK


'''
