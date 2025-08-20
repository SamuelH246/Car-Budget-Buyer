import pandas


# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration at the start and end"""
    return f"{decoration * 3} {statement} {decoration * 3}"

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

        print(f"❗ Please choose an option from {valid_answers} ❗\n")

def instructions():
    print(make_statement("Instructions", "ℹ️"))

    print('''
Instructions blah blah blah
    ''')

def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry this can't be blank. Please try again. \n")


def int_check(question, low, high):
    """Checks user enters an integer between optional bounds"""
    error = "❗ Invalid input. Please enter a valid number. ❗\n"
    while True:
        try:
            to_check = input(question)
            response = int(to_check)

            if response == 0:
                return 0

            if response < low or response > high:
                if response > high:
                    print(f"❗ Please enter a number between {low} to {high}. ❗\n")
                elif response < low:
                    print(f"❗ Please enter a whole number of at least {low}. ❗\n")
            else:
                return response
        except ValueError:
            print(error)

def currency(x):
    """Formats numbers as currency ($#.##)"""
    return "${:.2f}".format(x)

# Main routine goes here


# Program main heading
print(make_statement("Car Budget Buyer", "🚗"))
print()

# Asks users name
name = not_blank("Hello! What's your name? ")

# Ask user if they want to see the instructions
# Display them if necessary
print()
want_instructions = string_check(f"Hi {name}, Would you like a tutorial/explanation on how the program works? ")

if want_instructions == "yes":
    instructions()

print()

# Ask for budget
print(f"\nAlright {name}, Let's find a car you can afford!")

budget = int_check("Enter your budget (minimum $5,000 , maximum $200,000): $", 5000, 200000)
print(f"\nYour budget is ${budget}\n")

# Shopping cart
cart = []


# Display items
cars = [
    {"item": "Basic Car", "price": 5000, "quantity": 10},
    {"item": "Standard Car", "price": 10000, "quantity": 5},
    {"item": "Luxury Car", "price": 25000, "quantity": 2},
    {"item": "Sports Car", "price": 50000, "quantity": 1},
]

# Shows list
while True:
    affordable_cars = [car for car in cars if car["price"] <= budget and car["quantity"] > 0]
    if not affordable_cars:
        print("You can't afford any more cars or stock is out. Time to checkout.")
        break

    print("Cars you can afford:")
    for i, car in enumerate(affordable_cars, start=1):
        print(f"{i}. {car['item']} - ${car['price']} (In stock: {car['quantity']})")
    print()

    # Asks user to select car or quit
    selection_number = int_check("Which car would you like to purchase?, or type '0' to quit: ", 0, 4)
    if selection_number == 0:
        break
    elif budget >= 5000:
        selected_item = affordable_cars[selection_number - 1]

        # Calculates number of cars the user can buy
        max_can_buy_stock = selected_item['quantity']
        max_can_buy_budget = budget // selected_item['price']
        max_can_buy = min(max_can_buy_stock, max_can_buy_budget)

        # Tells number of cars the user can buy
        # Asks how many user wants to buy + calculates total price
        print(f"\nYou can add up to {max_can_buy} of {selected_item['item']} to your cart.")
        quantity = int_check(f"How many {selected_item['item']} would you like to add? ", 1, max_can_buy)
        total_cost = quantity * selected_item['price']

        # Update stock and budget
        selected_item['quantity'] -= quantity
        budget -= total_cost
        print(f"{quantity} x {selected_item['item']} added to cart. Remaining budget: ${budget}\n")

        # Adds order to cart
        cart.append({
            "item": selected_item['item'],
            "price": selected_item['price'],
            "quantity": quantity,
            "total_cost": total_cost
        })

    # Tells user they can't afford anymore with current budget
    elif budget <= 5000:
        print("You can't afford anymore cars with your budget. Proceed to Checkout")
        break
    else:
        print("You have used the budget amount.")

# Checkout
if not cart:
    print("Thank you for using Car Budget Buyer!")
    exit()

print(make_statement("🛒 Checkout Summary", "🛒"))



# ---- Receipt Generation ----
# create dataframe / table from dictionary
receipt = pandas.DataFrame(cart)

# Currency Formatting (uses currency function)
receipt["Total"] = receipt["price"] * receipt["quantity"]
for column in ["price", "Total"]:
    receipt[column] = receipt[column].apply(currency)

# Output movie frame without index
receipt_string = receipt.to_string(index=False)

# Additional strings / Headings
heading_string = make_statement("Car Purchase Receipt", "=")
summary_heading = make_statement("Summary", "-")

# Total calculations
total_cost = sum(item["price"] * item["quantity"] for item in cart)
summary = [
    f"Total Cost: {currency(total_cost)}"
]

# List of strings to be outputted / written to file
to_write = [heading_string, "\n",
            summary_heading,
            receipt_string, "\n",
            *summary
           ]

# Print area
print()
for item in to_write:
    print(item)

# create file to hold data (add .txt extension)
file_name = "car_purchase_receipt"
write_to = "{}.txt".format(file_name)

text_file = open(write_to, "w+")

# write the item to file
for item in to_write:
    text_file.write(item)
    text_file.write("\n")

text_file.close()