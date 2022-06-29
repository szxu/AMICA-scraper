# selenium 4
from selenium import webdriver
from selenium.webdriver.common.by import By
#
# from utils.settings import GlobalVariables
from util.df_handler import DfHandler
from util.chrome_option_setter import ChromeOptionSetter
from scraper.util.text_segmenter import TextSegmenter
from util.comment import Comment

class WxcScraper():
    def getCommentContent(self, id):
        cDriver = webdriver.Chrome()
        cDriver.refresh()
        print("asdasdasd")
        cDriver.get("https://bbs.wenxuecity.com/currentevent/" + str(id) + ".html")
        cDriver.implicitly_wait(0.5)

        text = cDriver.find_elements(By.XPATH, "//div[@id='postbody']")[0].text

        cDriver.close()
        return text

    def getPageContent(self, driver, df, pageNum, catName):
        driver.get("https://bbs.wenxuecity.com/" + str(catName) + "/?page=" + str(pageNum))
        driver.implicitly_wait(0.5)

        posts = driver.find_elements(By.CLASS_NAME, "odd") + driver.find_elements(By.CLASS_NAME, "even")
        for post in posts:

            comments = post.find_elements(By.TAG_NAME, 'p')
            parentId = 0
            for i in range(len(comments)):
                comment = comments[i]
                links = comment.find_elements(By.TAG_NAME, 'a')
                title = str(links[0].text)
                commentUrl = links[0].get_attribute('href')
                id = int(commentUrl.replace("https://bbs.wenxuecity.com/" + str(catName) + "/", "").replace(".html", ""))
                userId = str(links[1].text)
                commentAtrTxt = comment.find_element(By.TAG_NAME, 'small').text
                commentAtrTxtList = commentAtrTxt.split(")")
                commentAtrTxtList2 = commentAtrTxtList[-1].split("(")
                time = str(commentAtrTxtList2[0])
                text = self.getCommentContent(id)
                segmentedText = TextSegmenter.seg(title + text)
                if i == 0:
                    parentId = id
                    isArticle = True
                else:
                    isArticle = False
                #parentId = self.getParentId(id)

                parentTitle = ""
                parentText = ""
                parentUserId = 0
                website = "WXC"
                category = catName

                curComment = Comment(id, website, category, isArticle, title, text, userId, parentId,
                             parentTitle, parentText, parentUserId, time, segmentedText)
                curComment.addToDf()

    def init(self, target):
        os = ChromeOptionSetter()
        global chromeOptions
        chromeOptions = os.set_options()
        catName = ""
        driver = webdriver.Chrome(chrome_options=chromeOptions)
        driver.set_page_load_timeout(10)

        df = DfHandler.make_comment_df()
        #driver.refresh()
        for i in range(1, 10):
            try:
                self.getPageContent(driver, df, i, catName)
            except Exception as ex:
                print(ex)
                continue

        driver.quit()



    # def getParentId(self, commentId):
    #     parentId = 0
    #     global cDriver
    #     cDriver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()),
    #                                chrome_options=option)
    #     cDriver.refresh()
    #
    #     cDriver.get("https://bbs.wenxuecity.com/currentevent/" + str(commentId) + ".html")
    #     cDriver.implicitly_wait(0.5)
    #     postParent = cDriver.find_elements(By.ID, "postparent")
    #     #print(postParent)
    #     if len(postParent) == 1:
    #         parentLinks = postParent[0].find_elements(By.TAG_NAME, 'a')
    #         parentUrl = parentLinks[0].get_attribute('href')
    #         parentId = int(parentUrl.replace("https://bbs.wenxuecity.com/currentevent/", "").replace(".html", ""))
    #     #print("parentId:" + str(parentId))
    #     cDriver.close()
    #     return parentId