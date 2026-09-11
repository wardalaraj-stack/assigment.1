"""HarborFlow Assignment 1 starter file."""


#Task_01 starts#-------------------------------------------------------------------------------------
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
        else: 
            invalid_booking_refrence()     

        if is_valid:
            print(f"\nBooking reference: {normalized}")
            print("Valid booking reference.")
            print("Returning to main menu...")
            print()
        
        #print_menu()
    else:
        print("no")
        invalid_booking_refrence()

def invalid_booking_refrence():
    
        print(f"""  
Invalid booking reference.
Expected format: HFL-XXX-YYYY
    
1. Validate again 
2. Exit
        """)
        while True:    
            servise = read_positive_number("Select an option: ")
            if servise == 1:
                validate_booking_reference()
                break
                
            elif servise == 2:
                print("Goodbye.")
                break
            else:
                print("Invalid choice! please select 1 or 2 ")
                invalid_booking_refrence()
#Task_02 ends here#-------------------------------------------------------------------------------------


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


#Task_05 Starts here#------------------------------------------
def check_van_capacity():
#05.1 - 05.10
    """Check van capacity against a list of parcel weights."""
    """Process parcel weights from left to right and print the result."""
    capacity = read_positive_number("Capacity (kg): ")

    while True:
    #05.1 - 05.3 - 
        raw_weights = input("Parcel weights (kg, comma-separated): ")
        parts = [part.strip() for part in raw_weights.split(",")]
        #parts is a list of strings, each representing a weight, with spaces stripped
        try:
            weights = [float(part) for part in parts]
            if weights and all(weight > 0 for weight in weights):
            # if and all() ensure that the list is not empty and all weights are positive
                break
                #continue to the next step if all weights are valid
        except ValueError:
            pass
        print("ERROR!")
        print(f"Please enter one or more positive weights separated by commas.")
        print("")

    remaining = capacity
    accepted = []
    rejected = []

    print("\nProcessing result:")
    #\n means a new line before printing the result
    for position, weight in enumerate(weights, start=1):
    #enumerate() gives us both the index (position) and the weight value, starting at 1
        if weight <= remaining:
            accepted.append(weight)
            remaining -= weight
            print(
                f"- {weight:.2f} kg accepted; remaining capacity is {remaining:.2f} kg."
                #.2f formats the number to two decimal places
                
            )
        else:
            rejected.append((position, weight))
            print(f"- {weight:.2f} kg rejected; it does not fit.")

    loaded = sum(accepted)
    print(f"""\nFinal totals:
    Accepted parcels: {len(accepted)}
    Loaded weight: {loaded:.2f} kg
    Remaining capacity: {remaining:.2f} kg""")

    return {
        #05.10 - return a dictionary with the results
        "accepted": accepted,
        "rejected": rejected,
        "loaded_weight": loaded,
        "remaining_capacity": remaining,
    }
#Task_05 ends here#--------------------------------------------


#Task_06 starts here#-------------------------------------------------------
def read_not_negative_number(prompt):
#05.2
    """Read and return a not negative floating-point number."""
    while True:
        try:
            value = float(input(prompt).strip())
            if value >= 0:
                return value
        except ValueError:
            pass
        print("Please enter a valid number. 0 or bigger")        
    
def classify_service_performance():
# It checks the delivery performance and gives a service status.

    #06.1 Keep asking for the promised delivery time until valid input is entered.
    # Ask the user for the promised delivery time.
    promised = read_positive_number("Enter promised delivery time in minutes: ")

            
    #06.2 Keep asking for the actual delivery time until valid input is entered.
    # Ask the user for the actual delivery time.
    actual = read_positive_number("Enter actual delivery time in minutes: ")
    
    
    # Ask the user how many parcels were damaged.
    damaged = read_not_negative_number("Enter number of damaged parcels: ")

    # Calculate the delay.
    #06.4 Actual time minus promised time gives the signed delay.
    delay = actual - promised

    #06.5 Check damaged parcels first.
    # Damage has priority over the delivery time.
    if damaged > 0:

        # If there is at least one damaged parcel,
        # the service has failed.
        status = "SERVICE FAILURE"

    # If there are no damaged parcels,
    #06.6 check whether the delivery was early or on time.
    elif delay <= 0:

        # A negative delay means early.
        # A zero delay means exactly on time.
        status = "ON TIME"

    # If the delay is between 1 and 15 minutes,
    # classify it as a minor delay.
    elif delay <= 15:

        # 15 minutes is included in MINOR DELAY.
        status = "MINOR DELAY"

    # If none of the conditions above are true,
    # the delay is greater than 15 minutes.
    else:

        # Classify the delivery as a major delay.
        status = "MAJOR DELAY"

    print(f"""
    Delay: {delay} minutes
    Service status: {status}""")
#Task_06 ends here#---------------------------------------------------------

#Task_07 starts here#-------------------------------------------------
def produce_weekly_report():
# This function creates the weekly dispatch report.

    # Store the names of the seven days in order.
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    # Keep asking for the daily delivery counts until valid input is entered.
    while True:

        # Get all seven delivery counts in one input.
        counts_input = input(
            "Enter seven daily delivery counts (Monday-Sunday), separated by commas: "
        )

        # Split the input at each comma. and stripi them from whitespacse 
        parts = counts_input.strip().split(",")

        # Check that exactly seven values were entered.
        if len(parts) != 7:
            print("Error - Weekly report requires 7 delivery counts.")
            continue

        # Create an empty list to store the seven counts.
        counts = []

        # Assume the input is valid.
        valid = True

        # Go through each value that the user entered.
        for part in parts:

            # Remove spaces around the value.
            part = part.strip()

            # Try to convert the value to an integer.
            try:
                count = int(part)

                # Check if the count is negative.
                if count < 0:
                    print("Error - Value cannot be negative.")
                    valid = False
                    break

                # Add the valid count to the list.
                counts.append(count)

            # This runs if the value is not a whole number.
            except ValueError:
                print("Error - Please enter whole numbers.")
                valid = False
                break

        # If an invalid value was found, ask for the counts again.
        if not valid:
            continue

        # If all seven counts are valid, leave the input loop.
        break

    # Keep asking for the daily target until a valid target is entered.
    while True:

        # Ask the user for the daily delivery target.
        target_input = input("Enter daily delivery target: ")
        #consider target_input = int(input("Enter daily delivery target: "))

        # Try to convert the target into an integer.
        try:
            target = int(target_input)

            # Check if the target is negative.
            if target < 0:
                print("Error - Value cannot be negative.")

            # Zero and positive numbers are valid.
            else:
                break
                # Break means the input is valid, so leave the loop.

        # This runs if the user does not enter a whole number.
        except ValueError:
            print("Error - Please enter a whole number.")

    # Start the total at zero.
    total = 0

    # Add each daily count to the total.
    for count in counts:
        total = total + count

    # Calculate the average by dividing the total by seven.
    average = total / 7

    # Start with Monday as the highest day.
    highest = counts[0]
    highest_day = days[0]

    # Start with Monday as the lowest day.
    lowest = counts[0]
    lowest_day = days[0]

    # Go through all seven days.
    for i in range(7):
        #ra

        # Get the current day's delivery count.
        current_count = counts[i]

        # Check if this count is greater than OR equal to
        # the current highest count.
        # Using >= means the later tied day replaces the earlier day.
        if current_count >= highest:
            highest = current_count
            highest_day = days[i]

        # Check if this count is less than OR equal to
        # the current lowest count.
        # Using <= means the later tied day replaces the earlier day.
        if current_count <= lowest:
            lowest = current_count
            lowest_day = days[i]

    # Start the target-meeting day counter at zero.
    days_meeting_target = 0

    # Check each daily delivery count.
    for count in counts:

        # A day meets the target when deliveries are
        # greater than or equal to the target.
        if count >= target:
            days_meeting_target += days_meeting_target


    print(f"""
{'Total deliveries ':.<21}: {total}
{'Average per day ':.<21}: {average:.2f}
{'Highest day ':.<21}: {highest_day}
{'Lowest day ':.<21}: {lowest_day}
{'Days meeting target ':.<21}: {days_meeting_target}
""")
#Task_07 ends here#---------------------------------------------------


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
    print(f"\n{'Cheapest service':.<25}: {cheapest_name:>07} SEK")
    print(f"{'Most expensive service':.<25}: {most_expensive_name:>07} SEK")
#Task_09 ends here#------------------------------------------------


if __name__ == "__main__":
	# Start the application only when this file is run directly.
	main()
