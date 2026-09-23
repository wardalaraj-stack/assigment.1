#Task_02 starts here#
def validate_booking_reference():
    reference = input("Enter booking reference: ")
    normalized = reference.strip().upper()
    #strip() removes thr white space from before and after the refrense only

    parts = normalized.split("-")
    #.splits the refrense at the "-" and removes it 

    is_valid = False

    if len(parts) == 3:
    #cheaks if the parts splited by .split() are ==3

        prefix = parts[0]
        code = parts[1]
        number = parts[2]
        # naming the parts 

    # validating the parts are matching with they should be
        prefix_ok = (prefix == "HFL")
        code_ok = (len(code) == 3 and code.isalpha())
        #.isalpha() is to make sure the 3 charecters in the string input are alphabitical not numbers or stuff
        number_ok = (len(number) == 4 and number.isdigit())
        #.isdigit - same thing but in reverse so it looks for digits 
        
        if prefix_ok and code_ok and number_ok:
            is_valid = True

    if is_valid:
        print(f"\nBooking reference: {normalized}")
        print("Valid booking reference.")
        print("Returning to main menu...")
    else:
        print(f"""
Invalid booking reference.
Expected format: HFL-XXX-YYYY
    
1. Validate again 
2. Exit
        """)

        servise = input("Select an option: ").strip()
        if servise == "1":
            validate_booking_reference()
        elif servise == "2":
            print("Goodbye.")
            main()
#Task_02 ends here#


def main():
    while True:
        print("")
        print("HARBORFLOW DISPATCH CONSOLE")
        print("1. Exit")
        print("2. Validate booking reference")

        choice = input("Select a service: ").strip()

        if choice == "1":
            print("Goodbye.")
            break
        elif choice == "2":
            validate_booking_reference()
        else:
            print("Error - Select a service from 1 to 8.")


if __name__ == "__main__":
    main()