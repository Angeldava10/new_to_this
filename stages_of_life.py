#keeping practicing of if_elif_else with a really long chain
#added an element of random with import random to use all version

import random
randint = [2,65]
age = random.randint(2,65)

if age == 2:
    print('You are just a little baby!')
elif age <= 4 :
    print('You are just a toddler')
elif age == 4 or age < 13:
    print('You are just a kid')
elif age == 13 and age < 20:
    print("You are a teenager, why you wanna like a grown up?")
elif age == 20 and age < 65:
    print('You are adult now, you need to take care of things')
else:
    print('You are and old person, take care of youserlf.')
