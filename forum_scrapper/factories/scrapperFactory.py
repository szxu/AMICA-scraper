from scrapper.wxcScrapper import WxcScrapper
from scrapper.mitScrapper import mitScrapper
from scrapper.hrScrapper import HrScrapper

class ScrapperFactory():
    def createScrap(wenName, catName):
        if wenName == 'WXC':
            scrapper = WxcScrapper()
        elif wenName == 'MIT':
            scrapper = mitScrapper()
        elif wenName == 'HR':
            scrapper = HrScrapper()

        scrapper.init(catName)