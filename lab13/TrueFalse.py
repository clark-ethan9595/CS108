'''TrueFalse class for the quiz.
Created on Dec 4, 2014
Lab 13
@author: Ethan Clark (elc3)
'''

from Problem import Problem

#Class to model a TrueFalse problem.    
class TrueFalse(Problem):
    
    #Constructor to create an instance of the TrueFalse class.
    def __init__(self, q, a):
        if not isinstance(a, bool):
            raise TypeError('The answer must be a boolean value.')
        else:
            super().__init__(q)
            self.answer = a
    
    #Method that formats a TrueFalse problem.    
    def ask_question(self):
        return super().get_question() + '\nIs this statement True or False?'
    
    #Method that checks the answer of the instance.
    def check_answer(self, a):
        return str(self.answer) == a
    
    #Method that returns the answer of the instance.
    def get_answer(self):
        return str(self.answer)

#-----------MAINCODE------------    
if __name__ == "__main__":
    
    #Tests for the TrueFalse class.
    t = TrueFalse('question', False)
    assert t.get_question() == 'question'
    #assert t.get_answer == 'False'
    #assert t.ask_question == 'question' + '\nIs this statement True or False?'
    assert not (t.check_answer('True'))
    assert (t.check_answer('False'))
    
    print('All test have been passed!')