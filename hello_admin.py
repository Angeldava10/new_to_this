##practicing conditional test with list and for loopz

users = ['angeldava_10', 'swag12_23', 'thegoat_575', 'admin', 'monkey_king123']#list with usernames and admin

#becuase admin is diferent then the other user we need to single him out 
for user in users:
    if user == 'admin':
        print('\nHello ' + user + ', would you like a to see a status report?')
    else:
        print('\nHello ' + user + ', thank you for loging in again.')