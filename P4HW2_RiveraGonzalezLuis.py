# Luis Rivera
# 3/27/2025
# P4HW2
# The program however will calculate gross pay for multiple employees, determined by user, and also calculates total amount paid for overtime, total amount paid for regular pay and total amount paid for all employees.


# Ask the user for employee's name
employee_name = input(f'Enter employees\'s name or "Done" to terminate: ')
overtime_total = 0
regularPay_total = 0
grossPay_total = 0
employee_count = 0

# Calculates emplyees pay and updates total amounts 
while employee_name.lower() != "done":
    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

    # calculate overtime if hours worked is more than 40
    overtime_hours = 0
    overtime_pay = 0
    regular_pay = 0
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_payRate = pay_rate * 1.5
        overtime_pay = overtime_hours * overtime_payRate
        regular_pay = 40 * pay_rate
    else:
        regular_pay = hours_worked * pay_rate
    
    # Update total amounts
    grossPay_total += regular_pay + overtime_pay
    regularPay_total += regular_pay
    employee_count += 1

    # Print employees info
    print(f"\nEmployee's Name:\t{employee_name}")
    print(100 * '-')
    print(f"Hours Worked\tPay Rate\tOvertime\tOverTime Pay\tRegHour Pay\tGross Pay")
    print(f"{hours_worked:.2f}\t\t{pay_rate:.2f}\t\t{overtime_hours:.2f}\t\t{overtime_pay:.2f}\t\t{regular_pay:.2f}\t\t{(regular_pay+overtime_pay):.2f}")
    print()
    employee_name = input(f'Enter employees\'s name or "Done" to terminate: ')

# Prints total amount summary
print()
print(f"Total number of employees entered: {employee_count}")
print(f"Total amount paid for overtime ${overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${regularPay_total:.2f}")
print(f"Total amount paid in gross: ${grossPay_total:.2f}")
print()