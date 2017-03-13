'''Window that opens to explain instructions to user for the game "SpaceShip Adventures."
Created on Dec 8, 2014
Final Project
@author: Ethan Clark (elc3)
'''

#Import tkinter to build a user interface.
from tkinter import *

#Class to pull up a window for the instructions to the game SpaceShip Adventures.
class InstructionsWindow:
    
    #Constructor for the InstructionsWindow class to make an instance.
    def __init__(self):
        
        #Create a window and give it a title.
        self.window = Tk()
        self.window.title('Instructions')
        
        #Create a frame for the window.
        main_frame = Frame(self.window)
        main_frame.pack()
        
        #Labels for all the instructions, objectives, and keyboard shortcuts.
        label1 = Label(main_frame, text = 'Instructions for SpaceShip Adventures')
        label1.config(font = 'Times 20 bold')
        label1.pack()
        
        label2 = Label(main_frame, text = 'Objectives of the Game:')
        label2.config(font = 'Times 18 bold')
        label2.pack()
        
        label3 = Label(main_frame, text = "1. Don't let the enemy ships reach the bottom by shooting them.")
        label3.pack()
        
        label4 = Label(main_frame, text = "2. Don't get hit by the asteroids.")
        label4.pack()
        
        label5 = Label(main_frame, text = "3. Don't get hit by the enemy spaceship laser beams.")
        label5.pack()
        
        label6 = Label(main_frame, text = 'How to Play SpaceShip Adventures:')
        label6.config(font = 'Times 18 bold')
        label6.pack()
        
        label7 = Label(main_frame, text = "1. Move your space ship by using the left and right keyboard arrows.")
        label7.pack()
        
        label8 = Label(main_frame, text = "2. Use the space bar to shoot laser beams.")
        label8.pack()
        
        label9 = Label(main_frame, text = "KeyBoard Shortcuts:")
        label9.config(font = 'Times 18 bold')
        label9.pack()
        
        label10 = Label(main_frame, text = "1. Press 'P' to pause the game.")
        label10.pack()
        
        label11 = Label(main_frame, text = "2. Press 'R' to resume the game.")
        label11.pack()
        
        label12 = Label(main_frame ,text = "3. Press 'S' to start the game.")
        label12.pack()
        
        label13 = Label(main_frame, text = "4. Press 'RETURN' to restart the game.")
        label13.pack()
        
        #Call the main loop method to loop through the class's constructor class.
        self.window.mainloop()

#--------MAINCODE--------        
if __name__ == '__main__':
    
    #Call an instance of InstructionsWindow class.
    InstructionsWindow()