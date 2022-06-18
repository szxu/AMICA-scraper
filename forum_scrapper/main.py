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
    def scrap_news(target):
        df, cdf = ScraperFactory.create_news_scraper(target)
        filename = target["web_name"] + "_" + target["cat_name"] + "_" + target["year"] + "_" + target["month"]

        if target["file_type"] == "csv":
            path = BASE_PATH + '/files/news/' + filename + '.csv'
            df.to_csv(path, index=False)
            c_path = BASE_PATH + '/files/news/' + filename + '_comments' + '.csv'
            cdf.to_csv(c_path, index=False)
        elif target["file_type"] == "json":
            path = BASE_PATH + '/files/news/' + filename + '.json'
            df.to_json(path, orient='records')
            c_path = BASE_PATH + '/files/news/' + filename + '_comments' + '.json'
            cdf.to_json(c_path, orient='records')
        else:
            print("error")

    @staticmethod
    def scrap_forum(target):
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

        target = {
            "source_type_input": "",
            "web_name": "",
            "cat_name": "",
            "file_type": "",
            "year": "",
            "month": "",
            "day": ""
        }

        target["source_type_input"] = input("Please enter the type of source(News or Forum): ").lower()
        target["web_name"] = input("Please enter web name from (WXC, HR or MIT): ").upper()
        target["cat_name"] = input("Please enter category name from (morenews or currentEvent or Chats or USANews, Military): ")
        target["file_type"] = input("Please enter the export file type (csv or json): ")
        target["year"] = input("Please enter the year ex. 2022: ")
        target["month"] = input("Please enter the month ex. 06: ")
        print("Now scraping year/month: " + target["year"] + '/' + target["month"])

        if target["source_type_input"] == "news":
            self.scrap_news(target)
        elif target["source_type_input"] == "forum":
            self.scrap_forum(target)
        else:
            print("Please enter a valid source type!")



if __name__ == '__main__':
    m = Main()
    m.main()
