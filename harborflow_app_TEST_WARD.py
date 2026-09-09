"""HarborFlow Assignment 1 starter file."""


#Task_011 starts#-------------------------------------------------------------------------------------
def print_menu():
# Display all services that the dispatcher can select.
	print("""HARBORFLOW DISPATCH CONSOLE
	1. Close console
	2. Validate booking reference
	3. Calculate delivery quote
	4. Consolidate parcel labels
	5. Check van capacity
	6. Classify service performance
	7. Produce weekly dispatch report
	8. Compare service scenarios""")

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
			pass

		# This runs for text input and for numbers outside the valid range.
		print("Error - Select a service from 1 to 8.")

def main():
	# True means the menu should continue appearing; False ends the program. (related to task 1.2.a)
	console_active = True

	while console_active:
	# run untill colected
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
#Task_01 end#-------------------------------------------------------------------------------------


#Task_02 starts here#-------------------------------------------------------------------------------------
def validate_booking_reference():
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
        print(f"\nBooking reference: {normalized}")
        print("Valid booking reference.")
        print("Returning to main menu...")
    else:
        print(f"""
Invalid booking reference.
Expected format: HFL-XXX-YYYY
    
1. Validate again 
2. Exit
        """)

        servise = input("Select an option: ").strip()
        if servise == "1":
            validate_booking_reference()
        elif servise == "2":
            print("Goodbye.")
            main()
#Task_02 ends here#-------------------------------------------------------------------------------------

#task 3 starts here#-------------------------------------------------------------------------------------
def read_positive_number(prompt):       #this will be importamt for task 9
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
    name = ""
    #set the name to be empyu first

    if service_code == "S":
        name = "Standard"
    elif service_code == "X":
        name = "Express"
    elif service_code == "P":
        name = "Priority"

    return name

def calculate_quote(distance, weight, service_code):
    multiplier = 1.00

    if service_code == "S":
        multiplier = 1.00
    elif service_code == "X":
        multiplier = 1.25
    elif service_code == "P":
        multiplier = 1.60

    subtotal = 45.00 + (distance * 6.50) + (weight * 4.00)
    #gets the distance and weight vales from the user
    quote = subtotal * multiplier

    return quote

def calculate_delivery_quote():
# thiscalcoulates the delivery quote based on the distance, weight and service code provided by the user

    distance = read_positive_number("Enter delivery distance in kilometres: ")
    weight = read_positive_number("Enter parcel weight in kilograms: ")
    service_code = read_service_code()

    price = calculate_quote(distance, weight, service_code)

    print(f"\n{'Service':.<20}: {service_name(service_code)}")
    print(f"{'Delivery quote':.<20}: {format(price, '.2f')} SEK")
#task 3 ends here#-------------------------------------------------------------------------------------

#Task 4 starts here#-------------------------------------------------------------------------------------
def consolidate_parcel_labels():
    raw_input = input("Enter parcel labels separated by commas: ")

    # Split the full string at every comma.
    label_parts = raw_input.split(",")

    # Create an empty list that will store only the unique normalized labels.
    unique_labels = []

    # Loop through every item created by the split.
    for item in label_parts:
        # Strip spaces around the label so " box-1 " becomes "box-1".
        cleaned = item.strip().upper()

        # Ignore empty items such as "", " ", or labels made by repeated commas.
        if cleaned == "":
            # This prevents blank labels from being counted or printed.
            continue

        # Check whether this normalized label has already appeared.
        # This is the duplicate check using a list.
        # If it is not in the list, add it in first-seen order.
        if cleaned not in unique_labels:
            unique_labels.append(cleaned)
            # .append() adds the new label to the end of the list, preserving order.

    print("\nUnique parcel labels:")
    # Print each normalized label with numbering starting at 1.
    # Enumerate gives the number and the label value.
    for number, label in enumerate(unique_labels, start=1):
        print(f"{number}. {label}")

    # Print the total number of unique labels.
    print(f"Total labels: {len(unique_labels)}\n")

    print("Returning to main menu...\\n")
#Task 4 ends here#-------------------------------------------------------------------------------------

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
