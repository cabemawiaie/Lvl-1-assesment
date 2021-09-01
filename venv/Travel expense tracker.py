#Year 11 assesment task
def force_number(message):
    while True:
        try:
            number = float(input(message))
            break
        except ValueError:
            print("Please enter a number")
            continue
    
        if number < 0:
            print("Please enter an amount greater than 0")
            continue
        else:
             break
    return ("${:,.2f}".format(number))
    
daily_budget = force_number("What is your daily budget?")
print(daily_budget) 
