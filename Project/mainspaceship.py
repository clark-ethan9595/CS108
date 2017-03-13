'''Program to create a main spaceship for "SpaceShip Adventures."
Created on Nov 24, 2014
Final Project
@author: Ethan Clark (elc3)
'''

#Create a class to model a space ship.
class Main_SpaceShip:
    
    ''' Class to model the main spaceship for the game "SpaceShip Adventures"
        Invariants:
            The first x coordinate equals 250.
            The first y coordinate equals 465.
    '''
    
    #Constructor to create an instance of the main spaceship class.
    def __init__(self, x1, y1):
        
        #Checks to see if the invariants are followed.
        if isinstance(x1, int) == False or isinstance(y1, int) == False:
            raise ValueError('Please use integer values.')
        
        elif x1 != 250:
            raise ValueError('Invalid x coordinate for first ship point: must be 250.')
        
        elif y1 != 465:
            raise ValueError('Invalid y coordinate for first ship point: must be 465.')
        
        #Create an instance if the invariants checked out good.
        else:
            
            self.x1 = x1
            self.y1 = y1
            self.x2 = x1 + 7
            self.y2 = y1 + 20
            self.x3 = x1 + 12
            self.y3 = y1 + 20
            self.x4 = x1 + 13
            self.y4 = y1 + 10
            self.x5 = x1 + 14
            self.y5 = y1 + 20
            self.x6 = x1 + 14
            self.y6 = y1 + 30
            self.x7 = x1 - 14
            self.y7 = y1 + 30
            self.x8 = x1 - 14
            self.y8 = y1 + 20
            self.x9 = x1 - 13
            self.y9 = y1 + 10
            self.x10 = x1 - 12
            self.y10 = y1 + 20
            self.x11 = x1 - 7
            self.y11 = y1 + 20
            
            self.color = "Blue"
        
            self.velocity = 10
    
    #Method for the main ship class to put the ship on the canvas.    
    def render_mainship(self, canvas):
        
        canvas.create_polygon(self.x1, self.y1, self.x2, self.y2, self.x3, self.y3, self.x4, self.y4,
                              self.x5, self.y5, self.x6, self.y6, self.x7, self.y7, self.x8, self.y8,
                              self.x9, self.y9, self.x10, self.y10, self.x11, self.y11, fill = self.color)
    
    #Method for the main ship class to move the ship to the left.    
    def moveLeft(self):
        
        if self.x1 <= 0:
            self.x1 = 500
            self.x2 = 505
            self.x3 = 510
            self.x4 = 511
            self.x5 = 512
            self.x6 = 512
            self.x7 = 488
            self.x8 = 488
            self.x9 = 489
            self.x10 = 490
            self.x11 = 495
        else:
            self.x1 -= self.velocity
            self.x2 -= self.velocity
            self.x3 -= self.velocity
            self.x4 -= self.velocity
            self.x5 -= self.velocity
            self.x6 -= self.velocity
            self.x7 -= self.velocity
            self.x8 -= self.velocity
            self.x9 -= self.velocity
            self.x10 -= self.velocity
            self.x11 -= self.velocity
    
    #Method for the main ship class to move the ship to the right.
    def moveRight(self):
        
        if self.x1 >= 500:
            self.x1 = 0
            self.x2 = 5
            self.x3 = 10
            self.x4 = 11
            self.x5 = 12
            self.x6 = 12
            self.x7 = -12
            self.x8 = -12
            self.x9 = -11
            self.x10 = -10
            self.x11 = -5
        else:
            self.x1 += self.velocity
            self.x2 += self.velocity
            self.x3 += self.velocity
            self.x4 += self.velocity
            self.x5 += self.velocity
            self.x6 += self.velocity
            self.x7 += self.velocity
            self.x8 += self.velocity
            self.x9 += self.velocity
            self.x10 += self.velocity
            self.x11 += self.velocity
    
    #Method to detect if an asteroid hits the main spaceship.        
    def asteroid_collision(self, asteroidx, asteroidy, asteroidx1, asteroidy1):
        
        self.asteroidx = asteroidx
        self.asteroidy = asteroidy
        self.asteroidx1 = asteroidx1
        self.asteroidy1 = asteroidy1
        
        #Check if the asteroid touches the main point/tip of the space ship.
        if self.get_x1_point() > self.asteroidx and self.get_x1_point() < self.asteroidx1:
            if self.get_y1_point() > self.asteroidy and self.get_y1_point() < self.asteroidy1:
                return True
            
        #Check if the asteroid touches the left or right smaller tips of the space ship.
        elif self.get_x4_point() > self.asteroidx and self.get_x4_point() < self.asteroidx1:
            if self.get_y4_point() > self.asteroidy and self.get_y4_point() < self.asteroidy1:
                return True
            
        elif self.get_x9_point() > self.asteroidx and self.get_x9_point() < self.asteroidx1:
            if self.get_y9_point() > self.asteroidy and self.get_y9_point() < self.asteroidy1:
                return True
            
        #Return false if the asteroid does not touch the main space ship.
        else:
            return False
    
    #Method to see if an enemy laser hit the main spaceship.    
    def enemy_laser_collision(self, laserx, lasery):
        
        self.laserx = laserx
        self.lasery = lasery
        
        #Check if the tip of the laser point is touching the main ship.
        if self.laserx >= self.get_x7_point() and self.laserx <= self.get_x5_point():
            if self.lasery >= self.get_y5_point() and self.lasery <= self.get_y7_point():
                return True
            
        else:
            return False
    
    #Method (accessor) for the current x1 value of the specific instance.    
    def get_x1_point(self):
        
        return self.x1
    
    #Method (accessor) for the current y1 value of the specific instance.
    def get_y1_point(self):
        
        return self.y1
    
    #Method (accessor) for the current x4 value of the specific instance.
    def get_x4_point(self):
        
        return self.x4
    
    #Method (accessor) for the current y4 value of the specific instance.
    def get_y4_point(self):
        
        return self.y4
    
    #Method (accessor) for the current x5 value of the specific instance.
    def get_x5_point(self):
        
        return self.x5
    
    #Method (accessor) for the current y5 value of the specific instance.
    def get_y5_point(self):
        
        return self.y5
    
    #Method (accessor) for the current x7 value of the specific instance.   
    def get_y7_point(self):
        
        return self.y8
    
    #Method (accessor) for the current y7 value of the specific instance.
    def get_x7_point(self):
        
        return self.x8
    
    #Method (accessor) for the current x9 value of the specific instance.
    def get_x9_point(self):
        
        return self.x9
    
    #Method (accessor) for the current y9 value of the specific instance.
    def get_y9_point(self):
        
        return self.y9
   
#------MAINCODE----------
if __name__ == "__main__":
    
    #Test that all the accessor methods work properly.
    mainship_one = Main_SpaceShip(250, 465)
    assert mainship_one.get_x1_point() == 250
    assert mainship_one.get_y1_point() == 465
    mainship_one.moveLeft()
    assert mainship_one.get_x1_point() == 240
    assert mainship_one.get_y1_point() == 465
    mainship_one.moveRight()
    mainship_one.moveRight()
    assert mainship_one.get_x1_point() == 260
    assert mainship_one.get_y1_point() == 465
    print("The first tests have been passed!")
        
    #Test that the first raise exception works properly.
    try:
        mainship_two = Main_SpaceShip('hi', 465)
    except ValueError as e:
        print(e)
        
    try:
        mainship_three = Main_SpaceShip(250, 465.7)
    except ValueError as e:
        print(e)
    
    #Test that the second raise exception works properly.
    try: 
        mainship_four = Main_SpaceShip(230, 465)
    except ValueError as e:
        print(e)
    
    #Test that the third raise exception works properly.    
    try:
        mainship_five = Main_SpaceShip(250, 480)
    except ValueError as e:
        print(e)