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
    
# It checks the delivery performance and gives a service status.
def classify_service_performance():

    #06.1 Keep asking for the promised delivery time until valid input is entered.
    while True: 

        # Try to convert the user's input into a number.
        try:
            # Ask the user for the promised delivery time.
            promised = float(input("Enter promised delivery time in minutes: "))

            # Check if the number is negative.
            if promised < 0:
                # Show an error if the number is negative.
                print("Error - Value cannot be negative.")

            # If the number is valid, leave the loop.
            else:
                break

        # This runs if the user enters something that is not a number.
        except ValueError:
            # Tell the user to enter a number.
            print("Error - Please enter a number.")

    #06.2 Keep asking for the actual delivery time until valid input is entered.
    while True:

        # Try to convert the user's input into a number.
        try:
            # Ask the user for the actual delivery time.
            actual = float(input("Enter actual delivery time in minutes: "))

            # Check if the number is negative.
            if actual < 0:
                # Show an error if the number is negative.
                print("Error - Value cannot be negative.")

            # If the number is valid, leave the loop.
            else:
                break

        # This runs if the user enters something that is not a number.
        except ValueError:
            # Tell the user to enter a number.
            print("Error - Please enter a number.")

    #06.3 Keep asking for the number of damaged parcels until valid input is entered.
    while True:

        # Try to convert the input into a whole number.
        try:
            # Ask the user how many parcels were damaged.
            damaged = int(input("Enter number of damaged parcels: "))

            #06.7 Check if the number is negative.
            if damaged < 0:
                # Show an error if the number is negative.
                print("Error - Value cannot be negative.")

            # If the number is valid, leave the loop.
            else:
                break

        # This runs if the user does not enter a whole number.
        except ValueError:
            # Tell the user to enter a whole number.
            print("Error - Please enter a whole number.")

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