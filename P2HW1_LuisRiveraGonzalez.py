 # Luis Rivera Gonzalez
 # 2/25/2025
 # P2HW1 
 # This program calculates and displays travel expenses

# Getting user input
print("This program calculates and displays travel expenses\n")
budget = float(input("Enter Budget: "))
print()
location = input("Enter your travel destination: ")
print()
fuel = float(input("How much do you think you will spend on gas? "))
print()
accomodation = float(input("Approximately, how much will you need for accomodation/hotel? "))
print()
food = float(input("Last, how much do you need for food? "))
print()

#Calculating remaining balance
remaining_balance = budget - fuel - accomodation - food

# Printing information for the user
print(("-" * 12) + "Travel Expenses" + ("-" * 12)) 
print(f"{'Location:':<25} {location}")
print(f"{'Initial Budget:':<25} ${budget:.2f}")
print(f"{'Fuel:':<25} ${fuel:.2f}")
print(f"{'Accomodation:':<25} ${accomodation:.2f}")
print(f"{'Food:':<25} ${food:.2f}")
print("-" * 40)
print(f"{'\nRemaining Balance:':<25} ${remaining_balance:.2f}")