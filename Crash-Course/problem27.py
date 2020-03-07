# Filling an array with random numbers

import random
arr = []
for _ in range(10):
	arr.append(random.randrange(0, 10))

print(arr)

# Finding the minimum and maximum elements of in an array

print(min(arr))
print(max(arr))

# How many odd and even numbers in the list?

lst = arr

for i in lst:
	if i % 2 == 0:
		print(f'{i} is even.')
	else:
		print(f'{i} is odd.')

# Separate positive numbers from negative

numbers = [1, -2, -3, 4, 8, 9, -7]
pos = []
neg = []
for i in numbers:
	if i > 0:
		pos.append(i)
	else:
		neg.append(i)

print(pos)
print(neg)

# Output the items that are larger thatn the arithemetic mean of array

array = arr
mean = sum(array) / len(array)
largers = []
for i in array:
	if i > mean:
		largers.append(i)

print(mean)
print(largers)
		
# The amount of the elements whose values belong to the specified range

amount = 0
for i in range(0, 10):
	amount += i

print(amount)

# The distribution of values by range

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Replacing list items

lst1 = ['one', 'seven', 'three', 'five']
lst2 = [1, 7, 3, 5]

# Checking a file extension

# Find the longest word in a string

string = "find the longest word in a string"
strlst = string.split()
print(max(strlst, key=len))
	
# Convert text to a word list with punctuation removed

text = 'Hi! How is going the training of Python?'

# Intersection of lists. find the same items from two lists

lst1 = [2, 3, 4]
lst2 = [3, 4, 5]
sameItems = set(lst1).intersection(set(lst2))
print(list(sameItems))
