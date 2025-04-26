entries = []

def add_entry(entry_date, entry_content):
    entries.append({"content": entry_content, "date": entry_date})

def get_entries():
    return entries