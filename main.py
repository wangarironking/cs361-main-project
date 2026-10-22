import json
from datetime import datetime

fileHandler = "budgetTracker.json"

data = {"budget":0, "expenses": []}

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
    data["expenses"].append(addExpense)
    print("Good job! You successfully added an expense!")
    print(f"This is your expense: ${userExpense:.2f}")
    print(f"This is your date: {userDate}")
    print(f"This is your category: {expenseCategory}")
def lookUpExpense():
    print("========================")
    print("====EXPENSE HISTORY====")
    print("========================")
    if not data["expenses"]:
        print("You haven't recorded any expenses yet")
        return
    OGLIST = data["expenses"]
    recentExpenses = sorted(OGLIST, key=lambda item: item["data"], reverse=True)
    


    filteringDevice = input("Type 1 to keep all expenses showing in the list. Type 2 to filter by category")
    if filteringDevice == "1":
        print("these are all the expenses that you have: ")
    elif filteringDevice == "2":
        categoryType = input("please enter a category that you would like to filter: ").strip()
        mostRecent = [expense for expense in mostRecent if expense["category"].lower() == categoryType.lower()]
    else:
        print("I'm sorry but that is not a valid response. Please choose 1 or 2.")
        return
    for expense in recentExpenses:
            print(f"expense log: {expense['date']}")
            print(f"expense category: {expense['category']}")
            print(f"expense amount: {expense['amount']}")
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
            lookUpExpense()
        elif userSelection == "4":
            print("Thank you for using the program. Goodbye!")
            break
        else:
            print("please select a number integer from 1-4")

if __name__ == "__main__":
    interactMenu()
        
