responses = {}

#set a flag to indicate that polling is active
polling_active = True

while polling_active:
    #prompt for the person's name and response
    name = input('\nWhat is your name? ')
    response = input("Which places would you like to go someday?").title()
    
    #store the response in the dictionary
    responses[name] = response
    
    #find out if anyone else is going to take the poll
    repeat = input('Would you like to let another person respond? (yes / no) ')
    if repeat == 'no':
        polling_active = False
        
#polling is complete. show results
print('\n---- Poll Results ---')
for name, response in responses.items():
    print(name.title() + ' would like to go  ' + response + '.')