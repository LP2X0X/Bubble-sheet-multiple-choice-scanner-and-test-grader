import os
import pandas as pd
from pathlib import Path

def Collect_Data():
    # Get path to answer file 
    cwd_path = os.path.realpath(os.getcwd())
    while True:
        file_name = input("Please enter the answer file name: ")
        path = cwd_path + "\\" + file_name + ".xlsx"
        if file_name == "":
            continue
        elif os.path.exists(path):
            break
        else:
            continue

    # Get the sheets name
    ids =  (pd.ExcelFile(path)).sheet_names

    # Get the paper's id
    while True:
        pid = input('Please enter paper\'s id: ')
        if pid == "":
            continue
        if pid in ids:
            break
        else:
            continue

    # Read dataframe
    values= []
    values.append((pd.read_excel(path, sheet_name = pid, header = None)).values)
    values[0] = values[0].flatten()
    return values[0]

