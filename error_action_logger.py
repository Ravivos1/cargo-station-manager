import os
from datetime import date

# append a normal action entry to the actions log file
def writeToActionLog(text:str):
    if os.path.exists("Cargo_Station_Actions.txt"):
        with open("Cargo_Station_Actions.txt", "a", encoding="utf-8") as file:
            file.write(f"{date.today()} | "+text+"\n")
    else:
        with open("Cargo_Station_Actions.txt", "w", encoding="utf-8") as file:
            file.write(f"{date.today()} | "+text+"\n")

# append an error entry (with its real exception type and location) to the errors log file
def writeToErrorsLog(text:str, loc:str, error_type:str="ValueError"):
    if os.path.exists("Cargo_Station_Errors.txt"):
        with open("Cargo_Station_Errors.txt", "a", encoding="utf-8") as file:
            file.write(f"{date.today()} | {error_type} | "+text+" | "+loc+"\n")
    else:
        with open("Cargo_Station_Errors.txt", "w", encoding="utf-8") as file:
            file.write(f"{date.today()} | {error_type} | "+text+" | "+loc+"\n")
