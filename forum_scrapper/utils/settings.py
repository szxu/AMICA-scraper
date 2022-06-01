from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
import pandas as pd
from IPython.display import display

class GlobalVariables():
    global __CDF__
    __CDF__ = pd.DataFrame([], columns=list(["Comment ID",
                                             "Website",
                                             "Category",
                                                "Is Article",
                                                "Comment Title",
                                                "Comment Text",
                                                "User ID",
                                                "Parent ID",
                                                "Parent Title",
                                                "Parent Text",
                                                "Parent User ID",
                                                "Comment Time",
                                                "Segmented Text"]))



