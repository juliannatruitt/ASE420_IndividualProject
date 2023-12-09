import src.TimeCalculation as TimeCalculation
from datetime import datetime, timedelta
import unittest


class TestPriority(unittest.TestCase):

    def test_correct_time_is_returned(self):
        time_passed = TimeCalculation.TimeCalculation().calculate_time_spent_doing_activity('3:00pm', '6:00pm')
        expected_time_passed = timedelta(hours=3)

        self.assertEqual(time_passed, expected_time_passed)


if __name__ == '__main__':
    unittest.main()

'''
-----------------------------------------------------------------------
OUTPUT: (using --> 'python -m unittest test.test_timecalculation' in terminal)
----------------------------------------------------------------------- 

Ran 1 test in 0.004s

OK

'''