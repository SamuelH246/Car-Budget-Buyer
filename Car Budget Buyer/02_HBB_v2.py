# Functions go here

# Title
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration at the start and end"""
    return f"{decoration * 3} {statement} {decoration * 3}"

# Checks for Yes / No input
def string_check(question, valid_answers=('yes', 'no'), num_letters=1):
    """Checks that users enter the full word or the 'n' letter/s of a word from a list of valid responses"""
    while True:
        response = input(question).lower()

        for item in valid_answers:
            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the "n" letters
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_answers}")

# Displays Instructions
def instructions():
    print(make_statement("Instructions", "ℹ️"))

    print('''
Instructions blah blah blah
    ''')

# Makes sure input is not blank
def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry this can't be blank. Please try again. \n")

# Checks integer
def int_check(question):
    """Checks users enter an integer"""

    error = "Oops - please enter an integer  more than zero"

    while True:

        try:
            # change the response to an integer that it's more than zero
            response = int(input(question))

            return response

        except ValueError:
            print(error)

# Float input for prices
def float_check(question):
    """Checks users enter a float (decimal number)"""
    while True:
        try:
            response = float(input(question))
            if response > 0:
                return response
            else:
                print("Please enter a number more than zero.")
        except ValueError:
            print("Oops - please enter a valid number.")

# Creates an item dictionary with fixed price
def item(name, price, quantity):
    """Returns a dictionary with item details using a fixed price."""

    return {
        "name": name,
        "price": round(price, 2),
        "quantity": quantity}

# Main routine goes here
# List to hold product details
products = []
cart = []

category_items = {
    "Toiletries": [...],
    "Bedroom": [...],
    "Office": [...],
    "Kitchen": [...]
}


# Program main heading

print(make_statement("Budget Buyer", "🛒"))

# ask user for their name (and check it's not blank)
print()
name = not_blank("Hello Earthling!, what may I call you?: ")

# Ask user if they want to see the instructions
# Display them if necessary
print()
want_instructions = string_check(f"Hi {name}, Would you like a tutorial/explanation on how the program works? ")
if want_instructions == "yes":
    instructions()
print()

# Asks user for budget
# Rounds budget to two decimal place
budget = round(float_check("How much money do you have to spend? "), 2)
print()

# Displays their budget
# Asks what products they wish for
print(f"Great, your budget is ${budget}")
print()


# Categories
# Items within categories (name, price, quantity)
category_items = {
    "Toiletries": [
        item("Shampoo", 12.00, 2),
        item("Soap Bars", 4.00, 4),
        item("Toilet Paper", 8.00, 6),
        item("Toothpaste", 3.50, 1),
        item("Toothbrush", 2.00, 1),
        item("Deodorant", 5.00, 1),
        item("Mouthwash", 6.50, 1),
        item("Razor Blades", 9.00, 3),
        item("Hairbrush", 7.50, 1),
        item("Tissues", 3.00, 2)
    ],
    "Bedroom": [
        item("Pillow", 15.00, 1),
        item("Bedsheets", 30.00, 1),
        item("Blanket", 25.00, 1),
        item("Mattress Protector", 20.00, 1),
        item("Lamp", 18.00, 1),
        item("Curtains", 35.00, 2),
        item("Rug", 40.00, 1),
        item("Alarm Clock", 22.00, 1),
        item("Laundry Basket", 12.00, 1),
        item("Wall Art", 14.00, 1)
    ],
    "Office": [
        item("Pens", 5.00, 10),
        item("Notebook", 4.00, 1),
        item("Sticky Notes", 3.00, 5),
        item("Desk Lamp", 20.00, 1),
        item("Stapler", 6.00, 1),
        item("Printer Paper", 7.50, 1),
        item("Scissors", 4.50, 1),
        item("Highlighters", 6.00, 4),
        item("Binder Clips", 3.00, 10),
        item("Folder Set", 8.00, 5)
    ],
    "Kitchen": [
        item("Dish Soap", 5.00, 2),
        item("Sponges", 3.00, 4),
        item("Trash Bags", 7.00, 10),
        item("Paper Towels", 6.00, 2),
        item("Aluminium Foil", 4.00, 1),
        item("Plastic Wrap", 3.50, 1),
        item("Dish Towels", 10.00, 2),
        item("Cutting Board", 12.00, 1),
        item("Measuring Cups", 9.00, 1),
        item("Oven Mitts", 8.00, 1)
    ]
}


# ------------------------------------------------------------Ask help from sir, chat gpt
while True:
    print("Now choose a category shown below:")

    # Display categories nicely
    categories = list(category_items.keys())
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}", end="  ")
    print()

    # Ask user for category choice or exit
    choice = input("\nEnter your choice (or 'xxx' to exit): ").lower()
    if choice == "xxx":
        break

    try:
        choice_num = int(choice)
        if 1 <= choice_num <= len(categories):
            selected_category = categories[choice_num - 1]
            print(f"\nItems in {selected_category}:\n")

            # Show items in the selected category
            items = category_items[selected_category]
            for i, product in enumerate(items, 1):
                print(f"{i}. {product['name']} - ${product['price']:.2f} (Qty: {product['quantity']})")
            print()

            # Item selection loop
            while True:
                item_choice = input(
                    f"Enter the number of the item you want to select from {selected_category}, or type 'back' to go back: ").lower()

                if item_choice == "back":
                    print()
                    break
                elif item_choice == "xxx":
                    exit()
                else:
                    try:
                        item_num = int(item_choice)
                        if 1 <= item_num <= len(items):
                            chosen_item = items[item_num - 1]
                            if chosen_item['price'] > budget:
                                print(
                                    f"\nSorry, you don't have enough budget for {chosen_item['name']}. Your balance is ${budget:.2f}.\n")
                            else:
                                budget -= chosen_item['price']
                                print(f"\nYou selected {chosen_item['name']} costing ${chosen_item['price']:.2f}")
                                print(f"Your new updated balance is: ${budget:.2f}\n")
                        else:
                            print(f"\n❗ Please choose a number between 1 and {len(items)}. ❗\n")
                    except ValueError:
                        print("\n❗ Please enter a valid number or 'back'. ❗\n")
        else:
            print(f"\n❗ Please choose a number between 1 and {len(categories)}. ❗\n")
    except ValueError:
        print("\n❗ Please enter a valid number. ❗\n")





