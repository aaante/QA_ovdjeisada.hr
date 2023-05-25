from selenium.webdriver.remote.webdriver import WebDriver

from page_base import PageBase


class PagePhone(PageBase):
    __url = "tel:+385958937551"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return self.__url
