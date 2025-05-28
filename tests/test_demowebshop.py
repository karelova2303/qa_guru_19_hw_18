import allure

from models.api_request import ApiRequest
from models.cart import Cart

api_request = ApiRequest()
cart = Cart()
id_book = '13/1/1'
id_accessory = '62/1/1'


@allure.title('Тест на добавление товара из раздела "Книги" в корзину')
def test_add_book_in_the_cart(browser_manager):
    api_request.authorization_user_api()
    api_request.open_page_with_cookies()
    api_request.add_product_on_id(id_book)
    cart.open_cart()
    cart.should_be_added_product_to_cart('Computing and Internet')
    cart.should_be_the_price_match('10.00')
    cart.clear_cart()


@allure.title('Тест на добавление товара из раздела "Аксессуары" в корзину')
def test_add_tcp_material_in_the_cart(browser_manager):
    api_request.authorization_user_api()
    api_request.open_page_with_cookies()
    api_request.add_product_on_id(id_accessory)
    cart.open_cart()
    cart.should_be_added_product_to_cart('TCP Public MT/AT')
    cart.should_be_the_price_match('1700.00')
    cart.clear_cart()
