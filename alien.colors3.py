#Doing an if-elif-else chain and running three blocks to produce each version of the chain

alien_color = ['green', 'yellow', 'red']#list of type of aliens

first_player = 'green'
second_player = 'yellow'
third_player =  'red'
 
if first_player in alien_color:                         #this block is for the first_player
    print('Great player! You have earned 5 points.')
elif second_player in alien_color:
    print('Good job player! You have earned 10 points!')
else:
    print('Congratulation player! You have earned 15 points!')


first_player = 'blue'
second_player = 'yellow'
third_player =  'red'

if first_player in alien_color:                         #this block is for the second_player
    print('Great player! You have earned 5 points.')
elif second_player in alien_color:
    print('\nGood job player! You have earned 10 points!')
else:
    print('Congratulation player! You have earned 15 points!')


first_player = 'blue'
second_player = 'orange'
third_player =  'red'

if first_player in alien_color:                         #this block is for the third_player
    print('Great player! You have earned 5 points.')
elif second_player in alien_color:
    print('Good job player! You have earned 10 points!')
else:
    print('\nCongratulation player! You have earned 15 points!')