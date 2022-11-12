# Writing dictionaries on dictionaries

cities = {
    'New york city': {
        'country': 'United States',
        'population': '8.468 million',
        'fact': 'Is home to the first pizzeria in America.'
    },
    'Los Angeles': {
        'country': 'United States',
        'population': ' 3.849 million',
        'fact' : 'Only city to have hosted the Olympics twice.'
    },
    'chicago': {
       'country' : 'United States',
        'population' : '2.697 million',
        'fact': 'Rests on 234 square miles of land'
    }   
}

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    fact = city_info['fact']

    print("\n" + city.title() + " is in " + country + ".")
    print("  It has a population of about " + population + ".")
    print('  ' + fact)