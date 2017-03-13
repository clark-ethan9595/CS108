''' The driver program to analyze the employee data file.
October 29, 2014
Lab 09
@author Ethan Clark (elc3)
'''

import employee

employees = []

def print_averages(totals, counts, out_file):
    out_file.write('Rank\tAverage Salary\n')
    for rank in totals:
        out_file.write(rank + '\t' + str(totals[rank] / counts[rank]) + '\n')

#Open the Employee Information File and add the employees to our list.
with open('Salary.txt', 'r') as f:
    for line in f:
        employees.append(line)
    for i in range(len(employees)):
        employees[i] = employees[i].replace('\n', '')
        employees[i] = employee.Employee(employees[i])

#Test to see if the list is the same length as the employee file.
print(len(employees))
print(employees[0])

#Get the needed information from the list of employees.
if len(employees) < 1:
    print('Invalid number of employees!')
else:
    totals = {}
    counts = {}
    max_employee = employees[0]
    min_employee = employees[0]
    for i in employees:
        if i.get_rank() in totals:
            totals[i.get_rank()] = totals[i.get_rank()] + i.get_salary()
            counts[i.get_rank()] += 1
        else:
            totals[i.get_rank()] = i.get_salary()
            counts[i.get_rank()] = 1
        if i.get_salary() > max_employee.get_salary():
            max_employee = i
        if i.get_salary() < min_employee.get_salary():
            min_employee = i
        
print(totals)
print(counts)

with open('employee_stats.txt', 'w') as e:
    e.write('The employee with the largest salary is: ' + str(max_employee) + '\n')
    e.write('The employee with the smallest salary is: ' + str(min_employee) + '\n')
    print_averages(totals, counts, e)