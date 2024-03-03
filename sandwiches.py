def make_sandwiches(*sanwdiches):
    print('\nPreparing your sandwhich.')
    for sandwiches in sanwdiches:
        print('\n...adding your sandwhich: ' + sandwiches)
    print('\nYour sandwhcih has been prepare!')
    

make_sandwiches('chicken')
make_sandwiches('chicken', 'salad')
make_sandwiches('chicken', 'bacon', 'egg')