import faker
import time
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        url_login_part = '/accounts/login/'
        assert url_login_part in self.browser.current_url, 'Link page should be is right'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), 'Form of login should be present'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM), 'Form of register should be present'

    def register_new_user(self, 
                          email = f'email32165{str(time.time())}{faker.Faker().email()}',
                          password = 'eda22d0fjg7ghf82q30g9rh'):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_FIELD)
        email_field.send_keys(email)
        password_field_1 = self.browser.find_element(*LoginPageLocators.REGISTER_FIRST_PASSWORD)
        password_field_1.send_keys(password)
        password_field_2 = self.browser.find_element(*LoginPageLocators.REGISTER_SECOND_PASSWORD)
        password_field_2.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
        print('Registration was successful')
