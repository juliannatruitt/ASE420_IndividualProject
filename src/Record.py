from datetime import date
from Table import ManipulateTables


class Record(object):
    def __init__(self, date_entered, start_time, end_time, description, tag, connection):
        self.date_entered = date_entered
        self._start_time = start_time
        self._end_time = end_time
        self._description = description
        self._tag = tag
        self._connection = connection

    def get_date(self):
        return self.date_entered

    def set_date(self, new_date):
        self.date_entered = new_date

    def get_start_time(self):
        return self._start_time

    def get_end_time(self):
        return self._end_time

    def get_description(self):
        return self._description

    def get_tag(self):
        return self._tag

    def set_tag(self, new_tag):
        self._tag = new_tag

    def get_database_connection(self):
        return self._connection

    def remove_colon_from_tag(self):
        if self.get_tag().startswith(":"):
            self.set_tag(self.get_tag()[1:])

    def record(self):
        self.remove_colon_from_tag()
        self.set_tag(self.get_tag().upper())
        if self.get_date().startswith("today") or self.get_date().startswith("Today"):
            self.set_date(date.today().strftime("%Y/%m/%d"))
        if ManipulateTables(self.get_database_connection()).check_if_table_is_created(self.get_tag()) is not None:
            ManipulateTables(self.get_database_connection()).insert_into_table(self.get_tag(), self.get_date(), self.get_start_time(), self.get_end_time(), self.get_description())
            print(f"recorded entry into table {self.get_tag()}")
        else:
            ManipulateTables(self.get_database_connection()).create_table(self.get_tag())
            ManipulateTables(self.get_database_connection()).insert_into_table(self.get_tag(), self.get_date(), self.get_start_time(), self.get_end_time(), self.get_description())
            print("table created and entry recorded")
            self.get_database_connection().get_connection().commit()

