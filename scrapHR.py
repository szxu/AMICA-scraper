# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
import pandas as pd
from IPython.display import display

from textSeg import TextSeg
from comment import Comment

class ScrapHR():
    def getCommentContent(self, commentUrl):
        global cDriver
        cDriver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()), chrome_options=option)
        cDriver.refresh()
        cDriver.get(commentUrl)
        cDriver.implicitly_wait(0.5)

        commentParentId = int(
            commentUrl.replace("https://huaren.us/showtopic.html?topicid=", "").replace("&fid=398", ""))
        commentList = cDriver.find_element(By.CLASS_NAME, "post-list")
        comments = commentList.find_elements(By.CLASS_NAME, "post-item")

        print(len(comments))
        for comment in comments:
            commentId = int(comment.get_attribute("id"))
            userName = comment.find_element(By.CLASS_NAME, "post-user").find_element(By.CLASS_NAME, "avatar-wrap").get_attribute('href').replace("https://huaren.us/userinfo.html?uid=", "")
            commentText = comment.find_element(By.CLASS_NAME, "post-content").text
            commentTime = comment.find_element(By.CLASS_NAME, "post-top-action").text.split("发表于：")[1].split("|只看")[0]
            commentSegText = TextSeg.seg(commentText)
            curComment = Comment(commentId, commentParentId, commentText, userName, commentTime, commentSegText)
            print([curComment.getCId, curComment.getCPid, curComment.getCTxt, curComment.getUName, curComment.getCTime, curComment.getCStxt])
            curComment.addToDf()
        cDriver.close()

    def getPageContent(self, pageNum):
        driver.get("https://huaren.us/showforum.html?forumid=398&page=" + str(pageNum) + "&order=tid")
        driver.implicitly_wait(0.5)
        posts = driver.find_elements(By.CLASS_NAME, "hr-topic")
        for postIdx in range(4, len(posts)):
            links = posts[postIdx].find_elements(By.TAG_NAME, 'a')
            commentUrl = links[0].get_attribute('href')
            self.getCommentContent(commentUrl)

    def init(self):
        service = Service(executable_path=ChromeDriverManager().install())
        global option
        option = webdriver.ChromeOptions()
        chrome_prefs = {}
        option.experimental_options["prefs"] = chrome_prefs
        chrome_prefs["profile.default_content_settings"] = {"images": 2}
        chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}

        global driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()),
                                  chrome_options=option)
        driver.refresh()
        for i in range(1, 5):
            self.getPageContent(i)
        driver.quit()
