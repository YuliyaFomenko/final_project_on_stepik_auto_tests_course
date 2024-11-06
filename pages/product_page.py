from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.click_on_button_add_to_basket()
        self.solve_quiz_and_get_code()
        # time.sleep(5)
        self.should_be_message_product_in_cart()
        # time.sleep(5)
        self.should_be_product_names_equal()
        # time.sleep(5)
        self.should_be_message_with_basket_cost()
        # time.sleep(5)
        self.should_be_costs_equal()
        
    def click_on_button_add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        link.click()
        
    def should_be_message_product_in_cart(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRODUCT_IN_CART), "Message 'Product in the cart' is not presented" # Разобраться с проверкой ассерта
    
    def should_be_product_names_equal(self):
        book_name_in_message = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_MESSAGE)
        book_in_message = book_name_in_message.text
        book_name_in_cart = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_CART)
        book_in_cart = book_name_in_cart.text
        assert book_in_message == book_in_cart, "Product names are not equal" # Разобраться с проверкой ассерта, работает
    
    def should_be_message_with_basket_cost(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_COST_CART), "Message with basket cost is not presented" # Разобраться с проверкой ассерта
    
    def should_be_costs_equal(self):
        book_cost_in_message = self.browser.find_element(*ProductPageLocators.BOOK_COST_IN_MESSAGE)
        cost_in_message = book_cost_in_message.text
        book_cost_in_cart = self.browser.find_element(*ProductPageLocators.BOOK_COST_IN_CART)
        cost_in_cart = book_cost_in_cart.text
        assert cost_in_message == cost_in_cart, "Costs are not equal" # Разобраться с проверкой ассерта