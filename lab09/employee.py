''' A program to practice classes, files, and modules dealing with employee information.
October 30, 2014
Lab 09
@author Ethan Clark (elc3)
'''

import sys

class Employee:
    '''
    Models an employee with his or her information.
    Invariants:
        Salary must be greater than $20000.
    '''
    
    def __init__(self, line = ''):
        if line == '':
            self._first = 'E'
            self._last = 'Clark'
            self._rank = 'CEO'
            self._salary = 100000
        else:
            strings = line.split(' ')
            first_name = strings[0]
            self._first = first_name[0]
            self._last = strings[1]
            self._rank = strings[2]
            if float(strings[3]) < 20000:
                print('Invalid salary!', file=sys.stderr)
                sys.exit(-1)
            else:
                self._salary = float(strings[3])
            
    def get_rank(self):
        return self._rank
    
    def get_salary(self):
        return self._salary
            
    def __str__(self):
        return self._last + ', ' + self._first + '.: ' + self._rank + ' ($' + str(self._salary) + ')'



#------------MAIN CODE--------------
if __name__ == '__main__':

    employee_one = Employee()
    print(employee_one)
    print(employee_one.get_rank())
    print(employee_one.get_salary())
    
    employee_two = Employee('Jaymes Gontjes Janitor 50000')
    print(employee_two)