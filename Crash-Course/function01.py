''' This is first Function. '''
def my_func():
	print('Monday')

my_func()


''' This is Second Function. '''
def my_function(str):
	print(f'Hello, {str}!')

my_function('Python') 


''' This is Third Function. '''
def my_country(Country = 'India'):
	print(f'I am from {Country}.')

my_country('USA')
my_country()
my_country('France')
my_country('Russia')


''' This is Fourth Function. '''
def list_func(items):
	for x in items:
		print(x)

trees = ['A', 'B', 'C']
list_func(trees)


''' This is Fiveth Function. '''
def multiply(x):
	return x * 5

print(multiply(3))
print(multiply(5))
print(multiply(9))


''' This is Sixth Function. '''
def drive(age):
	if age == 18:
		print('Make licence!')
	elif age > 18:
		print('You can drive!')
	else:
		print('You can\'t drive!')

drive(18)

''' This is Seventh Program. '''
cars = ['BMW_X7', 'Audi', 'Farrari', 'Aston']
print(len(cars))
cars.append('Ford')
print(cars)
cars.remove('Aston')
print(cars)
