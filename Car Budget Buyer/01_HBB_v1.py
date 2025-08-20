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

# Main routine goes here
# List to hold product details
products = []


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


