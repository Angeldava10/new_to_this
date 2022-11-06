# Practicing dictionaries with list 

pets = [] 

animal = {
    'animal' : 'dog',
    'name': 'leo',
    'owner': 'camille',
    'personality': 'good boy'
}
pets.append(animal)

animal = {
    'animal': 'cat',
    'name': 'lupita',
    'owner': 'yuliana',
    'personality': 'reserved'
}
pets.append(animal)

for animal in pets:
    print("\nHere's what I know about " + animal['name'].title() + ":")
    for key, value in animal.items():                          #ValueError: too many values to unpack (expected 2) when u see this use item()
        print("\t" + key + ": " + str(value))
    
