 # Luis Rivera Gonzalez
 # 2/6/2025
 # P1HW1 
 # This program gets the user's input and does some math calculations

print("----Calculating Exponents----\n")
base_num = int(input("Enter an integer as the base value: "))
exponent_num = int(input("Enter an integer as the exponent: "))
result = base_num**exponent_num
print()
print(base_num, "raised to the power of", exponent_num, "is", result,"!!\n\n")


print("----Addition and Subtraction----\n")
starting_num = int(input("Enter a starting integer: "))
adding_num = int(input("Enter an integer to add: "))
subtracting_num = int(input("Enter an integer to subtract: "))
result = starting_num + adding_num - subtracting_num
print()
print(starting_num, "+", adding_num, "-", subtracting_num, "is equal to", result)
