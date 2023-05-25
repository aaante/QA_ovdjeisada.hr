from selenium.webdriver.remote.webdriver import WebDriver

from page_base import PageBase


class PageFacebook(PageBase):
    __url = "https://www.facebook.com/ovdjeisada"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return self.__url
