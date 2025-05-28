import allure
import requests
from allure_commons.types import AttachmentType
from selene import browser, have

from models.data import URL, LOGIN, PASSWORD


class ApiRequest:
    @allure.step('Авторизация через API')
    def authorization_user_api(self):
        result = requests.post(
            url=f'{URL}/login',
            data={"Email": LOGIN, "Password": PASSWORD, "RememberMe": False},
            allow_redirects=False
        )
        assert result.status_code == 302
        allure.attach(body=result.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=str(result.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")
        self.cookie = result.cookies.get("NOPCOMMERCE.AUTH")

        return self

    @allure.step(f'Открываем страницу {URL}')
    def open_page_with_cookies(self):
        browser.open(URL)
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": self.cookie})
        browser.open(URL)

    @allure.step(f'Добавляем товар в корзину через API')
    def add_product_on_id(self, id):
        response = requests.post(f'{URL}addproducttocart/catalog/{id}',
                                 cookies={'NOPCOMMERCE.AUTH': self.cookie})
        assert response.status_code == 200
        allure.attach(body=response.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=str(response.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")
