### Version 1 User Manual
## Rules that apply to all commands:
* Use the CMD to enter in all the different commands.
* When entering in a date, use the format yyyy/mm/dd, otherwise you will be displayed with an error to put the date in the right format
* Once you locate the folder that the program is located in, make sure to run "python main.py" before you enter query, record, priority, or report.
* NOTE: when i give examples of what different commands look like, I enclose them in quotation marks (""), you should not include those quotation marks when you are entering in your command on the CMD.
## Query:
* When querying a tag, you need to make sure you add a colon (:) before the tag. You can write the tag in all uppercase or lowercase, it doesnt matter.
## Record:
## report
* A report should be of length 3.
* An example of a report is: "report 2023/11/05 2023/11/26"
* When making a report the first date must come before the second date or you will recive an error to fix your input.
* Dates must be in correct format (yyyy/mm/dd).
* You will be returned the rows of each table in the database that has a date recorded within those dates.
## priority
* A priority should be of length 1.
* An example is: "priority" (thats the only way to run this command)
* You will be returned the table (the tag) in which you have recorded most of you time to.
* priority is calculated by adding up all the starttimes - endtimes in each row of each table.
* You will also be returned how much time you have spend doing that activity.
