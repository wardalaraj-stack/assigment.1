"""
Inputs

[07.1 ] Read one comma-separated input containing exactly seven daily delivery counts
  in Monday-to-Sunday order.
[07.2 ] Read one daily delivery target.
[07.3 ] Accept zero as a valid count and target.
[07.4 ] Reject negative counts and negative targets.
[07.5 ] Reject input containing fewer or more than seven delivery counts.
[07.6 ] Keep the day names paired with their original input positions.

Calculations

[07.7 ] Calculate total deliveries with an accumulator while traversing the list.
[07.8 ] Calculate average deliveries as total divided by 7.
[07.9 ] Find the highest daily count without using max().
[07.10 ] Find the lowest daily count without using min().
[07.11 ] Report the last day with the highest count when there is a tie.
[07.12 ] Report the last day with the lowest count when there is a tie.
[07.13 ] Count every day whose deliveries are greater than or equal to the target.
[07.14 ] Do not use sum(), index(), or a statistics library.
[07.15 ] Print the average with two decimal places.
"""


# This function creates the weekly dispatch report.
def produce_weekly_report():

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
Total deliveries: {total}
Average per day: {average:.2f}
Highest day: {highest_day}
Lowest day: {lowest_day}
Days meeting target: {days_meeting_target}
""")



def main():
    while True:
        print("""\nHARBORFLOW DISPATCH CONSOLE
        7. Produce weekly dispatch report
        0. Exit""")
        choice = input("Select an option: ").strip()
        if choice == "7":
            produce_weekly_report()
        elif choice == "0":
            print("Goodbye.")
            return
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()