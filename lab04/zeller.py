''' Program to tell us the day of the week.
Fall 2014
Lab 04
@authors Jake Schott (jps29) and Ethan Clark (elc3)
'''

#Prompt user for the year, the month, and the day of the month.
year = int(input("Please give the year:"))
month = int(input("Please give the month:"))
day_month = int(input("Please give the day of the month:"))

#adjust for the first two months
if month == 1:
    month = 13
    year = year - 1
elif month == 2:
    month = 14
    year = year -1

#calculate the day of the week
day_week = (day_month + int(((month + 1) * 26) / 10) + (year % 100) + int((year % 100) / 4) + int((year // 100) / 4) + 5 * (year // 100)) % 7

#make a list for the days of the week
days_list = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

#determine the day and print it out
if day_week == 0:
    print('The day of the week is', days_list[0])
elif day_week == 1:
    print('The day of the week is', days_list[1])
elif day_week == 2:
    print('The day of the week is', days_list[2])
elif day_week == 3:
    print('The day of the week is', days_list[3])
elif day_week == 4:
    print('The day of the week is', days_list[4])
elif day_week == 5:
    print('The day of the week is', days_list[5])
elif day_week == 6:
    print('The day of the week is', days_list[6])
