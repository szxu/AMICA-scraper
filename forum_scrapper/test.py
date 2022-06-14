# selenium 4
import os
import pandas as pd
import json

from utils.df_handler import DfHandler
from scrapper.factories.scraper_factory import ScraperFactory


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
        file_type = "csv"
        df = DfHandler.make_news_df()

        if file_type == "csv":
            path = BASE_PATH + '/files/news/' + web_name + "_" + cat_name + '.csv'
            df = pd.read_csv(path)
        elif file_type == "json":
            path = BASE_PATH + '/files/news/' + web_name + "_" + cat_name + '.json'
            with open(path) as f:
                data = json.load(f)
            df = pd.DataFrame(data)
        else:
            print("error")

        id_list = DfHandler.get_ids(df)
        running_df = ScraperFactory.create_news_scraper(web_name, cat_name, id_list)
        result_df = DfHandler.append_df(running_df, df)

        if file_type == "csv":
            result_df.to_csv(path, mode = 'a', index=False)
        elif file_type == "json":
            result_df.to_json(path, orient='records')
        else:
            print("error")

    @staticmethod
    def scrap_forum():
        # webName = input("Please enter web name from (WXC, HR or MIT): ").upper()
        web_name = "HR"
        # catName = input("Please enter category name from (currentEvent or Chats or USANews, Military): ")
        cat_name = "Chats"
        file_type = "csv"

        if file_type == "csv":
            path = BASE_PATH + '/files/forum/' + web_name + "_" + cat_name + '.csv'
            #df = DfHandler.make_comment_df()
            df = pd.read_csv(path)
            #ScraperFactory.create_forum_scraper(web_name, cat_name)
            # ParentUpdater.init()
            df.to_csv(path, mode = 'a', index=False)
            #df.to_csv(path, index=False)
        elif file_type == "json":
            path = BASE_PATH + '/files/forum/' + web_name + "_" + cat_name + '.json'
            with open(path) as f:
                data = json.load(f)
            #df = DfHandler.make_comment_df()
            df = pd.DataFrame(data)
            # ScraperFactory.create_forum_scraper(web_name, cat_name, df)
            # ParentUpdater.init()
            df.to_json(path, orient='records')




    def main(self):
        global BASE_PATH
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        # source_type_input = input("Please enter the type of source(News or Forum): ").lower()
        source_type_input = "news".lower()

        if source_type_input == "news":
            self.scrap_news()
        elif source_type_input == "forum":
            self.scrap_forum()
        else:
            print("Please enter a valid source type!")

if __name__ == '__main__':
    m = Main()
    m.main()
