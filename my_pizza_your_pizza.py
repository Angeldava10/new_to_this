favorite_pizza = ['peperonni', 'bacon', 'chesse']
friends_pizza = favorite_pizza[:]

favorite_pizza.append('without pineapple')
friends_pizza.append('with pineapple')

print('My favorite pizzas are:')
for favorites_pizza in favorite_pizza:
    print(favorites_pizza)

print('\nMy friends favorite pizzas are:')
for friend_pizza in friends_pizza:
    print(friend_pizza)