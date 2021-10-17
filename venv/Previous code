#Year 11 assesment task

# Setting variables
food = {}
accommodation = {}
travel = {}
miscellaneous = {}
activity = {}
expenses = {}
category_list = ["accommodation", "food", "travel", "miscellaneous", "activity"]

# Forcing valid input from user
def force_number(message):
    while True:
        try:
            number = float(input(message))
            if(number <= 0):
               print("Please enter an amount greater than $0")
               continue
        except ValueError:
            print("Please enter an amount")
            continue
        else:
           break
    return ("${:,.2f}".format(number))

# Getting yes or no answer only
def confirm_answer(question):
    while True:
        reply = input(question).lower().strip()
        if reply == "yes":
            return True
            break
        elif reply == "no":
            return False
            break
        else:
            print("Please enter yes or no")
            continue

# Getting user's category choice
def category(category_list):
    print(category_list)
    while True:
        category = input("Which category does your expense fall under?").lower().strip()
        if category in category_list:
            return category
        else:
            print("Please enter a category in the list")

def continue_spending():
    tracking = True
    expenses = {}
    while tracking:
        #Prompt for user's expense and expense type
        category(category_list)
        name = input("What is your expense for? e.g breakfast, movies, taxi  ").strip().title()
        expense = force_number("Enter your expense:$")
        #Stores expense in the dictionary
        expenses[name] = expense
        #Finding out if user wants to enter another expense
        repeat = confirm_answer("Would you like to enter another expense?")
        if repeat == False:
            tracking = False
            return expenses

def history(Chosen_Category, User_Expenses):
    history = confirm_answer("Would you like to see your expense history?")
    while history == True:
        if Chosen_Category == "food":
            print("~ Food expenditure ~")
            food = User_Expenses
            print(food)
        elif Chosen_Category == "travel":
            print("~ Travel expenditure ~")
            travel = User_Expenses
            print(travel)
        elif Chosen_Category == "accommodation":
            print("~ Accommodation expenditure ~")
            accommodation = User_Expenses
            print(accommodation)
        elif Chosen_Category == "activity":
            print("~ Activity expenditure ~")
            activity = User_Expenses
            print(activity)
        elif Chosen_Category == "miscellaneous":
            print("~ Miscellaneous expenditure ~")
            miscellaneous = User_Expenses
            print(miscellaneous)
        else:
            print("Thank you, for using this program")


#MAIN

daily_budget = force_number("What is your daily budget: $")
print("You have set your daily budget to {}".format(daily_budget))
budget_confirmation = confirm_answer("Are you sure this is your budget? [yes or no]")
while budget_confirmation == False:
    daily_budget = force_number("What is your daily budget?")
    budget_confirmation = confirm_answer("Are you sure this is your budget? [yes or no]")
else:
    print("Thank you, you may proceed")

Chosen_Category = category(category_list)
User_Expenses = continue_spending()
history(Chosen_Category, User_Expenses)

