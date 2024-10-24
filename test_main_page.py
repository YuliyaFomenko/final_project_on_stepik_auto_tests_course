from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/"

def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()
    time.sleep(10)

def test_guest_can_go_to_login_page(browser): 
   browser.get(link)
   time.sleep(10)
   go_to_login_page(browser)
