''' 
Practice using strings and functions to validate user inputted strings.
October 16, 2014
Lab 07
@author Ethan Clark (elc3)
'''

#Create a function to validate a social security number.
def isvalidSSN(possible_ssn):
    if possible_ssn[3] != '-' or possible_ssn[6] != '-':
        return False
    possible_ssn_list = list(possible_ssn)
    num_dashes = possible_ssn_list.count('-')
    if num_dashes != 2:
        return False
    y = possible_ssn.replace('-', '')
    x = y.isdigit()
    if x == False:
        return False
    if len(y) == 9:
        return True
    else:
        return False

#Create a function to validate a password with certain criteria.
def isValidPassword():
    possible_password = input('Please give a possible password: ')
    password_list = list(possible_password)
    print(password_list)
    if len(possible_password) < 8:
        return False
    if possible_password.isalnum() == False:
        return False
    count = 0
    for a in possible_password:
        if a.isdigit() == True:
            count += 1
    if count < 2:
        return False
    else:
        return True

#Checks the validity of the first characters of a credit card number.
def isValidPrefix(credit_card):
    credit_card = int(credit_card)
    if credit_card[0:1] != '4' or credit_card[0:1] != '5' or credit_card[0:1] != '6' or credit_card[0,2] != '37':
        return False
    else:
        return True
    
#Function to sum the odd digits of the credit card number.
def sum_of_odds(credit_card):
    sum_odds = 0
    for c in credit_card[:0:-2]:
        sum_odds += int(c)
    return sum_odds
                
print(sum_of_odds('4388576018402626'))

#Function to sum the doubles of the even characters of a credit card number.
def sum_of_double_evens(credit_card):
    start = len(credit_card) - 1
    credit_card_evens = list(int(credit_card[start:0:-2]))
    doubled_evens = []
    for c in credit_card_evens:
        c = c * 2
        doubled_evens.append(c)
    sum_doubled_evens = sum(doubled_evens)
    return sum_doubled_evens
print(sum_of_double_evens('4388576018402626'))

#Function to check all the validity checks of being a credit card number.
def isValidCC(cc):
    mod_ten_check = (sum_of_odds(cc) + sum_of_double_evens(cc)) % 10
    if len(cc) < 13 or len(cc) > 16:
        return False
    elif cc.isdigit() == False:
        return False
    elif isValidPrefix(cc) == False:
        return False
    elif mod_ten_check != 0:
        return False
    else:
        return True
    
#Create a menu function to drive the program.
def menu():
    print('Please select from the following list of options (type the appropriate character): ')
    print('A. Print a nice message')
    print('S. Validate a Social Security Number')
    print('P. Validate a password')
    print('C. Validate a credit card number')
    print('Q. Quit')

'''
while True:
    menu()    
    user_choice = input('Choice: ')
    if user_choice == 'A' or user_choice == 'a':
        print('Have a nice day!')
    elif user_choice == 'Q' or user_choice == 'q':
        print('Good-bye!')
        break
    elif user_choice == 'S' or user_choice == 's':
        possible_ssn = input('Please give a possible social security number: ')
        if isvalidSSN(possible_ssn) == True:
            print('Valid SSN!')
        else:
            print('Invalid SSN!')
    elif user_choice == 'P' or user_choice == 'p':
        possible_password = input('Please give a possible password: ')
        if isValidPassword(possible_password) == True:
            print('Valid Password!')
        else:
            print('Invalid Password!')
    elif user_choice == 'C' or user_choice == 'c':
        credit_card = input('Please give a possible credit card number: ')
        if isValidCC(credit_card) == True:
            print('Valid Credit Card!')
        else:
            print('Invalid Credit Card')
    else:
        print("I'm sorry, that is not a valid option.")
'''