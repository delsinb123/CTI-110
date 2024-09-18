# Delsin Barrett
# 9/4/2024
# P3HW2
# Calculate payrates using if/else statements

#Get info from user
name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

#Display Name

print("-------------------------------\nEmployee name: ", name)

#Calculate employee pay

if hours > 40:
    #They have overtime
    pay_amt = 40 * pay_rate
    ot_pay_rate = 1.5 * pay_rate
    ot_hours = hours - 40
    ot_pay_amt = ot_hours * ot_pay_rate
else:
    pay_amt = hours * pay_rate
    ot_hours = 0
    ot_pay_amt = 0

#Calculate gross pay
gross_pay = pay_amt + ot_pay_amt

print()

#Display Headings
print(f"{'Hours Worked':<16}{'Pay Rate':<12}{'OverTime Hours':<18}{'OverTime Pay':<18}{'RegHour Pay':<18}{'Gross Pay':<16}")
print("-" * 100)
print(f"{hours:<16}{pay_rate:<12}{ot_hours:<18}${ot_pay_amt:<17.2f}${pay_amt:<17.2f}${gross_pay:<15.2f}") 
