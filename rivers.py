# Learning about dictionaies

rivers = {'nile': 'egypt', 'the amazon river': 'amazon', 'volga': 'europe'}

for river,country in rivers.items():
    print('\n' + 'The ' + river.title() + ' runs through ' + country.title()) #printing keys and values together

for river in rivers.keys():
    print('\n' +  str(river.title()) + '.')#printing keys seperated of values

for countries in rivers.values():
    print('\n' + str(countries.title()) + '.')#printing values seperated of keys