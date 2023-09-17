import json

from requests import Response
from selenium.webdriver.remote.webdriver import WebDriver

from api.status_codes import StatusCodes
from scheme.schema_register_login import RegisterUserResponse
from tests.web.locators import MainLocators
from web.pages.main import MainPage


class TestUnsuccessfulRegisterWeb:

    def test_unsuccessful_register_web(self, driver: WebDriver, unsuccessful_register: Response):
        main_page = MainPage(driver)
        main_page.open_url()
        main_page.click_by_element(MainLocators.POST_REGISTER_UNSUCCESSFUL)
        main_page.wait_text_to_be_present_in_element(locator=MainLocators.RESPONSE_FRAME, text='{')
        web_text = main_page.find_element(MainLocators.RESPONSE_FRAME).text
        web_text_status_code = main_page.find_element(MainLocators.STATUS_CODE).text
        api_text = unsuccessful_register.json()
        assert web_text_status_code == '400', \
            f'Статус код {web_text_status_code} не совпадает с ожидаемым - {StatusCodes.STATUS_400}'
        assert RegisterUserResponse(**json.loads(web_text)) == RegisterUserResponse(**api_text)
