"""
name = input("Name: ")

age = input("Age: ")
next_age = int(age)+ 1
print(next_age)

name = "Ada Lovelace"
print(name[0:3])

price = 8.5
print(f"{price:.2f}")
print(f"{price:7.2f}")
print(f"{price:07.2f}") 
print(f"{price:.>7.2f}") 

code = input("Enter code: ")
A = code[0:3]
B = code[4:] 
C = code[-6:] 

print(f"A: {A}")
print(f"B: {B}")
print(f"C: {C}")




#YOUR TASK: Create a small Python program that reads information about a
#table, the client, and three products, then prints a formatted receipt.
input :
Table number: 7
Client name: Ada Lovelace
Tea, 18.5
Sandwich, 42
Fruit, 12.75
"""

#YOUR PROGRAM MUST
#· ask the user for a table number and client name
#· ask the user for three product names and their prices
#· convert the table number and prices to appropriate numeric types
#· display the client's name in uppercase
#· calculate the subtotal of the three prices
#· display each price with exactly two decimal places
#· align the product names and prices to create a readable receipt
#· display the table number, client name, and subtotal in the required format

table_number = int(input("Table number: "))
client_name = input("Client name: ")

products = []
for number in range(1, 4):
	product_name = input(f"Product {number} name: ")
	price = float(input(f"Product {number} price: "))
	products.append((product_name, price))

subtotal = sum(price for _, price in products)
#_, is a common convention in Python to indicate that the variable is intentionally being ignored. In this case, we are only interested in the price, so we use _ to ignore the product name.

print("\nReceipt")
print(f"Table: {table_number}")
print(f"Client: {client_name.upper()}")
print("-" * 30)
for product_name, price in products:
	print(f"{product_name:.<23} {price:>07.2f}")
	#:<20 means left-align the product name in a field of 20 characters
	#:>8.2f means right-align the price in a field of 8 characters with 2 decimal places
print("-" * 30)
print(f"{'Subtotal':<20} {subtotal:>8.2f}")
