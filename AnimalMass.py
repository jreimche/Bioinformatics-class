#! /usr/bin/env python

"""
This code will create a dictionary of animals and their corresponding mass
If an animal is over 20g it will print big next to its name
If an animal is under 20g it will print small next to its name
"""
#create dictionary of snake IDs and their mass (g)
animal_dict = {
'Snake1':2,
'Snake2':4,
'Snake3':8,
'Snake4':22,
'Snake5':24,
'Snake6':28
}


#create list of snakes
SnakeList = ['Snake1', 'Snake2', 'Snake3', 'Snake4', 'Snake5', 'Snake6']

#create empty variable called SnakeWeight
SnakeWeight = 0 

#loop through each snake in the list and put the corresponding value as SnakeWeight, then put SnakeWeight through ifelse statment: if SnakeWeight is >= 20g print big next to the Snake ID, if SnakeWeight if < 20g, print small next to Snake ID
for Snake in SnakeList:
	SnakeWeight = animal_dict[Snake]
	if SnakeWeight >= 20:
		print("%s is big" % (Snake))
	else:
		print("%s is small" % (Snake))

