''' A program to print an updated dictionary.
Fall 2014
Lab 03
@authors Ethan Clark and Jacob Schott (elc3 and jps29)
'''

#Create a dictionary for people and their scores.
scoreDict = {'Joe':10, 'Tom':23, 'Barb':13, 'Sue':19, 'Sally':12}

#Print Barb's score.
print("Barb's score is :", scoreDict['Barb'])

#Update Sally's score to 13.
scoreDict['Sally'] = 13

#Delete Tom and his score from the dictionary.
scoreDict.pop('Tom')

#Print the update dictionary.
print(scoreDict)