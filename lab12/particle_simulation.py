'''
GUI controller for a particle simulation
Created Fall 2014
Lab 12
@author: Serita Nelesen (smn4) and Ethan Clark (elc3)
'''

#Import the necessary files for this program.
from tkinter import *
from random import randint
from particle import *
from helpers import *

#Create a class to model particle movement.
class ParticleSimulation:
    
    #Constructor for the particle simulation class.
    def __init__(self):
        '''
        Constructor that sets the window and the instance variables
        making a user interface to run the particle simulation.
        '''
        
        #Create a window and set the window title and the window exiting protocol.
        self.window = Tk()
        self.window.title("Particle Simulation")
        self.window.protocol('WM_DELETE_WINDOW', self.exitClean)
        
        #Create a canvas for the particles to go on.
        self.width = 400
        self.canvas = Canvas(self.window, bg='black',
                        width = self.width, height = self.width)
        self.canvas.pack()
        
        #Create a button for the user to add particles to the simulation.
        add_particle_bt = Button(self.window, text = 'Add particle', 
                                 command = self.addParticle)
        add_particle_bt.pack()
        
        #Set the terminate option to the Boolean value of false.
        self.terminate = False
        
        #Create an empty list that the particles will be added to.
        self.p_list = []
        
        #Bind the mouse click to remove a particle from the simulation.
        self.canvas.bind('<Button-1>', self.checkRemoveParticle)
        
        #Call the animate method to do the animation of creating a particle.
        self.animate()
        
        #Loop for the window to stay on the screen.
        self.window.mainloop()
    
    #Method in the particle class to create a particle in the simulator.
    def animate(self):
        '''
        An animation method to put the particle on the canvas and move and render
        the other particles accordingly.
        '''
        
        while not self.terminate:
            self.canvas.delete(ALL)
            for c in self.p_list:
                c.move(self.canvas)
                c.render(self.canvas)
                for i in self.p_list:
                    c.bounce(i)
            self.canvas.after(50)
            self.canvas.update()
    
    #Method to run when the button is clicked to add another particle.
    def addParticle(self):
        '''
        Method that creates a random particle when the user clicks the button.
        '''
        
        #Get a random integer between 0 and 400 for where the particle starts.
        x_var = randint(0, 400)
        y_var = randint(0, 400)
        
        #Get a random integer between -25 and 25 to set the particle's speed.
        x_vel_var = randint(-25, 25)
        y_vel_var = randint(-25, 25)
        
        #Set the new particle's radius to be 15 pixels.
        radius = 15
        
        #Get a random color for the particle by calling the two color functions at the top of the program.
        new_color = getRandomColor()
        
        #Create the particle by calling the particle class and append it to the particle list.
        self.particle_one = Particle(x_var, y_var, x_vel_var, y_vel_var, radius, new_color)
        self.p_list.append(self.particle_one)
    
    #Method to see if the user clicks a particle to remove it.    
    def checkRemoveParticle(self, event):
        '''
        Method to check if the user clicked on the particle in attempt
        to remove the particle from the simulation.
        '''
        
        copy = self.p_list[:]
        for c in copy:
            if (((event.y - c.get_y())**2) + ((event.x - c.get_x())**2))**(1/2) < c.get_radius():
                self.p_list.remove(c)
    
    #Method to end the animation loop once the window is closed.        
    def exitClean(self):
        '''
        Method to cleanly exit the program by ending the animation loop when
        the window is closed.
        '''
        
        self.terminate = True
        self.window.destroy()

#Create an instance of our Particle Simulation Class.        
ParticleSimulation()