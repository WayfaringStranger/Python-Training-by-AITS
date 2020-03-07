usernamelist = ['shubham007', 'lucifer007']
passwordlist = ['123456', '012345']


print('Enter username and password: ')
user_name, user_pass = input().split()
if user_name in usernamelist:
	print(f'Username : {user_name}, Password : {user_pass}')
else:
	print('Enter write info!')	
