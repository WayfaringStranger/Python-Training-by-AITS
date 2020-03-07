# Question 1

import random 

r = random.randint(100, 999)

print(r)

s = 0
for _ in range(3):
	s += r % 10
	r //= 10
	
print(f'Sum of Ques! {s}')

# Question 2

s = "AGCS"

c = "AITS"

print(s.replace(s[1], c[1]))

# Question 3
string = "hello20"

for i in string:
	if(i.isdigit()):
		print(i)


# Question 4

digits = [9.5, 3.8, 2.7, 17.0]

print(max(digits))

# Question 5

string = "HackerRank"
countL = 0
countU = 0

for i in string:
	if(i.islower()):
		countL += 1
	if(i.isupper()):
		countU += 1

print((countL * 100) / len(string))
print((countU * 100) / len(string))
	

# Question 6

string = input()
revstring = string[::-1]

if string == revstring:
	print("Y")
else:
	print("N")
	
