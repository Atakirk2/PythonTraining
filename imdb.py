import requests
from bs4 import BeautifulSoup

url =  "https://www.imdb.com/chart/top/"

response = requests.get(url)

content = response.content

soup = BeautifulSoup(content, "html.parser")

titles = soup.find_all("td", {"class": "titleColumn"})

ratings = soup.find_all("td", {"class", "ratingColumn imdbRating"})

for title, rating in zip(titles, ratings):
    title = title.text
    rating = rating.text

    title = title.strip()
    rating = rating.strip()

    title = title.replace("\n", "")
    rating = rating.replace("\n", "")
    print(title, " Rating: ",end='')
    print(rating)
