meals = {'Tea': 10, 'Pizza': 100, 'Samosa': 10, 'Coffee': 20, 'Ice-Cream': 30}

for item in meals:
	print(item, end=' ')


def resaurent():
	total_cost = 0
	while(True):
		meal_name = input('\nEnter meal name for buy them or q for Quit: ')
		if meal_name in meals:
			meal_quantity = int(input('Enter meal quantity: '))
			total_cost = total_cost + (meals[meal_name] * meal_quantity)
			
		elif meal_name == 'q':
			print(f'Total Cost is {total_cost}!')
			break

		else:
			print('Enter Correct meal name or Quit Key!')


if __name__ == "__main__":
	resaurent()
			
	
