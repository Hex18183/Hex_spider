import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0"}
movies = []
url = f"https://movie.douban.com/top250?start="
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')

for item in soup.find_all("div", class_="item"):
    title = item.find("span", class_="title").text
    rating = item.find("span", class_="rating_num").text
    info = item.find("div", class_="bd").p.text.replace("\n", "").replace("\xa0", "").replace(" ", "").strip()
    movies.append({
        "排名": len(movies) + 1,
        "电影名称": title,
        "评分": rating,
        "详情": info
    })
for key in range(len(movies)+1):
    print(movies[key])

