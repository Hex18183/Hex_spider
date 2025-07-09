from bs4 import BeautifulSoup
import requests


def get_movies():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3883.400 QQBrowser/10.8.4559.400"
        , "Host": "movie.douban.com"}
    movie_list = []

    for i in range(0, 10):  # 每页25部 循环10次
        link = "https://movie.douban.com/top250?start=" + "str(i*25)"
        r = requests.get(link, headers=headers, timeout=10)
        print("第", str(i + 1), "页,响应码：", r.status_code)

        soup = BeautifulSoup(r.text, "lxml")  # lxml改成了html.parser
        div_list = soup.find_all("div", class_="hd")

        for each in div_list:
            movie = each.a.span.text.strip()
            movie_list.append(movie)
    return movie_list


movies = get_movies()
print(movies)
