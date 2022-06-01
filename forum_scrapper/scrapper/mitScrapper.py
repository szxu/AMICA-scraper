# selenium 4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException
)

from utils.settings import GlobalVariables
from utils.textSegmenter import TextSegmenter
from utils.comment import Comment
from utils.optionSetter import OptionSetter

class mitScrapper():
    def getCommentContent(self, driver, commentNum, catName):
        #print(commentNum)

        driver.get("https://www.mitbbs.com/article/" + str(catName) + "/" + str(commentNum) + "_3.html")
        driver.implicitly_wait(0.5)

        id = commentNum
        news_bg_td = driver.find_element(By.XPATH, "//td[@class='news-bg']")
        center_td = news_bg_td.find_elements(By.TAG_NAME, "td")[-1]
        center_td_texts = center_td.text.split(",")
        time = center_td_texts[-1]
        urls = center_td.find_elements(By.XPATH, "//a[@class='news' ]")
        commentParentUrl = urls[0].get_attribute('href')
        parentId = int(commentParentUrl.replace("https://www.mitbbs.com/article_t/" + str(catName) + "/", "").replace(".html", ""))
        userId = urls[2].text
        content = driver.find_element(By.XPATH, "//td[@class='jiawenzhang-type']")
        title = content.text.split("美东)")[0].split("标  题:")[-1].split("发信站:")[0]
        text = content.text.split("美东)")[-1].split("※ 来源")[0].replace("\n", "")
        segmentedText = TextSegmenter.seg(title + text)

        if parentId == id:
            isArticle = True
        else:
            isArticle = False

        parentTitle = ""
        parentText = ""
        parentUserId = 0
        website = "MIT"
        category = catName

        curComment = Comment(id, website, category, isArticle, title, text, userId, parentId,
                             parentTitle, parentText, parentUserId, time, segmentedText)
        curComment.addToDf()

    def init(self, catName):
        os = OptionSetter()
        chromeOptions = os.setOption()

        driver = webdriver.Chrome(chrome_options = chromeOptions)
        driver.set_page_load_timeout(10)

        for i in range(64644917, 64644817, -2):
            if any(GlobalVariables.__CDF__["Comment ID"] == i):
                continue
            else:
                try:
                    self.getCommentContent(driver, i, catName)
                except:
                    continue
        #TimeoutException or NoSuchElementException
        driver.quit()
