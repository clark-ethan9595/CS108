''' A program to make Calvin usernames.
Fall 2014
Lab 03
@authors Ethan Clark and Jacob Schott (elc3 and jps29)
'''
#Ask the user for first name, last name, and student ID.
first_name = input('Please give your first name : ')
last_name = input('Please give your last name : ')
student_id = input('Please give your student ID number : ')

#Get the fist letter of the first name.                 
first_name = first_name[0:1]

#Get the first five letters of the last name.
last_name = last_name[0:5]

#Get the last two digits of the student ID.
student_id = student_id[5:7]

#Create the username in all lowercase letters.
login_id = first_name + last_name + student_id
login_id = login_id.lower()

#Print the Calvin username.
print("Your login id would be :", login_id)