def calculate_payroll():
    total_payroll = 0.0
    
    while True:
        hourly_wage = float(input("Please enter the employee's hourly wage (negative to stop): "))
        if hourly_wage < 0:
            break
        
        hours_worked = float(input("Enter the hours worked: "))
        if hours_worked > 40:
            regular_pay = 40 * hourly_wage
            overtime_pay = (hours_worked - 40) * (1.5 * hourly_wage)
            employee_pay = regular_pay + overtime_pay 
        else:
            employee_pay = hourly_wage * hours_worked

        total_payroll = total_payroll + employee_pay

    if total_payroll > 5000:
        print("The payroll exceeded the budget. ")

    return total_payroll

def main():
    total_payroll = calculate_payroll()
    print("Total payroll is: ", total_payroll)

main()