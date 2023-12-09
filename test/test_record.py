# review to make better tests! figure out issues??!
import unittest
from src.Record import Record
from src.Connection import CreateConnection
from io import StringIO
import sys


class TestRecord(unittest.TestCase):
    connection = CreateConnection()
    record = Record('2023/11/29', '11:30am', '2:00pm', "'Study for finals'", ':STUDY', connection)

    def test_date_return_correctly(self):
        self.assertEqual(self.record.get_date(), '2023/11/29')

    def test_starttime_return_correctly(self):
        self.assertEqual(self.record.get_start_time(), '11:30am')

    def test_endtime_return_correctly(self):
        self.assertEqual(self.record.get_end_time(), '2:00pm')

    def test_description_return_correctly(self):
        self.assertEqual(self.record.get_description(), "'Study for finals'")

    def test_remove_colon_from_tag_returns_correctly(self):
        self.record.remove_colon_from_tag()
        self.assertEqual(self.record.get_tag(), 'STUDY')

    def test_that_record_adds_to_an_already_created_table(self):
        record = Record('2023/11/29', '1:00pm', '2:00pm', "'do ase420 homework'", ':STUDY', self.connection)

        captured_output = StringIO()
        sys.stdout = captured_output

        record.record()
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip()
        output_we_want = f"recorded entry into table {record.get_tag()}"

        self.assertEqual(output, output_we_want)

    # this test works only once, because after the first run a table is already created so if you do not put a new
    # TAG, it will fail.
    def test_that_records_creates_new_table_entry_that_includes_a_table_that_doesnt_exist(self):
        record = Record('2023/12/25', '1:00pm', '8:00pm', "'Celebrate Christmas'", ':CHRISTMASTIMEISHERE', self.connection)

        captured_output = StringIO()
        sys.stdout = captured_output

        record.record()
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip()
        output_we_want = "table created and entry recorded"

        self.assertEqual(output, output_we_want)


if __name__ == '__main__':
    unittest.main()


'''
----------------------------------------------------------------------
OUTPUT: (using -- > "python -m unittest test.test_record" in terminal)
-----------------------------------------------------------------------

Ran 7 tests in 0.001s                                                 
                                                                      
OK   
'''

