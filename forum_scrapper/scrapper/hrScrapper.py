# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

from utils.optionSetter import OptionSetter
from utils.settings import GlobalVariables
from utils.textSegmenter import TextSegmenter
from utils.comment import Comment

class HrScrapper():
    def getPageContent(self, driver, pageNum, catNum):
        driver.get("https://huaren.us/showtopic.html?topicid=" + str(pageNum) + "&fid=" + str(catNum))
        commentList = driver.find_element(By.CLASS_NAME, "post-list")
        comments = commentList.find_elements(By.CLASS_NAME, "post-item")
        parentTitle = ""
        parentId = 0

        for i in range(len(comments)):
            comment = comments[i]

            id = int(comment.get_attribute("id"))
            userId = comment.find_element(By.CLASS_NAME, "post-user").find_element(By.CLASS_NAME, "avatar-wrap").get_attribute('href').replace("https://huaren.us/userinfo.html?uid=", "")
            content = comment.find_element(By.CLASS_NAME, "post-content").text
            time = comment.find_element(By.CLASS_NAME, "post-top-action").text.split("发表于：")[1].split("|只看")[0]

            if i == 0:
                parentId = id
                isArticle = True
                parentTitle = comment.find_element(By.CLASS_NAME, "post-content").find_element(By.CLASS_NAME, "topic-title").text
                text = content.split(parentTitle)[-1]
            else:
                isArticle = False
                text = content

            title = parentTitle
            segmentedText = TextSegmenter.seg(title + text)

            parentText = ""
            parentUserId = ""
            website = "HR"
            category = _CAT_NAME

            curComment = Comment(id, website, category, isArticle, title, text, userId, parentId,
                             parentTitle, parentText, parentUserId, time, segmentedText)

            curComment.addToDf()


    def init(self, catName):
        os = OptionSetter()
        global chromeOptions
        chromeOptions = os.setOption()

        driver = webdriver.Chrome(chrome_options=chromeOptions)
        driver.set_page_load_timeout(10)

        global _CAT_NAME
        _CAT_NAME = catName

        if catName == "Chats":
            catNum = 398
        else:
            catNum = 0

        for i in range(2812616, 2812606, -1):
            if any(GlobalVariables.__CDF__["Comment ID"] == i):
                continue
            else:
                try:
                    self.getPageContent(driver, i, catNum)
                except:
                    continue
        driver.quit()






    # def getPageContent(self, driver, pageNum, catNum):
    #     driver.get("https://huaren.us/showforum.html?forumid=" + str(catNum) + "&page=" + str(pageNum) + "&order=tid")
    #     driver.implicitly_wait(0.5)
    #     posts = driver.find_elements(By.CLASS_NAME, "hr-topic")
    #     for postIdx in range(4, len(posts)):
    #         links = posts[postIdx].find_elements(By.TAG_NAME, 'a')
    #         commentUrl = links[0].get_attribute('href')
    #         self.getCommentContent(commentUrl)