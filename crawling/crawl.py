from naver import NaverWebtoonCrawler

webtoon_id_yumi = 651673
crawler = NaverWebtoonCrawler(webtoon_id_yumi)
crawler.crawl_episode(1)