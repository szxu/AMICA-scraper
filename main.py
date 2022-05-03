# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
import pandas as pd
from IPython.display import display

import settings
import scrapWXC
import scrapHR

if __name__ == '__main__':

    settings.init()
    scrapHR.init()

    #print(settings.commentsPd.dtypes)
    #display(settings.commentsPd)

    settings.commentsDf.to_csv('out.csv', index=False)




