import requests
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/top250?start='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.97 Safari/537.36 Core/1.116.537.400 QQBrowser/19.4.6561.400'
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
for item in soup.find_all('div', class_='item'):
    rank = item.em.text
    title = item.find('span', class_='title').text
    info = item.find('div', class_='bd').p.text.strip().replace('\n', '').replace(' ', '')
    rate = item.find('span', property='v:average').text
    print(f'排名:{rank},标题:{title} , 简介:{info}, 评分:{rate}')
