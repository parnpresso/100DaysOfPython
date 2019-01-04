from collections import defaultdict, namedtuple


Interest = namedtuple('interest', 'bank_name rate')
interests = defaultdict(list)

interest_raw_data = [
  {'bank_name': 'Kasikorn', 'rate': '0.90%'},
  {'bank_name': 'SCB', 'rate': '1.00%'},
  {'bank_name': 'Bangkok', 'rate': '0.50%'},
  {'bank_name': 'Krungsri', 'rate': '0.80%'},
]

for interest in interest_raw_data:
    interest_tupled = Interest(
        bank_name=interest.get('bank_name'),
        rate=interest.get('rate'),
    )
    interests[interest_tupled.bank_name].append(interest_tupled)

print(interests['Kasikorn'])
