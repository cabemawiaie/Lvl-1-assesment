#Year 11 assesment task
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
budget_confirmation = confirm_answer("Are you sure this is your budget? [yes or no]")
if budget_confirmation == False:
    daily_budget = force_number("What is your daily budget then?")
elif budget_confirmation == True:
    print ("Thank you, you may proceed") 
