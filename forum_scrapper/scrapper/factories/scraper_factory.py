from scrapper.forum_scraper.wxc_scrapper import WxcScrapper
from scrapper.forum_scraper.mit_scrapper import MitScrapper
from scrapper.forum_scraper.hr_scrapper import HrScrapper
from scrapper.news_scraper.wxc_news_scraper import WxcNewsScrapper

class ScraperFactory():
    def create_forum_scraper(wenName, catName, id_list):
        if wenName == 'WXC':
            scraper = WxcScrapper()
        elif wenName == 'MIT':
            scraper = MitScrapper()
        elif wenName == 'HR':
            scraper = HrScrapper()

        scraper.init(catName, df)

    def create_news_scraper(wenName, catName, id_list):
        if wenName == 'WXC':
            scraper = WxcNewsScrapper()

        return scraper.init(catName, id_list)
