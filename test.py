import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.97 Safari/537.36 Core/1.116.537.400 QQBrowser/19.4.6561.400'
}
url = 'https://movie.douban.com/top250?start='

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'lxml')

item=soup.find_all('div', class_='item')

for i in item:
    rank=i.find('em').text
    title=i.find('span', class_='title').text
    info=i.find('p').text.strip().replace('\n', '').replace(' ', '')
    rate=i.find('span', class_='rating_num').text
    print(f"排名：{rank} 标题：{title} \t评分：{rate} \t简介：{info}")

