# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
import pandas as pd
from IPython.display import display

import settings
from scrapFactory import ScrapFactory
from updateParent import UpdateParent

if __name__ == '__main__':
    settings.init()
    #webName = input("Please enter web name from (WXC, HR or MIT): ").upper()
    webName = "MIT"
    settings.__CDF__ = pd.read_csv(webName + '.csv')
    ScrapFactory.createScrap(webName)
    UpdateParent.init("")

    #print(Settings.commentsDf.dtypes)
    #display(Settings.commentsDf)

    settings.__CDF__.to_csv(webName + '.csv', index=False)




