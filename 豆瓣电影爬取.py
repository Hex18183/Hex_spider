import requests
from bs4 import BeautifulSoup
import csv
import time
import random


def scrape_douban():
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
        print(movies)

    # for i in range(0, 250, 25):
    #     url = f"https://movie.douban.com/top250?start={i}"
    #     response = requests.get(url, headers=headers)
    #     soup = BeautifulSoup(response.text, "html.parser")
    #
    #     for item in soup.find_all("div", class_="item"):
    #         title = item.find("span", class_="title").text
    #         rating = item.find("span", class_="rating_num").text
    #         year = item.find("p").text.split("/")[-1].strip()[:4]
    #         movies.append({
    #             "排名": len(movies) + 1,
    #             "电影名称": title,
    #             "评分": rating,
    #             "年份": year
    #         })
    #     time.sleep(random.uniform(2, 5))  # 防止被封
    #
    # # 保存为CSV
    # with open("douban_top250.csv", "w", newline="", encoding="utf-8-sig") as f:
    #     writer = csv.DictWriter(f, fieldnames=["排名", "电影名称", "评分", "年份"])
    #     writer.writeheader()
    #     writer.writerows(movies)


scrape_douban()
