# from time import sleep
# from selenium import webdriver
#
# browser = webdriver.Google_Chrome()
# browser.get('https://www.instagram.com/')
# sleep(5)
# browser.close()
#
# from time import sleep
# from selenium import webdriver
#
# browser = webdriver.Firefox()
# browser.implicitly_wait(5) # устанавливаем пятисекундную задержку
# # Если Selenium не может найти элемент, он ждет, чтобы все загрузилось и пытается снова
#
# browser.get('https://www.instagram.com/')
#
# # Следующие строки говорят боту найти ссылку с текстом Log in и кликнуть по ней.
# login_link = browser.find_element_by_xpath("//a[text()='Log in']")
# login_link.click()
#
# sleep(5)
#
# browser.close()
#
# from time import sleep
# from selenium import webdriver
#
# browser = webdriver.Firefox()
# browser.implicitly_wait(5)
#
# browser.get('https://www.instagram.com/')
#
# login_link = browser.find_element_by_xpath("//a[text()='Log in']")
# login_link.click()
#
# sleep(2)
#
# username_input = browser.find_element_by_css_selector("input[name='username']")
# password_input = browser.find_element_by_css_selector("input[name='password']")
#
# username_input.send_keys("<имя пользователя>")
# password_input.send_keys("<пароль>")
#
# login_button = browser.find_element_by_xpath("//button[@type='submit']")
# login_button.click()
#
# sleep(5)
#
# browser.close()
#
# def test_login_page(browser):
#     browser.get('https://www.instagram.com/accounts/login/')
#     username_input = browser.find_element_by_css_selector("input[name='username']")
#     password_input = browser.find_element_by_css_selector("input[name='password']")
#     username_input.send_keys("<your username>")
#     password_input.send_keys("<your password>")
#     login_button = browser.find_element_by_xpath("//button[@type='submit']")
#     login_button.click()
#
#     errors = browser.find_elements_by_css_selector('#error_message')
#     assert len(errors) == 0
#
#     from time import sleep
#
#     class LoginPage:
#         def __init__(self, browser):
#             self.browser = browser
#
#         def login(self, username, password):
#             username_input = self.browser.find_element_by_css_selector("input[name='username']")
#             password_input = self.browser.find_element_by_css_selector("input[name='password']")
#             username_input.send_keys(username)
#             password_input.send_keys(password)
#             login_button = browser.find_element_by_xpath("//button[@type='submit']")
#             login_button.click()
#             sleep(5)
#
#
#
# from selenium import webdriver
# from pages import HomePage
#
# browser = webdriver.Firefox()
# browser.implicitly_wait(5)
#
# home_page = HomePage(browser)
# login_page = home_page.go_to_login_page()
# login_page.login("<your username>", "<your password>")
#
# browser.close()
#
# def test_login_page(browser):
#     home_page = HomePage(browser)
#     login_page = home_page.go_to_login_page()
#     login_page.login("<your username>", "<your password>")
#
#     errors = browser.find_elements_by_css_selector('#error_message')
#     assert len(errors) == 0
#
# from instapy import InstaPy
#
# InstaPy(username="<your_username>", password="<your_password>").login()
#
# INFO [2019-12-17 22:03:19] [username]  -- Connection Checklist [1/3] (Internet Connection Status)
# INFO [2019-12-17 22:03:20] [username]  - Internet Connection Status: ok
# INFO [2019-12-17 22:03:20] [username]  - Current IP is "17.283.46.379" and it's from "Germany/DE"
# INFO [2019-12-17 22:03:20] [username]  -- Connection Checklist [2/3] (Instagram Server Status)
# INFO [2019-12-17 22:03:26] [username]  - Instagram WebSite Status: Currently Up
#
# from instapy import InstaPy
#
# session = InstaPy(username="<your_username>", password="<your_password>")
# session.login()
# session.like_by_tags(["bmw", "mercedes"], amount=5) # [1]
#
# INFO [2019-12-17 22:15:58] [username]  Tag [1/2]
# INFO [2019-12-17 22:15:58] [username]  --> b'bmw'
# INFO [2019-12-17 22:16:07] [username]  desired amount: 14  |  top posts [disabled]: 9  |  possible posts: 43726739
# INFO [2019-12-17 22:16:13] [username]  Like# [1/14]
# INFO [2019-12-17 22:16:13] [username]  https://www.instagram.com/p/B6MCcGcC3tU/
# INFO [2019-12-17 22:16:15] [username]  Image from: b'mattyproduction'
# INFO [2019-12-17 22:16:15] [username]  Link: b'https://www.instagram.com/p/B6MCcGcC3tU/'
# INFO [2019-12-17 22:16:15] [username]  Description: b'Mal etwas anderes \xf0\x9f\x91\x80\xe2\x98\xba\xef\xb8\x8f Bald ist das komplette Video auf YouTube zu finden (n\xc3\xa4here Infos werden folgen). Vielen Dank an @patrick_jwki @thehuthlife  und @christic_  f\xc3\xbcr das bereitstellen der Autos \xf0\x9f\x94\xa5\xf0\x9f\x98\x8d#carporn#cars#tuning#bagged#bmw#m2#m2competition#focusrs#ford#mk3#e92#m3#panasonic#cinematic#gh5s#dji#roninm#adobe#videography#music#bimmer#fordperformance#night#shooting#'
# INFO [2019-12-17 22:16:15] [username]  Location: b'K\xc3\xb6ln, Germany'
# INFO [2019-12-17 22:16:51] [username]  --> Image Liked!
# INFO [2019-12-17 22:16:56] [username]  --> Not commented
# INFO [2019-12-17 22:16:57] [username]  --> Not following
# INFO [2019-12-17 22:16:58] [username]  Like# [2/14]
# INFO [2019-12-17 22:16:58] [username]  https://www.instagram.com/p/B6MDK1wJ-Kb/
# INFO [2019-12-17 22:17:01] [username]  Image from: b'davs0'
# INFO [2019-12-17 22:17:01] [username]  Link: b'https://www.instagram.com/p/B6MDK1wJ-Kb/'
# INFO [2019-12-17 22:17:01] [username]  Description: b'Someone said cloud? \xf0\x9f\xa4\x94\xf0\x9f\xa4\xad\xf0\x9f\x98\x88 \xe2\x80\xa2\n\xe2\x80\xa2\n\xe2\x80\xa2\n\xe2\x80\xa2\n#bmw #bmwrepost #bmwm4 #bmwm4gts #f82 #bmwmrepost #bmwmsport #bmwmperformance #bmwmpower #bmwm4cs #austinyellow #davs0 #mpower_official #bmw_world_ua #bimmerworld #bmwfans #bmwfamily #bimmers #bmwpost #ultimatedrivingmachine #bmwgang #m3f80 #m5f90 #m4f82 #bmwmafia #bmwcrew #bmwlifestyle'
# INFO [2019-12-17 22:17:34] [username]  --> Image Liked!
# INFO [2019-12-17 22:17:37] [username]  --> Not commented
# INFO [2019-12-17 22:17:38] [username]  --> Not following
#
# from instapy import InstaPy
#
# session = InstaPy(username="<your_username>", password="<your_password>")
# session.login()
# session.like_by_tags(["bmw", "mercedes"], amount=5)
# session.set_dont_like(["naked", "nsfw"])
#
# from instapy import InstaPy
#
# session = InstaPy(username="<your_username>", password="<your_password>")
# session.login()
# session.like_by_tags(["bmw", "mercedes"], amount=5)
# session.set_dont_like(["naked", "nsfw"])
# session.set_do_follow(True, percentage=50)
#
# from instapy import InstaPy
#
# session = InstaPy(username="<your_username>", password="<your_password>")
# session.login()
# session.like_by_tags(["bmw", "mercedes"], amount=5)
# session.set_dont_like(["naked", "nsfw"])
# session.set_do_follow(True, percentage=50)
# session.set_do_comment(True, percentage=50)
#
# from instapy import InstaPy
#
# session = InstaPy(username="<your_username>", password="<your_password>")
# session.login()
# session.like_by_tags(["bmw", "mercedes"], amount=5)
# session.set_dont_like(["naked", "nsfw"])
# session.set_do_follow(True, percentage=50)
# session.set_do_comment(True, percentage=50)
# session.set_comments(["Nice!", "Sweet!", "Beautiful :heart_eyes:"])
#
# from instapy import InstaPy
#
# session = InstaPy(username="<your_username>", password="<your_password>")
# session.login()
# session.like_by_tags(["bmw", "mercedes"], amount=5)
# session.set_dont_like(["naked", "nsfw"])
# session.set_do_follow(True, percentage=50)
# session.set_do_comment(True, percentage=50)
# session.set_comments(["Nice!", "Sweet!", "Beautiful :heart_eyes:"])
# session.end()
#
# session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)
#
# session = InstaPy(username='test', password='test', headless_browser=True)
#
# session.set_use_clarifai(enabled=True, api_key='<your_api_key>')
# session.clarifai_check_img_for(['nsfw'])
#
# session.set_relationship_bounds(enabled=True, max_followers=8500)
#

from time import sleep
from selenium import webdriver

browser = webdriver.Chrome()  # Исправлено на Chrome
browser.get('https://www.instagram.com/')
sleep(5)
browser.close()

from time import sleep
from selenium import webdriver

browser = webdriver.Firefox()
browser.implicitly_wait(5)

browser.get('https://www.instagram.com/')

login_link = browser.find_element_by_xpath("//a[text()='Log in']")
login_link.click()

sleep(5)

browser.close()

from time import sleep
from selenium import webdriver

browser = webdriver.Firefox()
browser.implicitly_wait(5)

browser.get('https://www.instagram.com/')

login_link = browser.find_element_by_xpath("//a[text()='Log in']")
login_link.click()

sleep(2)

username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

username_input.send_keys("<имя пользователя>")
password_input.send_keys("<пароль>")

login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

sleep(5)

browser.close()

def test_login_page(browser):
    browser.get('https://www.instagram.com/accounts/login/')
    username_input = browser.find_element_by_css_selector("input[name='username']")
    password_input = browser.find_element_by_css_selector("input[name='password']")
    username_input.send_keys("<your username>")
    password_input.send_keys("<your password>")
    login_button = browser.find_element_by_xpath("//button[@type='submit']")
    login_button.click()

    errors = browser.find_elements_by_css_selector('#error_message')
    assert len(errors) == 0

from time import sleep

class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):
        username_input = self.browser.find_element_by_css_selector("input[name='username']")
        password_input = self.browser.find_element_by_css_selector("input[name='password']")
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button = self.browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        sleep(5)


from selenium import webdriver
from pages import HomePage

browser = webdriver.Firefox()
browser.implicitly_wait(5)

home_page = HomePage(browser)
login_page = home_page.go_to_login_page()
login_page.login("<your username>", "<your password>")

browser.close()

def test_login_page(browser):
    home_page = HomePage(browser)
    login_page = home_page.go_to_login_page()
    login_page.login("<your username>", "<your password>")

    errors = browser.find_elements_by_css_selector('#error_message')
    assert len(errors) == 0

from instapy import InstaPy

session = InstaPy(username="<your_username>", password="<your_password>")
session.login()

session.like_by_tags(["bmw", "mercedes"], amount=5)
session.set_dont_like(["naked", "nsfw"])
session.set_do_follow(True, percentage=50)
session.set_do_comment(True, percentage=50)
session.set_comments(["Nice!", "Sweet!", "Beautiful :heart_eyes:"])

session.end()

session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)

session = InstaPy(username='test', password='test', headless_browser=True)

session.set_use_clarifai(enabled=True, api_key='<your_api_key>')
session.clarifai_check_img_for(['nsfw'])

session.set_relationship_bounds(enabled=True, max_followers=8500)

