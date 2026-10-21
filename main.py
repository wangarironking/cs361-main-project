import json
from datetime import datetime

fileHandler = "budgetTracker.json"

data = {"budget":0, "expenses": []}

def interactMenu():
    while True:
        print("========================")
        print("PERSONAL BUDGET TRACKER")
        print("========================")
        print("Option 1: Add an Expense")
        print("Option 2: Set a monthly cap")
        print("Option 3: Look at Expense History")
        print("Option 4: Exit the program")
        print("")
        print("")
        print("")
        userSelection = input("Please enter your option number")
        if userSelection == "1":
            print("You selected to add an expense")
        elif userSelection == "2":
            print("You selected to set a monthly cap")
        elif userSelection == "3":
        
