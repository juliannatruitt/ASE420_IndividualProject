import re
from datetime import datetime
from Priority import Priority
from Query import Query
from Record import Record
import FullDescription
from Report import Report


class InputsValidator(object):

    def validate_length(self, inputs, expected_length):
        try:
            if len(inputs) == expected_length:
                return True
            else:
                raise ValueError("Wrong amount of inputs entered.")
        except ValueError as e:
            print(f"Error: {e}")
            return False

    def validate_date(self, date):
        try:
            pattern1 = r"^\d{4}/\d{2}/\d{2}$"
            if re.match(pattern1, date):
                return True
            elif date == 'today' or date == 'Today':
                return True
            else:
                raise ValueError("invalid date entered, use format YYYY/mm/dd")
        except ValueError as e:
            print(f"Error: {e}")
            return False

    def validate_tag(self, tag):
        try:
            if tag.startswith(":"):
                return True
            else:
                raise ValueError("tag entered incorrectly, it should begin with a ':'")
        except ValueError as e:
            print(f"Error: {e}")
            return False

    def check_all(self): pass


class InputsValidatorPriority(InputsValidator):
    def __init__(self, inputs, database):
        self.inputs = inputs
        self.connection = database

    def check_all(self):
        if self.validate_length(self.inputs, 1):
            Priority(self.connection).priority()


class InputsValidatorQuery(InputsValidator):
    def __init__(self, inputs, database):
        self.inputs = inputs
        self.connection = database

    def validate_keyword(self, keyword):
        try:
            if keyword.startswith("'") and keyword.endswith("'"):
                return True
            else:
                raise ValueError(
                    "Keyword to find entered incorrectly, ensure you are entering only one with with single quotations around it")
        except ValueError as e:
            print(f"Error: {e}")
            return False

    def check_all(self):
        if (self.validate_length(self.inputs, 1)) and (self.validate_date(self.inputs[0]) or
                                                       self.validate_tag(self.inputs[0]) or  # fix the above else statements from executing.
                                                       self.validate_keyword(self.inputs[0])):
            Query(self.inputs[0], self.connection).deciding_what_to_query()


class InputsValidatorRecord(InputsValidator):
    def __init__(self, inputs, database):
        self.inputs = inputs
        self.description = FullDescription.GetFullDescription(self.inputs[3:len(self.inputs) - 1]).get_description_input()
        self.connection = database

    def validate_length(self, inputs, expected_length):
        try:
            if len(inputs) >= expected_length:
                return True
            else:
                raise ValueError("Wrong amount of inputs entered.")
        except ValueError as e:
            print(f"Error: {e}")
            return False


    def validate_time(self, time):
        try:
            pattern1 = r"^\d{2}:\d{2}$"
            pattern2 = r"^\d{2}:\d{2}[ap]m$"
            pattern3 = r"^\d{1}:\d{2}$"
            pattern4 = r"^\d{1}:\d{2}[ap]m$"
            if re.match(pattern1, time) or re.match(pattern2, time) or re.match(pattern3, time) or re.match(pattern4,
                                                                                                            time):
                return True
            else:
                raise ValueError("Time entered incorrectly")
        except ValueError as e:
            print(f"Error: {e}")
            return False

    def validate_description(self, description):
        try:
            if description.startswith("'") and description[len(description) - 2].startswith(
                    "'"):  # -2 because last character is a space
                return True
            else:
                raise ValueError("description not entered in the right format. Make sure it starts with ' and ends with '")
        except ValueError as e:
            print(f"Error: {e}")
            return False

    def check_all(self):
        if (self.validate_length(self.inputs, 5) and
                self.validate_date(self.inputs[0]) and
                self.validate_time(self.inputs[1]) and
                self.validate_time(self.inputs[2]) and
                self.validate_description(self.description) and
                self.validate_tag(self.inputs[len(self.inputs) - 1])):

            Record(self.inputs[0], self.inputs[1], self.inputs[2], self.description,
                   self.inputs[len(self.inputs) - 1], self.connection).record()


class InputsValidatorReport(InputsValidator):
    def __init__(self, inputs, database):
        self.inputs = inputs
        self.connection = database

    def validate_start_date_to_end_date(self, start_date, end_date):
        def add_quotes_to_date_to_mainpluate(date_entered):
            new_date = f'"{date_entered}"'
            date = datetime.strptime(new_date, '"%Y/%m/%d"')
            return date

        try:
            start_date_in_quotes = add_quotes_to_date_to_mainpluate(start_date)
            end_date_in_quotes = add_quotes_to_date_to_mainpluate(end_date)
            difference = start_date_in_quotes - end_date_in_quotes
            if difference.days < 0:
                return True
            else:
                raise ValueError("The first date you enter needs to come before the second day you entered with at least one day "
                      "between the two")
        except ValueError as e:
            print(f"Error: {e}")
            return False

    def check_all(self):
        if (self.validate_length(self.inputs, 2) and
                self.validate_date(self.inputs[0]) and
                self.validate_date(self.inputs[1]) and
                self.validate_start_date_to_end_date(self.inputs[0], self.inputs[1])):

            Report(self.inputs[0], self.inputs[1], self.connection).report()

