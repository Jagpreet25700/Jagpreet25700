import requests
from bs4 import BeautifulSoup
url=  'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

response = requests.get(url)
response.encoding = 'utf-8'  # ensure correct decoding
website_html = response.text

soup = BeautifulSoup(website_html,"html.parser")

all_movies = soup.find_all(name = "h3",class_ = "title")
#print(all_movies)
movies_title = [movie.getText() for movie in all_movies]

#for n in range(len(movies_title) -1,-1,-1):
#    print(movies_title[n])

movies = movies_title[::-1]

with open("100_movies_project/movies.txt",mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
