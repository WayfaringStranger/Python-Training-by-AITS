n = int(input('Enter the number of lines: '))
chnum = 65
k = 2 * n - 2
for i in range(n):
	for j in range(k):
		print(end=' ')
	k = k - 1
	for j in range(i + 1):
		ch = chr(chnum)
		print(ch, end=' ')
		chnum = chnum + 1
	print('\r')
	
	
