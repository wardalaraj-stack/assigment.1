#_________TASK____07_____________#

# Weekly report: exactly seven non-negative delivery counts are required; target must be non-negative.
 
def read_weekly_counts(prompt):

    while True:

        try: 
            weekly_counts = input(prompt)
            count_lst = weekly_counts.split(",")
            week_list = []
            for amount in count_lst:
                week_list.append(int(amount))
    
        except ValueError:
            # The text could not be converted (e.g. "abc"), so ask again.
            print("Error - Please enter a whole number.")
            continue

        if len(week_list) == 7:
            valid = True
            for num in week_list:
                if num < 0 :
                    valid = False
            if not valid:
                print("Error - Value cannot be negative.")
                continue

        else:
            print("Error - Weekly report requires 7 delivery counts.")
            continue

        return week_list



def produce_weekly_report():

    days = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
        ]

    week_list = read_weekly_counts("Completed deliveries: ")
    target = read_not_negative_number("Daily target: ")
    tot_delivery = 0
    days_met_target = 0
    highest = week_list[0]
    lowest = week_list[0]
    highest_day = days[0]
    lowest_day = days[0]

    for i, num in enumerate(week_list):
        tot_delivery += num

        if num >= target:
            days_met_target += 1

        if num >= highest:
            highest = num
            highest_day = days[i]
        if num <= lowest:
            lowest = num
            lowest_day = days[i]

    avg_per_day = tot_delivery / 7

    print("Weekly dispatch report")
    print(f"Total deliveries: {tot_delivery}")
    print(f"Average per day: {avg_per_day:.2f}")      
    print(f"Highest day: {highest_day} ({highest})")
    print(f"Lowest day: {lowest_day} ({lowest})")
    print(f"Days meeting target: {days_met_target}")
   
    