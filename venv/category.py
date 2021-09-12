tracking = True
while tracking:
    history = {}
    type = input("What is your expense for e.g breakfast, movies, taxi? ").strip().title()
    expense = float(input("Enter your expense:$"))
    history[type] = expense
    repeat = input("Would you like to enter another expense?")
    if repeat == "no":
        tracking = False
        for type, expense in history.items():
            print(f"{type}: {expense}")
    else:
        tracking = True
