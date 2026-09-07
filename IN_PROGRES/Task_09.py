#09.1 
def compare_service_scenarios():

    # 09.2 Keep asking for the distance until valid input is entered.
    while True:
        raw_distance = input("Enter distance in km: ").strip()
        try:
            distance = float(raw_distance)
            if distance < 0:
                print("Error - Value cannot be negative.")
                continue
            break
        except ValueError:
            print("Error - Please enter a number.")

    # 09.2 Keep asking for the weight until valid input is entered.
    while True:
        try:
            raw_weight = input("Enter weight in kg: ").strip()
            weight = float(raw_weight)
            if weight < 0:
                print("Error - Value cannot be negative.")
                continue
            break
        except ValueError:
            print("Error - Please enter a number.")

services = []
standard_quote = subtotal * 1.0
express_quote = subtotal * 1.25
priority_quote = subtotal * 1.6


print(f"""
Distance: {distance:.2f} km
Weight: {weight:.2f} kg
Standard Quote: ${standard_quote:.2f}
Express Quote: ${express_quote:.2f}
Priority Quote: ${priority_quote:.2f}
""")