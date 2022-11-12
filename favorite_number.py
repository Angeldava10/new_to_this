# writing favorite_numers in fewer lines of codes
favorite_numbers = {
    'Angel': [5,2,3],
    'Camille': [4,10,12],
    'Yuliana' : [6, 8, 9],
    'Anthony' : [1,0,25],
    'William': [30,7,100]
    } 

for name,numbers in favorite_numbers.items():
    print('\n' + name + ' favorite numbers are:')
    for number in numbers:
        print('#' + str(number))