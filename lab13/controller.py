'''User Interface to take a quiz.
Created Fall 2014 (December 4, 2014)
Lab 13
@author: Serita Nelesen (smn4) and Ethan Clark (elc3)
'''

#Import tkinter and the quiz class.
from tkinter import *
from quiz import Quiz

#Class for the user interface for the quiz.
class Controller:
    
    #Constructor to create the window and its features.
    def __init__(self):
        
        #Create a window and give it a title.
        self.window = Tk()
        self.window.title('Simple Quiz')
        
        #Create an instance of the quiz class.
        self.quiz = Quiz()
        
        #Labels for the question to appear on the screen.
        self.question_text = Text(self.window, font="arial 16", width = 40, height = 4, wrap = WORD)
        self.question_text.insert(1.0, self.quiz.ask_current_question())
        self.question_text.pack()
        
        #Variable and entry for the user to put in his or her answer.
        self.answer = StringVar()
        self.answerEntry = Entry (self.window, textvariable = self.answer)
        self.answerEntry.pack(side = LEFT)
        
        #Bind the return key to enter the answer in the entry.
        self.answerEntry.focus_set()
        self.answerEntry.bind("<Return>", self.check_answer)
        
        #Label for the instructions for the quiz.
        self.instructions = StringVar()
        self.instructions.set('\u21D0 Enter your answer here')
        self.instrLabel = Label(self.window, textvariable = self.instructions)
        self.instrLabel.pack(side = LEFT)
        
        #Main loop to loop through the initialization method.
        self.window.mainloop()
    
    #Method that checks if the user was correct or incorrect.    
    def check_answer(self, event):
        if self.quiz.check_current_answer(self.answer.get()):
            #Got it right!!
            self.instructions.set("Good job!  Next question ...")
        else:
            self.instructions.set("Sorry, the answer was " + self.quiz.get_current_answer()) 
        self.answer.set('')
        
        #Go to the next question if it exists
        self.question_text.delete(1.0, END)  
        if (self.quiz.has_next()):
            self.quiz.next()
            self.question_text.insert(1.0, self.quiz.ask_current_question())
        else:  
            self.question_text.insert(1.0, 'Sorry, there are no more questions.')
            self.answerEntry.configure(state='disabled')

#Create an instance of the controller class.   
Controller()