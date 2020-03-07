students = {'Pankaj': 58, 'Shalom': 78, 'Suraj': 72, 'Stuti': 82, 'Praveen': 57, 'Priyanka': 76, 'Sakshi': 67, 'Ekta': 88, 'Monika': 77}

def result():
	print('Students Names!')
	for student in students:
		print(student, end=' ')
	
	print('\nEnter student name for marks or q for Quit!')
	while(True):
		key  = input('Enter here: ')
		if key in students:
			print(students[key])

		elif key == 'q':
			break

		else:
			print('Please! Enter correct key!')



if __name__ == '__main__':
	result()

	
