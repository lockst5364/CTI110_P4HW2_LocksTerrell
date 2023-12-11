#CTI-110
#P4HW2 - Salary Calculator
#Terrell Locks
#November 26, 2023
#

#all values that are used are added here

employees = 2
overtime_pay = 0
reghour_pay = 0
gross_pay = 0
hours = 0
overtime = 0

#user inputs employee information

name = (input('Enter Employee\'s name or "Done" to terminate: '))
hours = float(input(f"How many hours did {name} work: "))
pay = float(input(f"What is {name}'s pay rate: "))

print('')

#employee's pay is calculated

while name == 'Done':
        employees+=1
if hours > 40:
        overtime = hours - 40
        overtime_pay = overtime * pay * 1.5
        reghour_pay = pay * 40
        gross_pay = overtime_pay + reghour_pay
else:
        overtime = 0
        overtime_pay = 0
        reghour_pay = pay * hours
        gross_pay = reghour_pay

overtime = overtime + overtime_pay
reghour_pay = reghour_pay + pay
total_gross = overtime + reghour_pay

print('Employee name:   ', name)
print('')
print('Hours worked   Pay Rate  Overtime   Overtime Pay    RegHour Pay   Gross Pay')
print('-------------------------------------------------------------------------------')
print(f'{hours}           {pay}      {overtime}          {overtime_pay}               ${reghour_pay}       ${gross_pay}')

print('')

#employee's pay is displayed

name = (input('Enter Employee\'s name or "Done" to terminate: '))
hours = float(input(f"How many hours did {name} work: "))
pay = float(input(f"What is {name}'s pay rate: "))

print('Employee name:   ', name)
print('')
print('Hours worked   Pay Rate  Overtime   Overtime Pay    RegHour Pay   Gross Pay')
print('-------------------------------------------------------------------------------')
print(f'{hours}           {pay}      {overtime}          {overtime_pay}              ${reghour_pay}        ${gross_pay}')


print('')

name = (input('Enter Employee\'s name or "Done" to terminate: '))

#final results are calculated

print('')
print("Total number of employees entered: ", employees)
print(f"Total amount paid for overtime: ",  overtime_pay)
print(f"Total amount paid for regular hours: ", reghour_pay)
print(f"Total amount paid for in gross: ",  total_gross)
