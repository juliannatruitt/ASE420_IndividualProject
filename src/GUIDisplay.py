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


