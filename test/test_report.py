import unittest
from src.Report import Report
from src.Table import GetDataFromTables
from src.Connection import CreateConnection


class TestReport(unittest.TestCase):
    connection = CreateConnection()
    table = GetDataFromTables(connection)

    def test_invalid_dates_between_returns_empty_array(self):
        report = Report('2023/11/20', '2023/11/05', self.connection)
        isValid = report.get_all_dates_between()
        self.assertEquals(isValid, [])
        #self.assertFalse(isValid)

    def test_get_all_dates_between_dates_works(self):
        report = Report('2023/11/14', '2023/11/26', self.connection)
        isValid = report.get_all_dates_between()
        self.assertIsNotNone(isValid)


if __name__ == '__main__':
    unittest.main()


'''
-----------------------------------------------------------------------
OUTPUT: (using --> 'python -m unittest test.test_report' in terminal)
-----------------------------------------------------------------------                                                                                                          

Ran 2 tests in 0.005s

OK

'''