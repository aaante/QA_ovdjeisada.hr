from selenium.webdriver.remote.webdriver import WebDriver

from page_base import PageBase


class PageRSDIUcitiTrebaNauciti(PageBase):
    __url = "https://ovdjeisada.hr/usluge/rad-s-djecom/kako-nauciti-uciti/kako-nauciti-uciti-radionica/"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    @property
    def expected_url(self) -> str:
        return self.__url
