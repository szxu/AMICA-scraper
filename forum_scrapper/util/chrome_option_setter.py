from selenium import webdriver
from fake_useragent import UserAgent


class ChromeOptionSetter():
    @staticmethod
    def set_options():
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
        chromeOptions.add_argument("--no-sandbox")
        chromeOptions.add_argument("--disable-setuid-sandbox")
        chromeOptions.add_argument("--remote-debugging-port=9222")
        chromeOptions.add_argument("--disable-dev-shm-using")
        chromeOptions.add_argument("--disable-extensions")
        chromeOptions.add_argument("--disable-gpu")
        chromeOptions.add_argument("start-maximized")
        chromeOptions.add_argument("disable-infobars")
        #chromeOptions.add_argument(r"user-data-dir=.\cookies\\test")
        chrome_prefs = {}
        chrome_prefs["profile.default_content_settings"] = {"images": 2}
        chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}
        chromeOptions.experimental_options["prefs"] = chrome_prefs
        #chromeOptions.binary_location = "/usr/b/chromedriver"
        chromeOptions.binary_location = ("/usr/bin/google-chrome-beta")

        ua = UserAgent()
        user_agent = ua.random
        print(user_agent)
        chromeOptions.add_argument(f'user-agent={user_agent}')

        return chromeOptions