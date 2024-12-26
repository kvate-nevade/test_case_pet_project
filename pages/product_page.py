from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button_add_to_basket.click()

    def alert_add_to_basket_successful(self):
        alert_add_to_basket_successful_text = self.browser.find_element(*ProductPageLocators.ALLERT_ADD_TO_BASKET).text
        check_text = 'был добавлен в вашу корзину.'
        assert check_text in alert_add_to_basket_successful_text, 'Alert add to basket not found.'

    def product_name_isequal_in_alert(self):
        product_name_from_alert_text = self.browser.find_element(*ProductPageLocators.ALLERT_ADD_TO_BASKET_PRODUCT_NAME).text
        product_name_from_h1_text = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert product_name_from_alert_text == product_name_from_h1_text, 'Product name from basket not equal product name from h1.'

    def should_be_alert_with_basket_price(self):
        sum_from_basket_price = self.browser.find_element(*ProductPageLocators.ALLERT_COSTS_OF_BASKET)
        assert sum_from_basket_price, 'Alert with product price is not found.'

    def alert_with_basket_price_equal_product_price(self):
        cost_goods_in_alert = self.browser.find_element(*ProductPageLocators.ALLERT_COSTS_OF_BASKET_NUMBER).text
        cost_good_in_card = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert cost_goods_in_alert == cost_good_in_card, 'Cost goods in alert is not equal cost in card.'