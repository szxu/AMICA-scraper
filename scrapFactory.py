import settings
from scrapWXC import ScrapWXC
from scrapMIT import ScrapMIT
from scrapHR import ScrapHR

class ScrapFactory():
    def createScrap(name):
        if name == 'WXC':
            scrap = ScrapWXC()
        elif name == 'MIT':
            scrap = ScrapMIT()
        elif name == 'HR':
            scrap = ScrapHR()

        scrap.init()