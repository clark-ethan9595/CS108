'''The parent Problem class to create a general question.
Created on Dec 4, 2014
Lab 13
@author: Ethan Clark (elc3)
'''

#Main parent class to receive and return the question.
class Problem:
    
    #Constructor to create an instance of the Problem class.
    def __init__(self, question):
        self.question = question
     
    #Method that returns the question of the current class.    
    def get_question(self):
        return self.question