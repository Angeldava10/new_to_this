# Exercise of dicitionaries

favorite_places = {
    'Angel': ['beach', ' theaters', 'gym'],
    'Yuliana': ['dave and buster' , 'trampoline park ', 'spa'],
    'Camille': ['home alone', 'mall', 'restaurants']
}

for name,places in favorite_places.items():
    print('\n' + name + ' favorite places are:')
    for place in places:                  
        print('\n' + '- ' + place.title())
    