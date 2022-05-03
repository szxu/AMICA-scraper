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
    settings.commentsDf.loc[len(settings.commentsDf.index)] = [comment.getCId, comment.getCPid, comment.getCTxt, comment.getUName, comment.getCTime, comment.getCStxt]

def getParentId(commentId):
    parentId = 0
    global cDriver
    cDriver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()), chrome_options=option)
    cDriver.refresh()

    cDriver.get("https://bbs.wenxuecity.com/currentevent/" + str(commentId) + ".html")
    cDriver.implicitly_wait(0.5)
    postParent = cDriver.find_elements(By.ID, "postparent")
    print(postParent)
    if len(postParent) == 1:
        parentLinks = postParent[0].find_elements(By.TAG_NAME, 'a')
        parentUrl = parentLinks[0].get_attribute('href')
        parentId = int(parentUrl.replace("https://bbs.wenxuecity.com/currentevent/", "").replace(".html", ""))

    print("parentId:" + str(parentId))
    cDriver.close()
    return parentId

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
            commentSegText = textSeg.seg(commentText)
            commentParentId = getParentId(commentId)
            curComment = settings.Comment(commentId, commentParentId, commentText, userName, commentTime, commentSegText)
            addToDf(curComment)

            # print(curComment.getCTxt)
            # print(curComment.getTime)
            #break

def init():
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
        getPageContent(i)
    driver.quit()