from selenium.webdriver.remote.webdriver import WebDriver

from page_base import PageBase


class PageInstagram(PageBase):
    __url = "https://www.instagram.com/ovdje_i_sada/"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return self.__url
