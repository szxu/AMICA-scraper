# selenium 4

import pandas as pd

from utils.parentUpdater import ParentUpdater
from utils.settings import GlobalVariables
from factories.scrapperFactory import ScrapperFactory

if __name__ == '__main__':
    #webName = input("Please enter web name from (WXC, HR or MIT): ").upper()
    webName = "WXC"
    #catName = input("Please enter web name from (currentEvent or Chats or USANews, Military): ")
    catName = "currentEvent"

    GlobalVariables.__CDF__ = pd.read_csv('forum_scrapper/csv_files/' + webName + "_" + catName + '.csv')
    ScrapperFactory.createScrap(webName, catName)
    ParentUpdater.init()

    #print(Settings.commentsDf.dtypes)
    #display(Settings.commentsDf)

    GlobalVariables.__CDF__.to_csv('forum_scrapper/csv_files/' + webName + "_" + catName + '.csv', index=False)




