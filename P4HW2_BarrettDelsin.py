# Delsin Barrett
# 9/4/2024
# P4HW2
# Calculate payrates using if/else statements and loops

# Create variabkes for num employees and their pay
num_emp = 0
total_ot = 0
total_reg = 0
total_gross = 0

#Get info from user
name = input("Enter employee's name: ")
while name != "Done":
    
    num_emp +=  1
    
    
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
        total_ot = total_ot + ot_pay_amt
        total_reg += pay_amt
        total_gross += gross_pay
    else:
        pay_amt = hours * pay_rate
        ot_hours = 0
        ot_pay_amt = 0
        total_ot = total_ot + ot_pay_amt
        total_reg += pay_amt
       

    #Calculate gross pay
    gross_pay = pay_amt + ot_pay_amt

    total_gross += gross_pay
    

    print()

    #Display Headings
    print(f"{'Hours Worked':<16}{'Pay Rate':<12}{'OverTime Hours':<18}{'OverTime Pay':<18}{'RegHour Pay':<18}{'Gross Pay':<16}")
    print("-" * 100)
    print(f"{hours:<16}{pay_rate:<12}{ot_hours:<18}${ot_pay_amt:<17.2f}${pay_amt:<17.2f}${gross_pay:<15.2f}")

    #Get new input for the name variable- stop endless loop
    name = input("Enter employee's name: ")
        
#Loop ends here
print("Goodbye")

#Print total paid and num of employees
print(f"Total number of employees entered: {num_emp}")
print(f"Total amount paid for overtime: ${total_ot:.2f}")
print(f"Total amount paid for regular hours: ${total_reg:.2f}")
print(f"Total amount paid for gross: ${total_gross:.2f}")

