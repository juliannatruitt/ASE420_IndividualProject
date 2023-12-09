from datetime import timedelta, datetime
from Table import GetDataFromTables
from GUIDisplay import DisplayReport


class Report(object):
    def __init__(self, start_date, end_date, connection):
        self._start_date = start_date
        self._end_date = end_date
        self._connection = connection

    def get_start_date(self):
        return self._start_date

    def get_end_date(self):
        return self._end_date

    def get_database_connection(self):
        return self._connection

    def add_quotes_to_date_to_mainpluate(self, date_entered):
        new_date = f'"{date_entered}"'
        date = datetime.strptime(new_date, '"%Y/%m/%d"')
        return date

    def get_all_dates_between(self):
        list_of_dates = []
        current_date = self.add_quotes_to_date_to_mainpluate(self.get_start_date())
        end_date = self.add_quotes_to_date_to_mainpluate(self.get_end_date())
        while current_date <= end_date:
            list_of_dates.append(current_date.strftime("%Y/%m/%d"))
            current_date += timedelta(days=1)
        return list_of_dates

    def report(self):
        date_range = self.get_all_dates_between()
        all_rows = GetDataFromTables(self.get_database_connection()).get_rows_within_a_range_of_dates(date_range)
        DisplayReport().display_report(self.get_start_date(), self.get_end_date(), all_rows)
