from scrapper.forum_scraper.wxc_scrapper import WxcScrapper
from scrapper.forum_scraper.mit_scrapper import MitScrapper
from scrapper.forum_scraper.hr_scrapper import HrScrapper
from scrapper.news_scraper.wxc_news_scraper import WxcNewsScrapper

class ScraperFactory():
    def create_forum_scraper(web_name, catName, id_list):
        if web_name == 'WXC':
            scraper = WxcScrapper()
        elif web_name == 'MIT':
            scraper = MitScrapper()
        elif web_name == 'HR':
            scraper = HrScrapper()

        scraper.init(catName, df)

    def create_news_scraper(target):
        if target["web_name"] == 'WXC':
            scraper = WxcNewsScrapper()

        return scraper.init(target)
