sandwich_orders = ['tuna', 'chicken', 'salad', 'salami','pastrami', 'pastrami']
finished_sandwiches = []


print('\nWere sorry but we run out of pastrami')
while 'pastrami' in sandwich_orders:
     sandwich_orders.remove('pastrami')
        

while sandwich_orders:
    current_sandwiches = sandwich_orders.pop()
    
    print('Your sandwhich ' + current_sandwiches + ' is being made')
    
    finished_sandwiches.append(current_sandwiches)
    
    
print('\nThe following sandwhich is made:')
for sandwhich in finished_sandwiches:
    print(sandwhich)
        





    
    