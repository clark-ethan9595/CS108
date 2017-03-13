''' Variables and Expessions
September 11, 2014
Lab 02
@author Ethan and Mollie (elc3 and mfh6)
'''

#Ask user for a three digit number.
number = int(input('Give a three digit number where the first and last digits are more than 2 apart : '))

#Get the reverse of the user entered number.
rev_number = (number//1)%10 * 100 +  (number//10)%10 * 10 + (number//100)%10

#Find the difference of the number and the reverse of the number.
difference = abs(number - rev_number)

#Find the reverse of the difference.
rev_difference = (difference//1)%10 * 100 +  (difference//10)%10 * 10 + (difference//100)%10

#Print the difference of the difference and the reverse of the difference.
print(difference + rev_difference)

print(rev_number)
