from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def basket_contains_text_about_its_empty(self):
        content_container = self.browser.find_element(*BasketPageLocators.TEXT_CONTAINER)
        assert content_container, 'Basket should be contains text about its empty'


    def basket_contains_no_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORM), 'Basket contains items, but shoud not be'