from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent


class ChromeOptionSetter():
    @staticmethod
    def set_options():
        chrome_options = Options()
        chrome_options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-setuid-sandbox")
        chrome_options.add_argument("--remote-debugging-port=9222")
        chrome_options.add_argument("--disable-dev-shm-using")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("start-maximized")
        chrome_options.add_argument("disable-infobars")
        #chrome_options.add_argument(r"user-data-dir=.\cookies\\test")
        chrome_prefs = {}
        chrome_prefs["profile.default_content_settings"] = {"images": 2}
        chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}
        chrome_options.experimental_options["prefs"] = chrome_prefs
        #chrome_options.binary_location = "/usr/b/chromedriver"
        chrome_options.binary_location = ("/usr/bin/google-chrome-beta")

        ua = UserAgent()
        user_agent = ua.random
        #print(user_agent)
        chrome_options.add_argument(f'user-agent={user_agent}')

        return chrome_options

    @staticmethod
    def set_options2():
        chrome_options = Options()
        chrome_prefs = {}
        chrome_prefs["profile.default_content_settings"] = {"images": 2}
        chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}
        chrome_options.experimental_options["prefs"] = chrome_prefs

        ua = UserAgent()
        user_agent = ua.random
        print(user_agent)
        chrome_options.add_argument(f'user-agent={user_agent}')
        return chrome_options