# selenium 4

import pandas as pd

from utils.df_handler import ParentUpdater
from utils.settings import GlobalVariables
from scrapper.factories.scraper_factory import ScraperFactory

class Main():
    """
    Run scraper.
    """

    @staticmethod
    def scrap_news():
        web_name = input("Please enter web name from (WXC, HR or MIT): ").upper()
        cat_name = input("Please enter category name from (morenews): ")

        GlobalVariables.init()
        GlobalVariables.__NDF__ = pd.read_csv(
            '/home/ktonxu/project/coen493/Misinfo Analysis/forum_scrapper/csv_files/news/' + web_name + "_" + cat_name + '.csv')
        ScraperFactory.create_news_scraper(web_name, cat_name)
        ParentUpdater.init()

        GlobalVariables.__NDF__.to_csv(
            '/home/ktonxu/project/coen493/Misinfo Analysis/forum_scrapper/csv_files/news/' + web_name + "_" + cat_name + '.csv',
            index=False)

    @staticmethod
    def scrap_forum():
        web_name = input("Please enter web name from (WXC, HR or MIT): ").upper()
        cat_name = input("Please enter category name from (currentEvent or Chats or USANews, Military): ")

        DataFrameMaker
        GlobalVariables.__CDF__ = pd.read_csv('forum_scrapper/csv_files/forum/' + web_name + "_" + cat_name + '.csv')
        ScraperFactory.create_forum_scraper(web_name, cat_name)
        ParentUpdater.init()

        GlobalVariables.__CDF__.to_csv('forum_scrapper/csv_files/forum/' + web_name + "_" + cat_name + '.csv',
                                       index=False)


    def main(self):
        # source_type_input = input("Please enter the type of source(News or Forum): ").upper()
        source_type_input = "FORUM".lower()

        if source_type_input == "news":
            self.scrap_news()
        elif source_type_input == "forum":
            self.scrap_forum()
        else:
            print("Please enter a valid source type!")



if __name__ == '__main__':
    Main.main()





