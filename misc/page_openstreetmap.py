from selenium.webdriver.remote.webdriver import WebDriver

from page_base import PageBase


class PageOpenStreetMap(PageBase):
    __url = "https://www.openstreetmap.org/?mlat=45.77270&mlon=15.98400#map=19/45.77270/15.98400"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return self.__url
