def show_magicians(magicians_names):
    for magicians in magicians_names:
        print('\nYour a wizard ' + magicians.title() + '.')
       
    

def make_great(magicians_names):
    great_magicians = []
    
    while magicians_names:
        magicians_name = magicians_names.pop()
        great_magician = magicians_name + ' The Great'                           #modyfing the list and the function
        great_magicians.append(great_magician)
        
        
    for great_magician in great_magicians:
        magicians_names.append(great_magician)
    
    

magicians_names = ['harry potter', 'jason', 'dumbeldort']
show_magicians(magicians_names)
 
make_great(magicians_names)
show_magicians(magicians_names)
