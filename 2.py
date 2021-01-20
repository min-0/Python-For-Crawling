import requests
import json
from bs4 import BeautifulSoup

def get_blog_posts(id):

    print("<" + id + ">" + " 을(를) 파헤치자")

    url = data['tistory-left'] + id + data['tistory-right']
    req = requests.get(url)

    soup = BeautifulSoup(req.content, 'html.parser')

    res = soup.select('#mArticle > div > a.link_post > strong')

    if len(res) == 0:
        print("nothing")
    else:
        for i in res:
            print(i.contents[0])

def blogpost_scraping(data):

    for i in data['member']:
        get_blog_posts(i)


if __name__ == "__main__":

    with open('./data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    blogpost_scraping(data)