notes = []

def add_note():
    note = input("Enter a note: ")
    notes.append(note)

def view_notes():
    for note in notes:
        print(note)

while True:
    choice = input("Enter 'a' to add a note, 'v' to view notes, or 'q' to quit: ")
    if choice == 'a':
        add_note()
    elif choice == 'v':
        view_notes()
    elif choice == 'q':
        break
    else:
        print("Invalid choice. Try again.")
