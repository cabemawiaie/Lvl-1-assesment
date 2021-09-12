#Year 11 assesment task
#Making sure user input is valid
def force_number(message):
    while True:
        try:
            number = float(input(message))
            #Accepting values higher than 0 only
            if(number <= 0):
               print("Please enter an amount greater than $0")
               continue
        except ValueError:
            print("Please enter an amount")
            continue
        else:
            print("Thank you")
        break
    return ("${:,.2f}".format(number))

#Getting yes or no answer only
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

daily_budget = force_number("What is your daily budget?")
print("You have set your daily budget to {}".format(daily_budget))
#Confirming user's budget
budget_confirmation = confirm_answer("Are you sure this is your budget? [yes or no]")
while budget_confirmation == False:
    daily_budget = force_number("What is your daily budget?")
    budget_confirmation = confirm_answer("Are you sure this is your budget? [yes or no]")
else:
    print("Thank you, you may proceed")

category_list = ["accomodation", "food", "travel", "miscellaneous", "activity"]

def category(category_list):
    print(category_list)
    while True:
        category = input("Which category does your expense fall under?").lower().strip()
        if category in category_list:
            return category
            print("Thank you")
        else:
            print("Please enter a category in the list")


category(category_list)

def continue_spending():
    tracking = True
    expenses = {}
    while tracking:
        #Prompt for user's expense and expense type
        expense_type = input("What is your expense for? e.g breakfast, movies, taxi").strip().title()
        expense = float(input("Enter your expense: "))
        #Stores expense in the dictionary
        expenses[expense_type] = expense
        #Finding out if user wants to enter another expense
        repeat = input("Would you like to enter another expense?")
        if repeat == "no":
            tracking = False
print("Expense history")
for expense_type, expense in expenses.items():
    print("{} : ${:.2f}".format(expense_type, expense))

