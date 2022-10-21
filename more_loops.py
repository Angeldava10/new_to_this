#adding loops to foods.py
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_food = my_foods[:]

print('My favorite foods are:')
for myfood in my_foods:
    print(myfood)
    
print('\nMy friends food is also mines:')
for friends in friends_food:
    print(friends)
    