#this is simualiting a websites checking that everone has a unique username

current_users = ['John', 'david', 'Angel', 'samuel', 'anthony']#list of current users in websites

new_users = ['john', 'ANTHONY', 'camille', 'Yuliana', 'william']#list of new users in websites

#this is to put every single item on list title()
current_user = [current.title() for current in current_users]

#creating a loop in if statement to compare the two list
for new_user in new_users:
    if new_user.title() in current_user:
        print('The username ' + new_user + ', is not available please wrtie another one.')
    else:
        print('The username ' + new_user + ' is available.')

 