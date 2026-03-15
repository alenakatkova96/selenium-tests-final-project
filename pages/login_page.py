from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login URL is not correct"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(By.CSS_SELECTOR, "#id_registration-email")
        password1_input = self.browser.find_element(By.CSS_SELECTOR, "#id_registration-password1")
        password2_input = self.browser.find_element(By.CSS_SELECTOR, "#id_registration-password2")
        register_button = self.browser.find_element(By.CSS_SELECTOR, "#register_form button")

        email_input.send_keys(email)
        password1_input.send_keys(password)
        password2_input.send_keys(password)
        register_button.click()


