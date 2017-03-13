''' A program to sort numbers from min to max.
Fall 2014
Lab 03
@authors Ethan Clark and Jacob Schott (elc3 and jps29)
'''

''' Begin by asking the user for four numbers.
Put the numbers in a list.
Locate the minimum, assign it to a variable, then remove it from the list.
Repeat the process two more times.
Order numbers from least to greatest in a list.
Print the list.
'''

#Ask the user for four numbers.
num_one = int(input("Please enter number 1 :"))
num_two = int(input("Please enter number 2 :"))
num_three = int(input("Please enter number 3:"))
num_four = int(input("Please enter number 4:"))

#Create a list with the four numbers.
storage = [num_one, num_two, num_three, num_four]

#Find the lowest number of the list, make variable, then remove it. Repeat twice.
num_low = min(storage)
storage.remove(num_low)
num_low_mid = min(storage)
storage.remove(num_low_mid)
num_high_mid = min(storage)
storage.remove(num_high_mid)
num_high = min(storage)

#Create new list with new variables of the ordered numbers.
storage = [num_low, num_low_mid, num_high_mid, num_high]

print(storage)