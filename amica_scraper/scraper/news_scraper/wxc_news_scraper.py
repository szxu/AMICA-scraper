# selenium 4
from selenium import webdriver
from selenium.webdriver.common.by import By

from util.chrome_option_setter import ChromeOptionSetter
from scraper.util.text_segmenter import TextSegmenter
from util.news import News
from util.comment import Comment
from util.df_handler import DfHandler


class WxcNewsScraper():
    def get_post_content(self, url, cdf, cur_news):
        p_driver = webdriver.Chrome()
        p_driver.refresh()
        p_driver.get(url)
        p_driver.implicitly_wait(0.5)

        source = p_driver.find_elements(By.ID, "postmeta")[0].find_elements(By.TAG_NAME, "span")[0].text
        text = p_driver.find_elements(By.ID, "articleContent")[0].text
        read_count = p_driver.find_elements(By.ID, "countnum")[0].text

        other_posts = p_driver.find_elements(By.CLASS_NAME, "otherposts")[0]

        divs = other_posts.find_elements(By.TAG_NAME, "div")
        div_count = len(divs)

        for i in range(4, div_count-4, 3):
            div = divs[i]
            p_driver.execute_script("arguments[0].style.display = 'block';", div)
            id = cur_news.id + '/' + div.get_attribute("id")
            website = cur_news.web
            category = cur_news.cat
            is_article = False
            title = ""
            parentid = cur_news.id
            parent_title = cur_news.title
            parent_text = ""
            parent_userid = source
            segmented_text = ""

            reply = div.find_elements(By.CLASS_NAME, "reply")[0].text.split(" 发表评论于 ")
            userid = reply[0]
            time = reply[1]

            comment_text = div.find_elements(By.CLASS_NAME, "summary")[0].text.replace("\n", " ")

            cur_comment = Comment(id, website, category, is_article, title, comment_text, userid, parentid,
                                 parent_title, parent_text, parent_userid, time, segmented_text)
            #curComment.print_comment()
            cdf = cur_comment.add_row(cdf)


        p_driver.close()
        return source, text, read_count, cdf

    def get_page_content(self, driver, df, cdf, page_num, target):
        driver.get("https://www.wenxuecity.com/news/" + str(target["cat_name"]) + "/?page=" + str(page_num))
        driver.implicitly_wait(0.5)

        posts = driver.find_elements(By.CLASS_NAME, "list")[0].find_elements(By.TAG_NAME, "li")
        for i in range(len(posts)):
            isend = False
            post = posts[i]
            post_url = post.find_elements(By.TAG_NAME, 'a')[0].get_attribute('href')
            title = post.find_elements(By.TAG_NAME, 'a')[0].text
            time = post.find_elements(By.TAG_NAME, 'span')[0].text
            id = post_url.split("/news/")[-1].replace(".html", "")
            year, month, day = time.split("-")
            if int(year) == int(target["year"]) and int(month) == int(target["month"]):
                website = "WXC"
                category = target["cat_name"]
                cur_news = News(id, website, category, title, "", "", time, "", "")

                source, text, read_count, cdf = self.get_post_content(post_url, cdf, cur_news)
                text = text.replace("\n", " ")
                segmented_text = ""#TextSegmenter.seg(title + text)

                cur_news = News(id, website, category, title, text, source, time, read_count, segmented_text)
                df = cur_news.add_row(df)

            if int(year) < int(target["year"]) or (int(year) == int(target["year"]) and int(month) < int(target["month"])):
                print("Ending because current month earlier than target month")
                isend = True
                break

            # if i >= 5:
            #     print("Ending because i >= 5")
            #     isend = True
            #     break
            print("Finish Scraping Post " + str(id))
        return df, cdf, isend

    def init(self, target):
        target["cat_name"] = input("Please enter category name from (morenews or ent): ")

        os = ChromeOptionSetter()
        global chromeOptions
        chromeOptions = os.set_options()

        driver = webdriver.Chrome(chrome_options=chromeOptions)
        driver.set_page_load_timeout(10)
        driver.refresh()

        df = DfHandler.make_news_df()
        cdf = DfHandler.make_comment_df()

        for i in range(1, 5000):
            try:
                df, cdf, isend = self.get_page_content(driver, df, cdf, i, target)
                if isend == True:
                    break
            except Exception as ex:
                print(ex)
            print("Finish Scraping Page " + str(i))

        driver.quit()

        return df, cdf
