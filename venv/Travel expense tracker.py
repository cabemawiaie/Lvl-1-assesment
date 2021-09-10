#Year 11 assesment task
#Making sure user input is valid
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

daily_budget = force_number("What daily budget do you have in mind?")
print("You have set your daily budget to {}".format(daily_budget))
budget_confirmation = confirm_answer("Are you sure this is your budget? [yes or no]")
while budget_confirmation == False:
    daily_budget = force_number("What is your daily budget?")
    budget_confirmation = confirm_answer("Are you sure this is your budget? [yes or no]")
else:
    print("Thank you, you may proceed")

category_list = ["accomodation", "food", "travel", "miscellaneous", "activity"]

def category(category_list):
    print(category_list)
    category = input("Which category in the list above does your expense fall under?").lower().strip()
    while category in category_list:
        return category
        print("Thank you")
    else:
        print("Please enter a category in the list")
        category = input("Which category does your expense fall under?")


category(category_list)
