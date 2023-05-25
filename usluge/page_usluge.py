from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_base import PageBase


class PageUsluge(PageBase):
    __url = "https://ovdjeisada.hr/usluge/"
    __cookies_prihvati_button = (By.XPATH, "//div[@id='cmplz-cookiebanner-container']/div[@role='dialog']//button["
                                           ".='Prihvati']")
    __first_carousel = (By.XPATH, "//div[@class='slick-list']")
    __fc_first_carousel_element = (By.XPATH, "/html//div[@id='main-content']/article//div[@class='slick-list']/div["
                                             "@role='listbox']/div[1]/div[@class='et_pb_code_inner']")
    __fc_left_button = (By.XPATH, "/html//div[@id='main-content']/article/div[@class='entry-content']//div["
                                  "@class='et_pb_row et_pb_row_2']/div/button[1]")
    __fc_right_button = (By.XPATH, "/html//div[@id='main-content']/article/div[@class='entry-content']//div["
                                   "@class='et_pb_row et_pb_row_2']/div/button[2]")
    __fc_last_carousel_element = (By.XPATH, "/html//div[@id='main-content']/article//div[@class='slick-list']/div["
                                            "@role='listbox']/div[9]/div[@class='et_pb_code_inner']")
    __fc_seventh_carousel_element = (By.XPATH, "/html//div[@id='main-content']/article//div[@class='slick-list']/div["
                                               "@role='listbox']/div[7]/div[@class='et_pb_code_inner']")
    __fc_seventh_carousel_element_element_1 = (By.XPATH, "/html//div[@id='main-content']/article/div["
                                                         "@class='entry-content']//div[@class='slick-list']/div["
                                                         "@role='listbox']/div[6]//h2[@class='pricing_title']")
    __fc_seventh_carousel_element_element_2 = (By.XPATH, "/html//div[@id='main-content']/article/div["
                                                         "@class='entry-content']/div[@class='et-l et-l--post']//div["
                                                         "@class='slick-list']/div[@role='listbox']/div[7]//ul["
                                                         "@class='pricing']/li[1]/span[1]/img[@alt='Price tag ']")
    __fc_seventh_carousel_element_element_3 = (By.XPATH, "/html//div[@id='main-content']/article/div["
                                                         "@class='entry-content']//div[@class='slick-list']/div["
                                                         "@role='listbox']/div[7]//ul[@class='pricing']//span["
                                                         ".='70€/527,42kn (grupno)']")
    __fc_seventh_carousel_element_element_4 = (By.XPATH, "/html//div[@id='main-content']/article/div["
                                                         "@class='entry-content']/div[@class='et-l et-l--post']//div["
                                                         "@class='slick-list']/div[@role='listbox']/div[7]//ul["
                                                         "@class='pricing']/li[2]/span[1]/img[@alt='Price tag ']")
    __fc_seventh_carousel_element_element_5 = (By.XPATH, "/html//div[@id='main-content']/article/div["
                                                         "@class='entry-content']//div[@class='slick-list']/div["
                                                         "@role='listbox']/div[7]//ul[@class='pricing']//span["
                                                         ".='90€/678,11kn (individualno)']")
    __fc_seventh_carousel_element_element_6 = (By.XPATH, "/html//div[@id='main-content']/article/div["
                                                         "@class='entry-content']/div[@class='et-l et-l--post']//div["
                                                         "@class='slick-list']/div[@role='listbox']/div[7]//ul["
                                                         "@class='pricing']//img[@alt='Clock ']")
    __fc_seventh_carousel_element_element_7 = (By.XPATH, "/html//div[@id='main-content']/article/div["
                                                         "@class='entry-content']/div[@class='et-l et-l--post']//div["
                                                         "@class='slick-list']/div[@role='listbox']/div[7]//ul["
                                                         "@class='pricing']//span[.='60-90 min']")
    __fc_seventh_carousel_element_element_8 = (By.XPATH, "/html//div[@id='main-content']/article/div["
                                                         "@class='entry-content']//div[@class='slick-list']/div["
                                                         "@role='listbox']/div[7]//a["
                                                         "@href='/usluge/rad-s-djecom/kako-nauciti-uciti/']")
    __fc_seventh_carousel_element_element_9 = (By.XPATH, "/html//div[@id='main-content']/article/div["
                                                         "@class='entry-content']//div[@class='slick-list']/div["
                                                         "@role='listbox']/div[7]//a["
                                                         "@href='/usluge/rad-s-mladima/radionice-kako-uciti/']")
    __locator_list = [__fc_seventh_carousel_element_element_1, __fc_seventh_carousel_element_element_2,
                      __fc_seventh_carousel_element_element_3, __fc_seventh_carousel_element_element_4,
                      __fc_seventh_carousel_element_element_5, __fc_seventh_carousel_element_element_6,
                      __fc_seventh_carousel_element_element_7, __fc_seventh_carousel_element_element_8,
                      __fc_seventh_carousel_element_element_9]

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def close_cookies(self):
        super()._click(self.__cookies_prihvati_button)

    def scroll_to_first_carousel(self):
        super()._scroll_to(self.__first_carousel)

    def find_fc_first_carousel_element(self):
        return super()._find(self.__fc_first_carousel_element)

    def find_fc_left_button(self):
        return super()._find(self.__fc_left_button)

    def find_fc_right_button(self):
        return super()._find(self.__fc_right_button)

    def find_fc_last_carousel_element(self):
        return super()._find(self.__fc_last_carousel_element)

    def find_fc_seventh_carousel_element(self):
        return super()._find(self.__fc_seventh_carousel_element)

    def check_elements_displayed_seventh_carousel_element(self):
        super()._check_elements_displayed(self._driver, self.__locator_list)

    @property
    def expected_url(self) -> str:
        return self.__url
