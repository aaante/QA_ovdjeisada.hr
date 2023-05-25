from selenium.webdriver.remote.webdriver import WebDriver

from page_base import PageBase


class PageGmaps(PageBase):
    __url = "https://www.google.com/maps/place/Zemljakova+ul.+3,+10000,+Zagreb/@45.7727415,15.9839423," \
            "17z/data=!3m1!4b1!4m6!3m5!1s0x4765d5df1832ecfb:0xb32333742eb30433!8m2!3d45.7727415!4d15.9839423!16s%2Fg" \
            "%2F11c2dklltz"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return self.__url
