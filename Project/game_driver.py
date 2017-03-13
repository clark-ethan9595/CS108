'''CS108 Final Project: SpaceShip Adventures Game.
Created on Nov 24, 2014
Final Project
@author: Ethan Clark (elc3)
'''

#Import the user graphical interface program for Python.
from tkinter import *

#Import the main spaceship class.
from mainspaceship import *

#Import the enemy spaceship class.
from spaceships import *

#Import the user laser beam class.
from laser_beam import *

#Import the asteroid class.
from asteroids import *

#Import the enemy laser beam class.
from enemy_laser import *

#Import the instructions window class.
from instructions_interface import *

#Import the random module to get random integers when creating the enemy ships.
from random import randint

#Create a class to set up and run the SpaceShip game.
class SpaceShip_Adventure:
    
    #Constructor for the SpaceShip_Adventure class.
    def __init__(self):
        
        #Create a window and set the title of the window.
        self.window = Tk()
        self.window.title('SpaceShip Adventure')
        self.window.protocol('WM_DELETE_WINDOW', self.cleanexit)
        
        #Create a canvas that the spaceships will appear on.
        self.width = 500
        self.canvas = Canvas(self.window, bg = 'black', width = self.width, height = self.width)
        self.canvas.pack()
        
        #Bind the left and right arrows along with the space bar to the canvas.
        self.canvas.bind('<Left>', self.processLeft)
        self.canvas.bind('<Right>', self.processRight)
        self.canvas.bind('<space>', self.processSpaceBar)
        
        #Bind the return, p, s, and r keys to the canvas.
        self.canvas.bind('<Return>', self.processReturn)
        self.canvas.bind('<p>', self.processP)
        self.canvas.bind('<s>', self.processS)
        self.canvas.bind('<r>', self.processR)
        
        #Focus set for the binded keys.
        self.canvas.focus_set()
        
        #Create a button frame to go below the canvas for the welcome phrase and the buttons.
        button_frame = Frame(self.window)
        button_frame.pack()
        
        #Create a welcoming phrase below the canvas and above the buttons.
        title_label = Label(button_frame, text = "Welcome to SpaceShip Adventures!")
        title_label['fg'] = 'Red'
        title_label.grid(row = 0, column = 1, pady = 5)
        
        #Button to start the game.
        start_button = Button(button_frame, text = 'Start', width = 10,
                              command = self.startgame)
        start_button.grid(row = 1)
        
        #Button to stop the game.
        pause_button = Button(button_frame, text = 'Pause', width = 10,
                              command = self.pausegame)
        pause_button.grid(row = 1, column = 1)
        
        #Button to resume the game.
        resume_button = Button(button_frame, text = 'Resume', width = 10,
                               command = self.resumegame)
        resume_button.grid(row = 1, column = 2)
        
        #Button to restart the game.
        restart_button = Button(button_frame, text = 'Restart', width = 10,
                                command = self.restartgame)
        restart_button.grid(row = 2)
        
        #Button to pull up an instructions window.
        instructions_button = Button(button_frame, text = "Instructions", width = 10,
                                     command = self.instructionsWindow)
        instructions_button.grid(row = 2, column = 2)
        
        #Create a frame for the score labels with their string variables.
        score_frame = Frame(self.window)
        score_frame.pack()
        
        #Labels to indicate the users current score.
        score_label = Label(score_frame, text = 'Current Score:')
        score_label['fg'] = 'Red'
        score_label.grid(row = 0, column = 0)
        
        self.score_var = StringVar()
        current_score_label = Label(score_frame, textvariable = self.score_var)
        current_score_label['fg'] = 'Red'
        current_score_label.grid(row = 0, column = 2)
        
        #Labels to indicate the users high score since they started playing.
        high_score_label = Label(score_frame, text = 'High Score:')
        high_score_label['fg'] = 'Red'
        high_score_label.grid(row = 0, column = 4)
        
        self.high_score_var = StringVar()
        high_label = Label(score_frame, textvariable = self.high_score_var)
        high_label['fg'] = 'Red'
        high_label.grid(row = 0, column = 6)
        
        #Frame for the level label and variable.
        level_frame = Frame(self.window)
        level_frame.pack()
        
        #Labels to indicate the level of the game at hand.
        self.current_level_var = StringVar()
        self.current_level_label = Label(level_frame, textvariable = self.current_level_var)
        self.current_level_label['fg'] = 'Red'
        self.current_level_label.grid(row = 0, column = 0, padx = 10)
        
        #Labels to indicate the status of the game at hand.
        self.current_status_var = StringVar()
        self.current_status_label = Label(level_frame, textvariable = self.current_status_var)
        self.current_status_label['fg'] = 'Red'
        self.current_status_label.grid(row = 0, column = 3)
        
        #Frame for the reason lost variable.
        final_frame = Frame(self.window)
        final_frame.pack()
        
        #Labels to indicate how the user lost the game.
        self.reason_lost_var = StringVar()
        self.reason_lost_label = Label(final_frame, textvariable = self.reason_lost_var)
        self.reason_lost_label['fg'] = 'Red'
        self.reason_lost_label.grid(row = 0)
        
        #Variable to use for the animation loop.
        self.terminate = True
        
        #Call the animation function to do the animating on the canvas.
        self.animate()
        
        #Main loop to loop through the class.
        self.window.mainloop()
        
    #Method to start the game.        
    def startgame(self):
                
        #Variable to determine when to send the enemy ships down.
        self.enemyship_tracker = 0
        
        #Variable to determine when to send the asteroids down.
        self.asteroid_tracker = 0
        
        #Variable to track the score of the current game.
        self.score_counter = 0
        
        #Variable to determine how fast the ships and asteroids fall down.
        self.level_tracker = 0
        
        #Set the current game score to 0.
        self.score_var.set(0)
        
        #Set the reason lost string variable to an empty string.
        self.reason_lost_var.set('')
        
        #Set the high score to the highest score recorded in the high_score text file.
        with open('high_score.txt', 'r') as f:
            self.high_list = f.readlines()
            self.length_list = len(self.high_list)
            self.high_score_from_file = self.high_list[self.length_list - 1]
            self.high_score_var.set(self.high_score_from_file)
        
        #Create an instance of the main spaceship class.
        self.game_spaceship = Main_SpaceShip(250, 465)
        
        #Create four empty lists for the enemy ships, the enemy lasers, the main ship lasers, and the asteroids.
        self.enemy_list = []
        self.friendly_laser_list = []
        self.asteroid_list = []
        self.enemy_laser_list = []
        
        #Set the terminate variable to False so the animation loop runs.
        self.terminate = False
        
        #Call the animation function.
        self.animate()
    
    #Method for the user to pause the game.    
    def pausegame(self):
        
        #Set the terminate variable to True to stop the animation loop.
        self.terminate = True
    
    #Method for the user to resume the game after it has been paused.    
    def resumegame(self):
        
        #Set the terminate variable to False so the animation loop runs again.
        self.terminate = False
        
        #Call the animation function.
        self.animate()
        
    def restartgame(self):
        
        #Delete everything on the current canvas.
        self.canvas.delete(ALL)
                
        #Create an instance of the main spaceship class.
        self.game_spaceship = Main_SpaceShip(250, 465)
        
        #Reset the score to 0.
        self.score_var.set(0)
        
        #Reset the reason lost and current status string variable to an empty string.
        self.reason_lost_var.set('')
        self.current_status_var.set('')
        
        #Set the high score to the highest score recorded in the high_score text file.
        with open('high_score.txt', 'r') as f:
            self.high_list = f.readlines()
            self.length_list = len(self.high_list)
            self.high_score_from_file = self.high_list[self.length_list - 1]
            self.high_score_var.set(self.high_score_from_file)
        
        #Create four empty lists for the enemy ships, the enemy lasers, the main ship lasers, and asteroids.
        self.enemy_list = []
        self.friendly_laser_list = []
        self.asteroid_list = []
        self.enemy_laser_list = []
              
        #Variable to determine when to send the enemy ships down.
        self.enemyship_tracker = 0
        
        #Variable to determine when to send the asteroids down.
        self.asteroid_tracker = 0
        
        #Variable to track the score of the current game.
        self.score_counter = 0
        
        #Variable to determine how fast the ships and asteroids fall down.
        self.level_tracker = 0
        
        #Set the terminate variable to False so the animation loop runs.
        self.terminate = False
        
        #Call the animation function.
        self.animate()
                
    #Method to stop the game once the enemy ships enter friendly territory.    
    def stopgame(self):
        
        #Set the current status variable label to say "GAME OVER!".
        self.current_status_var.set("GAME OVER!")
        
        #Set the terminate variable to True to stop the animation loop.
        self.terminate = True
    
    #Method that gets called when the left arrow is clicked.    
    def processLeft(self, event):
        
        #Call the main spaceship method of moving the ship to the left.
        self.game_spaceship.moveLeft()
    
    #Method that gets called when the right arrow is clicked.    
    def processRight(self, event):
        
        #Call the main spaceship method of moving the ship to the right.
        self.game_spaceship.moveRight()
    
    #Method that gets called when the space bar is clicked.    
    def processSpaceBar(self, event):
        
        #Create an instance of a laser beam and add it to the list of laser beams.
        x1 = self.game_spaceship.get_x1_point()
        self.laser_beam = LaserBeam(x1)
        self.friendly_laser_list.append(self.laser_beam)
    
    #Method that gets called when the Return key is clicked.    
    def processReturn(self, event):
        
        #Call the restart game method.
        self.restartgame()
    
    #Method that gets called when the P key is clicked.    
    def processP(self, event):
        
        #Call the pause game method.
        self.pausegame()
    
    #Method that gets called when the S key is clicked.    
    def processS(self, event):
        
        #Call the start game method.
        self.startgame()
    
    #Method that gets called when the R key is clicked.    
    def processR(self, event):
        
        #Call the resume game method.
        self.resumegame()
      
    #Method to pull up the instructions window for the user.
    def instructionsWindow(self):
        
        #Create an instance of the InstructionsWindow class.
        InstructionsWindow()
              
    #Method for the game class to do the animating on the canvas.    
    def animate(self):
        
        #Animation Loop.    
        while not self.terminate:
            
            #Delete everything on the canvas and render the main ship on the screen.    
            self.canvas.delete(ALL)
            self.game_spaceship.render_mainship(self.canvas)
            
            #Loop through the enemy ship list and move accordingly.    
            for c in self.enemy_list:
                
                #If an enemy is below 480 pixels (y-coordinate), end the game.
                if c.get_y1_value_enemy() >= 480:
                    self.reason_lost_var.set("Don't let the enemy ships reach the bottom!")
                    self.stopgame()
                    
                #Move and render the enemy ships if it is not at the bottom of the canvas yet.
                c.move_enemyships(self.canvas)
                c.render_enemyships(self.canvas)
                
                #Determine if the enemy is going to shoot their laser beams or not.
                if c.enemy_laser_shot(self.level_tracker) == True:
                    x1 = c.get_x1_value_enemy()
                    y1 = c.get_y1_value_enemy()
                    enemy_laser = Enemy_LaserBeam(x1, y1)
                    self.enemy_laser_list.append(enemy_laser)
                    
            #Loop through the laser list and move the laser shots accordingly.                                
            for c in self.friendly_laser_list:
                c.move_laser_beam(self.canvas)
                c.render_laser_beam(self.canvas)

            #Loop through the enemy laser beam list and move accordingly.
            for c in self.enemy_laser_list:
                
                #Remove the laser beam if it goes past the bottom of the canvas.
                if c.get_enemy_beam_y1() >= 510:
                    self.enemy_laser_list.remove(c)
                
                #Move the lasers if they are not at the bottom of the screen.
                else:
                    c.move_enemy_beam()
                    c.render_enemy_beam(self.canvas)
            
            #Loop through the asteroid list and move accordingly.    
            for c in self.asteroid_list:
                
                #Remove the asteroid from the list once it goes past the bottom of the canvas.
                if c.get_asteroid_y_value() >= 500:
                    self.asteroid_list.remove(c)
                
                #Else move the asteroid down the canvas.
                else:
                    c.move_asteroid()
                    c.render_asteroid(self.canvas)
                        
            #Loop through the enemy laser list and see if it hits the main spaceship.
            for c in self.enemy_laser_list:
                
                enemy_beam_x1 = c.get_enemy_beam_x1()
                enemy_beam_y1 = c.get_enemy_beam_y1()
                
                #If an enemy laser hits the main spaceship, end the game.
                if self.game_spaceship.enemy_laser_collision(enemy_beam_x1, enemy_beam_y1) == True:
                    self.reason_lost_var.set("Don't get hit by the enemy laser beams!")
                    self.stopgame()

            #Loop through the laser list and the enemy ships list and determine if a collision occurs.    
            for a in self.friendly_laser_list:
                
                laser_y1_val = a.get_laser_beam_y1()
                laser_x1_val = a.get_laser_beam_x1()
                
                for c in self.enemy_list:
                    
                    if c.laser_collision(laser_y1_val, laser_x1_val) == True:
                        
                        #If a laser collides with an enemy ship, increase score by 100 and remove both
                        #the enemy ship and the laser.
                        self.score_counter += 100
                        self.score_var.set(self.score_counter)
                        self.enemy_list.remove(c)
                        self.friendly_laser_list.remove(a)
                        
            #Loop through the asteroid list and see if any asteroid hits the main spaceship.            
            for c in self.asteroid_list:
                
                asteroid_x_val = c.get_asteroid_x_value()
                asteroid_y_val = c.get_asteroid_y_value()
                asteroid_x1_val = c.get_asteroid_x1_value()
                asteroid_y1_val = c.get_asteroid_y1_value()
                
                #If an asteroid collides with the main ship, end the game.
                if self.game_spaceship.asteroid_collision(asteroid_x_val, asteroid_y_val,
                                                          asteroid_x1_val, asteroid_y1_val) == True:
                    self.reason_lost_var.set("Don't get hit by asteroids!")
                    self.stopgame()
            
            #Increase the tracker variables by one.    
            self.enemyship_tracker += 1
            self.asteroid_tracker += 1
            self.level_tracker += 1
            
            #Checks on the self.level_tracker to determine how fast the enemy ships fall down and what level.
            if 0 <= self.level_tracker <= 3000:
                self.launch_tracker = 180
                self.asteroid_launcher = 160
                self.current_level_var.set('LEVEL ONE')
            elif 3000 < self.level_tracker <= 6000:
                self.launch_tracker = 160
                self.asteroid_launcher = 140
                self.current_level_var.set('LEVEL TWO')
            elif 6000 < self.level_tracker <= 9000:
                self.launch_tracker = 140
                self.asteroid_launcher = 120
                self.current_level_var.set('LEVEL THREE')
            elif 9000 < self.level_tracker <= 12000:
                self.launch_tracker = 120
                self.asteroid_launcher = 100
                self.current_level_var.set('LEVEL FOUR')
            elif 12000 < self.level_tracker <= 15000:
                self.launch_tracker = 100
                self.asteroid_launcher = 80
                self.current_level_var.set('LEVEL FIVE')
            elif self.level_tracker > 15000:
                self.launch_tracker = 80
                self.asteroid_launcher = 60
                self.current_level_var.set('LEVEL SIX')
            
            #If the tracker numbers are equal, create an enemy ship and add it to the list.    
            if self.enemyship_tracker == self.launch_tracker:
                x1 = randint(20, 480)
                y1 = -40
                self.enemy_one = Enemy_SpaceShips(x1, y1)
                self.enemy_list.append(self.enemy_one)
                self.enemyship_tracker = 0
            
            #If the tracker numbers are equal, create an asteroid and add it to the list.    
            if self.asteroid_tracker == self.asteroid_launcher:
                x = randint(15, 465)
                y = - 70
                velocity = randint(2, 6)
                size = randint(10, 30)
                self.asteroid_one = Asteroid(x, y, size, velocity)
                self.asteroid_list.append(self.asteroid_one)
                self.asteroid_tracker = 0
                
            #Check to see if the user now has a new high score.
            if self.score_counter > int(self.high_score_var.get()):
                self.high_score_var.set(self.score_counter)
            
            #Open the high_score text file as a read and write option.    
            with open('high_score.txt', 'r+') as f:
                
                #List of the scores in the text file.
                self.high_score_list = f.readlines()
                
                #Length of the high_score_list or the number of lines in the high_score text file.
                self.length = len(self.high_score_list)
                
                #If the current score is bigger than the high score in the file, write the new score to the file.
                if self.score_counter > int(self.high_score_list[self.length - 1]):
                    f.write('\n')
                    f.write(str(self.score_counter))
            
            #Pause the canvas briefly and update based on the new animations that just took place.        
            self.canvas.after(10)
            self.canvas.update()
                
    #Method to end the animation loop when the window is closed.
    def cleanexit(self):
        self.window.destroy()
        self.terminate = True
        
#Create an instance of the SpaceShip Adventure class.        
SpaceShip_Adventure()