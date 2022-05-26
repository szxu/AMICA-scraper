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

class ScrapWXC():
    def getCommentContent(self, id):
        global cDriver
        cDriver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()), chrome_options=option)
        cDriver.refresh()
        cDriver.get("https://bbs.wenxuecity.com/currentevent/" + str(id) + ".html")
        cDriver.implicitly_wait(0.5)

        text = cDriver.find_elements(By.XPATH, "//div[@id='postbody']")[0].text

        cDriver.close()
        return text

    def getPageContent(self, pageNum):
        driver.get("https://bbs.wenxuecity.com/currentevent/?page=" + str(pageNum))
        driver.implicitly_wait(0.5)
        posts = driver.find_elements(By.CLASS_NAME, "odd") + driver.find_elements(By.CLASS_NAME, "even")
        for post in posts:
            comments = post.find_elements(By.TAG_NAME, 'p')
            parentId = 0
            for i in range(len(comments)):
                comment = comments[i]
                links = comment.find_elements(By.TAG_NAME, 'a')
                title = str(links[0].text)
                commentUrl = links[0].get_attribute('href')
                id = int(commentUrl.replace("https://bbs.wenxuecity.com/currentevent/", "").replace(".html", ""))
                if any(settings.__CDF__["Comment ID"] == id):
                    break
                userId = str(links[1].text)
                commentAtrTxt = comment.find_element(By.TAG_NAME, 'small').text
                commentAtrTxtList = commentAtrTxt.split(")")
                commentAtrTxtList2 = commentAtrTxtList[-1].split("(")
                time = str(commentAtrTxtList2[0])
                text = self.getCommentContent(id)
                segmentedText = TextSeg.seg(title + text)
                if i == 0:
                    parentId = id
                    isArticle = True
                else:
                    isArticle = False
                #parentId = self.getParentId(id)

                parentTitle = ""
                parentText = ""
                parentUserId = 0
                website = "WXC"
                category = "currentevent"

                curComment = Comment(id, isArticle, title, text, userId, parentId,
                                     parentTitle, parentText, parentUserId, time,
                                     website, category, segmentedText)
                curComment.addToDf()

                # print(curComment.getCTxt)
                # print(curComment.getTime)
                #break
            #break

    def init(self):
        service = Service(executable_path=ChromeDriverManager().install())
        global option
        option = webdriver.ChromeOptions()
        chrome_prefs = {}
        option.experimental_options["prefs"] = chrome_prefs
        chrome_prefs["profile.default_content_settings"] = {"images": 2}
        chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}
        global driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()), chrome_options=option)

        driver.refresh()
        for i in range(1, 2):
            self.getPageContent(i)
        driver.quit()



    # def getParentId(self, commentId):
    #     parentId = 0
    #     global cDriver
    #     cDriver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()),
    #                                chrome_options=option)
    #     cDriver.refresh()
    #
    #     cDriver.get("https://bbs.wenxuecity.com/currentevent/" + str(commentId) + ".html")
    #     cDriver.implicitly_wait(0.5)
    #     postParent = cDriver.find_elements(By.ID, "postparent")
    #     #print(postParent)
    #     if len(postParent) == 1:
    #         parentLinks = postParent[0].find_elements(By.TAG_NAME, 'a')
    #         parentUrl = parentLinks[0].get_attribute('href')
    #         parentId = int(parentUrl.replace("https://bbs.wenxuecity.com/currentevent/", "").replace(".html", ""))
    #     #print("parentId:" + str(parentId))
    #     cDriver.close()
    #     return parentId