# List
numlist = [1,2,3,4,5]
numlist.reverse()
numlist.sort()

mystring = ‘parn’
list_name = list(mystring)

list_name[0]
list_name[2]

list_name.pop()
list_name.insert(5, ‘n’)

list_name[0] = ‘P’

del list_name[0]
list_name.insert(0, ‘PP’)

list_name.pop(0)

list_name.append(‘!’)

# Tuple
mystr = ‘parn’

l = list(mystr)
t = tuple(mystr)

l[0] = ‘P’
t[0] = ‘P’ # Will error

for letter in l:
    print(letter)

for letter in t:
    print(letter)

# Dict
user = {‘name’: ‘parn’, ‘age’: 24}

people = {}
people[‘parn’] = 24
people[‘presso’] = 42

people.keys()
people.values()
people.items()

for key in people.keys():
    print(key)

for value in people.values():
    print(value)

for key, value in people.items():
    print(f’{key} is {str(value)}’)

