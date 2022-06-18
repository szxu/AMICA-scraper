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
        # df = DfHandler.make_news_df()
        # cdf = DfHandler.make_comment_df()

        df, cdf = ScraperFactory.create_news_scraper(target)
        #result_df = DfHandler.append_df(running_df, df)

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

    def get_user_input(self, target):
        global BASE_PATH
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))

        # target = {
        #     "source_type_input": "",
        #     "web_name": "",
        #     "cat_name": "",
        #     "file_type": "",
        #     "year": "",
        #     "month": "",
        #     "day": ""
        # }

        # source_type_input = input("Please enter the type of source(News or Forum): ").lower()
        target["source_type_input"] = "news".lower()
        # webName = input("Please enter web name from (WXC, HR or MIT): ").upper()
        target["web_name"] = "WXC"
        # catName = input("Please enter category name from (morenews): ")
        target["cat_name"] = "morenews"
        target["file_type"] = "csv"
        target["year"] = "2022"
        #target["month"] = "06"
        print("Now scraping year/month: " + target["year"] + '/' + target["month"])

        if target["source_type_input"] == "news":
            self.scrap_news(target)
        elif target["source_type_input"] == "forum":
            self.scrap_forum(target)
        else:
            print("Please enter a valid source type!")


    def main(self):
        target = {
            "source_type_input": "",
            "web_name": "",
            "cat_name": "",
            "file_type": "",
            "year": "",
            "month": "",
            "day": ""
        }

        for i in range(5, 0, -1):
            target["month"] = '0' + str(i)
            self.get_user_input(target)


if __name__ == '__main__':
    m = Main()
    m.main()
