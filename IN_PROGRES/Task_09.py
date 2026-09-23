import os
import sys

# Add the project folder so this file can import the shared Task 3 functions.
project_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_folder)

from harborflow_app import calculate_quote, read_positive_number


def main():
    # Keep showing the Task 9 menu until the user chooses to exit.
    while True:
        print("""\nHARBORFLOW DISPATCH CONSOLE
        8. Compare service scenarios
        0. Exit""")
        choice = input("Select an option: ").strip()
        if choice == "8":
            # Start the service comparison when option 8 is selected.
            compare_service_scenarios()
        elif choice == "0":
            # Stop the loop and close this standalone Task 9 runner.
            print("Goodbye.")
            return
        else:
            # Reject menu choices other than 8 and 0.
            print("Invalid option.")


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


if __name__ == "__main__":
    main()