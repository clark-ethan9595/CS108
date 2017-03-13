'''Program to create a laser beam for "SpaceShip Adventures."
Created on Dec 1, 2014
Final Project
@author: Ethan Clark (elc3)
'''

#Class to model a laser shot from a spaceship.
class LaserBeam():
    
    ''' A class to model a laser beam for the game "SpaceShip Adventures."
        Invariants:
            x must be an integer between 0 and 600.
            y must be 465.
            x1 must be an integer between 0 and 600 (same as x)
            y1 must be 445.
            Color must be white.
    '''
    
    #Constructor to create an instance of the LaserShot class.
    def __init__(self, x):
        
        #Check to see if the invariants were followed.
        if isinstance(x, int) == False:
            raise ValueError('Please use integer values.')
        
        if x < 0 or x > 500:
            raise ValueError('Invalid x coordinate: must be equal to or between 0 and 600.')
        
        #Create instance if the invariants checked out good.
        else:
            self.x = x
            self.y = 465
            self.x1 = x
            self.y1 = 445
            self.color = 'White'
            self.laser_vel = -10
    
    #Method for the LaserShot class to put the laser shot on the canvas.    
    def render_laser_beam(self, canvas):
        
        canvas.create_line(self.x, self.y, self.x1, self.y1, fill = self.color)
    
    #Method for the LaserShot class to move the laser shot on the canvas.    
    def move_laser_beam(self, canvas):
        
        self.y = self.y + self.laser_vel
        self.y1 = self.y1 + self.laser_vel
    
    #Method (accessor) to return the x1 coordinate of the laser beam.    
    def get_laser_beam_x1(self):
        
        return self.x1
    
    #Method (accessor) to return the y1 coordinate of the laser beam.    
    def get_laser_beam_y1(self):
        
        return self.y1
    
#------MAINCODE-------
if __name__ == "__main__":
    
    #Test that the accessor methods work properly.
    laser_one = LaserBeam(450)
    assert laser_one.get_laser_beam_x1() == 450
    assert laser_one.get_laser_beam_y1() == 445
    print('All tests have been passed!')
    
    #Test that the first raise exception works properly.       
    try:
        laser_two = LaserBeam('hi')
    except ValueError as e:
        print(e)
        
    try:
        laser_three = LaserBeam(510.01)
    except ValueError as e:
        print(e)
    
    #Test that the second raise exception works properly.
    try:
        laser_four = LaserBeam(610)
    except ValueError as e:
        print(e)