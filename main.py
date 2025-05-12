from database import entries, get_entries, add_entry

menu = """Please select:
1, Add an Entry
2, View All Entries
3, Exit

Your Selection is:
"""
def prompt_new_entry():
    entry_content = input("What have you learnt today?")
    entry_date = input("What date?")
    add_entry(entry_date, entry_content)

def display_entries(entries):
    for entry in entries:
        print(f"On this day: {entry['date']}\nYou've learnt {entry['content']}\n\n")

user_input = input(menu)

while user_input != 3:
    if user_input == "1":
        prompt_new_entry()
        user_input = input(menu)
    elif user_input == "2":
        entries = get_entries()
        display_entries(entries)
        user_input = input(menu)
    else:
        print("invalid input.")
        user_input = input(menu)