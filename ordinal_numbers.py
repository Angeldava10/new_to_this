#writing with names of numbers it.

numbers = list(range(1,10)) #list of numbers

#this loop put enfasis on 1,2,3 cause they have diferent names but the others are the same so they go with else
for number in numbers:
    if number == 1:
        print(str(number) + 'st')
    elif number == 2:
        print(str(number) + 'nd' )
    elif number == 3:
        print(str(number) + 'rd')
    else:
        print(str(number) + 'th')