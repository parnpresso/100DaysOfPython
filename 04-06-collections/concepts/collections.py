from collections import defaultdict, deque, namedtuple, Counter

# Tuple
user = ('parn', 'handsome')
print(f'My name is {user[0]}, and I am {user[1]}')

# Named tuple
User = namedtuple('User', 'name status')
user_parn = User(name='Parnpresso', status='Single')
print(user_parn)
print(user_parn[0])
print(user_parn[1])
print(user_parn.name)
print(user_parn.status)

# Dict
user = {'name': 'parn'}
print(user['name'])
print(user.get('name'))  # Safer

# Default dict
users = [
    ('parn', 3),
    ('gap', 2),
    ('pae', 5),
    ('parn', 7),
]

users_sum = defaultdict(list)
for name, amount in users:
    users_sum[name].append(amount)

print(users_sum)


# Counter
text = 'Hello, My name is parn, aka Parnpresso. Parn is my name.'
print(Counter(text).most_common(5))


# Deque
lst = list(range(10000000))
deq = deque(range(10000000))
