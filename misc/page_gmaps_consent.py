from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_base import PageBase


class PageGmapsConsent(PageBase):
    __url = "https://consent.google.com/m?continue=https://www.google.com/maps/place/Zemljakova%2Bul.%2B3,%2B10000," \
            "%2BZagreb/@45.7727415,15.9839423," \
            "17z/data%3D!3m1!4b1!4m5!3m4!1s0x4765d5df1832ecfb:0xb32333742eb30433!8m2!3d45.7727415!4d15.9839423&gl=HR" \
            "&m=0&pc=m&uxe=eomtm&hl=hr&src=1"
    __prihvati_sve_button = (By.XPATH, "/html//body[@id='yDmH0d']/c-wiz[@class='SSPGKf']/div/div["
                                       "@class='kFwPee']//div[@class='VtwTSb']/form[2]//button/span["
                                       "@class='VfPpkd-vQzf8d']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def click_prihvati_sve_button(self):
        super()._click(self.__prihvati_sve_button)
