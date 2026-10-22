import json
from datetime import datetime
import time


fileOpener = "budgetInfo.json"
data = {"budget":0, "expenses": []}

def startupCommunication():
    
    with open(fileOpener,"w") as file:
        json.dump(data, file, indent =2)
def summonInfo():
    global data
    try:
        with open(fileOpener, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Did not find any budget. starting a new budget")
    except json.JSONDecodeError:
        print("the budget file of interest is empty or invalid. Starting a new budget")

def monthCap():
    print("========================")
    print("====MONTHLY BUDGET AMOUNT====")
    print("========================")
    print("")
    print("")
    print(f"The monthly cap is: ${data["budget"]:.2f}")
    try:
        newCap = int(input("Please input a new monthly cap for your plan: "))
    except ValueError:
        print("I'm sorry but that is not a valid number please enter a valid whole number")
        return
    if newCap <=0:
        print("The monthly cap that you enter has to be positive")
        return

    print("confirm whether you would like to save and finalize this monthly cap")
    print("press 1 to save it ")
    print("press 2 to cancel it")
    userSelection = input("enter either 1 or 2: ").strip()
    if userSelection == "1":
        data["budget"] = newCap
        startupCommunication()

    elif userSelection == "2":
        print("you chose to cancel the budget plan")
        return
    else:
        print("you did not choose a valid selection")
        return

    statusMonth = datetime.now().strftime("%Y-%m")
    totalValue = 0
    for value in data["expenses"]:
        if value["date"].startswith(statusMonth):
            totalValue += value["amount"]
    leftOverMoney = data["budget"] - totalValue

    print(f"This is your monthly budget: ${data['budget']:.2f}")
    print(f"This is your expenses this month: {totalValue:.2f}")
    print(f"This is your remaining budget: {leftOverMoney:.2f}")



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
        userDate = input("please enter a date in the format of YYYY-MM-DD")
        datetime.strptime(userDate, "%Y-%m-%d")
    except ValueError:
        print("Incorrect date format. Please use YYYY-MM-DD")
        return
    expenseCategory = input("please input a category that you would like to label your expense: ").strip()
    if not expenseCategory:
        print("Please input a category. It cannot be blank")
        return
    addExpense = {
        "amount": userExpense,
        "date": userDate,
        "category": expenseCategory
    }
    print("Would you like to have this expense saved?")
    print("press 1 to confirm and 2 to cancel")
    userSelection = input("Please enter 1 or 2: ").strip()

    if userSelection =="1":
        data["expenses"].append(addExpense)
        startupCommunication()
    elif userSelection == "2":
        print("you canceled the expense and nothing is saved")
        return
    else:
        print("that input was invalid. Expense was not saved")
        return


  
    print("Good job! You successfully added an expense!")
    print(f"This is your expense: ${userExpense:.2f}")
    print(f"This is your date: {userDate}")
    print(f"This is your category: {expenseCategory}")

    print("Do you want to look at your expense history?")
    print("Press 1 for yes and 2 to return to the main menu page")
    additionalChoice = input("Please enter 1 or 2: ").strip()
    if additionalChoice == "1":
        lookUpExpense()
    elif additionalChoice == "2":
        return
    else:
        print("that is not a valid selection. Returning to main menu")
        return


def lookUpExpense():
    print("========================")
    print("====EXPENSE HISTORY====")
    print("========================")
    if not data["expenses"]:
        print("You haven't recorded any expenses yet")
        return
   
    OGLIST = data["expenses"]
    recentExpenses = sorted(OGLIST, key=lambda item: item["date"], reverse=True)
    


    filteringDevice = input("Type 1 to keep all expenses showing in the list. Type 2 to filter by category")
    if filteringDevice == "1":
        print("these are all the expenses that you have: ")
    elif filteringDevice == "2":
        categoryType = input("please enter a category that you would like to filter: ").strip()
        recentExpenses = [expense for expense in recentExpenses if expense["category"].lower() == categoryType.lower()]
        if not recentExpenses:
            print("There are no expenses found for that specific category")
            return
    else:
        print("I'm sorry but that is not a valid response. Please choose 1 or 2.")
        return

    timerCountBegin = time.perf_counter()
    for expense in recentExpenses[:20]:
            print(f"expense log: {expense['date']}")
            print(f"expense category: {expense['category']}")
            print(f"expense amount: {expense['amount']}")

    timerCountEnd = time.perf_counter()
    timeDilation = timerCountEnd - timerCountBegin
    print("")
    print(f"we managed to display the expense history in: {timeDilation:.4f} seconds")
def interactMenu():
    while True:
        print("========================")
        print("PERSONAL BUDGET TRACKER")
        print("========================")
        print("")
        print("this program tracks expenses, reviews spending history, and manages a monthly budget")
        print("")
        print("There is no subscription needed. Your budget information is stored locally on your device in budgetInfo.json")
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
            monthCap()
        elif userSelection == "3":
            print("You selected to look at expense history")
            lookUpExpense()
        elif userSelection == "4":
            print("Thank you for using the program. Goodbye!")
            break
        else:
            print("please select a number integer from 1-4")

if __name__ == "__main__":
    summonInfo()
    
    interactMenu()
        
