#making hello_admin.py list empty and writing a conditional test for it 

users = []#list with usernames and admin

#this if is to make sure the list is not empty if it is it run to the else statment
if users:
     for user in users:
        if user == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print('\nHello ' + users+ ', thank you for loging in again.')
else:
    print('We need to find some users!')