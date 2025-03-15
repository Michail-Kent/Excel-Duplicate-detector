# Excel-Duplicate-detector
Find Duplicate Names in an Excel File
This Python script scans an Excel file for duplicate full names by combining the first and last names from specified columns. It helps identify duplicate entries in datasets such as employee lists, student records, or customer databases.

Features
File Selection: Uses Tkinter's file dialog to let the user select an Excel file.
Column Detection: Automatically selects the second (column B) and third (column C) columns as first and last name fields.
Duplicate Detection: Combines first and last names to check for duplicates.
Excel Row Numbers: Displays the row numbers of duplicate names for easy identification.
User-Friendly Output: Prints clear messages about duplicates or confirms when none are found.
Requirements
Python 3.x
pandas (pip install pandas)
openpyxl (pip install openpyxl) for .xlsx support
tkinter (built into Python)
Usage
Run the script.
Select an Excel file when prompted.
The script will scan for duplicate names and display the results in the console.
Author
Kent
Date of Creation: January 25, 2025
Feel free to modify the code to fit your needs! 🚀

