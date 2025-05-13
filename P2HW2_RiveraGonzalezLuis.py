 #Luis Rivera Gonzalez
 #2/27/2025
 #P2HW2
 #This program gets grades from user and calculate lowest, highest, sum and average of grades 

# Get user input (Grades)
module_1 = float(input("Enter grade for Module 1: "))
module_2 = float(input("Enter grade for Module 2: "))
module_3 = float(input("Enter grade for Module 3: "))
module_4 = float(input("Enter grade for Module 4: "))
module_5 = float(input("Enter grade for Module 5: "))
module_6 = float(input("Enter grade for Module 6: "))

# Calculate lowest, highest, sum and average of grades 
grades = [module_1, module_2, module_3, module_4, module_5, module_6]
lowest = min(grades)
highest = max(grades)
sum_of_grades = sum(grades)
average = sum_of_grades / len(grades)

# Print results
print("\n" + ("-" * 12) + "Results" + ("-" * 12)) 
print(f"{'Lowest Grade:':<20} {lowest:.2f}")
print(f"{'Highest Grade:':<20} {highest:.2f}")
print(f"{'Sum of Grades:':<20} {sum_of_grades:.2f}")
print(f"{'Average:':<20} {average:.2f}")
print("-" * 32)