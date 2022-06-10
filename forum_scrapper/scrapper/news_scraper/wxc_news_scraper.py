# selenium 4
from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.chrome_option_setter import ChromeOptionSetter
from scrapper.util.text_segmenter import TextSegmenter
from utils.news import News

class WxcNewsScrapper():
    def getCommentContent(self, id):
        c_driver = webdriver.Chrome()
        c_driver.refresh()
        c_driver.get("https://bbs.wenxuecity.com/currentevent/" + str(id) + ".html")
        c_driver.implicitly_wait(0.5)
        text = c_driver.find_elements(By.XPATH, "//div[@id='postbody']")[0].text

        c_driver.close()
        return text

    def get_post_content(self, url):
        p_driver = webdriver.Chrome()
        p_driver.refresh()
        p_driver.get(url)
        p_driver.implicitly_wait(0.5)

        source = p_driver.find_elements(By.ID, "postmeta")[0].find_elements(By.TAG_NAME, "span")[0].text
        text = p_driver.find_elements(By.ID, "articleContent")[0].text

        p_driver.close()
        return source, text

    def get_page_content(self, driver, pageNum, catName):
        driver.get("https://www.wenxuecity.com/news/" + str(catName) + "/?page=" + str(pageNum))
        driver.implicitly_wait(0.5)

        posts = driver.find_elements(By.CLASS_NAME, "list")[0].find_elements(By.TAG_NAME, "li")
        for post in posts:

            post_url = post.find_elements(By.TAG_NAME, 'a')[0].get_attribute('href')
            title = post.find_elements(By.TAG_NAME, 'a')[0].text
            time = post.find_elements(By.TAG_NAME, 'span')[0].text
            id = post_url.split("/news/")[-1].replace(".html", "")

            text, source = self.get_post_content(post_url)

            segmented_text = TextSegmenter.seg(title + text)
            website = "WXC"
            category = catName

            cur_news = News(id, website, category, title, text, source, time, segmented_text)
            cur_news.addToDf()


    def init(self, cat_name):
        os = ChromeOptionSetter()
        global chromeOptions
        chromeOptions = os.set_options()

        driver = webdriver.Chrome(chrome_options=chromeOptions)
        driver.set_page_load_timeout(10)
        driver.refresh()

        for i in range(1, 2):
            try:
                self.get_page_content(driver, i, cat_name)
            except Exception as ex:
                print(ex)
                continue

        driver.quit()