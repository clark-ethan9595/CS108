'''Program to create asteroids for "SpaceShip Adventures."
Created on Dec 2, 2014
Final Project
@author: Ethan Clark (elc3)
'''

#Class to model an asteroid for the "SpaceShip Adventure" game.
class Asteroid:
    
    ''' A class to model an asteroid for the game "SpaceShip Adventure."
        Invariants:
            x must be between 15 and 465.
            y must be -70.
            Velocity must be between 2 and 6.
    '''
    
    #Constructor to create an instance of an asteroid.
    def __init__(self, x, y, random_size, velocity):
        
        #Check to see if the invariants were followed.
        if isinstance(x, int) == False or isinstance(y, int) == False:
            raise ValueError('Please use integer values.')
        
        elif isinstance(random_size, int) == False or isinstance(velocity, int) == False:
            raise ValueError('Please use integer values.')
        
        elif x < 15 or x > 465:
            raise ValueError('Invalid first x coordinate: must be equal to or between 15 and 465.')
        
        elif y != -70:
            raise ValueError('Invalid first y coordinate: must equal -70.')
        
        elif random_size < 10 or random_size > 30:
            raise ValueError('Invalid size integer: must integer between 10 and 30.')
        
        elif velocity < 1 or velocity > 10:
            raise ValueError('Invalid velocity, must be between 2 and 6.')
        
        #Create an instance if the invariants checked out good.
        else:
        
            self.x = x
            self.y = y
            self.random_size = random_size
            self.x1 = x + random_size
            self.y1 = y + random_size
            self.color = 'Gray'
            self.velocity = velocity
    
    #Method to create the asteroid on the canvas.    
    def render_asteroid(self, canvas):
        
        canvas.create_oval(self.x, self.y, self.x1, self.y1, fill = self.color)
    
    #Method to move the asteroid down the canvas.    
    def move_asteroid(self):
        
        self.y = self.y + self.velocity
        self.y1 = self.y1 + self.velocity
    
    #Method (accessor) to return the x coordinate of the asteroid.    
    def get_asteroid_x_value(self):
        
        return self.x
    
    #Method (accessor) to return the y coordinate of the asteroid.    
    def get_asteroid_y_value(self):
        
        return self.y
    
    #Method (accessor) to return the x1 coordinate of the asteroid.
    def get_asteroid_x1_value(self):
        
        return self.x1
    
    #Method (accessor) to return the y1 coordinate of the asteroid.
    def get_asteroid_y1_value(self):
        
        return self.y1
    
#------MAINCODE------
if __name__ == "__main__":
    
    #Test that the accessor methods work properly.
    asteroid_one = Asteroid(100, -70, 10, 5)
    assert asteroid_one.get_asteroid_x_value() == 100
    assert asteroid_one.get_asteroid_y_value() == -70
    assert asteroid_one.get_asteroid_x1_value() == 110
    assert asteroid_one.get_asteroid_y1_value() == -60
    print('The first tests have been passed!')
    
    #Test that the first raise exception works properly.
    try:
        asteroid_testone = Asteroid('hi', -70, 10, 5)
    except ValueError as e:
        print(e)
        
    try:
        asteroid_testtwo = Asteroid(100, -70.6, 10, 5)
    except ValueError as e:
        print(e)
        
    #Test that the second raise exceptoin works properly.
    try:
        asteroid_testthree = Asteroid(100, -70, 'hi', 5)
    except ValueError as e:
        print(e)
        
    try:
        asteroid_testfour = Asteroid(100, -70, 10, 4.99)
    except ValueError as e:
        print(e)
    
    #Test that the third raise exception works properly.
    try:
        asteroid_two = Asteroid(0, -70, 10, 5)
    except ValueError as e:
        print(e)
    
    #Test that the fourth raise exception works properly.    
    try:
        asteroid_three = Asteroid(60, -100, 15, 5)
    except ValueError as e:
        print(e)
    
    #Test that the fifth raise exception works properly.    
    try:
        asteroid_four = Asteroid(60, -70, 20, 15)
    except ValueError as e:
        print(e)
    
    #Test that the sixth raise exception works properly.    
    try:
        asteroid_five = Asteroid(60, -70, 45, 4)
    except ValueError as e:
        print(e)