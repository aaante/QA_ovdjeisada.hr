from selenium.webdriver.remote.webdriver import WebDriver

from page_base import PageBase


class PageRSOPlayAttentionTretman(PageBase):
    __url = "https://ovdjeisada.hr/usluge/psiholosko-savjetovaliste/play-attention-za-odrasle/"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    @property
    def expected_url(self) -> str:
        return self.__url
