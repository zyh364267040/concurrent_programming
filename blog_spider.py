# -*- coding = utf-8 -*-
# @Time: 2021/8/30 下午9:40
"""
爬取博客园
"""
import requests
import bs4


# headers
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

# 博客园新闻页50页的url
urls = [
    f'https://news.cnblogs.com/n/page/{page}/'
    for page in range(1, 50+1)
]


def craw(url):
    r = requests.get(url=url, headers=headers)
    print(url, len(r.text))
    return r.text


def parse(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a', target="_blank")
    return [(link['href'], link.get_text()) for link in links]


if __name__ == '__main__':
    for result in parse(craw(urls[2])):
        print(result)
