import requests
from bs4 import BeautifulSoup

url_naver_webtoon_episode_list = 'http://comic.naver.com/webtoon/list.nhn'
params_webtoon_episode_list = {
    'titleId': '651673',
    'weekday': 'wed',
}


def get_html_from_url(url, params):
    response = requests.get(url, params)
    return response.text


html = get_html_from_url(url_naver_webtoon_episode_list, params_webtoon_episode_list)

soup = BeautifulSoup(html, 'lxml')

div_comicinfo = soup.find('div', class_='comicinfo')

div_comicinfo_detail = div_comicinfo.find('div', class_='detail')

title = div_comicinfo_detail_h2 = div_comicinfo_detail.find('h2')

div_comicinfo_detail_h2_wrt_nm = div_comicinfo_detail_h2.find('span', class_='wrt_nm')
author_name = div_comicinfo_detail_h2.text.strip()

# print(div_comicinfo_detail_h2.contents[0].strip())
print(author_name)
