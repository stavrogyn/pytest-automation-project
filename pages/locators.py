from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.ID, "login_link")


class LoginPageLocators():
    REGISTER = (By.ID, "register_form")
    LOGIN = (By.ID, "login_form")


class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    COST_OF_PRODUCT = (By.XPATH, "//div[contains(@class, 'product_main')]/p[contains(@class, 'price_color')]")
    NAME_OF_PRODUCT = (By.XPATH, "//div[contains(@class, 'product_main')]/h1")

    NAME_OF_PRODUCT_IN_ADD_MESSAGE = (By.XPATH, "(//div[contains(@class, 'alertinner')]/strong)[1]")
    MESSAGE_PRODUCT_WAS_ADDED = (By.XPATH, "(//div[contains(@class, 'alertinner')][1])")
    BASKET_INFO_MESSAGE = (By.XPATH, "//div[contains(@class, 'alert-info')]")
    COST_OF_PRODUCT_IN_ADD_MESSAGE = (By.XPATH, "//div[contains(@class, 'alertinner')]/p/strong")
    MESSAGE_SUCCESS_BENEFIT_OFFER = (By.XPATH, "//strong[contains(text(),'Deferred benefit offer')]")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
