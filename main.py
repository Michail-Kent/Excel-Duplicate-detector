import pandas as pd #para ma scan excel
from tkinter import Tk
from tkinter.filedialog import askopenfilename #para lumabas file manager ui

def find_duplicate_names(file_path):
    
    df = pd.read_excel(file_path)
    
    #dapat yung excel na iiscan ay greater than or equal 2
    if len(df.columns) < 2:
        print("The Excel file must have at least two columns (First Name and Last Name).")
        return
    
    #0 start ng bilang dito kung papalitan nyo yung column na iiscan
    first_name_col = df.columns[1]  #column {1} b
    last_name_col = df.columns[2]   #column {2} c
    
    print(f"Scanning columns: '{first_name_col}' (First Name) and '{last_name_col}' (Last Name) for duplicates.")
    
    
    df['Full Name'] = df[first_name_col].astype(str) + " " + df[last_name_col].astype(str)
    
    
    duplicates = df[df.duplicated(subset=['Full Name'], keep=False)]
    
    if duplicates.empty:
        print("No duplicates found.")
    else:
        
        duplicate_groups = duplicates.groupby('Full Name').apply(lambda x: list(x.index + 1))  
        
        print("Duplicate full names and their Excel row numbers:")
        for full_name, rows in duplicate_groups.items():
            print(f"Full Name: {full_name}, Excel Rows: {rows}")


Tk().withdraw()  
file_path = askopenfilename(
    title="Select Excel File",
    filetypes=[("Excel files", "*.xlsx *.xls"), ("All files", "*.*")]
)

if file_path:
    find_duplicate_names(file_path)
else:
    print("No file selected.")
    
    
    
    
    
    
 #feel free to modify this code kung trip nyo
    
    
    
    
    

    
#author: kent
#date of creation: Jan 25, 2025