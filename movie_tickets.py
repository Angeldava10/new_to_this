

theaters = '\nWhat age are u?'
theaters += "\nenter 'quit when finish"

while True:
    age = input(theaters)
    if age == 'quit':
        break
    age = int(age)
    
    if age < 3:
        print("\nThe ticket is free")
    elif age <13:
        print('\nThe ticket cost $10')
    else :
        print('\nThe ticket cost $15')
        
    
   
    