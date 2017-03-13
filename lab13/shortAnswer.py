''' Models a short answer problem
Created Fall 2014
Lab 13
@author: Serita Nelesen (smn4) and Ethan Clark (elc3)
'''

from Problem import Problem

#Class to model a ShortAnswer problem.  
class ShortAnswer(Problem):
    
    #Constructor to create an instance of the ShortAnswer class.
    def __init__(self, q, a):
        super().__init__(q)
        self.answer = a
    
    #Method to return a formatted question for short answer.          
    def ask_question(self):
        return super().get_question()+'?'
    
    #Method to check the answer of the instance.
    def check_answer(self, a):
        return self.answer == a
    
    #Method that returns the answer of the instance.
    def get_answer(self):
        return self.answer

#--------------MAINCODE------------------    
if __name__ == "__main__":
    
    #Tests for the short answer class.
    q = ShortAnswer('question', 'answer')
    assert q.get_question() == 'question'
    assert q.get_answer() == 'answer'
    assert q.ask_question() == 'question?'
    assert not (q.check_answer('ans'))
    assert q.check_answer('answer')
    
    print('All ShortAnswer tests passed!')