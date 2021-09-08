category_list = ["accomodation", "food", "travel", "miscellaneous", "activity"]

def category(category_list):
    print(category_list)
    category = input("Which category does your expense fall under?").lower().strip()
    while category in category_list:
        return category
        print("Thank you")
    else:
        print("Please enter a category in the list")
        category = input("Which category does your expense fall under?")


category(category_list)
