from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Current URL haven't 'login' substring}"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER), "Register form is not presented"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIl).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASS).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASS_CONF).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BUTTON_TO_REGISTER).click()
