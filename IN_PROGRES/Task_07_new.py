#_________TASK____07_____________#

# Weekly report: exactly seven non-negative delivery counts are required;
# target must be non-negative.
# Note: read_not_negative_number() is defined in Task 6 and reused here.


def read_weekly_counts(prompt):
    """Repeatedly read 7 comma-separated, non-negative whole numbers.

    Returns them as a list of integers once the input is valid.
    """
    # Keep asking until valid input is entered; return exits the loop.
    while True:

        try:
            # Read the raw text and split it into pieces at the commas.
            weekly_counts = input(prompt)
            count_lst = weekly_counts.split(",")

            # Convert each piece to an integer and collect it in a new list.
            week_list = []
            for amount in count_lst:
                week_list.append(int(amount))

        except ValueError:
            # A piece could not be converted (e.g. "abc"), so ask again.
            print("Error - Please enter a whole number.")
            continue

        if len(week_list) == 7:
            # Flag pattern: assume valid, flip to False if any count is negative.
            valid = True
            for num in week_list:
                if num < 0:
                    valid = False

            # Checked after the for loop, so continue restarts the while loop.
            if not valid:
                print("Error - Value cannot be negative.")
                continue

        else:
            # Wrong number of counts, so ask again.
            print("Error - Weekly report requires 7 delivery counts.")
            continue

        # All checks passed: hand the list back to the caller.
        return week_list


def calculate_total(week_list):
    """Return the sum of all daily counts (without using sum())."""
    tot_delivery = 0
    for num in week_list:
        tot_delivery += num
    return tot_delivery


def count_days_meeting_target(week_list, target):
    """Return how many days met or exceeded the target."""
    days_met_target = 0
    for num in week_list:
        if num >= target:
            days_met_target += 1
    return days_met_target


def find_highest_index(week_list):
    """Return the position of the highest count (without using max()).

    Uses >= so that on a tie, the LAST day with the highest value wins.
    """
    # Start by treating the first day as the highest so far.
    highest_i = 0
    for i, num in enumerate(week_list):
        if num >= week_list[highest_i]:
            highest_i = i
    return highest_i


def find_lowest_index(week_list):
    """Return the position of the lowest count (without using min()).

    Uses <= so that on a tie, the LAST day with the lowest value wins.
    """
    # Start by treating the first day as the lowest so far.
    lowest_i = 0
    for i, num in enumerate(week_list):
        if num <= week_list[lowest_i]:
            lowest_i = i
    return lowest_i


def produce_weekly_report():
    """Read the weekly counts and target, then print the weekly report.

    Calculations are done by the helper functions above; this function
    only collects input and prints the results.
    """
    # Weekday names; a position in week_list maps to the same position here.
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    # Collect validated input.
    week_list = read_weekly_counts("Completed deliveries: ")
    target = read_not_negative_number("Daily target: ")

    # Calculate the statistics.
    tot_delivery = calculate_total(week_list)
    avg_per_day = tot_delivery / 7
    days_met_target = count_days_meeting_target(week_list, target)
    highest_i = find_highest_index(week_list)
    lowest_i = find_lowest_index(week_list)

    # Use the positions to look up each count and its weekday name.
    highest = week_list[highest_i]
    highest_day = days[highest_i]
    lowest = week_list[lowest_i]
    lowest_day = days[lowest_i]

    # Print the report in the exact format required by the brief.
    print("Weekly dispatch report")
    print(f"Total deliveries: {tot_delivery}")
    print(f"Average per day: {avg_per_day:.2f}")
    print(f"Highest day: {highest_day} ({highest})")
    print(f"Lowest day: {lowest_day} ({lowest})")
    print(f"Days meeting target: {days_met_target}")