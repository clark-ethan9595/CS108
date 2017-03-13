'''Program to create enemy laser beams for the game "SpaceShip Adventures."
Created on Dec 11, 2014
Final Project
@author: Ethan Clark (elc3)
'''

#Class to model a laser beam from an enemy spaceship.
class Enemy_LaserBeam:
    
    ''' A class to model an enemy laser beam for the game "SpaceShip Adventures."
        Invariants:
            x must be an integer equal to or between 0 and 500.
            y must be an integer equal to or between -50 and 550.
    '''
    
    #Constructor method to create an instance of the class.
    def __init__(self, x, y):
        
        #Check to see if the invariants were followed.
        if isinstance(x, int) == False or isinstance(y, int) == False:
            raise ValueError('Please use integer values.')
        
        elif x <= 0 or x >= 500:
            raise ValueError('Invalid x coordinate: must be equal to or between 0 and 500.')
        
        elif y <= -50 or y >= 550:
            raise ValueError('Invalid y coordinate: must be equal to or between 0 and 500.')
        
        #Create instance variables for the class.
        else:
            self.x = x
            self.y = y
            self.x1 = x
            self.y1 = y + 20
            
            self.color = 'White'
            self.velocity = 4
    
    #Method to put the enemy laser beam on the screen.
    def render_enemy_beam(self, canvas):
        
        canvas.create_line(self.x, self.y, self.x1, self.y1, fill = 'White')
    
    #Method to move the enemy laser beam down the screen.
    def move_enemy_beam(self):
        
        self.y += self.velocity
        self.y1 += self.velocity
    
    #Method (accessor) to return the x1 value of the instance laser beam.    
    def get_enemy_beam_x1(self):
        
        return self.x1
    
    #Method (accessor) to return the y1 value of the instance laser beam.
    def get_enemy_beam_y1(self):
        
        return self.y1
    
#-------MAINCODE-------
if __name__ == "__main__":
    
    #Test the accessor methods.
    enemy_laser_one = Enemy_LaserBeam(450, 300)
    assert enemy_laser_one.get_enemy_beam_x1() == 450
    assert enemy_laser_one.get_enemy_beam_y1() == 320
    print('All first tests have been passed!')
    
    #Test that the first raise exception works properly.
    try:
        enemy_laser_two = Enemy_LaserBeam('hi', 300)
    except ValueError as e:
        print(e)
    
    try:
        enemy_laser_three = Enemy_LaserBeam(450, 300.6)
    except ValueError as e:
        print(e)
    
    #Test that the second raise exception works properly.
    try:
        enemy_laser_four = Enemy_LaserBeam(-10, 300)
    except ValueError as e:
        print(e)
    
    #Test that the third raise exception works properly.    
    try:
        enemy_laser_five = Enemy_LaserBeam(300, 600)
    except ValueError as e:
        print(e)
    