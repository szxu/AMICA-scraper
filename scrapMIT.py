# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
import pandas as pd
from IPython.display import display

import settings
from textSeg import TextSeg
from comment import Comment

class ScrapMIT():
    def getCommentContent(self, commentNum):
        #print(commentNum)
        if any(settings.__CDF__["Comment ID"] == commentNum):
            return
        driver.get("https://www.mitbbs.com/article/Military/" + str(commentNum) + "_3.html")
        driver.implicitly_wait(0.5)

        id = commentNum

        news_bg_td = driver.find_element(By.XPATH, "//td[@class='news-bg']")
        center_td = news_bg_td.find_elements(By.TAG_NAME, "td")[-1]
        center_td_texts = center_td.text.split(",")
        time = center_td_texts[-1]
        urls = center_td.find_elements(By.XPATH, "//a[@class='news' ]")
        commentParentUrl = urls[0].get_attribute('href')
        parentId = int(commentParentUrl.replace("https://www.mitbbs.com/article_t/Military/", "").replace(".html", ""))
        userId = urls[2].text
        title = ""
        text = driver.find_element(By.XPATH, "//td[@class='jiawenzhang-type']").text.split("美东)")[-1].split("※ 来源")[0].replace("\n", "")
        segmentedText = TextSeg.seg(title + text)

        if parentId == id:
            parentId = 0
            isArticle = True
        else:
            isArticle = False

        parentTitle = ""
        parentText = ""
        parentUserId = 0
        website = "Mit"
        category = "military"

        curComment = Comment(id, website, category, isArticle, title, text, userId, parentId,
                             parentTitle, parentText, parentUserId, time, segmentedText)
        curComment.addToDf()

    def init(self):
        service = Service(executable_path=ChromeDriverManager().install())
        option = webdriver.ChromeOptions()
        chrome_prefs = {}
        option.experimental_options["prefs"] = chrome_prefs
        chrome_prefs["profile.default_content_settings"] = {"images": 2}
        chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}

        global driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()),
                                  chrome_options=option)
        driver.refresh()
        for i in range(64591479, 64590367, -2):
            try:
                self.getCommentContent(i)
            except:
                continue

        driver.quit()
