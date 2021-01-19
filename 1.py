
# 목표는, 멤버들 블로그 전체 게시글 가져오기
# 아이디를 넣으면, 그 아이디의 블로그 전체 게시글 제목들을 가져오는 함수 구현

import requests
import json
from bs4 import BeautifulSoup

def get_blog_posts(id):
    url = data['tistory-left'] + id + data['tistory-right']
    req = requests.get(url)
    
    soup = BeautifulSoup(req.content, 'html.parser')

    res = soup.select('#mArticle > div > a.link_post > strong')

    for i in res:
        print(i.contents[0])
      
""" # def blogpost_crawling(data):
#     for i in data['member']:
#         get_blog_posts(i) """

if __name__ == "__main__":
    
    with open('./data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    get_blog_posts(data['member'][0])