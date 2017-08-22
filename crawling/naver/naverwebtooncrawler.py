import os

__all__ = (
    'NaverWebtoon',
    'NaverWebtoonCrawler',
)

class NaverWebtoonCrawler:
    _url_datail_base = 'http://comic.naver.com/webtoon/detail.nhn?' \
                       'titleId={webtoon_id}&' \
                       'no={episode_num}'

    def __init__(self, webtoon_id):
        self.webtoon_id = webtoon_id

    def crawl_page(self, page_num):
        return ''

    def crawl_episode(self, episode_num=None):
        if not episode_num:
            url_detail = self._url_datail_base.format(
                self.webtoon_id
            )
        else:
            url_detail = self._url_datail_base.format(
                webtoon_id=self.webtoon_id,
                episode_num=episode_num
            )
        os.makedirs('{]/{}'.format(self.webtoon_id, episode_num))
        return ''

    def crawl_all_episode(self):
        return ''


class NaverWebtoon:
    def __init__(self, url_thumbnail, title, rating, date):
        self._url_thumbnail = url_thumbnail
        self._title = title
        self._rating = rating
        self._date = date

    @property
    def url_thumbnail(self):
        return self._url_thumbnail

    @property
    def title(self):
        return self._title

    @property
    def rating(self):
        return self._rating

    @property
    def date(self):
        return self._date
