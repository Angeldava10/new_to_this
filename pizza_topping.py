pizza = '\nPlease tell me the toppings you want on your pizza'
pizza += '\n(Enter quit when you finish)'

while True:
    topping = input(pizza)
    
    if topping == 'quit':
        break
    else:
        print('\nYou have added ' + topping + ' to your pizza.')
        
    