from src.CheckInputValues import InputsValidatorRecord,InputsValidatorPriority,InputsValidatorReport,InputsValidatorQuery
from src.Connection import CreateConnection
import unittest
from io import StringIO
import sys


class TestPriority(unittest.TestCase):
    connection = CreateConnection()

    def test_valid_recordinputs_successfully_records(self):
        valid_record = InputsValidatorRecord(["today", "8:00pm", "10:00pm", "'Hangout with Friends'", ":FRIENDS"], self.connection)

        captured_output = StringIO()
        sys.stdout = captured_output

        valid_record.check_all()
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip()

        exepcted_output = "recorded entry into table FRIENDS"

        self.assertEqual(output, exepcted_output)

    def test_invalid_recordinputs_unsuccessfully_records(self):
        #incorrect date format makes record invalid
        invalid_record = InputsValidatorRecord(["12/07/2023", "8:00pm", "10:00pm", "'Hangout with Friends'", ":FRIENDS"],
                                               self.connection)
        captured_output = StringIO()
        sys.stdout = captured_output

        invalid_record.check_all()
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip()

        exepcted_output = "Error: invalid date entered, use format YYYY/mm/dd"

        self.assertEqual(output, exepcted_output)

    def test_invalid_queryinputs_unsuccessfully_execute(self):
        invalid_query = InputsValidatorQuery(['12/25/2023', 'secondparameter'], self.connection)

        captured_output = StringIO()
        sys.stdout = captured_output

        invalid_query.check_all()
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip()

        exepcted_output = "Error: Wrong amount of inputs entered."

        self.assertEqual(output, exepcted_output)

    def test_invalid_priorityinputs_unsuccessfully_executes(self):
        invalid_query = InputsValidatorPriority(['only parameter should be priority', 'sdjsdjs'], self.connection)

        captured_output = StringIO()
        sys.stdout = captured_output

        invalid_query.check_all()
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip()

        expected_output = "Error: Wrong amount of inputs entered."

        self.assertEqual(output, expected_output)


    def test_invalid_report_inputs_unsuccessfully_executes(self):
        invalid_query = InputsValidatorReport(['01/01/2023', '12/31/2023'], self.connection)

        captured_output = StringIO()
        sys.stdout = captured_output

        invalid_query.check_all()
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip()

        expected_output = "Error: invalid date entered, use format YYYY/mm/dd"

        self.assertEqual(output, expected_output)



if __name__ == '__main__':
    unittest.main()

'''
------------------------------------------------------------------------
OUTPUT (using --> 'python -m unittest test.test_input_values' in terminal)
------------------------------------------------------------------------

Ran 5 tests in 0.006s

OK


'''


