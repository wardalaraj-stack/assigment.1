def print_menu():
	# Display all services that the dispatcher can select.
	# Each print statement creates one exact line of the required menu.
	print("""HARBORFLOW DISPATCH CONSOLE
	1. Close console
	2. Validate booking reference
	3. Calculate delivery quote
	4. Consolidate parcel labels
	5. Check van capacity
	6. Classify service performance
	7. Produce weekly dispatch report
	8. Compare service scenarios""")


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
	# pass temporarily keeps the menu runnable until Task 2 is implemented.
	pass


def calculate_delivery_quote():
	# This function will calculate a delivery price in Task 3.
	# pass temporarily keeps the menu runnable until Task 3 is implemented.
	pass


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
