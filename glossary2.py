# This is glossary.py more advance, looping through dictionaries.
#added 5 more terms to the dictionary
python_words = {
    'int': 'converts the specified value into an integer number.', 
    'str' : 'converts the specified value into a strings.',
    'del' : 'is used to delete objects.', 
    'print': 'prints the specified message to the screen, or other standard output device.',
    'pop': 'removes the specified item from the dictionary.',
    'list': 'is a data structure in Python that is a mutable, or changeable, ordered sequence of elements.',
    'dic':  'Pythons efficient key/value hash table structure.',
    'for': 'used for iterating over a sequence.' ,
    'if': 'It allows for conditional execution of a statement.',
    'float': 'is a method that returns a floating-point number for a provided number or string.'
    }

for words,python in python_words.items():
    print('\n' + words.title() + ': ' + python)
