menu = """Please select:
1, Add an Entry
2, View All Entries
3, Exit

Your Selection is:
"""
user_input = input(menu)

while user_input != 3:
    if user_input == "1":
        print("1")
    elif user_input == "2":
        print("2")
    else:
        print("invalid input.")