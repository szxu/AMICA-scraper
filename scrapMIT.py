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

def getCommentContent(commentNum):
    driver.get("https://www.mitbbs.com/article/Military/" + str(commentNum) + "_3.html")
    driver.implicitly_wait(0.5)

    commentId = commentNum


    news_bg_td = driver.find_element(By.XPATH, "//td[@class='news-bg']")
    center_td = news_bg_td.find_elements(By.TAG_NAME, "td")[-1]
    center_td_texts = center_td.text.split(",")
    commentTime = center_td_texts[-1]
    urls = center_td.find_elements(By.XPATH, "//a[@class='news' ]")
    commentParentUrl = urls[0].get_attribute('href')
    commentParentId = int(commentParentUrl.replace("https://www.mitbbs.com/article_t/Military/","").replace(".html",""))
    userName = urls[2].text
    commentText = driver.find_element(By.XPATH, "//td[@class='jiawenzhang-type']").text.split("美东)")[-1].split("※ 来源")[0].replace("\n","")
    commentSegText = textSeg.seg(commentText)
    print(commentId)

    curComment = settings.Comment(commentId, commentParentId, commentText, userName, commentTime, commentSegText)
    curComment.addToDf()


def init():
    service = Service(executable_path=ChromeDriverManager().install())
    option = webdriver.ChromeOptions()
    chrome_prefs = {}
    option.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}

    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()), chrome_options=option)
    driver.refresh()
    for i in range(64509653, 64508653, -2):
        try:
            getCommentContent(i)
        except:
            continue

    driver.quit()