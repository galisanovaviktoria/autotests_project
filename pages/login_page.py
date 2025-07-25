from .base_page import BasePage
from .locators  import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    # 1) в URL должна быть подстрока 'login'
    def should_be_login_url(self):
        assert "login" in self.browser.current_url, \
            f"'login' not found in current url → {self.browser.current_url}"

    # 2) должен быть блок «Войти»
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form is not presented"

    # 3) должен быть блок «Регистрация»
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Register form is not presented"

    # 4) объединяем все проверки
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
