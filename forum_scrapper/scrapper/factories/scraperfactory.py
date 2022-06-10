from scrapper.forum_scraper.wxc_scrapper import WxcScrapper
from scrapper.forum_scraper.mit_scrapper import MitScrapper
from scrapper.forum_scraper.hr_scrapper import HrScrapper
from scrapper.news_scraper.wxc_news_scraper import WxcNewsScrapper

class ScraperFactory():
    def create_forum_scraper(wenName, catName):
        if wenName == 'WXC':
            scrapper = WxcScrapper()
        elif wenName == 'MIT':
            scrapper = MitScrapper()
        elif wenName == 'HR':
            scrapper = HrScrapper()

        scrapper.init(catName)

    def create_news_scraper(wenName, catName):
        if wenName == 'WXC':
            scrapper = WxcNewsScrapper()

        scrapper.init(catName)