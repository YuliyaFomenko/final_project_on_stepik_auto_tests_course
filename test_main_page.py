import time
from .pages.main_page import MainPage
from .pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    time.sleep(5)
    page.go_to_login_page()
    time.sleep(5)
    login_page = LoginPage(browser, browser.current_url)
    time.sleep(5)
    login_page.should_be_login_page()
    time.sleep(5)
