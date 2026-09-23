"""
DIT014 - Assignment 1 - HarborFlow Dispatch Console
Task 5: Check van capacity

Includes the Task 8 validation relevant to:
- van capacity > 0
- every parcel weight > 0
"""


def read_positive_number(prompt):
    """Read one numeric value greater than zero."""
    while True:
        raw_value = input(prompt)

        try:
            value = float(raw_value)
        except ValueError:
            print("Error - Value must be greater than zero.")
            continue

        if value > 0:
            return value

        print("Error - Value must be greater than zero.")


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


if __name__ == "__main__":
    check_van_capacity()
