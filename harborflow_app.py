"""HarborFlow Assignment 1 starter file."""

def print_menu():
	# Display all services that the dispatcher can select.
	# Each print statement creates one exact line of the required menu.
	print("HARBORFLOW DISPATCH CONSOLE")
	print("1. Close console")
	print("2. Validate booking reference")
	print("3. Calculate delivery quote")
	print("4. Consolidate parcel labels")
	print("5. Check van capacity")
	print("6. Classify service performance")
	print("7. Produce weekly dispatch report")
	print("8. Compare service scenarios")


def main():
	# Keep the console open and send each menu choice to the correct function.
	# True means the menu should continue appearing; False ends the program. (related to task 1.2.a)
	console_active = True

	while console_active:
		# Show the menu and collect one valid choice on every loop iteration.
		print_menu()
	
		choice = read_menu_choice()

		# Option 1 changes the loop state so the while loop can finish.
		if choice == 1:
			print("Console closed. Dispatch data remains safe.")
			console_active = False
		# Each other option calls a separate function for that service.
		elif choice == 2:
			validate_booking_reference()
		elif choice == 3:
			calculate_delivery_quote()
		elif choice == 4:
			consolidate_parcel_labels()
		elif choice == 5:
			check_van_capacity()
		elif choice == 6:
			classify_service_performance()
		elif choice == 7:
			produce_weekly_report()
		elif choice == 8:
			compare_service_scenarios()


def read_menu_choice():
	# Keep asking until the user enters an integer from 1 through 8.
	while True:
		try:
			# int() converts text such as "3" into the number 3.
			userchoice = int(input("Select service: "))
			# The valid range check prevents unknown menu options.
			if 1 <= userchoice <= 8:
				# return sends the valid choice back to main().
				return userchoice
		except ValueError:
			# Non-numeric input causes ValueError, so the loop can ask again.
			pass

		# This runs for text input and for numbers outside the valid range.
		print("Error - Select a service from 1 to 8.")


def validate_booking_reference():
	# This function will validate a HarborFlow booking reference in Task 2.
	
    reference = input("Enter booking reference: ")
    normalized = reference.strip().upper()
    #strip() removes thr white space from before and after the refrense only

    parts = normalized.split("-")
    #.splits the refrense at the "-" and removes it 

    is_valid = False

    if len(parts) == 3:
    #cheaks if the parts splited by .split() are ==3

        prefix = parts[0]
        code = parts[1]
        number = parts[2]
        # naming the parts 

    # validating the parts are matching with they should be
        prefix_ok = (prefix == "HFL")
        code_ok = (len(code) == 3 and code.isalpha())
        #.isalpha() is to make sure the 3 charecters in the string input are alphabitical not numbers or stuff
        number_ok = (len(number) == 4 and number.isdigit())
        #.isdigit - same thing but in reverse so it looks for digits 
        
        if prefix_ok and code_ok and number_ok:
            is_valid = True

    if is_valid:
        print("Booking reference: " + normalized)
        print("Valid booking reference.")
    else:
        print("Invalid booking reference.")
		

def read_positive_number(prompt):
# ---------------------------------------------------------------------------
# read_positive_number(prompt)
#
# What it does:
#   Repeatedly asks the user to type a number (using the message passed in
#   as "prompt") until they enter something that is both:
#     1. a valid number, and
#     2. greater than zero.
#
# How it works:
#   - Runs inside a "while True" loop so it can keep re-asking on bad input.
#   - Uses try/except to safely attempt float(raw_value). If the text isn't
#     a valid number (e.g. "abc"), float() raises a ValueError, which is
#     caught instead of crashing the program.
#   - If conversion succeeds but the number is zero or negative, it is
#     rejected too.
#   - In both failure cases the required error message is printed and
#     "continue" sends control back to the top of the loop to ask again.
#   - Once a valid positive number is found, it is returned to whichever
#     function called this one.
# ---------------------------------------------------------------------------

    while True:
        raw_value = input(prompt)
        #prompt is the temporary name for whatever the input is called 

        try:
            value = float(raw_value)
        except ValueError:
            print("Error - Value must be a number.")
            continue

        if value <= 0:
            print("Error - Value must be greater than zero.")
            continue

        return value


def read_service_code():
# ---------------------------------------------------------------------------
# read_service_code()
#
# What it does:
#   Asks the user to enter a service code and keeps asking until they enter
#   exactly S, X, or P (letters only, case-insensitive).
#
# How it works:
#   - Runs inside a "while True" loop so invalid entries are re-prompted.
#   - strip() removes accidental leading/trailing spaces, and upper()
#     converts lowercase letters (e.g. "s") to uppercase ("S") so the
#     comparison below works no matter how the user typed it.
#   - Checks the normalized code against the three allowed values using
#     "or" conditions. If it matches one of them, that code is returned
#     immediately.
#   - If it doesn't match any of them, the required error message is
#     printed and the loop repeats to ask again.
# ---------------------------------------------------------------------------

    while True:
        raw_code = input("Enter service code (S, X or P): ")
        code = raw_code.strip().upper()

        if code == "S" or code == "X" or code == "P":
            return code

        print("Error - Service code must be S, X or P.")


def service_name(service_code):
# ---------------------------------------------------------------------------
# service_name(service_code)
#
# What it does:
#   Converts a one-letter service code (S, X, or P) into its full display
#   name (Standard, Express, or Priority), for use in printed output.
#
# How it works:
#   - Starts with an empty "name" as a fallback.
#   - Uses a simple if/elif chain to match the incoming service_code against
#     the three known codes and assign the matching full name.
#   - Returns whatever name was set (or the empty string, if somehow given
#     a code outside S/X/P, which shouldn't happen since the code is always
#     produced by read_service_code() first).
# ---------------------------------------------------------------------------

    name = ""

    if service_code == "S":
        name = "Standard"
    elif service_code == "X":
        name = "Express"
    elif service_code == "P":
        name = "Priority"

    return name


def calculate_quote(distance, weight, service_code):
# ---------------------------------------------------------------------------
# calculate_quote(distance, weight, service_code)
#
# What it does:
#   The single, reusable pricing formula for the whole console. Given a
#   distance, a weight, and a service code, it returns the numeric quote
#   price. This function does no input() or print() of its own - it is
#   pure calculation, so it can be reused by both the quote service and
#   the service-comparison service without copying the formula.
#
# How it works:
#   - Picks the correct multiplier for the given service_code using
#     if/elif: Standard (S) = 1.00, Express (X) = 1.25, Priority (P) = 1.60.
#   - Calculates the base subtotal using the fixed formula:
#       subtotal = 45.00 + (distance * 6.50) + (weight * 4.00)
#     This applies the flat base charge, the per-kilometre distance rate,
#     and the per-kilogram weight rate.
#   - Multiplies that subtotal by the chosen multiplier to get the final
#     quote, with no intermediate rounding.
#   - Returns the resulting number to the caller.
# ---------------------------------------------------------------------------

    multiplier = 1.00

    if service_code == "S":
        multiplier = 1.00
    elif service_code == "X":
        multiplier = 1.25
    elif service_code == "P":
        multiplier = 1.60

    subtotal = 45.00 + (distance * 6.50) + (weight * 4.00)
    quote = subtotal * multiplier

    return quote


def calculate_delivery_quote():
# ---------------------------------------------------------------------------
# calculate_delivery_quote()
#
# What it does:
#   This is the delivery-quote SERVICE: it handles all the user-facing
#   input and output for Task 3, then hands the actual math off to
#   calculate_quote(). This keeps input/output separate from the formula.
#
# How it works:
#   - Calls read_positive_number() twice to safely collect a valid distance
#     and a valid weight (each one loops internally until valid).
#   - Calls read_service_code() to safely collect a valid S/X/P code.
#   - Passes all three values into calculate_quote() to get the numeric
#     price back.
#   - Prints the service's full name (via service_name()) and the price,
#     formatted to exactly two decimal places using format(price, ".2f"),
#     followed by the currency label "SEK".
#   - Once printing is done, the function simply ends, which returns
#     control back to whatever called it (main()).
# ---------------------------------------------------------------------------

    distance = read_positive_number("Enter delivery distance in kilometres: ")
    weight = read_positive_number("Enter parcel weight in kilograms: ")
    service_code = read_service_code()

    price = calculate_quote(distance, weight, service_code)

    print("Service: " + service_name(service_code))
    print("Delivery quote: " + format(price, ".2f") + " SEK")

	# This function will calculate a delivery price in Task 3.


def consolidate_parcel_labels():
	# This function will remove duplicate parcel labels in Task 4.
	# pass temporarily keeps the menu runnable until Task 4 is implemented.
	pass


def check_van_capacity():
	# This function will decide which parcels fit in the van in Task 5.
	# pass temporarily keeps the menu runnable until Task 5 is implemented.
	pass


def classify_service_performance():
	# This function will classify a route's delivery performance in Task 6.
	# pass temporarily keeps the menu runnable until Task 6 is implemented.
	pass


def produce_weekly_report():
	# This function will calculate the weekly delivery report in Task 7.
	# pass temporarily keeps the menu runnable until Task 7 is implemented.
	pass


def compare_service_scenarios():
	# This function will compare Standard, Express, and Priority in Task 9.
	# pass temporarily keeps the menu runnable until Task 9 is implemented.
	pass


if __name__ == "__main__":
	# Start the application only when this file is run directly.
	main()
