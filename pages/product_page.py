from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        add_to_basket_button.click()

    def should_be_message_product_was_added(self):
        assert "has been added to your basket" in \
            self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_WAS_ADDED).text, \
            "Product was added didn't show"

        assert self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text == \
            self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT_IN_ADD_MESSAGE).text, \
            "Product name in add-message != name in general page"

    def should_be_message_basket_info(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_INFO_MESSAGE), \
            "Basket info message didn't show"

        assert self.browser.find_element(*ProductPageLocators.COST_OF_PRODUCT).text == \
            self.browser.find_element(*ProductPageLocators.COST_OF_PRODUCT_IN_ADD_MESSAGE).text, \
            "Product cost in basket != product cost in general page"

    def should_be_message_success_added_showed(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_PRODUCT_WAS_ADDED), \
            "Message about benefit offer did not show"

    def should_be_message_success_added_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_PRODUCT_WAS_ADDED), \
            "Message about benefit did not disappear"
