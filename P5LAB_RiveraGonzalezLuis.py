# Luis Rivera Gonzalez
# 4/1/2025
# P5LAB
# his program will simulate a customer using a self-checkout machine. A random float value will be generated as the total owed for the purchase. The user should be prompted to enter the amount of money they will put into the self-checkout machine (as a float). The program should then display the amount of dollars, quarters, dimes, nickels, and pennies required to make the change

import random

def main():
    owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${owed}")
    cash = float(input("How much cash will you put in the self-checkout? "))
    change = (cash - owed)
    print(f"Change is: ${change:.2f}\n")
    disperse_change(change)


def disperse_change(num):
    # Get the ammount of money as a float
    amount = num

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
            

main()
