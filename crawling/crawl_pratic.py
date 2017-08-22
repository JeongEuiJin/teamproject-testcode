import requests
from bs4 import BeautifulSoup

url_naver_webtoon_episode_list = 'http://comic.naver.com/webtoon/list.nhn'

titleId_goh = '318995'  # god of highschool
titleId_ym = '651673'  # 유미 세포
titleId_gosu = '662774'  # 고수
params_webtoon_episode_list = {
    'titleId': titleId_gosu,
    'page': 3
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


# author_name = div_comicinfo_detail_h2.text.strip()
#
# # print(div_comicinfo_detail_h2.contents[0].strip())
# print(author_name)

# title = soup.select_one('div.comicinfo > div.detail > h2').contents[0].strip()
# author_name = soup.select_one('div.comicinfo > div.detail > h2 > span').text.strip()
# print(title)




episode_list = []

# tr_list = soup.select('table.viewList > tr')
# for tr in tr_list:
#     print(tr.text)
# str.upper()

table = soup.find('table', class_='viewList')
tr_list = table.find_all('tr')
for tr in tr_list:
    if not tr.find('td', class_='title'):
        continue
    title = tr.find('td', class_='title').find('a').text
    link = tr.find('td', class_='title').find('a')['href']
    rating = tr.find_all('td')[2].find('strong').text
    date = tr.find('td', class_='num').text
    print(title)
    print(link)
    print(rating)
    print(date)
