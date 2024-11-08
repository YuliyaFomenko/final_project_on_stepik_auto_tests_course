from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    
    MESSAGE_PRODUCT_IN_CART = (By.CSS_SELECTOR, ".alert:nth-child(1)")
    BOOK_NAME_IN_MESSAGE = (By.CSS_SELECTOR, ".alert:nth-child(1) strong")
    BOOK_NAME_IN_CART = (By.CSS_SELECTOR, ".product_main h1")
    
    MESSAGE_COST_CART = (By.CSS_SELECTOR, ".alert:nth-child(3)")
    BOOK_COST_IN_MESSAGE = (By.CSS_SELECTOR, ".alert:nth-child(3) strong")
    BOOK_COST_IN_CART = (By.CSS_SELECTOR, ".product_main .price_color")