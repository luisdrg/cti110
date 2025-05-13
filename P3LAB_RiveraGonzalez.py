# Luis Rivera Gonzalez
# 3/4/2025
# P3LAB
# Using if/else statments

# Get the ammount of money as a float
amount = float(input("Enter the amount of money as a float: $"))

# Print no change if the amount is $0.00
if(amount == 0.00):
    print('No change')

# Convert amount into an integer
amount = int(round(amount  * 100, 2))

# Calculate num_dollars in ammount
num_dollars = amount // 100
amount = amount - (num_dollars * 100)

# Calculate num_quarters in ammount
num_quarters = amount // 25
amount = amount - (num_quarters * 25)

# Calculate num_dimes in ammount
num_dimes = amount // 10
amount = amount - (num_dimes * 10)

# Calculate num_nickel in ammount
num_nickel = amount // 5
amount = amount - (num_nickel * 5)

# Set num_pennies
num_pennies = amount

# Print the most efficient number of dollars, quarters, dimes, nickels, and pennies needed to make the given amount of money (with proper grammar)
if(num_dollars > 0):
    if(num_dollars > 1):
        print(f"{num_dollars} Dollars")
    else: 
        print(f"{num_dollars} Dollar")

if(num_quarters > 0):
    if(num_quarters > 1):
        print(f"{num_quarters} Quarters")
    else:
        print(f"{num_quarters} Quarter")

if(num_dimes > 0):
    if(num_dimes > 1):
        print(f"{num_dimes} Dimes")
    else:
        print(f"{num_dimes} Dime")

if(num_nickel > 0):
    if(num_nickel > 1):
        print(f"{num_nickel} Nickels")
    else:
        print(f"{num_nickel} Nickel")

if(num_pennies > 0):
    if(num_pennies > 1):
        print(f"{num_pennies} Pennies")
    else:
        print(f"{num_pennies} Penny")