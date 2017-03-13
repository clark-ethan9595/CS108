'''
Driver to run the calculator interface for the user.
Created on Nov 13, 2014
Lab 11
@author: Ethan Clark (elc3)
'''

from tkinter import *
from calculator import *

class Driver:
    def __init__(self):
        window = Tk()
        window.title('Calculator Operations')
        
        Label(window, text = "Input 1:").grid(row = 1, sticky = E)
        
        self.operand1 = StringVar()
        operand1Entry = Entry(window, width = 6, textvariable = self.operand1)
        operand1Entry.grid(row = 1, column = 1, sticky = W)
        
        Label(window, text = "Input 2:").grid(row=2, sticky = E)
        
        self.operand2 = StringVar()
        operand2Entry = Entry(window, width = 6, textvariable = self.operand2)
        operand2Entry.grid(row = 2, column = 1, sticky = W)
        
        frame = Frame(window)
        frame.grid(row = 3, columnspan = 2)
        self.operation = StringVar()
        self.operation.set('+')
        
        add_rb = Radiobutton(frame, text="+", variable = self.operation, value = '+')
        add_rb.pack(side = LEFT)
        
        sub_rb = Radiobutton(frame, text='-', variable = self.operation, value = '-')
        sub_rb.pack(side = LEFT)
        
        mult_rb = Radiobutton(frame, text='*', variable = self.operation, value = '*')
        mult_rb.pack(side = LEFT)
        
        div_rb = Radiobutton(frame, text='/', variable = self.operation, value = '/')
        div_rb.pack(side = LEFT)
        
        Label(window, text = 'Operator:').grid(row = 3, column = 2)
        
        opLabel = Label(window, textvariable = self.operation, width = 3)
        opLabel.grid(row = 3, column = 3)
        
        Button(window, text = "Calculate", command = self.doCalculation).grid(row = 4)
        
        Label(window, text = 'Result').grid(row = 4, column = 1)
        
        self.result_text = StringVar()
        Label(window, textvariable = self.result_text).grid(row = 4, column = 2)
        
        self.calc = Calculator()
        
        self.error_label = Label(window, text = "Let's do some calculations!")
        self.error_label.grid(row = 6)
        
        Label(window, text = 'Memory Value').grid(row = 5)
        Button(window, text = 'Add to memory', 
               command = self.changeCalcMemory).grid(row = 5, column = 1)
        self.memory_label = Label(window, text = 'There is nothing in memory').grid(row = 5, column = 2)
        
        window.mainloop()
        
    def doCalculation(self):
        try:
            result = self.calc.calculate(self.operand1.get(), self.operation.get(), 
                                         self.operand2.get())
            self.result_text.set(result)
        except ValueError as e:
            self.error_label['text'] = "Please try again with numbers."
        except ZeroDivisionError as e:
            self.error_label['text'] = "I'm sorry; you cannot divide by zero."
            
    def changeCalcMemory(self):
        memory = self.result_text
        self.memory_label['text'] = memory
            
Driver()