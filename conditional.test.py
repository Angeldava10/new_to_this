#testing equality
animal_1 = 'dog'
animal_2 = 'cat'
animal_3 = 'dog'

if animal_1 == animal_3:
    print('Its equal.')
else:
    print('Its unequal.')

if animal_1 != animal_2:
    print('\nIts unequal')
else:
    print('\nIts equal')

#understanding the lower()
animal = 'Dog'.lower()
print("\nIs Animal equals 'dog' I predict true.")
print(animal == 'Dog'.lower())

#numerical test using equals, not equal, greather or equal then and lesser or equal than

number_1 = 5
number_2 = 10

if(number_1 == 5):
    print('\nIts equal')

if(number_2 != 11):
    print('\nIts unequal')

if(number_2 >= number_1):
    print('\nIts a higher number.')

if(number_1 <= number_2):
    print('Its a lower number.')

#using 'and' and 'or'
if number_1 == 5 and number_2 == 10:
    print('\nTheir are equal')
    
if number_2 != 5 or number_1 != 2:
    print('Their are not equal')

#testing whether something is on a list using in
numbers = [1 , 3 , 5 , 6]
number_1= 4
number_2 = 5

if number_2 in numbers: 
    print('\nIts on the list.')
else:
    print('\nIts not on the list.')

#testing whether someting is not on the list using in 
if number_1 in numbers:
    print('Its on the list.')
else:
    print('Its not on the list')






