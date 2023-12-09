import tkinter as tk
from tkinter import ttk


class DisplayReport(object):

    def display_report(self, start_date, end_date, date_range):
        popup = tk.Tk()
        popup.title(f"Reported Entries from {start_date} to {end_date}")

        tree = ttk.Treeview(popup, columns=("Date", "StartTime", "EndTime", "Task"), show="headings")

        tree.heading("Date", text="Date")
        tree.heading("StartTime", text="Start Time")
        tree.heading("EndTime", text="End Time")
        tree.heading("Task", text="Task")

        for date in date_range:
            tree.insert("", "end", values=date)

        tree.pack(padx=10, pady=10)
        popup.mainloop()


class DisplayQuery(object):
    def __init__(self, data_array, query_type):
        self.data_array = data_array
        self.query_type = query_type

    def display_table(self):

        popup = tk.Tk()
        popup.title(f"Query Table: {self.query_type}")

        tree = ttk.Treeview(popup, columns=("Date", "StartTime", "EndTime", "Task"), show="headings")

        tree.heading("Date", text="Date")
        tree.heading("StartTime", text="Start Time")
        tree.heading("EndTime", text="End Time")
        tree.heading("Task", text="Task")

        for data in self.data_array:
            tree.insert("", "end", values=data)

        tree.pack(padx=10, pady=10)
        popup.mainloop()

    def display_rows(self):

        popup = tk.Tk()
        popup.title(f"Query Rows that Contain Value: {self.query_type}")

        tree = ttk.Treeview(popup, columns=("Date", "StartTime", "EndTime", "Task"), show="headings")

        tree.heading("Date", text="Date")
        tree.heading("StartTime", text="Start Time")
        tree.heading("EndTime", text="End Time")
        tree.heading("Task", text="Task")

        for data in self.data_array:
            tree.insert("", "end", values=data)

        tree.pack(padx=10, pady=10)
        popup.mainloop()


'''
class DisplayPriority(object):
    def __init__(self, dict_of_top_priorities, top_table_dict):
        popup = tk.Tk()
        popup.title("Priorities")

        text_widget = scrolledtext.ScrolledText(popup, width=70, height=20)
        text_widget.pack(padx=10, pady=10)

        entries_info = f"Time most spend doing tasks in the tag: {top_table_dict['table_name']} -->  {top_table_dict['hours']} hours:\n\n"
        entries_info += f"Three top activites: \n\n"

        for dict in dict_of_top_priorities:
            key = dict["Key"]
            top_dict = dict["Dict1"]
            second_dict  = dict["Dict2"]
            third_dict = dict["Dict3"]


            entries_info += f"{key}, {top_dict}, {second_dict}, {third_dict}"
            entries_info += "\n"

        text_widget.insert(tk.END, entries_info)
        text_widget.config(state=tk.DISABLED)

        popup.mainloop()

'''

'''        

 popup = tk.Tk()
        popup.title("Query Entries")

        text_widget = scrolledtext.ScrolledText(popup, width=70, height=20)
        text_widget.pack(padx=10, pady=10)

        entries_info = f"Query entries from table {self.query_type}:\n\n"

        for date in self.data_array:
            entries_info += "\t".join(date)
            entries_info += "\n"
        text_widget.insert(tk.END, entries_info)

        text_widget.config(state=tk.DISABLED)

        popup.mainloop()
        
        
        popup = tk.Tk()
        popup.title("Query Entries")

        text_widget = scrolledtext.ScrolledText(popup, width=70, height=20)
        text_widget.pack(padx=10, pady=10)

        entries_info = f"Query entries with value {self.query_type}:\n\n"

        for date in self.data_array:
            entries_info += "\t".join(date)
            entries_info += "\n"
        text_widget.insert(tk.END, entries_info)

        text_widget.config(state=tk.DISABLED)

popup.mainloop()

'''

