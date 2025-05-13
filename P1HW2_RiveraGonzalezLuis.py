 # Luis Rivera Gonzalez
 # 2/6/2025
 # P1HW2
 # This program calculates and displays travel expenses

#Get inputs from the user
print("This program calculates and displays travel expenses\n")
budget = int(input("Enter Budget: "))
print()
destination = input("Enter you travel destination: ")
print()
gas = int(input("How much do you think you will spend on gas? "))
print()
hotel = int(input("Approximately, how much will you need for accomodation/hotel? "))
print()
food = int(input("Last, how much do you need for food? "))

#Print information provided by user
print()
print("----------Travel Expenses----------")
print("Location:", destination)
print("Initial Budget:", budget)
print()
print("Fuel:", gas)
print("Accomodation:", hotel)
print("Food:", food)
print()

#Calculate the remaining balance and print it
remaining_balance = budget - gas - hotel - food
print("Remaining Balance: ", remaining_balance)