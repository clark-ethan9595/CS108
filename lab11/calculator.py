'''
Provide calculator functionality
Created Fall 2014
Lab11
@author: smn4 and Ethan Clark (elc3)
'''

class Calculator:
    def __init__(self):
        self._memory = 0
        
    def changememory(self, memory):
        self._memory = memory
        
    def getmemory(self):
        return self._memory
   
    #Write appropriate definition of calculate here
    def calculate(self, first_num, type_operation, second_num):
        if first_num == 'M':
            if type_operation == '+':
                return (float(self._memory) + float(second_num))
            elif type_operation == '-':
                return (float(self._memory) - float(second_num))
            elif type_operation == '*':
                return (float(self._memory) * float(second_num))
            elif type_operation == '/':
                return (float(self._memory) / float(second_num))
            raise ValueError("Invalid operation: f")
        elif second_num == 'M':
            if type_operation == '+':
                return (float(first_num) + float(self._memory))
            elif type_operation == '-':
                return (float(first_num) - float(self._memory))
            elif type_operation == '*':
                return (float(first_num) * float(self._memory))
            elif type_operation == '/':
                return (float(first_num) / float(self._memory))
            raise ValueError("Invalid operation: f")
        else:
            if type_operation == '+':
                return (float(first_num) + float(second_num))
            elif type_operation == '-':
                return (float(first_num) - float(second_num))
            elif type_operation == '*':
                return (float(first_num) * float(second_num))
            elif type_operation == '/':
                return (float(first_num) / float(second_num))
            raise ValueError("Invalid operation: f")
        
        
if __name__ == '__main__':
    calc = Calculator()
    
    #Test addition good
    try:
        assert calc.calculate('3', '+', '9') == 12
        assert calc.calculate('-4', '+', '-8') == -12
        assert calc.calculate('-7', '+', '9') == 2
        assert calc.calculate('3', '+', '0') == 3
        assert calc.calculate('2.0', '+', '5.3') == 7.3
    except:
        assert False
        
    #Test subtraction good
    try:
        assert calc.calculate('3', '-', '9') == -6
        assert calc.calculate('-4', '-', '-8') == 4
        assert calc.calculate('-7', '-', '9') == -16
        assert calc.calculate('3', '-', '0') == 3
        assert calc.calculate('2.0', '-', '5.3') == -3.3
    except:
        assert False
        
    #Test division good
    try:
        assert calc.calculate('3', '/', '12') == 0.25
        assert calc.calculate('-4', '/', '-8') == 0.5
        assert calc.calculate('16', '/', '-8') == -2
        assert calc.calculate('0', '/', '3') == 0
        assert calc.calculate('-5.0', '/', '2') == -2.5
    except:
        assert False
        
    #Test multiplication good
    try:
        assert calc.calculate('3', '*', '9') == 27
        assert calc.calculate('-4', '*', '-8') == 32
        assert calc.calculate('-7', '*', '9') == -63
        assert calc.calculate('3', '*', '0') == 0
        assert calc.calculate('2.0', '*', '5.3') == 10.6
    except:
        assert False    
    
    #Test operator throws exception
    try:
        calc.calculate(4,'f','9')
        assert False
    except Exception as e:
        assert isinstance(e, ValueError)
        assert e.__str__() == 'Invalid operation: f'
    
    #Test divide by zero
    try:
        calc.calculate(5, '/', 0)
        assert False
    except Exception as e:
        assert isinstance(e, ZeroDivisionError)
        assert e.__str__() == 'float division by zero'
        
    
    #Test bad operand
    try:
        calc.calculate('hi', '+', '9')
        assert False
    except Exception as e:
        assert isinstance(e, ValueError)
        assert e.__str__() == "could not convert string to float: 'hi'"
    
    #See that all the tests worked
    print('All the tests have been passed!')