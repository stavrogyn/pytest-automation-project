from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.ID, "login_link")


class LoginPageLocators():
    REGISTER = (By.ID, "register_form")
    LOGIN = (By.ID, "login_form")
    REGISTER_EMAIl = (By.ID, "id_registration-email")
    REGISTER_PASS = (By.ID, "id_registration-password1")
    REGISTER_PASS_CONF = (By.ID, "id_registration-password2")
    BUTTON_TO_REGISTER = (By.XPATH, "//button[contains(@name, 'registration_submit')]")


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
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, "basket-items")
    MESSAGE_EMPTY_BASKET = (By.XPATH, f"//div[contains(@class, 'content-inner')/a[contains(@href, /ru/)]")
