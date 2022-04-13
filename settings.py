from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
import pandas as pd
from IPython.display import display


class Comment:
    def __init__(self, cId, cTxt, uName, cTime):
        self.cId = cId
        self.cTxt = cTxt
        self.uName = uName
        self.cTime = cTime

    @property
    def getCId(self):
        return self.cId

    @property
    def getCTxt(self):
        return self.cTxt

    @property
    def getUName(self):
        return self.uName

    @property
    def getCTime(self):
        return self.cTime


def init():

    global commentsPd
    commentsPd = pd.DataFrame([], columns=list(["commentId", "commentTxt", "userName", "commentTime"]))

    global service
    service = Service(executable_path=ChromeDriverManager().install())

    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))