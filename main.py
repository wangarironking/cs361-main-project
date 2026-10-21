import json
from datetime import datetime

fileHandler = "budgetTracker.json"

data = {"budget":0, "expenses": []}

def createExpense():
    print("========================")
    print("====ADD A NEW EXPENSE====")
    print("========================")
    try:
        userExpense = float(input("please enter a positive number for your expense!: "))
    except ValueError:
        print("You entered something that is not a positive number please try again")
        return
    if userExpense <=0:
        print("the amount should be positive. Please try again")
        return
    try:
        userDate = datetime.strptime(input("please enter a date in the format of YYYY-MM-DD"))
    except ValueError:
        print("Incorrect date format. Please use YYYY-MM-DD")
        return
    expenseCategory = input("please input a category that you would like to label your expense: ").strip()
    if expenseCategory == None:
        print("Please input a category. It cannot be blank")
        return
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
            createExpense()
        elif userSelection == "2":
            print("You selected to set a monthly cap")
        elif userSelection == "3":
            print("You selected to look at expense history")
        elif userSelection == "4":
            print("Thank you for using the program. Goodbye!")
            break
        else:
            print("please select a number integer from 1-4")

if __name__ == "__main__":
    interactMenu()
        
