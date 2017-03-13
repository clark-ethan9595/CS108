'''Program to create enemy spaceships for "SpaceShip Adventures."
Created on November 31, 2014
Final Project
@author: Ethan Clark (elc3)
'''

#Import the randint function.
from random import randint

#Class to model enemy spaceships.
class Enemy_SpaceShips:
    
    ''' A class to model an enemy spaceship in the game "SpaceShip Adventure"
        Invariants:
            First x coordinate (x1) must be an integer equal  to or between 20 and 480.
            First y coordinate (y1) must be -40.
            Color must be red.
    '''
    
    #Constructor to create an instance of the enemy spaceships.
    def __init__(self, x1, y1):
        
        #Checks to see if the invariants were followed.
        if isinstance(x1, int) == False or isinstance(y1, int) == False:
            raise ValueError('Please use integer values.')
        
        elif x1 < 20 or x1 > 480:
            raise ValueError('Invalid x coordinate: must be equal to or between 20 and 480.')
        
        elif y1 != -40:
            raise ValueError('Invalid y coordinate: must be -40.')
        
        #Create an instance if the invariants checked out good.
        else:
            self.x1 = x1
            self.y1 = y1
            self.x2 = x1 + 7
            self.y2 = y1 - 20
            self.x3 = x1 + 12
            self.y3 = y1 - 20
            self.x4 = x1 + 13
            self.y4 = y1 - 10
            self.x5 = x1 + 14
            self.y5 = y1 - 20
            self.x6 = x1 + 14
            self.y6 = y1 - 30
            self.x7 = x1 - 14
            self.y7 = y1 - 30
            self.x8 = x1 - 14
            self.y8 = y1 - 20
            self.x9 = x1 - 13
            self.y9 = y1 - 10
            self.x10 = x1 - 12
            self.y10 = y1 - 20
            self.x11 = x1 - 7
            self.y11 = y1 - 20
            
            self.color = 'Red'
            self.velocity = 1
            
            self.randint1 = randint(10, 400)
            self.randint2 = randint(10, 400)
    
    #Method for the enemy spaceships class to put the enemy ship on the canvas.    
    def render_enemyships(self, canvas):
        
        canvas.create_polygon(self.x1, self.y1, self.x2, self.y2, self.x3, self.y3, self.x4, self.y4,
                              self.x5, self.y5, self.x6, self.y6, self.x7, self.y7, self.x8, self.y8,
                              self.x9, self.y9, self.x10, self.y10, self.x11, self.y11, fill = self.color)
    
    #Method for the enemy spaceships class to move the enemy ships on the canvas.    
    def move_enemyships(self, canvas):
        
        self.y1 += self.velocity
        self.y2 += self.velocity
        self.y3 += self.velocity
        self.y4 += self.velocity
        self.y5 += self.velocity
        self.y6 += self.velocity
        self.y7 += self.velocity
        self.y8 += self.velocity
        self.y9 += self.velocity
        self.y10 += self.velocity
        self.y11 += self.velocity
    
    #Method to see if a laser beam collides with the enemy spaceship.
    def laser_collision(self, laser_y1_value, laser_x1_value):
        
        self.laser_y1_value = laser_y1_value
        self.laser_x1_value = laser_x1_value
        
        if self.laser_y1_value >= self.get_y6_value_enemy() and self.laser_x1_value <= self.get_x6_value_enemy():
            if self.laser_y1_value <= self.get_y8_value_enemy() and self.laser_x1_value >= self.get_x8_value_enemy():
                return True
        else:
            return False
    
    #Method to determine when the enemy ship shoots laser beams.    
    def enemy_laser_shot(self, tracker_variable):
        
        #If the user is on level one, don't have the enemy ships shoot lasers.
        if tracker_variable < 3000:
            return False
        
        #If the user is on level two, have the enemy ship shoot one laser beam.
        elif 3000 <= tracker_variable < 6000:
            
            if self.get_y1_value_enemy() == self.randint1:
                return True
            else:
                return False
        
        #If the user is on level three or higher, have the enemy shoot two laser beams.
        else:
            if self.get_y1_value_enemy() == self.randint1:
                return True
            
            if self.get_y1_value_enemy() == self.randint2:
                return True
            
            else:
                return False

    
    #Method to return the x1 coordinate of the enemy spaceship.    
    def get_x1_value_enemy(self):
        
        return self.x1
    
    #Method to return the y1 coordinate of the enemy spaceship.    
    def get_y1_value_enemy(self):
        
        return self.y1
     
    #Method (accessor) to return the x6 coordinate of the enemy spaceship (used for collision detection).   
    def get_x6_value_enemy(self):
        
        return self.x6
    
    #Method (accessor) to return the y6 coordinate of the enemy spaceship (used for collision detection).
    def get_y6_value_enemy(self):
        
        return self.y6
    
    #Method (accessor) to return the x8 coordinate of the enemy spaceship (used for collision detection).
    def get_x8_value_enemy(self):
        
        return self.x8
    
    #Method (accessor) to return the y8 coordinate of the enemy spaceship (used for collision detection).
    def get_y8_value_enemy(self):
        
        return self.y8

#-----MAINCODE--------    
if __name__ == "__main__":
    
    #Test that the accessor methods work properly.
    enemyship_one = Enemy_SpaceShips(400, -40)
    assert enemyship_one.get_x1_value_enemy() == 400
    assert enemyship_one.get_y1_value_enemy() == -40
    print("The first tests have been passed!")
        
    #Test that the first raise exception works properly.    
    try:
        enemyship_two = Enemy_SpaceShips('hi', -40)
    except ValueError as e:
        print(e)
        
    try:
        enemyship_three = Enemy_SpaceShips(300, -40.6)
    except ValueError as e:
        print(e)
    
    #Test that the second raise exception works properly.
    try:
        enemyship_four = Enemy_SpaceShips(500, -40)
    except ValueError as e:
        print(e)
    
    #Test that the third raise exception works properly.
    try:
        enemyship_five = Enemy_SpaceShips(300, -30)
    except ValueError as e:
        print(e)