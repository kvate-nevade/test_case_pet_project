import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.main_page import MainPage


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    prod_page = ProductPage(browser, link)
    prod_page.open()
    prod_page.add_to_basket()
    prod_page.should_not_be_alert_add_to_basket()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    prod_page = ProductPage(browser, link)
    prod_page.open()
    prod_page.add_to_basket()
    prod_page.should_be_is_disappear_add_to_basket()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    page_basket = BasketPage(browser, browser.current_url)
    page_basket.basket_contains_no_items()
    page_basket.basket_contains_text_about_its_empty()

@pytest.mark.user_test
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope = 'function', autouse = True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.register_new_user()
        main_page = MainPage(browser, browser.current_url)
        main_page.is_logged_in()


    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        prod_page = ProductPage(browser, link)
        prod_page.open()
        prod_page.should_not_be_alert_add_to_basket()


    @pytest.mark.need_review
    @pytest.mark.parametrize('promo_offer', ['0', '1', '2', '3', '4', '5', '6', 
                                            pytest.param('7', marks = pytest.mark.xfail), 
                                            '8', '9'])
    def test_user_can_add_product_to_basket(self, browser, promo_offer):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}'
        prod_page = ProductPage(browser, link)
        prod_page.open()
        prod_page.add_to_basket()
        prod_page.solve_quiz_and_get_code()
        prod_page.alert_add_to_basket_successful()
        prod_page.product_name_isequal_in_alert()
        prod_page.should_be_alert_with_basket_price()
        prod_page.alert_with_basket_price_equal_product_price()


@pytest.mark.need_review
@pytest.mark.parametrize('promo_offer', ['0', '1', '2', '3', '4', '5', '6', 
                                            pytest.param('7', marks = pytest.mark.xfail), 
                                            '8', '9'])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}'
    prod_page = ProductPage(browser, link)
    prod_page.open()
    prod_page.add_to_basket()
    prod_page.solve_quiz_and_get_code()
    prod_page.alert_add_to_basket_successful()
    prod_page.product_name_isequal_in_alert()
    prod_page.should_be_alert_with_basket_price()
    prod_page.alert_with_basket_price_equal_product_price()
