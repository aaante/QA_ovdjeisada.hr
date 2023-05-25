from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_base import PageBase


class PageKontakt(PageBase):
    __url = "https://ovdjeisada.hr/kontakt/"
    __cookies_prihvati_button = (By.XPATH, "//div[@id='cmplz-cookiebanner-container']/div[@role='dialog']//button["
                                           ".='Prihvati']")
    __large_map_widget_iframe = (By.XPATH, "//iframe[@height='444']")
    __large_map_widget_zoom_out_button = (By.XPATH, "/html//div[@id='map']/div["
                                                    "@class='leaflet-control-container']/div[1]/div/a[2]")
    __large_map_widget_zoom_in_button = (By.XPATH, "/html//div[@id='map']/div["
                                                   "@class='leaflet-control-container']/div[1]/div/a[1]")
    __large_map_widget_container = (By.XPATH, "//div[@id='map']")
    __form_fields = (By.XPATH, "//form[@class='et_pb_contact_form clearfix']")
    __ime = (By.XPATH, "/html//input[@id='et_pb_contact_ime_0']")
    __prezime = (By.XPATH, "/html//input[@id='et_pb_contact_prezime_0']")
    __mobitel = (By.XPATH, "/html//input[@id='et_pb_contact_mobitel_0']")
    __email = (By.XPATH, "/html//input[@id='et_pb_contact_e-mail_0']")
    __vasa_poruka = (By.XPATH, "/html//textarea[@id='et_pb_contact_poruka_0']")
    __hcaptcha_frame = (By.XPATH, "//iframe[@tabindex='0']")
    __hcaptcha_checkbox = (By.XPATH, "//div[@id='checkbox']")
    __posalji_button = (By.XPATH, "//div[@id='et_pb_contact_form_0']//form["
                                  "@action='https://ovdjeisada.hr/kontakt/']//button[@name='et_builder_submit_button']")
    __happy_path_actual_message = (By.XPATH, "//div[@id='et_pb_contact_form_0']//p")
    __unhappy_path_actual_message_1 = (By.XPATH, "//div[@id='et_pb_contact_form_0']//p[.='Please, fill in the "
                                                 "following fields:']")
    __unhappy_path_actual_message_ime = (By.XPATH, "//div[@id='et_pb_contact_form_0']/div["
                                                   "@class='et-pb-contact-message']/ul[1]/li[.='Ime']")
    __unhappy_path_actual_message_prezime = (By.XPATH, "//div[@id='et_pb_contact_form_0']/div["
                                                       "@class='et-pb-contact-message']/ul[1]/li[.='Prezime']")
    __unhappy_path_actual_message_email = (By.XPATH, "//div[@id='et_pb_contact_form_0']/div["
                                                     "@class='et-pb-contact-message']/ul[1]/li[.='E-mail']")
    __unhappy_path_actual_message_2 = (By.XPATH, "//div[@id='et_pb_contact_form_0']//ul/li[.='Invalid email']")
    __unhappy_path_actual_message_vasa_poruka = (By.XPATH, "//div[@id='et_pb_contact_form_0']/div["
                                                           "@class='et-pb-contact-message']/ul[1]/li[.='Vaša poruka']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def close_cookies(self):
        super()._click(self.__cookies_prihvati_button)

    def scroll_to_large_map_widget_iframe(self):
        super()._scroll_to(self.__large_map_widget_iframe)

    def switch_to_large_map_widget_iframe(self):
        super()._switch_to(self.__large_map_widget_iframe)

    def click_large_map_widget_zoom_out_button(self):
        super()._click(self.__large_map_widget_zoom_out_button)

    def click_large_map_widget_zoom_in_button(self):
        super()._click(self.__large_map_widget_zoom_in_button)

    def click_and_drag_on_large_map_widget_container(self):
        super()._click_and_drag(self.__large_map_widget_container)

    def scroll_to_form_fields(self):
        super()._scroll_to(self.__form_fields)

    def type_ime_1(self):
        super()._type(self.__ime, "%")

    def type_prezime_1(self):
        super()._type(self.__prezime, "%")

    def type_mobitel_1(self):
        super()._type(self.__mobitel, "")

    def type_email_1(self):
        super()._type(self.__email, "ante@ante.com")

    def type_vasa_poruka_1(self):
        super()._type(self.__vasa_poruka, "%")

    def switch_to_hcaptcha_frame(self):
        super()._switch_to(self.__hcaptcha_frame)

    def click_hcaptcha_checkbox(self):
        super()._click(self.__hcaptcha_checkbox)

    def click_posalji_button(self):
        super()._click(self.__posalji_button)

    def get_text_happy_path_actual_message(self):
        return super()._get_text(self.__happy_path_actual_message)

    def switch_to_default_content(self):
        super()._switch_to_default_content()

    def type_mobitel_2(self):
        super()._type(self.__mobitel, "12345678")

    def type_ime_2(self):
        super()._type(self.__ime, "")

    def get_text_unhappy_path_actual_message_1(self):
        return super()._get_text(self.__unhappy_path_actual_message_1)

    def get_text_unhappy_path_actual_message_ime(self):
        return super()._get_text(self.__unhappy_path_actual_message_ime)

    def type_prezime_2(self):
        super()._type(self.__prezime, "")

    def get_text_unhappy_path_actual_message_prezime(self):
        return super()._get_text(self.__unhappy_path_actual_message_prezime)

    def type_mobitel_3(self):
        super()._type(self.__mobitel, "%")

    def type_email_2(self):
        super()._type(self.__email, "")

    def get_text_unhappy_path_actual_message_email(self):
        return super()._get_text(self.__unhappy_path_actual_message_email)

    def type_email_3(self):
        super()._type(self.__email, "%")

    def get_text_unhappy_path_actual_message_2(self):
        return super()._get_text(self.__unhappy_path_actual_message_2)

    def type_vasa_poruka_2(self):
        super()._type(self.__vasa_poruka, "")

    def get_text_unhappy_path_actual_message_vasa_poruka(self):
        return super()._get_text(self.__unhappy_path_actual_message_vasa_poruka)

    @property
    def expected_url(self) -> str:
        return self.__url
