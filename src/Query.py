from Table import GetDataFromTables
from datetime import date
from GUIDisplay import DisplayQuery


class Query(object):
    def __init__(self, query_value, database):
        self._query_value = query_value
        self._connection = database

    def get_query(self):
        return self._query_value

    def set_query(self, new_query):
        self._query_value = new_query

    def get_database_connection(self):
        return self._connection

    def query_tag(self, table):
        self.set_query(self.get_query()[1:].upper())
        show_table = table.get_table(self.get_query())
        if bool(show_table):
            DisplayQuery(show_table, self.get_query()).display_table()

    def query_task(self, table):

        self.set_query(self.get_query().replace("'", "", 2))
        get_rows = table.get_rows(self.get_query(), 3)
        if bool(get_rows):
            DisplayQuery(get_rows, self.get_query()).display_rows()

    def query_date(self, table):
        if self.get_query().startswith("today") or self.get_query().startswith("Today"):
            self.set_query(date.today().strftime("%Y/%m/%d"))
        get_rows = table.get_rows(self.get_query(), 0)
        if bool(get_rows):
            DisplayQuery(get_rows, self.get_query()).display_rows()

    def deciding_what_to_query(self):
        table = GetDataFromTables(self.get_database_connection())
        try:
            if self.get_query().startswith(":"):
                self.query_tag(table)
            elif self.get_query().startswith("'"):
                self.query_task(table)
            elif self.get_query()[0].isdigit or self.get_query().startswith("today") or self.get_query().startswith(
                "Today"):
                self.query_date(table)
            else:
                raise ValueError("Invalid Query. Check to make sure you syntax is corrected")
        except ValueError as e:
            print(f"Error: {e}")

