# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
import pandas as pd
from IPython.display import display

import settings
import textSeg

def addToDf(comment):
    # print(comment.getCTxt)
    # print(comment.getTime)
    settings.commentsPd.loc[len(settings.commentsPd.index)] = [comment.getCId, comment.getCTxt, comment.getUName, comment.getCTime]

def getPageContent(pageNum):
    driver.get("https://bbs.wenxuecity.com/currentevent/?page=" + str(pageNum))
    driver.implicitly_wait(0.5)
    posts = driver.find_elements(By.CLASS_NAME, "odd") + driver.find_elements(By.CLASS_NAME, "even")
    for post in posts:
        comments = post.find_elements(By.TAG_NAME, 'p')
        for comment in comments:
            links = comment.find_elements(By.TAG_NAME, 'a')
            commentText = str(links[0].text)
            commentUrl = links[0].get_attribute('href')
            commentId = int(commentUrl.replace("https://bbs.wenxuecity.com/currentevent/","").replace(".html",""))
            userName = str(links[1].text)
            commentAtrTxt = comment.find_element(By.TAG_NAME, 'small').text
            commentAtrTxtList = commentAtrTxt.split("reads)")
            commentAtrTxtList2 = commentAtrTxtList[-1].split("(")
            commentTime = str(commentAtrTxtList2[0])
            print(commentTime)
            commentTextWords = textSeg.seg(commentText)
            curComment = settings.Comment(commentId, commentTextWords, userName, commentTime)
            addToDf(curComment)

            # print(curComment.getCTxt)
            # print(curComment.getTime)
            #break




def init():
    service = Service(executable_path=ChromeDriverManager().install())
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
    driver.refresh()
    for i in range(1, 500):
        getPageContent(i)
    driver.quit()