"""HarborFlow Assignment 1 starter file."""

#task 1 starts here#-------------------------------------------------------------------------------------
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
#task 1 ends here#-------------------------------------------------------------------------------------


#task 2 starts here#-------------------------------------------------------------------------------------	
def validate_booking_reference():
    # Read and normalize the booking reference.
    reference = input("Enter booking reference: ")
    normalized = reference.strip().upper()     # Add replace(" ") to remove the spaces ?

# while True: We could stay in the loop to make it easier but since the assignmnet does explicict says NOT TO we ignore this improvement. 
	
    # Check every part of the required HFL-CCC-NNNN format.
    is_valid = (
        len(normalized) == 12
        and normalized[0:3] == "HFL"
        and normalized[3] == "-"
        and normalized[4:7].isalpha()
        and normalized[7] == "-"
        and normalized[8:12].isdigit()
    )

    # Print the result of the validation.
    if is_valid:
        print("Booking reference:", normalized)
        print("Valid booking reference.")


    else:
        print("Invalid booking reference.")
#task 2 ends here#-------------------------------------------------------------------------------------


#task 3 starts here#-------------------------------------------------------------------------------------
def read_positive_number(prompt):       #this will be importamt for task 5-9
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
        raw_value = input(prompt).strip()
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

    print(f"""
{'Service':.<20}: {service_name(service_code)}
{'Delevery qoute':.<20}: {(price):.2f} SEK

Returning to DISPATCH CONSOLE ...
""")
#task 3 ends here#-------------------------------------------------------------------------------------

#task 4 starts here#-------------------------------------------------------------------------------------
def consolidate_parcel_labels():
    # Read the complete scanner export from one console line.
    raw_input = input("Scanned labels: ")

    # Split the original text wherever a comma appears.
    label_parts = raw_input.split(",")

    # This list stores only the first occurrence of each normalized label.
    unique_labels = []

    # Process labels from left to right.
    for part in label_parts:
        # Official Task 4 normalization:
        # strip() removes whitespace only from the beginning and end.
        # upper() converts letters to uppercase.
        # replace(" ", "") removes ordinary internal space characters.
        cleaned = part.strip().upper().replace(" ", "")

        # Add the label only when it has not already been retained.
        if cleaned not in unique_labels:
            unique_labels.append(cleaned)

    print("Unique load list:")

    # Print numbered output starting at 1.
    for index in range(len(unique_labels)):
        print(f"{index + 1}. {unique_labels[index]}")

    print(f"Total unique parcels: {len(unique_labels)}")
    #task 4 ends here#-------------------------------------------------------------------------------------
#task 4 ends here#-------------------------------------------------------------------------------------

#task 5 starts here#-------------------------------------------------------------------------------------
def read_positive_weights():
    """Read one comma-separated line where every parcel weight is > 0."""
    while True:
        raw_weights = input("Parcel weights (kg): ")
        parts = raw_weights.split(",")

        weights = []
        valid = True

        for part in parts:
            cleaned_part = part.strip()

            try:
                weight = float(cleaned_part)
            except ValueError:
                valid = False
                break

            if weight <= 0:
                valid = False
                break

            weights.append(weight)

        if valid:
            return weights

        print("Error - Value must be greater than zero.")

def check_van_capacity():
    # Read and validate one positive van weight capacity.
    capacity = read_positive_number("Van capacity (kg): ")

    # Read and validate all parcel weights from one comma-separated line.
    weights = read_positive_weights()

    # State used while processing parcels.
    remaining = capacity
    accepted = []
    rejected = []
    loaded = 0.0

    # Process parcel weights from left to right.
    for index in range(len(weights)):
        weight = weights[index]

        if weight <= remaining:
            print(f"Parcel {index + 1}: ACCEPTED")

            accepted.append(weight)
            loaded += weight
            remaining -= weight
        else:
            print(f"Parcel {index + 1}: REJECTED")

            # Do NOT stop here: a later lighter parcel may still fit.
            rejected.append([index + 1, weight])

    print(f"Accepted parcels: {len(accepted)}")
    print(f"Loaded weight: {loaded:.2f} kg")
    print(f"Remaining capacity: {remaining:.2f} kg")
    
  #Task_05 endshere#----------------------------------------------

  # ---------- Task 6: Classify service performance ----------
#task 5 ends here#-------------------------------------------------------------------------------------

#task 6 starts here#-------------------------------------------------------------------------------------
def read_not_negative_number(prompt):
    """Repeatedly read a number that may be zero but not negative."""
    # Keep asking until a valid value is entered; return exits the loop.
    while True:
        try:
            # input() returns text, so convert it to a whole number.
            value = int(input(prompt))
        except ValueError:
            # The text could not be converted (e.g. "abc"), so ask again.
            print("Error - Please enter a whole number.")
            continue
        if value < 0:
            # Negative values are invalid for minutes and parcel counts.
            print("Error - Value cannot be negative.")
        else:
            # Valid value: hand it back to the caller.
            return value

def classify_service_performance():
    """Read route data, calculate delay and print the service status."""
    # Collect the three route values, each validated by the helper.
    promised = read_not_negative_number("Promised minutes: ")
    actual = read_not_negative_number("Actual minutes: ")
    damaged = read_not_negative_number("Damaged parcels: ")

    # Positive delay means late; zero or negative means on time or early.
    delay = actual - promised

    # Apply the decision table in order. Damage is checked first
    # because it overrides timing, even for early arrivals.
    if damaged > 0:
        status = "SERVICE FAILURE"
    elif delay <= 0:
        status = "ON TIME"
    elif delay <= 15:
        status = "MINOR DELAY"
    else:
        status = "MAJOR DELAY"

    print(f"Delay: {delay} minutes")
    print(f"Service status: {status}")
#Task_06 endshere#----------------------------------------------


#task 7 starts here#-------------------------------------------------------------------------------------

#task 7 ends here#-------------------------------------------------------------------------------------


#Task_09 starts here#----------------------------------------------
def compare_service_scenarios():
    # Read one positive distance using the shared Task 8 validation helper.
    distance = read_positive_number("Enter Distance in (km): ")
    # Read one positive parcel weight using the same shared helper.
    weight = read_positive_number("Enter Weight in (kg): ")

    # Reuse the Task 3 calculation once for each service code.
    standard_price = calculate_quote(distance, weight, "S")
    express_price = calculate_quote(distance, weight, "X")
    priority_price = calculate_quote(distance, weight, "P")

    # Store names and prices in the required display order.
    services = [("Standard", standard_price),
                ("Express", express_price),
                ("Priority", priority_price)]

    # Print every service price with exactly two decimal places.
    print("\nService comparison:\n")
    for service_name, price in services:
        print(f"{service_name:.<25}: {price:>08.2f} SEK")
        # implemented :>08.2f for right-aligning the price 
        #in a field of 8 characters, with leading zeros and two decimal places. from laps 3 

    # Start both comparisons with Standard so ties keep the first service.
    cheapest_name, cheapest_price = services[0]
    most_expensive_name, most_expensive_price = services[0]

    # Compare the remaining services without changing the order of ties.
    for service_name, price in services[1:]:
        #we start with [1:] because we already initialized the cheapest and most expensive with the first service
        if price < cheapest_price:
            cheapest_name = service_name
            cheapest_price = price
        if price > most_expensive_price:
            most_expensive_name = service_name
            most_expensive_price = price

    # Print the cheapest and most expensive service names.
    print(f"\n{'Cheapest service':.<25}: {cheapest_name:>7} SEK")
    print(f"{'Most expensive service':.<25}: {most_expensive_name:>7} SEK")
    print()
#Task_09 ends here#------------------------------------------------


if __name__ == "__main__":
	# Start the application only when this file is run directly.
	main()