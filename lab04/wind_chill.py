''' Wind Chill calculator
fall of 2014
lab04
@authors Jake Schott (jps29) and Ethan Clark (elc3)
'''

#Prompt for and receive from the user the temperature in degrees and wind speed
temp = int(input('Please give the tempurature of the weather:'))
wind = int(input('Please give the wind speed of the weather:'))

#calculate chill
wind_chill = 35.74 + (0.6215 * temp) - (35.75 * wind**0.16) + (0.4275 * temp * wind**0.16)

#check to see if the equation will work
if wind < 2 or temp < -58 or temp > 41:
    print('Program will not work.')
else:
    print(wind_chill)

#Determine how many layers to wear.
if wind_chill < -40:
    print('5 Layers')
elif -40 <= wind_chill < -10:
    print('4 Layers')
elif -10 <= wind_chill < 20:
    print('3 Layers')
elif 20 <= wind_chill < 40:
    print('2 Layers')
elif wind_chill >= 40:
    print('1 Layer')