# Luis Rivera Gonzalez
# 3/20/2025
# P4LAB2
# Displays information to users using loops.

# Variable to control while loop
run_again = "yes"

# While loop to control the main logic
while run_again.lower() != "no":
    integer = int(input("Enter an integer: "))
    if integer >= 0:
        for i in range(1,13):
            print(f"{integer} * {i} = {integer * i}")
    else:
        print("This program does not handle negative number")
    run_again = input("Would you like to run the program again? ")

# While Loop ends here
print("Okay, Goodbye!")
