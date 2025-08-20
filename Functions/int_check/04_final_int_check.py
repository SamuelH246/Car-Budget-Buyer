def int_check(question, low, high):
    """Checks user enters an integer between optional bounds"""
    error = "❗ Invalid input. Please enter a valid number. ❗\n"
    while True:
        to_check = input(question).lower()

        if to_check == 'xxx':
            print("Thank you for using Car Budget Buyer")
            quit()

        try:
            response = int(to_check)

            if response < low or response > high:
                if response > high:
                    print(f"❗ Please enter a number between {low} to {high}. ❗\n")
                elif response < low:
                    print(f"❗ Please enter a whole number of at least {low}. ❗\n")
            else:
                return response
        except ValueError:
            print(error)