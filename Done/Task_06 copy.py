"""
# This function handles Task 6.
[06.1 ] Read promised delivery time in minutes.
[06.2 ] Read actual delivery time in minutes.
[06.3 ] Read the number of damaged parcels.
[06.4 ] Calculate delay as actual time minus promised time.
[06.5 ] A negative delay means the delivery was early.
[06.6 ] A zero delay means the delivery was exactly on time.
[06.7 ] Reject negative values for all three inputs.
"""

def read_positive_number(prompt):
#05.2
    """Read and return a positive floating-point number."""
    while True:
        try:
            value = float(input(prompt).strip())
            if value > 0:
                return value
        except ValueError:
            pass
        print("Please enter a positive number.")

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

def main():
    while True:
        print("""\nHARBORFLOW DISPATCH CONSOLE
        6. Check delivery performance
        0. Exit""")
        choice = input("Select an option: ").strip()
        if choice == "6":
            classify_service_performance()
        elif choice == "0":
            print("Goodbye.")
            return
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()