from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket is not empty"

    def should_be_text_basket_empty(self):
        language = self.language_checker()
        assert self.is_element_present(By.XPATH, f"//p/a[contains(@href, '/{language}/')]"), \
            "Text about empty-basket was not showed"
