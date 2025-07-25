from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    # блок «Войти»
    LOGIN_FORM        = (By.CSS_SELECTOR, "#login_form")
    LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASS_INPUT  = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON      = (By.CSS_SELECTOR, "button[name='login_submit']")

    # блок «Регистрация»
    REGISTER_FORM        = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASS1_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASS2_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON      = (By.CSS_SELECTOR, "button[name='registration_submit']")
