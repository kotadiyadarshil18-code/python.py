print("Welcome to Personal Journal Manager!")
print("Please select an option.")

from datetime import datetime

class JournalManager:
    def __init__(self, filename="journal.txt"):
        self.filename = filename

    def add_entry(self):
        try:
            entry = input("Enter your journal entry:\n")
            time = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

            with open(self.filename, "a") as file:
                file.write(f"{time}\n{entry}\n\n")

            print("\nEntry added successfully!")

        except Exception as e:
            print("Error while adding entry:", e)

    def view_entry(self):
        try:
            with open(self.filename, "r") as file:
                print("\nYour Journal Entries:")
                print("-" * 40)
                print(file.read())
        except FileNotFoundError:
            print("\nNo journal entries found. Start by adding a new entry!")
        except Exception as e:
            print("Error:", e)

    def search_entry(self):
        try:
            keyword = input("Enter keyword or date to search: ")

            with open(self.filename, "r") as file:
                found = False
                for line in file:
                    if keyword.lower() in line.lower():
                        print(line.strip())
                        found = True

            if not found:
                print("No matching entries found.")
        except FileNotFoundError:
            print("Journal file does not exist.")
        except Exception as e:
            print("Error:", e)

    def delete_entries(self):
        try:
            confirm = input("Are you sure you want to delete all entries? (yes/no): ")
            if confirm.lower() == "yes":
                with open(self.filename, "w") as file:
                    pass
                print("All journal entries deleted.")
            else:
                print("Delete operation cancelled.")
        except Exception as e:
            print("Error:", e)


jm = JournalManager()

while True:
    print("\n--- Journal Menu ---")
    print("1. Add a New Entry")
    print("2. View all Entries")
    print("3. Search for an Entry")
    print("4. Delete all Entries")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        jm.add_entry()
    elif choice == 2:
        jm.view_entry()
    elif choice == 3:
        jm.search_entry()
    elif choice == 4:
        jm.delete_entries()
    elif choice == 5:
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")