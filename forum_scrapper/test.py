# selenium 4
import os
import pandas as pd
import json

from utils.parent_updater import ParentUpdater
from utils.settings import GlobalVariables
from utils.dataframe_maker import DataFrameMaker
from scrapper.factories.scraperfactory import ScraperFactory


class Main():
    """
    Run scraper.
    """

    @staticmethod
    def scrap_news():
        # webName = input("Please enter web name from (WXC, HR or MIT): ").upper()
        web_name = "WXC"
        # catName = input("Please enter category name from (morenews): ")
        cat_name = "morenews"

        GlobalVariables.init()
        GlobalVariables.__NDF__ = pd.read_csv(
            '/home/ktonxu/project/coen493/Misinfo Analysis/forum_scrapper/files/news/' + web_name + "_" + cat_name + '.csv')
        ScraperFactory.create_news_scraper(web_name, cat_name)
        # ParentUpdater.init()

        # print(Settings.commentsDf.dtypes)
        # display(Settings.commentsDf)

        GlobalVariables.__NDF__.to_csv('/home/ktonxu/project/coen493/Misinfo Analysis/forum_scrapper/files/news/' + web_name + "_" + cat_name + '.csv', index=False)

    @staticmethod
    def scrap_forum():
        # webName = input("Please enter web name from (WXC, HR or MIT): ").upper()
        web_name = "HR"
        # catName = input("Please enter category name from (currentEvent or Chats or USANews, Military): ")
        cat_name = "Chats"
        file_type = "csv"
        path = ""
        if file_type == "csv":
            path = BASE_PATH + '/files/forum/' + web_name + "_" + cat_name + '.csv'
            df = DataFrameMaker.make_comment_df()
            df = pd.read_csv(path)
            #ScraperFactory.create_news_scraper(web_name, cat_name)
            # ParentUpdater.init()
            df.to_json(BASE_PATH + '/files/forum/' + web_name + "_" + cat_name + '.json', orient='records')
            #df.to_csv(path, index=False)
        elif file_type == "json":
            path = BASE_PATH + '/files/forum/' + web_name + "_" + cat_name + '.json'
            with open(path) as f:
                data = json.load(f)
            #df = DataFrameMaker.make_comment_df()
            df = pd.DataFrame(data)
            # ScraperFactory.create_forum_scraper(web_name, cat_name, df)
            # ParentUpdater.init()
            df.to_json(path, orient='records')




    def main(self):
        global BASE_PATH
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        # source_type_input = input("Please enter the type of source(News or Forum): ").lower()
        source_type_input = "FORUM".lower()

        if source_type_input == "news":
            self.scrap_news()
        elif source_type_input == "forum":
            self.scrap_forum()
        else:
            print("Please enter a valid source type!")

if __name__ == '__main__':
    m = Main()
    m.main()
