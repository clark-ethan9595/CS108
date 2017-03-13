'''Fill in the Blank problem for the quiz.
Created on Dec 4, 2014
Lab 13
@author: Ethan Clark (elc3)
'''

from Problem import Problem

#Class to model a FillInTheBlank problem.
class FillInTheBlank(Problem):
    
    #Constructor that creates an instance of the FillInTheBlank class.
    def __init__(self, q, a):
        super().__init__(q)
        self.answer = a
    
    #Method that returns a formatted FillInTheBlank question.          
    def ask_question(self):
        return super().get_question() + '\nFill in the blank.'
    
    #Method that checks the answer to the instance.
    def check_answer(self, a):
        return self.answer == a
    
    #Method that returns the answer of the current instance.
    def get_answer(self):
        return self.answer

#------------MAINCODE-------------    
if __name__ == '__main__':
    
    #Tests for the FillInTheBlank class.
    f = FillInTheBlank('question', 'answer')
    assert f.get_question() == 'question'
    assert f.get_answer() == 'answer'
    assert f.ask_question() == 'question' + '\nFill in the blank.'
    assert not (f.check_answer('ans'))
    assert f.check_answer('answer')
    
    print('All test have been passed!')