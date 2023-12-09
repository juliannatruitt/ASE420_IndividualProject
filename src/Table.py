from datetime import timedelta
from TimeCalculation import TimeCalculation


class ManipulateTables(object):
    def __init__(self, connection):
        self._connection = connection

    def get_database_connection(self):
        return self._connection

    def check_if_table_is_created(self, tag):
        return self.get_database_connection().cursor().execute(
            f"""SELECT name FROM sqlite_master WHERE type='table' AND name='{tag}'""").fetchone()

    def create_table(self, tag):
        self.get_database_connection().cursor().execute(f"""CREATE TABLE {tag}(
                            date text,
                            starttime text,
                            endtime text,
                            description text)""")
        self.get_database_connection().get_connection().commit()

    def insert_into_table(self, tag, date, start_time, end_time, description):
        self.get_database_connection().cursor().execute(f"""INSERT into {tag} (date, starttime, endtime, description) 
                                            VALUES('{date}','{start_time}','{end_time}', {description})""")
        self.get_database_connection().get_connection().commit()


class GetDataFromTables(object):
    def __init__(self, connection):
        self._connection = connection

    def get_database_connection(self):
        return self._connection

    def get_table(self, tag):
        try:
            table_created_or_not = ManipulateTables(self.get_database_connection()).check_if_table_is_created(tag)
            all_rows_in_table = []
            if table_created_or_not:
                rows = self.get_database_connection().cursor().execute(f"SELECT * FROM {tag}").fetchall()
                for row in rows:
                    all_rows_in_table.append(row)
            else:
                raise ValueError("tag does not exist!, create that tag using the record command")
        except ValueError as e:
            print(f"Error: {e}")
            return None
        return all_rows_in_table

    def get_rows(self, value_to_find, index_of_column_in_table_that_value_type_is_located):
        try:
            row_returned = False
            rows_that_contain_the_given_value = []
            all_tables = self.get_database_connection().cursor().execute("SELECT name FROM sqlite_master WHERE type='table'")
            for table_row in all_tables.fetchall():
                table = table_row[0]
                all_tables.execute(f"SELECT * FROM {table}")
                for row in all_tables:
                    if value_to_find in row[index_of_column_in_table_that_value_type_is_located]:
                        rows_that_contain_the_given_value.append(row)
                        row_returned = True
            if not row_returned:
                raise ValueError("No records of the value given in the database!")
        except ValueError as e:
            print(f"Error: {e}")
            return None
        return rows_that_contain_the_given_value

    def get_rows_within_a_range_of_dates(self, range_of_dates):
        try:
            row_returned = False
            all_rows = []
            all_tables = self.get_database_connection().cursor().execute("SELECT name FROM sqlite_master WHERE type='table'")
            for table_row in all_tables.fetchall():
                table = table_row[0]
                all_tables.execute(f"SELECT * FROM {table}")
                for row in all_tables:
                    for date in range_of_dates:
                        if date == row[0]:
                            all_rows.append(row)
                            row_returned = True
            if not row_returned:
                raise ValueError("There are no records between those dates. Try to enter in different dates!")
        except ValueError as e:
            print(f"Error: {e}")
            return None
        return all_rows


class CalculateTimeSpentInTables(object):
    def __init__(self, connection):
        self._connection = connection

    def get_database_connection(self):
        return self._connection

    def table_you_spent_the_most_time_on(self):
        maximum_time = timedelta()
        table_name_of_time_most_spent = ""
        all_tables = self.get_database_connection().cursor().execute("SELECT name FROM sqlite_master WHERE type='table'")
        for table in all_tables.fetchall():
            table_name = table[0]
            all_tables.execute(f"SELECT * FROM {table_name}")
            total_time_in_current_table = timedelta()
            for row in all_tables:
                total_time_in_current_table += TimeCalculation().calculate_time_spent_doing_activity(row[1], row[2])
            if total_time_in_current_table > maximum_time:
                maximum_time = total_time_in_current_table
                table_name_of_time_most_spent = table_name
        print(f"Time most spend doing tasks in the tag: {table_name_of_time_most_spent} -->  {maximum_time} hours")

    def row_of_most_time_spent(self):
        maximum_time = timedelta()
        activity = ""
        table_of_activity = ""
        all_tables = self.get_database_connection().cursor().execute("SELECT name FROM sqlite_master WHERE type='table'")
        for table in all_tables.fetchall():
            table_name = table[0]
            all_tables.execute(f"SELECT * FROM {table_name}")
            for row in all_tables:
                time_spent_on_activity = TimeCalculation().calculate_time_spent_doing_activity(row[1], row[2])
                if time_spent_on_activity > maximum_time:
                    maximum_time = time_spent_on_activity
                    activity = f"{row[3]}"
                    table_of_activity = table_name
        print(f"Activity you spent the most time on is: '{activity}' in the {table_of_activity} tag-->  {maximum_time} hours")
        return maximum_time

    # before you use this method, make sure you use the "get_row_most_time_spent" method first and put the results as
    # the parameter of this method.
    def next_row_of_most_time_spent(self, most_spent_activity):
        maximum_time = timedelta()
        activity = ""
        table_of_activity = ""
        all_tables = self.get_database_connection().cursor().execute("SELECT name FROM sqlite_master WHERE type='table'")
        for table in all_tables.fetchall():
            table_name = table[0]
            all_tables.execute(f"SELECT * FROM {table_name}")
            for row in all_tables:
                time_spent_on_activity = TimeCalculation().calculate_time_spent_doing_activity(row[1], row[2])
                if time_spent_on_activity >= most_spent_activity:
                    continue
                if time_spent_on_activity > maximum_time:
                    maximum_time = time_spent_on_activity
                    activity = f"{row[3]}"
                    table_of_activity = table_name
        print(f"Activity you spent the next most time on is: '{activity}' in the {table_of_activity} tag-->  {maximum_time} hours")
        return maximum_time

