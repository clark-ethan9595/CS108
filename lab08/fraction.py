'''
A program to practice basic class design and implementation to model fractions.
October 24, 2014
Lab 08
@author Ethan Clark (elc3)
'''

#Import the system-specific parameters.
import sys

#Function to compute greatest common divisor.
def computeGCD(alpha, beta):
    '''
    (int, int) -> int
    This function finds the greatest common divisor of two integers, using
    Euclid’s algorithm
    '''
    alpha = abs(alpha)
    beta = abs(beta)
    remainder = alpha % beta
    while (remainder != 0):
        alpha = beta
        beta = remainder
        remainder = alpha % beta
    return beta

#Exercise 8.1; creating a Fraction class for our program.
class Fraction:
    '''
    Models a fraction
    Invariants
        Denominator is not equal to 0.
        Numerator is any integer value.
    '''
    
    #Exercise 8.2; constructor function to add instance variables.
    def __init__(self, numerator = 0, denominator = 1):
        '''
        () -> Fraction
        Constructor
        '''
        if denominator == 0:
            print('Unable to create invalid fraction', file=sys.stderr)
            sys.exit(-1)
        else:
            self._denominator = denominator
        self._numerator = numerator
        self.simplify()
    
    #Exercise 8.5, accessor methods
    def get_Numerator(self):
        ''' Accessor for the numerator '''
        return self._numerator
    
    def get_Denominator(self):
        ''' Accessor for the denominator '''
        return self._denominator

    #Exercise 8.6; mutator to simplify the fraction given by the user.
    def simplify(self):
        ''' 
        Mutator to simplify the fraction and put the negative sign
        in the numerator (if applicable).
        '''
        gcd = computeGCD(self._numerator, self._denominator)
        if gcd != 0:
            self._numerator = self._numerator//gcd
            self._denominator = self._denominator//gcd
        if self._denominator < 0:
            self._numerator = self._numerator * -1
            self._denominator = self._denominator * -1
    
    #Exercise 8.7; multiply fractions.        
    def __mul__(self, other):
        '''
        Receive two fractions, multiply them, and return new fraction
        '''
        numerator = self._numerator * other.get_Numerator()
        denominator = self._denominator * other.get_Denominator()
        new_fraction = Fraction(numerator, denominator)
        return new_fraction
    
    #Exercise 8.3; specify exactly how to print the fraction.
    def __str__(self):
        ''' Print fraction nicely '''
        return (str(self._numerator) + '/' + str(self._denominator))
        
#--------------------MAIN CODE-----------------
#Exercise 8.3 test
f1 = Fraction()
print(f1)

#Exercise 8.4 tests
f2 = Fraction(1,2)
print(f2)
ftest1 = Fraction(1 + 2, 2 - 1)
print(ftest1)
ftest2 = Fraction(5 * 1, 3 * 4)
print(ftest2)

#Test to crash the program with dividing by 0.
#ftest3 = Fraction(6, 0)
#print(ftest3)

#Exercise 8.5 tests
ftest4 = Fraction()
print(ftest4.get_Denominator())
print(ftest4.get_Numerator())

#Exercise 8.6 tests
f3 = Fraction(2,4)
print(f3)
f4 = Fraction(3,9)
print(f4)
f5 = Fraction(-4, -16)
print(f5)
f6 = Fraction(5, -10)
print(f6)

#Exercise 8.7 tests
f7 = (f3 * f4)
print(f7)
f8 = (f5 * f6)
print(f8)
f9 = (f1 * f2)
print(f9)