import sqlite3
from datetime import date, timedelta, datetime
import re
import argparse

class CreateConnection(object):
    def __init__(self, database_name):
        self._connect = sqlite3.connect(database_name)

    def get_connection(self):
        return self._connect

    def cursor(self):
        return self.get_connection().cursor()


class Record(object):
    def __init__(self, dateEntered, starttime, endtime, description, tag, connection):
        self._dateEntered = dateEntered
        self._starttime = starttime
        self._endtime = endtime
        self._description = description
        self._tag = tag
        self._connection = connection

    def get_date(self):
        return self._dateEntered

    def set_date(self, newDate):
        self._dateEntered = newDate

    def get_starttime(self):
        return self._starttime

    def get_endtime(self):
        return self._endtime

    def get_description(self):
        return self._description

    def get_tag(self):
        return self._tag

    def set_tag(self, new_tag):
        self._tag = new_tag

    def get_database(self):
        return self._connection

    def remove_colon_from_tag(self):
        if self.get_tag().startswith(":"):
            self.set_tag(self.get_tag()[1:])

    def recordTable(self):
        self.remove_colon_from_tag()
        if self.get_date().startswith("today") or self.get_date().startswith("Today"):
            self.set_date(date.today().strftime("%Y/%m/%d"))
        if self.checkIfTableAlreadyCreated() is not None:
            self.insertIntoTable()
        else:
            self.createTable()
            self.insertIntoTable()
            print("table created and entry recorded")
            self.get_database().get_connection().commit()

    def insertIntoTable(self):
        self.get_database().cursor().execute(f"""INSERT into {self.get_tag()} (date, starttime, endtime, description) 
                                            VALUES('{self.get_date()}','{self.get_starttime()}','{self.get_endtime()}', {self.get_description()})""")
        print(f"recorded entry into table {self.get_tag()}")
        self.get_database().get_connection().commit()

    def checkIfTableAlreadyCreated(self):
        return self.get_database().cursor().execute(
            f"""SELECT name FROM sqlite_master WHERE type='table' AND name='{self.get_tag()}'""").fetchone()

    def createTable(self):
        self.get_database().cursor().execute(f"""CREATE TABLE {self.get_tag()}(
                            date text,
                            starttime text,
                            endtime text,
                            description text)""")
        print("table created")
        self.get_database().get_connection().commit()


class Query(object):
    def __init__(self, query_value, database):
        self._query_value = query_value
        self._database = database

    def get_query(self):
        return self._query_value

    def set_query(self, new_query):
        self._query_value = new_query

    def get_database(self):
        return self._database

    def deciding_what_to_query(self):
        if self.get_query().startswith(":"):
            self.set_query(self.get_query()[1:])
            self.query_tag()
        elif self.get_query().startswith("'") or self.get_query().startswith("\""):
            self.set_query(self.get_query().replace("\"", "", 2))
            self.set_query(self.get_query().replace("'", "", 2))
            self.query_description()
        elif self.get_query()[0].isdigit or self.get_query().startswith("today") or self.get_query().startswith(
                "Today"):
            if self.get_query().startswith("today") or self.get_query().startswith("Today"):
                self.set_query(date.today().strftime("%Y/%m/%d"))
            self.query_date()
        else:
            print("error in the query you entered. Check to make sure you syntax is corrected")

    def query_tag(self):
        table_created_or_not = self.checkIfTableAlreadyCreated()
        if table_created_or_not:
            rows = self.get_database().cursor().execute(f"SELECT * FROM {self.get_query()}").fetchall()
            for row in rows:
                print(row)
        else:
            print("tag does not exist!, create that tag using the record command")

    def query_description(self):
        # fix variable issue!!!!!! has to do with what is being fetched from cursor!!!!
        alltables = self.get_database().cursor().execute("SELECT name FROM sqlite_master WHERE type='table'")
        for tablerow in alltables.fetchall():
            table = tablerow[0]
            alltables.execute(f"SELECT * FROM {table}")
            for row in alltables:
                # if the descrition in row 3 (the column with the descrition), display the row
                if self.get_query() in row[3]:
                    print(row)

    def query_date(self):
        row_returned = False  # FIX THIS!!!!!!!
        alltables = self.get_database().cursor().execute("SELECT name FROM sqlite_master WHERE type='table'")
        for tablerow in alltables.fetchall():
            table = tablerow[0]
            alltables.execute(f"SELECT * FROM {table}")
            for row in alltables:
                if self.get_query() == row[0]:
                    print(row)
                    row_returned = True
        if not row_returned:
            print("You entered a date that has no records. Try again")

    def checkIfTableAlreadyCreated(self):
        return self.get_database().cursor().execute(
            f"""SELECT name FROM sqlite_master WHERE type='table' AND name='{self.get_query()}'""").fetchone()


class GetFullDescription(object):
    def __init__(self, description):
        self._description = description

    def get_description_input(self):
        total_lines_of_description = ''
        for x in range(0, len(self._description)):
            total_lines_of_description += self._description[x] + ' '
        return total_lines_of_description


class CheckInputValuesRecord(object):
    def __init__(self, argument):
        self.argument = argument
        self.description = GetFullDescription(self.argument[3:len(self.argument) - 1]).get_description_input()
        self.connection = CreateConnection("ver2_database.db")

    def isValidLength(self):
        isValid = False
        if len(self.argument) >= 5: #since i took record off the check since it checks before running this!
            isValid = True
        else:
            print("Did not include enough information in your record, review format and try again")
        return isValid

    def date_entered_correctly(self, index):
        isValid = False
        pattern1 = r"^\d{4}/\d{2}/\d{2}$"
        if re.match(pattern1, index):
            isValid = True
        elif index == 'today' or index == 'Today':
            isValid = True

        else:
            print("invalid date entered, user format YYYY/mm/dd")
        return isValid

    def get_correct_time_entered(self, index):
        isValid = False
        pattern1 = r"^\d{2}:\d{2}$"
        pattern2 = r"^\d{2}:\d{2}[ap]m$"
        pattern3 = r"^\d{1}:\d{2}$"
        pattern4 = r"^\d{1}:\d{2}[ap]m$"
        if re.match(pattern1, index) or re.match(pattern2, index) or re.match(pattern3, index) or re.match(pattern4, index):
            isValid = True
        return isValid

    def check_description(self):
        isValid = False
        if self.description.startswith("'") and self.description[len(self.description)-2].startswith("'"): #-2 because last character is a space
            isValid = True
        else:
            print("description not entered in the right format. Make sure it starts with ' and ends with '")
        return isValid

    def check_tag(self):
        isValid = False
        if self.argument[len(self.argument) - 1].startswith(":"):
            isValid = True
        else:
            print("tag entered incorrectly, make sure to put a : beforehand")
        return isValid

    def check_all(self):
        if (self.isValidLength() and self.date_entered_correctly(self.argument[0]) and
                self.get_correct_time_entered(self.argument[1]) and self.get_correct_time_entered(self.argument[2]) and
                self.check_description() and self.check_tag()):
            Record(self.argument[0], self.argument[1], self.argument[2], self.description,
                   self.argument[len(self.argument) - 1],
                   self.connection).recordTable()


class Report(object):
    def __init__(self, startdate, enddate, connection):
        self.startdate = startdate
        self.enddate = enddate
        self.connection = connection

    def get_start_date(self):
        return self.startdate
    def get_end_date(self):
        return self.enddate

    #first, make sure start date comes before the end date!
    def check_startdate_to_enddate_isvalid(self):
        startdate_in_quotes = self.add_quotes_to_date_to_mainpluate(self.startdate)
        enddate_in_quotes = self.add_quotes_to_date_to_mainpluate(self.enddate)
        difference = startdate_in_quotes - enddate_in_quotes
        if difference.days < 0:
            return True
        else:
            print("The first date you enter needs to come before the second day you entered with at least one day "
                  " between the two")
            return False

    #get all dates between start and end date
    def get_all_dates_between(self):
        if self.check_startdate_to_enddate_isvalid():
            list_of_dates = []
            current_date = self.add_quotes_to_date_to_mainpluate(self.startdate)
            end_date = self.add_quotes_to_date_to_mainpluate(self.enddate)
            while current_date <= end_date:
                list_of_dates.append(current_date.strftime("%Y/%m/%d"))
                current_date += timedelta(days=1)
            return list_of_dates
        else:
            return None

    def add_quotes_to_date_to_mainpluate(self, date_entered): #could use the code smell: dont change arguments!! and inline because i had two of the same methods!!
        new_date = f'"{date_entered}"'
        date = datetime.strptime(new_date, '"%Y/%m/%d"')
        return date

    #third, search all tables for the dates and display any that appear in a table:
    def show_tables_within_dates(self):
        all_dates = self.get_all_dates_between()
        row_returned = False  # FIX THIS!!!!!!!
        alltables = self.connection.cursor().execute("SELECT name FROM sqlite_master WHERE type='table'")
        for tablerow in alltables.fetchall():
            table = tablerow[0]
            alltables.execute(f"SELECT * FROM {table}")
            for row in alltables:
                for date in all_dates:
                    if date == row[0]:
                        print(row)
                        row_returned = True
        if not row_returned:
            print("There are no records between those dates. Try to enter in different dates!")


class Priority(object):
    def __init__(self, connection):
        self.connection = connection

    def convert_string_to_time(self, time):
        time_as_string = f'"{time}"'
        if 'm' in time_as_string:   # becuase m is in am or pm
            time_stamp = datetime.strptime(time_as_string, '"%I:%M%p"')
        else:
            time_stamp = datetime.strptime(time_as_string, '"%I:%M"')
        return time_stamp

    def go_through_all_tables_in_database(self):
        maximum_time = timedelta()
        table_name_of_time_most_spent = ""
        alltables = self.connection.cursor().execute("SELECT name FROM sqlite_master WHERE type='table'")
        for table in alltables.fetchall():
            table_name = table[0]
            alltables.execute(f"SELECT * FROM {table_name}")
            total_time_in_current_table = timedelta()
            for row in alltables:
                time_start = self.convert_string_to_time(row[1])
                time_end = self.convert_string_to_time(row[2])
                if time_end < time_start:
                    time_end += timedelta(days=1)
                time_spent_on_activity = time_end - time_start
                total_time_in_current_table += time_spent_on_activity
            if total_time_in_current_table > maximum_time:
                maximum_time = total_time_in_current_table
                table_name_of_time_most_spent = table_name
        print(f"Time most spend in table: {table_name_of_time_most_spent} with a time of: {maximum_time}")


class ParserClass(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser()

    def get_array_of_users_input_from_cmd(self):
        self.parser.add_argument("get_amount_of_inputs", type=str, nargs='+')
        args = self.parser.parse_args()
        return args.get_amount_of_inputs


if __name__ == "__main__":

    parser1 = ParserClass()
    user_inputs = parser1.get_array_of_users_input_from_cmd()

    if user_inputs[0] == "query" or user_inputs[0] == "Query" or user_inputs[0] == "QUERY":
        connection = CreateConnection("ver2_database.db")
        Query(user_inputs[len(user_inputs) - 1], connection).deciding_what_to_query()

    elif user_inputs[0] == "record" or user_inputs[0] == "Record" or user_inputs[0] == "RECORD":
        CheckInputValuesRecord(user_inputs[1:]).check_all()

    elif user_inputs[0] == "report" or user_inputs[0] == "Report" or user_inputs[0] == "REPORT":
        connection = CreateConnection("ver2_database.db")
        Report(user_inputs[1], user_inputs[2], connection).show_tables_within_dates() # make a check inputs for report and query and priority!

    elif user_inputs[0] == "priority" or user_inputs[0] == "PRIORITY":
        connection = CreateConnection("ver2_database.db")
        Priority(connection).go_through_all_tables_in_database()

    else:
        print("incorrectly entered a record or query. Check syntax and try again")


#add to user manual:
#   -when using record: make sure the first date entered comes before the second date entered!
#   -if you dont use am or pm, use miliraty time so that priority command works.