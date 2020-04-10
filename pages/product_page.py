from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_button.click()

    def should_be_message_about_adding(self):
        assert "has been added to your basket" in \
               self.browser.find_element(*ProductPageLocators.MESSAGE_ADDING_IN_BASKET).text, \
            "Message about adding didn't show"

    def should_be_basket_info(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ADDING_IN_BASKET), "Message about adding didn't show"
        assert self.browser.find_element(*ProductPageLocators.COST_OF_GOOD).text == \
               self.browser.find_element(*ProductPageLocators.MESSAGE_COST_OF_BASKET).text, \
            "Basket cost is not the same as cost of good"
