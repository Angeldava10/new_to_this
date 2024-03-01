def make_shirt(size= 'large', message= 'I love python'):
    print('Your t-shirt says ' + message + '.')
    print('Your t-shirt is size ' + size + '.')
    
make_shirt('medium')
make_shirt('large')

small = "'No pain no gain"
make_shirt(message=small,size='large')