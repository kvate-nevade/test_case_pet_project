import pytest
from .pages.product_page import ProductPage
from time import sleep

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
