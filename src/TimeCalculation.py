from datetime import datetime, timedelta


class TimeCalculation(object):

    def convert_string_to_time(self, time):
        time_as_string = f'"{time}"'
        if 'm' in time_as_string:  # because m is in am or pm
            time_stamp = datetime.strptime(time_as_string, '"%I:%M%p"')
        else:
            time_stamp = datetime.strptime(time_as_string, '"%I:%M"')
        return time_stamp

    def calculate_time_spent_doing_activity(self, start_time, end_time):
        start = self.convert_string_to_time(start_time)
        end = self.convert_string_to_time(end_time)
        if end < start:
            end += timedelta(days=1)
        time_spent_on_activity = end - start
        return time_spent_on_activity

