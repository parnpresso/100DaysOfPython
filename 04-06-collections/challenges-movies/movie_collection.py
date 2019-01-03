import requests
from collections import defaultdict, namedtuple, Counter


Movie = namedtuple('Movie', 'title year score')
directors = defaultdict(list)

url = 'https://raw.githubusercontent.com/sundeepblue/movie_rating_prediction/master/movie_metadata.csv'
data = requests.get(url)

movies = data.text.split('\r\n')

for movie in movies:
    detail = movie.split(',')

    try:
        director = detail[1]
        title = detail[11].replace('\xa0', '')
        year = detail[-5]
        score = detail[-3]
    except:
        continue

    m = Movie(title=title, year=year, score=score)
    directors[director].append(m)

print(directors['Christopher Nolan'])

cnt = Counter()
for director, movies in directors.items():
    cnt[director] += len(movies)

print(cnt.most_common(5))
