from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_base import PageBase


class PageTorusInc(PageBase):
    __url = "https://torus-inc.tech/"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return self.__url
