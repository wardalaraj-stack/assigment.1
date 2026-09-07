# ---------------------------------------------------------------------------
# HARBORFLOW DISPATCH CONSOLE
# TASK 4: CONSOLIDATE PARCEL LABELS
#
# This file follows the assignment requirements for Task 4:
# -4.1 Accept one comma-separated input string 
# -4.2 Normalize each label by trimming spaces and converting to uppercase
# -4.3 Ignore empty labels created by repeated or trailing commas
# -4.4 Remove duplicates while preserving first-seen order
# -4.5 Print each label with a number and the total count
# -4.6 Return to the persistent menu after the result is printed
#
# Important design limits from the assignment:
# - No set() is allowed
# - No list comprehensions are allowed
# - No dictionaries are allowed
# - No file reading or writing is used in this service
# ---------------------------------------------------------------------------


def consolidate_parcel_labels():
    """
     
    # What it does:
       Reads a comma-separated list of labels, normalizes each one,
       removes duplicates while keeping first-seen order, and prints the
      final list with numbers and a total count.
    
    # How it works:
       1. Read the user's raw text input as one string.
           raw input
       2. Split the string by commas to separate each label.
            raw_input.split(",")
            make list of labels
       3. Trim spaces from each label and convert it to uppercase.            cleaned = item.strip()
            normalized = cleaned.upper()            
       4. Ignore empty items caused by repeated commas or extra spaces.
          if cleaned == "":
       5. Use a list to store only the first occurrence of each unique label.
          if normalized not in unique_labels:
                unique_labels.append(normalized)
       6. Print each unique label with numbering starting at 1.
       7. Print the total number of unique labels.
     -------------------------------------------------------------------
"""
    # Read one comma-separated string from the user.
    raw_input = input("Enter parcel labels separated by commas: ")

    # Split the full string at every comma.
    # Example: "box-1, BOX-2, box-1" becomes ["box-1", " BOX-2", " box-1"]
    label_parts = raw_input.split(",")

    # Create an empty list that will store only the unique normalized labels.
    # We do NOT use set() because the assignment explicitly forbids it.
    unique_labels = []

    # Loop through every item created by the split.
    for item in label_parts:
        # Strip spaces around the label so " box-1 " becomes "box-1".
        cleaned = item.strip().upper()

        # Ignore empty items such as "", " ", or labels made by repeated commas.
        # This prevents blank labels from being counted or printed.
        if cleaned == "":
            continue

        # Normalize the label to uppercase so case differences do not create duplicates.
        normalized = cleaned.upper()

        # Check whether this normalized label has already appeared.
        # This is the duplicate check using a list.
        # If it is not in the list, add it in first-seen order.
        if normalized not in unique_labels:
            unique_labels.append(normalized)
            #.append() adds the new label to the end of the list, preserving order.

    # Print each normalized label with numbering starting at 1.
    # Enumerate gives the number and the label value.
    for number, label in enumerate(unique_labels, start=1):
        print(str(number) + ". " + label)

    # Print the total number of unique labels.
    print("Total labels: " + str(len(unique_labels)))


def print_menu():
    print("HARBORFLOW DISPATCH CONSOLE")
    print("1. Close console")
    print("4. Consolidate parcel labels")


def main():
    console_active = True

    while console_active:
        print_menu()

        while True:
            try:
                choice = int(input("Select service: "))
                if choice in (1, 4):
                    break
                print("Error - Select a service from 1 to 8.")
            except ValueError:
                print("Error - Select a service from 1 to 8.")

        if choice == 1:
            print("Console closed. Dispatch data remains safe.")
            console_active = False
        elif choice == 4:
            consolidate_parcel_labels()


# Ensures the script runs only when executed directly.
if __name__ == "__main__":
    main()
