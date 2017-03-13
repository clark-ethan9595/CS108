'''Program to generate quiz questions.
Created Fall 2014 (December 4, 2014)
Lab 13
@author: Serita Nelesen (smn4) and Ethan Clark (elc3)
'''

#Import all the needed classes for the quiz.
from shortAnswer import *
from TrueFalse import TrueFalse
from FillInTheBlank import FillInTheBlank
import random

#Class to model a quiz.
class Quiz:
    
    #Constructor to create an instance of the quiz.
    def __init__(self):
        
        #Create an empty list and add the questions and answers to the list.
        self.problems = []
        self.problems.append(ShortAnswer('Where were the olympics held in 1956', 'Melbourne'))
        self.problems.append(ShortAnswer('What is the hottest recorded temperature in the United States', '134'))
        self.problems.append(ShortAnswer('What baseball team plays in Miami', 'Marlins'))
        self.problems.append(FillInTheBlank('The physics term ________ means the bending of light.', 
                                            'Refraction'))
        self.problems.append(TrueFalse('Serbia is a country in Africa.', False))
        random.shuffle(self.problems)
        
        self.problemNum = 0
    
    #Method to return the current question in the list.    
    def ask_current_question(self):
        return self.problems[self.problemNum].ask_question()
    
    #Method to return the current answer to the question in the list.
    def get_current_answer(self):
        return self.problems[self.problemNum].get_answer()
    
    #Method to return if the answer was correct or incorrect.
    def check_current_answer(self, answer):
        return self.problems[self.problemNum].check_answer(answer)
    
    #Method to see if there is another question and answer in the list.
    def has_next(self):
        return self.problemNum < len(self.problems) - 1
    
    #Method to occur when there are no more questions and answers in the list.
    def next(self):
        if self.problemNum == len(self.problems) - 1:
            raise Exception("There are no more problems")
        self.problemNum += 1
        