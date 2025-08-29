# FUNCTION = A block of reusable code

def happy_birthday(name):
    print(f"Happy Birthday {name}!")
    print("You are awesome 🎉")
    print("Have a great year ahead!")
    print()

happy_birthday("Rahim")
happy_birthday("Ahmed")

# Function with multiple parameters
def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your amount PKR {amount:.2f}")
    print(f"Your due date is {due_date}")

display_invoice("Basit", 40000, "25-09-2025")

# Function with return value
def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("abdul", "basit")
print(full_name)
