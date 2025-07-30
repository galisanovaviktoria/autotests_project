from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print("Your code: ", alert.text)
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_added_product_name(self, expected_name):
        added_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
        assert added_name == expected_name, f"Expected product name '{expected_name}', but got '{added_name}'"

    def should_be_correct_price(self, expected_price):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert basket_price == expected_price, f"Expected basket price '{expected_price}', but got '{basket_price}'"

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
