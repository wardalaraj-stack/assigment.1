"""
DIT014 - Assignment 1 - HarborFlow Dispatch Console
Task 4: Consolidate parcel labels

SPEC-SAFE VERSION:
- splits at commas
- removes SURROUNDING spaces
- converts to uppercase
- removes duplicates
- preserves first-seen order
- does NOT use set()
"""


def consolidate_parcel_labels():
    # Read the complete scanner export from one console line.
    raw_input = input("Scanned labels: ")

    # Split the original text wherever a comma appears.
    label_parts = raw_input.split(",")

    # This list stores only the first occurrence of each normalized label.
    unique_labels = []

    # Process labels from left to right.
    for part in label_parts:
        # Official Task 4 normalization:
        # strip() removes whitespace only from the beginning and end.
        # upper() converts letters to uppercase.
        # replace(" ", "") removes ordinary internal space characters.
        cleaned = part.strip().upper().replace(" ", "")

        # Add the label only when it has not already been retained.
        if cleaned not in unique_labels:
            unique_labels.append(cleaned)

    print("Unique load list:")

    # Print numbered output starting at 1.
    for index in range(len(unique_labels)):
        print(f"{index + 1}. {unique_labels[index]}")

    print(f"Total unique parcels: {len(unique_labels)}")


if __name__ == "__main__":
    consolidate_parcel_labels()