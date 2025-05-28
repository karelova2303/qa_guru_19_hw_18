import allure
from selene import browser, have


class Cart():
    def __init__(self):
        self.topcartlink = browser.element('#topcartlink')
        self.product_name = browser.element('.product-name')
        self.product_unit_price = browser.element('.product-unit-price')
        self.removefromcart = browser.element('[name="removefromcart"]')
        self.updatecart = browser.element('[name="updatecart"]')

    @allure.step(f'Открываем корзину')
    def open_cart(self):
        self.topcartlink.click()

    @allure.step(f'Проверяем наименование добавленного товара')
    def should_be_added_product_to_cart(self, value):
        self.product_name.should(have.exact_text(value))

    @allure.step(f'Проверяем цену добавленного товара')
    def should_be_the_price_match(self, value):
        self.product_unit_price.should(have.exact_text(value))

    @allure.step(f'Очищаем корзину')
    def clear_cart(self):
        self.removefromcart.click()
        self.updatecart.click()
