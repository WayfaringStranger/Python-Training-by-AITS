import random

infolist = ['Jay', 15, 'March', 1999, 'Purnima', 'Aghanu', 'Dhanbad', 826001, 'Jharkhand']

infodict = {'name': 'Jay', 'day': 15, 'month': 'March', 'year': 1999, 'mummy': 'Purnima', 'daddy': 'Aghanu', 'dist': 'Dhanbad', 'pin': 826001, 'state': 'Jharkhand'}

print(random.choice(infolist))
print(random.choice(list(infodict.values())))

