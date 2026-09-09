"""HarborFlow dispatch console: van-capacity checking.
 Read the van capacity in kilograms.
[05.1 ] Read a comma-separated list of parcel weights in kilograms.
[05.2 ] Require the capacity and every weight to be positive numbers.
[05.3 ] Strip spaces around each weight.
[05.4 ] Process weights in their original left-to-right order.
[05.5 ] Start the remaining capacity at the entered capacity.
[05.6 ] Accept a parcel when its weight is less than or equal to the remaining
    capacity.
[05.7 ] Subtract accepted weights immediately.
[05.8 ] Reject a parcel when it is heavier than the remaining capacity.
[05.9 ] Do not stop after a rejection; continue with the next parcel.
[05.10 ] Do not subtract rejected weights.
"""


def _read_positive_number(prompt):
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

#Task_05 Starts here#------------------------------------------
def check_van_capacity():
#05.1 - 05.10
    """Check van capacity against a list of parcel weights."""
    """Process parcel weights from left to right and print the result."""
    capacity = _read_positive_number("Capacity (kg): ")

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

def main():
    while True:
        print("""\nHARBORFLOW DISPATCH CONSOLE
        5. Check van capacity
        0. Exit""")
        choice = input("Select an option: ").strip()
        if choice == "5":
            check_van_capacity()
        elif choice == "0":
            print("Goodbye.")
            return
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()