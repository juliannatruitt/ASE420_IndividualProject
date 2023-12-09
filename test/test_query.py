import unittest
from src.Query import Query
from src.Connection import CreateConnection
from io import StringIO
import sys


class TestQuery(unittest.TestCase):
    connection = CreateConnection()


    # tag is in the database already
    def test_tag_query_with_valid_tag(self):
        query = Query(':STUDY', self.connection)

        captured_output = StringIO()
        sys.stdout = captured_output

        query.deciding_what_to_query()

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip()
        output_we_dont_want = "tag does not exist!, create that tag using the record command"

        self.assertNotEqual(output, output_we_dont_want)

    # tag(table) is not in the database
    def test_tag_query_with_invalid_tag(self):
        query = Query(':HAHA', self.connection)

        captured_output = StringIO()
        sys.stdout = captured_output

        query.deciding_what_to_query()

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip()
        output_we_want = "Error: tag does not exist!, create that tag using the record command"

        self.assertEqual(output, output_we_want)

    def test_date_query_with_invalid_date(self):
        query = Query('2023/12/31', self.connection)

        captured_output = StringIO()
        sys.stdout = captured_output

        query.deciding_what_to_query()

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip()
        output_we_want = "Error: No records of the value given in the database!"

        self.assertEqual(output, output_we_want)

    def test_valid_query(self):
        query = Query('study', self.connection)

        captured_output = StringIO()
        sys.stdout = captured_output

        query.deciding_what_to_query()

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip()
        output_we_dont_want = "error in the query you entered. Check to make sure you syntax is corrected"

        self.assertNotEqual(output, output_we_dont_want)


    #given: that the date is recorded in the database already
    def test_date_query_value_returned_correctly(self):
        query = Query('2023/12/25', self.connection)
        returned_query_values = query.get_query()

        self.assertEqual('2023/12/25', returned_query_values)

    def test_tag_query_value_returned_correctly(self):
        query = Query(':WORK', self.connection)
        returned_query_values = query.get_query()

        self.assertEqual(':WORK', returned_query_values)


if __name__ == '__main__':
    unittest.main()


'''
-------------------------------------------------------------------------
OUTPUT: from running -> 'python -m unittest test.test_query' in Terminal
--------------------------------------------------------------------------


Ran 6 tests in 2.151s

OK


'''