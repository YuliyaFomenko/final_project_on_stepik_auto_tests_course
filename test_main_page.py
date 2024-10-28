import time
from .pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    time.sleep(5)
    page.should_be_login_link()
    time.sleep(5)
    page.go_to_login_page()
    time.sleep(5)
