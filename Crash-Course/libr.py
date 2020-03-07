week = ['monday', 'friday', 'saturday', 'wednesday', 'thursday', 'tuesday']
subject = ['Python', 'Java', 'JavaScript', 'Swift', 'Ruby', 'Dart']

for day in week:
	print(day)

userInput = input('Enter day of week: ')
for i in range(6):
	if userInput == week[i]:
		print(subject[i])
		break
