# ---------------------------------------------------------------------------
# read_positive_number(prompt)
#
# What it does:
#   Repeatedly asks the user to type a number (using the message passed in
#   as "prompt") until they enter something that is both:
#     1. a valid number, and
#     2. greater than zero.
#
# How it works:
#   - Runs inside a "while True" loop so it can keep re-asking on bad input.
#   - Uses try/except to safely attempt float(raw_value). If the text isn't
#     a valid number (e.g. "abc"), float() raises a ValueError, which is
#     caught instead of crashing the program.
#   - If conversion succeeds but the number is zero or negative, it is
#     rejected too.
#   - In both failure cases the required error message is printed and
#     "continue" sends control back to the top of the loop to ask again.
#   - Once a valid positive number is found, it is returned to whichever
#     function called this one.
# ---------------------------------------------------------------------------
def read_positive_number(prompt):
    while True:
        raw_value = input(prompt)
        #prompt is the temporary name for whatever the input is called 

        try:
            value = float(raw_value)
        except ValueError:
            print("Error - Value must be a number.")
            continue

        if value <= 0:
            print("Error - Value must be greater than zero.")
            continue

        return value


# ---------------------------------------------------------------------------
# read_service_code()
#
# What it does:
#   Asks the user to enter a service code and keeps asking until they enter
#   exactly S, X, or P (letters only, case-insensitive).
#
# How it works:
#   - Runs inside a "while True" loop so invalid entries are re-prompted.
#   - strip() removes accidental leading/trailing spaces, and upper()
#     converts lowercase letters (e.g. "s") to uppercase ("S") so the
#     comparison below works no matter how the user typed it.
#   - Checks the normalized code against the three allowed values using
#     "or" conditions. If it matches one of them, that code is returned
#     immediately.
#   - If it doesn't match any of them, the required error message is
#     printed and the loop repeats to ask again.
# ---------------------------------------------------------------------------
def read_service_code():
    while True:
        raw_code = input("Enter service code (S, X or P): ")
        code = raw_code.strip().upper()

        if code == "S" or code == "X" or code == "P":
            return code

        print("Error - Service code must be S, X or P.")


# ---------------------------------------------------------------------------
# service_name(service_code)
#
# What it does:
#   Converts a one-letter service code (S, X, or P) into its full display
#   name (Standard, Express, or Priority), for use in printed output.
#
# How it works:
#   - Starts with an empty "name" as a fallback.
#   - Uses a simple if/elif chain to match the incoming service_code against
#     the three known codes and assign the matching full name.
#   - Returns whatever name was set (or the empty string, if somehow given
#     a code outside S/X/P, which shouldn't happen since the code is always
#     produced by read_service_code() first).
# ---------------------------------------------------------------------------
def service_name(service_code):
    name = ""

    if service_code == "S":
        name = "Standard"
    elif service_code == "X":
        name = "Express"
    elif service_code == "P":
        name = "Priority"

    return name


# ---------------------------------------------------------------------------
# calculate_quote(distance, weight, service_code)
#
# What it does:
#   The single, reusable pricing formula for the whole console. Given a
#   distance, a weight, and a service code, it returns the numeric quote
#   price. This function does no input() or print() of its own - it is
#   pure calculation, so it can be reused by both the quote service and
#   the service-comparison service without copying the formula.
#
# How it works:
#   - Picks the correct multiplier for the given service_code using
#     if/elif: Standard (S) = 1.00, Express (X) = 1.25, Priority (P) = 1.60.
#   - Calculates the base subtotal using the fixed formula:
#       subtotal = 45.00 + (distance * 6.50) + (weight * 4.00)
#     This applies the flat base charge, the per-kilometre distance rate,
#     and the per-kilogram weight rate.
#   - Multiplies that subtotal by the chosen multiplier to get the final
#     quote, with no intermediate rounding.
#   - Returns the resulting number to the caller.
# ---------------------------------------------------------------------------
def calculate_quote(distance, weight, service_code):
    multiplier = 1.00

    if service_code == "S":
        multiplier = 1.00
    elif service_code == "X":
        multiplier = 1.25
    elif service_code == "P":
        multiplier = 1.60

    subtotal = 45.00 + (distance * 6.50) + (weight * 4.00)
    quote = subtotal * multiplier

    return quote


# ---------------------------------------------------------------------------
# calculate_delivery_quote()
#
# What it does:
#   This is the delivery-quote SERVICE: it handles all the user-facing
#   input and output for Task 3, then hands the actual math off to
#   calculate_quote(). This keeps input/output separate from the formula.
#
# How it works:
#   - Calls read_positive_number() twice to safely collect a valid distance
#     and a valid weight (each one loops internally until valid).
#   - Calls read_service_code() to safely collect a valid S/X/P code.
#   - Passes all three values into calculate_quote() to get the numeric
#     price back.
#   - Prints the service's full name (via service_name()) and the price,
#     formatted to exactly two decimal places using format(price, ".2f"),
#     followed by the currency label "SEK".
#   - Once printing is done, the function simply ends, which returns
#     control back to whatever called it (main()).
# ---------------------------------------------------------------------------
def calculate_delivery_quote():
    distance = read_positive_number("Enter delivery distance in kilometres: ")
    weight = read_positive_number("Enter parcel weight in kilograms: ")
    service_code = read_service_code()

    price = calculate_quote(distance, weight, service_code)

    print("Service: " + service_name(service_code))
    print("Delivery quote: " + format(price, ".2f") + " SEK")


# ---------------------------------------------------------------------------
# main()
#
# What it does:
#   Runs the persistent menu loop for the whole console. Shows the menu,
#   reads the user's choice, and dispatches to the matching service
#   function. This is the only place allowed to end the program normally.
#
# How it works:
#   - Runs inside a "while True" loop so the menu keeps reappearing after
#     every service finishes.
#   - Prints the menu text, then reads the user's choice with input(),
#     stripping any accidental surrounding spaces.
#   - If the choice is "1", prints a closing message and "break"s out of
#     the loop, which ends the program.
#   - If the choice is "3", calls calculate_delivery_quote() to run that
#     service; once that function finishes, control returns here and the
#     loop goes back to the top to show the menu again.
#   - Any other choice falls into the "else" branch, which prints the
#     required error message and then loops back to show the menu again
#     (invalid choices never crash or exit the program).
# ---------------------------------------------------------------------------
def main():
    while True:
        print("")
        print("HARBORFLOW DISPATCH CONSOLE")
        print("1. Exit")
        print("3. Calculate delivery quote")

        choice = input("Select a service: ").strip()

        if choice == "1":
            print("Goodbye.")
            break
        elif choice == "3":
            calculate_delivery_quote()
        else:
            print("Error - Select a service from 1 to 8.")


# ---------------------------------------------------------------------------
# This check makes sure main() only runs when this file is executed directly
# (e.g. "python harborflow_app.py"), and not if this file were ever imported
# as a module into another script.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    main()