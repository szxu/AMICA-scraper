# selenium 4
from selenium import webdriver
from selenium.webdriver.common.by import By

from datetime import date

from util.df_handler import DfHandler
from util.comment import Comment
from util.chrome_option_setter import ChromeOptionSetter

from scraper.util.text_segmenter import TextSegmenter
from scraper.util.time_retriever import Date_retriever
import chromedriver_autoinstaller as chromedriver


class MitUserScraper():
    def get_comment_content(self, c_driver, df, id, target):
        isend = False
        print(id)

        c_driver.get("https://www.mitbbs.com/article/" + str(target["cat_name"]) + "/" + str(id) + "_3.html")
        c_driver.implicitly_wait(0.01)

        news_bg_td = c_driver.find_element(By.XPATH, "//td[@class='news-bg']")
        center_td = news_bg_td.find_elements(By.TAG_NAME, "td")[-1]
        center_td_texts = center_td.text.split(",")
        time = center_td_texts[-1]

        year, month, day = Date_retriever.retrieve_date(time)
        comment_date = date(int(year), int(month), int(day))

        urls = center_td.find_elements(By.XPATH, "//a[@class='news' ]")
        comment_parent_url = urls[0].get_attribute('href')
        parent_id = int(
            comment_parent_url.replace("https://www.mitbbs.com/article_t/" + str(target["cat_name"]) + "/",
                                       "").replace(".html", ""))
        user_id = urls[2].text
        content = c_driver.find_element(By.XPATH, "//td[@class='jiawenzhang-type']")
        title = content.text.split("美东)")[0].split("标  题:")[-1].split("发信站:")[0]
        text = content.text.split("美东)")[-1].split("※ 来源")[0].replace("\n", "")
        segmented_text = ""  # TextSegmenter.seg(title + text)

        if parent_id == id:
            is_article = True
        else:
            is_article = False

        parent_title = ""
        parent_text = ""
        parent_user_id = 0
        website = "MIT"
        category = target["cat_name"]

        cur_comment = Comment(id, website, category, is_article, title, text, user_id, parent_id,
                              parent_title, parent_text, parent_user_id, time, segmented_text)
        cur_comment.print_comment()
        df = cur_comment.add_row(df)

        #isend = True

        return df, isend

    def get_list_of(self, os, u_driver, df, target):
        articles_tbody = u_driver.find_elements(By.ID, "userarticlediv")[0]
        articles = articles_tbody.find_elements(By.TAG_NAME, "tr")
        articles_dict = {}
        if len(articles) > 1:
            for i in range(1, len(articles)-2):
                article = articles[i]

                print(article.text)

                category = article.find_elements(By.TAG_NAME, "td")[2].text
                article_url = article.find_elements(By.TAG_NAME, "td")[1].find_elements(By.TAG_NAME, "a")[0].get_attribute('href')
                article_id = int(
                    article_url.replace("https://www.mitbbs.com/article_t/" + category + "/",
                                        "").replace(".html", ""))
                articles_dict[str(article_id)] = category

        for key in articles_dict:
            target["cat_name"] = articles_dict[key]
            article_id = int(key)
            try:
                chrome_options = os.set_options()
                c_driver = webdriver.Chrome(options=chrome_options)
                c_driver.set_page_load_timeout(10)
                df, isend = self.get_comment_content(c_driver, df, article_id, target)
                c_driver.quit()
                print("Finish Scraping Page " + str(article_id))
                if isend == True:
                    break
            except Exception as ex:
                print(ex)

        return df

    def get_user_page(self, df, target):
        os = ChromeOptionSetter()
        global chrome_options

        chrome_options = os.set_options()
        u_driver = webdriver.Chrome(options=chrome_options)
        u_driver.set_page_load_timeout(10)
        u_driver.refresh()
        user_id = target["user_id"]

        u_driver.get("https://www.mitbbs.com/user_info/" + user_id + "/")
        u_driver.implicitly_wait(0.5)

        # u_driver.execute_script("javascript:showarticle(2)")
        # u_driver.implicitly_wait(1)
        df = self.get_list_of(os, u_driver, df, target)

        u_driver.quit()

        return df

    def init(self, target):
        df = DfHandler.make_comment_df()
        df = self.get_user_page(df, target)

        return df

if __name__ == '__main__':
    target = {}
    target["user_id"] = 'hhcare'

    mus = MitUserScraper()
    df = mus.init(target)
    df.to_csv("/home/ktonxu/project/AMICA/AMICA-scraper/files/test/out.csv", index=False)

