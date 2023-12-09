from Table import CalculateTimeSpentInTables


class Priority(object):
    def __init__(self, connection):
        self._connection = connection

    def get_database_connection(self):
        return self._connection

    def print_top_three_activities(self):
        table = CalculateTimeSpentInTables(self.get_database_connection())
        top_activity = table.row_of_most_time_spent()
        second_activity = table.next_row_of_most_time_spent(top_activity)
        third_activity = table.next_row_of_most_time_spent(second_activity)

    def print_top_table(self):
        table = CalculateTimeSpentInTables(self.get_database_connection())
        table.table_you_spent_the_most_time_on()

    def priority(self):
        self.print_top_table()
        self.print_top_three_activities()
