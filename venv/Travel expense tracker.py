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

    
daily_budget = force_number("What is your daily budget?")
print("You have set your daily budget to {}".format(daily_budget))
