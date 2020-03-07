def main():
	print('This is a calculator which can perform following Operations: ')
	print('Enter each keyword for perform each Operation: ')
	print("For Addition - 'add' \nFor Subtraction - 'sub' \nFor Multiplication - 'mul' \nFor Division - 'div' \nFor Quit - 'q' ")
	condition_check()


def condition_check():
	while(True):
		user_input = input('Enter Operation name here: ')
		if user_input == 'add':
			print(addition())
		
		elif user_input == 'sub':
			print(subtraction())

		elif user_input == 'mul':
			print(multiplication())
		
		elif user_input == 'div':
			print(division())
		
		elif user_input == 'q':
			break

		else:
			print('Enter Right Input!')
			


def addition():
	a = int(input('Enter first value: '))
	b = int(input('Enter second value: '))
	return a + b


def subtraction():
	a = int(input('Enter first value: '))
	b = int(input('Enter second value: '))
	return a - b


def multiplication():
	a = int(input('Enter first value: '))
	b = int(input('Enter second value: '))
	return a * b


def division():
	a = int(input('Enter first value: '))
	b = int(input('Enter second value: '))
	return a / b

if __name__ == '__main__':
	main()