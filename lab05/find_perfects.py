''' A program to find perfect numbers.
Fall 2014
Lab 05
@author Ethan Clark (elc3)
'''

#Write a loop to find all the perfect numbers from 0 to 10,000.
found_num = 0
for value in range(2, 10001):
    low = 1
    high = value
    divisors = []

    while low < high:
        if (value % low) == 0:
            high = (value // low)
            divisors.append(low)
            if high != low:
                divisors.append(high)
        low = low + 1

    divisors.remove(value)
    
    if sum(divisors) == value:
        found_num += 1
        print(value, "is a perfect number!")
        if found_num == 4:
            break
