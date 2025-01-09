from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-group a.btn')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    ALLERT_ADD_TO_BASKET = (By.CSS_SELECTOR, '#messages > :nth-child(1) > .alertinner')
    ALLERT_ADD_TO_BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, '#messages > :nth-child(1) > .alertinner > strong')
    ALLERT_COSTS_OF_BASKET = (By.CSS_SELECTOR, '.alert-info strong')
    ALLERT_COSTS_OF_BASKET_NUMBER = (By.CSS_SELECTOR, '.alert-info strong')

class BasketPageLocators():
    TEXT_BASKET_IS_EMPTY = (By.CSS_SELECTOR, '#content_inner > p')
    BASKET_FORM = (By.CSS_SELECTOR, '#basket_formset')
