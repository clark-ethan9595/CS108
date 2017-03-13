''' A program to specify verses, container, and desired food/beverage.
Fall 2014
Lab 05
@author Ethan Clark (elc3)
'''

#Prompt user for their own version of the song lyrics
verses = int(input('Please give number of verses for song:'))
container = input('Please give a container for your food/beverage:')
substance = input('Please give a desired food/beverage:')

#Fix the number of verses to a variable to use in the last verse of the song.
number = verses

#Use a loop to write the song with the user-desired verses, container, and substance.
for count in range(verses, -1, -1):
    if verses != 0:
        print(verses, container + '(s) of', substance, 'on the wall,', verses, container + '(s) of', substance + '. Take one down, pass it around,', (verses - 1), container + '(s) of', substance, 'on the wall.')
        verses = verses - 1
    else:
        print(verses, container + '(s) of', substance, 'on the wall,', verses, container + '(s) of', substance + '. Go to the store and buy some more.', number, container + '(s) of', substance, 'on the wall.')
    
print('Finish')