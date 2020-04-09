from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.ID, "login_link")

class LoginPageLocators():
    REGISTER = (By.ID, "register_form")
    LOGIN = (By.ID, "login_form")