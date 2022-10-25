#Understanding how to add dictionaries to prints

python_words = {
    'int': ' converts the specified value into an integer number.', 
    'str' : 'converts the specified value into a strings.',
    'del' : ' is used to delete objects.', 
    'print': 'prints the specified message to the screen, or other standard output device.',
    'pop': 'removes the specified item from the dictionary.'}


integer = 'int'
print(integer.title() + ':' + python_words['int'])
string = 'str'
print('\n' + string.title() + ':' +  python_words['str'])
remove = 'del'
print('\n' + remove.title() + ':' + python_words['del'])
command = 'print'
print('\n' + command.title() + ':' +  python_words['print'])
split = 'pop'
print('\n' + split.title() + ':' + python_words['pop'])