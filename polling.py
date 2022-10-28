# Using lists and dictionary at the same time and writing a conditional test for it

list = ['jen', 'sarah', 'edward', 'phill', 'angel', 'yuliana', 'camille']#people that should take a poll

favorite_language = {                   #poll about favorite programming language 
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phill': 'python',
    }   

for lists in list:
    if lists in favorite_language:                                          
        # Those who took it.
        print('\n' + lists.title() + ', thank you for responding our poll!')
    else:
        # Those who havent.
        print('\n' + lists.title() + ', we invite you to respond to our poll!')

