from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.ID, "login_link")

class LoginPageLocators():
    REGISTER = (By.ID, "register_form")
    LOGIN = (By.ID, "login_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    COST_OF_GOOD = (By.XPATH, "//div[contains(@class, 'product_main')]/p[contains(@class, 'price_color')]")

    MESSAGE_ADDING_IN_BASKET = (By.XPATH,
                                    "(//div[contains(@class, 'alertinner')])[1]")
    MESSAGE_BASKET_INFO = (By.XPATH, "//div[contains(@class, 'alert-info')]")
    MESSAGE_COST_OF_BASKET = (By.XPATH,
                                    "//div[contains(@class, 'alertinner')]/p/strong")