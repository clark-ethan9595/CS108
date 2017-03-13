'''A program to see what kinds of errors are out there.
Created on Nov 6, 2014
Lab10
@author: elc3
'''

try:
    import happiness
except ImportError as ie:
    print('Dealt with Import Error:', ie)

try:
    'hi' + 4
except TypeError as te:
    print('Dealt with Type Error:', te)
    
try:
    10 / 0
except ZeroDivisionError as zde:
    print('Dealt with Zero Division Error:', zde)
    
try:
    'person'.find_first('e')
except AttributeError as ae:
    print('Dealt with Attribute Error:', ae)
    
try:
    [0,1,2]['summer']
except TypeError as te:
    print('Dealt with Type Error:', te)
    
try:
    ['hi','there','student'][5]
except IndexError as ie:
    print('Dealt with Index Error:', ie)
    
try:
    print(name)
except NameError as ne:
    print('Dealt with Name Error:', ne)
    
try:
    9 <= (3, 4)
except TypeError as te:
    print('Dealt with Type Error:', te)
    
try:
    f = open('missingFile.txt')
except FileNotFoundError as fnfe:
    print('Dealt with File Not Found Error:', fnfe)