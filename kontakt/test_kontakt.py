import time

import pytest

from kontakt.page_kontakt import PageKontakt


class TestBody:

    @pytest.mark.kontakt
    def test_large_map_widget(self, driver):
        kontakt = PageKontakt(driver)
        kontakt.open()
        kontakt.close_cookies()
        kontakt.scroll_to_large_map_widget_iframe()
        kontakt.switch_to_large_map_widget_iframe()
        kontakt.click_large_map_widget_zoom_out_button()
        kontakt.click_large_map_widget_zoom_in_button()
        kontakt.click_and_drag_on_large_map_widget_container()
        print("Large map widget is functional")

    @pytest.mark.kontakt
    def test_contact_form_happy_path_1(self, driver):
        kontakt = PageKontakt(driver)
        kontakt.open()
        kontakt.close_cookies()
        kontakt.scroll_to_form_fields()
        kontakt.type_ime_1()
        print("Typed '%' in 'Ime' input field")
        kontakt.type_prezime_1()
        print("Typed '%' in 'Prezime' input field")
        kontakt.type_mobitel_1()
        print("Typed nothing in 'Mobitel' input field")
        kontakt.type_email_1()
        print("Typed 'ante@ante.com' in 'E-mail' input field")
        kontakt.type_vasa_poruka_1()
        print("Typed '%' in 'Vaša poruka' input field")
        kontakt.switch_to_hcaptcha_frame()
        kontakt.click_hcaptcha_checkbox()
        time.sleep(25)  # This time.sleep is necessary for manually solving the captcha
        kontakt.switch_to_default_content()
        kontakt.click_posalji_button()
        time.sleep(10)  # This time.sleep is necessary for the method to function: 'wait.until(
        # ec.visibility_of_element_located' doesn't work here
        confirmation_message = "Hvala Vam što ste nam se javili, odgovorit ćemo u najkraćem mogućem roku! 🙂"
        assert kontakt.get_text_happy_path_actual_message() == confirmation_message, "Wrong confirmation message"
        print("Correct confirmation message is displayed")

    @pytest.mark.kontakt
    def test_contact_form_happy_path_2(self, driver):
        kontakt = PageKontakt(driver)
        kontakt.open()
        kontakt.close_cookies()
        kontakt.scroll_to_form_fields()
        kontakt.type_ime_1()
        print("Typed '%' in 'Ime' input field")
        kontakt.type_prezime_1()
        print("Typed '%' in 'Prezime' input field")
        kontakt.type_mobitel_2()
        print("Typed '12345678' in 'Mobitel' input field")
        kontakt.type_email_1()
        print("Typed 'ante@ante.com' in 'E-mail' input field")
        kontakt.type_vasa_poruka_1()
        print("Typed '%' in 'Vaša poruka' input field")
        kontakt.switch_to_hcaptcha_frame()
        kontakt.click_hcaptcha_checkbox()
        time.sleep(25)  # This time.sleep is necessary for manually solving the captcha
        kontakt.switch_to_default_content()
        kontakt.click_posalji_button()
        time.sleep(10)  # This time.sleep is necessary for the method to function: 'wait.until(
        # ec.visibility_of_element_located' doesn't work here
        confirmation_message = "Hvala Vam što ste nam se javili, odgovorit ćemo u najkraćem mogućem roku! 🙂"
        assert kontakt.get_text_happy_path_actual_message() == confirmation_message, "Wrong confirmation message"
        print("Correct confirmation message is displayed")

    @pytest.mark.kontakt
    def test_contact_form_unhappy_path_1(self, driver):
        kontakt = PageKontakt(driver)
        kontakt.open()
        kontakt.close_cookies()
        kontakt.scroll_to_form_fields()
        kontakt.type_ime_2()
        print("Typed nothing in 'Ime' input field")
        kontakt.type_prezime_1()
        print("Typed '%' in 'Prezime' input field")
        kontakt.type_mobitel_1()
        print("Typed nothing in 'Mobitel' input field")
        kontakt.type_email_1()
        print("Typed 'ante@ante.com' in 'E-mail' input field")
        kontakt.type_vasa_poruka_1()
        print("Typed '%' in 'Vaša poruka' input field")
        kontakt.switch_to_hcaptcha_frame()
        kontakt.click_hcaptcha_checkbox()
        time.sleep(25)  # This time.sleep is necessary for manually solving the captcha
        kontakt.switch_to_default_content()
        kontakt.click_posalji_button()
        time.sleep(10)  # This time.sleep is necessary for the method to function: 'wait.until(
        # ec.visibility_of_element_located' doesn't work here
        error_message_1 = "Please, fill in the following fields:"
        error_message_2 = "Ime"
        assert kontakt.get_text_unhappy_path_actual_message_1() == error_message_1, "Wrong error message"
        assert kontakt.get_text_unhappy_path_actual_message_ime() == error_message_2, "Wrong error message"
        print("Correct error message is displayed")

    @pytest.mark.kontakt
    def test_contact_form_unhappy_path_2(self, driver):
        kontakt = PageKontakt(driver)
        kontakt.open()
        kontakt.close_cookies()
        kontakt.scroll_to_form_fields()
        kontakt.type_ime_1()
        print("Typed '%' in 'Ime' input field")
        kontakt.type_prezime_2()
        print("Typed nothing in 'Prezime' input field")
        kontakt.type_mobitel_1()
        print("Typed nothing in 'Mobitel' input field")
        kontakt.type_email_1()
        print("Typed 'ante@ante.com' in 'E-mail' input field")
        kontakt.type_vasa_poruka_1()
        print("Typed '%' in 'Vaša poruka' input field")
        kontakt.switch_to_hcaptcha_frame()
        kontakt.click_hcaptcha_checkbox()
        time.sleep(25)  # This time.sleep is necessary for manually solving the captcha
        kontakt.switch_to_default_content()
        kontakt.click_posalji_button()
        time.sleep(10)  # This time.sleep is necessary for the method to function: 'wait.until(
        # ec.visibility_of_element_located' doesn't work here
        error_message_1 = "Please, fill in the following fields:"
        error_message_2 = "Prezime"
        assert kontakt.get_text_unhappy_path_actual_message_1() == error_message_1, "Wrong error message"
        assert kontakt.get_text_unhappy_path_actual_message_prezime() == error_message_2, "Wrong error message"
        print("Correct error message is displayed")

    # ❓INCOMPLETE👇
    @pytest.mark.kontakt
    def test_contact_form_unhappy_path_3(self, driver):
        kontakt = PageKontakt(driver)
        kontakt.open()
        kontakt.close_cookies()
        kontakt.scroll_to_form_fields()
        kontakt.type_ime_1()
        print("Typed '%' in 'Ime' input field")
        kontakt.type_prezime_1()
        print("Typed '%' in 'Prezime' input field")
        kontakt.type_mobitel_3()
        print("Typed '%' in 'Mobitel' input field")
        kontakt.type_email_1()
        print("Typed 'ante@ante.com' in 'E-mail' input field")
        kontakt.type_vasa_poruka_1()
        print("Typed '%' in 'Vaša poruka' input field")
        kontakt.switch_to_hcaptcha_frame()
        kontakt.click_hcaptcha_checkbox()
        time.sleep(25)  # This time.sleep is necessary for manually solving the captcha
        kontakt.switch_to_default_content()
        kontakt.click_posalji_button()
        time.sleep(10)  # This time.sleep is necessary for the method to function: 'wait.until(
        # ec.visibility_of_element_located' doesn't work here
        alert_pop_up = driver.switch_to.alert
        alert_text = alert_pop_up.text
        error_message = "Please, match the format requested. Only numbers allowed. Minimum length: 8 characters"
        assert alert_text == error_message, "Wrong error message"
        print("Correct error message is displayed")

    @pytest.mark.kontakt
    def test_contact_form_unhappy_path_4(self, driver):
        kontakt = PageKontakt(driver)
        kontakt.open()
        kontakt.close_cookies()
        kontakt.scroll_to_form_fields()
        kontakt.type_ime_1()
        print("Typed '%' in 'Ime' input field")
        kontakt.type_prezime_1()
        print("Typed '%' in 'Prezime' input field")
        kontakt.type_mobitel_1()
        print("Typed nothing in 'Mobitel' input field")
        kontakt.type_email_2()
        print("Typed nothing in 'E-mail' input field")
        kontakt.type_vasa_poruka_1()
        print("Typed '%' in 'Vaša poruka' input field")
        kontakt.switch_to_hcaptcha_frame()
        kontakt.click_hcaptcha_checkbox()
        time.sleep(25)  # This time.sleep is necessary for manually solving the captcha
        kontakt.switch_to_default_content()
        kontakt.click_posalji_button()
        time.sleep(10)  # This time.sleep is necessary for the method to function: 'wait.until(
        # ec.visibility_of_element_located' doesn't work here
        error_message_1 = "Please, fill in the following fields:"
        error_message_2 = "E-mail"
        assert kontakt.get_text_unhappy_path_actual_message_1() == error_message_1, "Wrong error message"
        assert kontakt.get_text_unhappy_path_actual_message_email() == error_message_2, "Wrong error message"
        print("Correct error message is displayed")

    @pytest.mark.kontakt
    def test_contact_form_unhappy_path_5(self, driver):
        kontakt = PageKontakt(driver)
        kontakt.open()
        kontakt.close_cookies()
        kontakt.scroll_to_form_fields()
        kontakt.type_ime_1()
        print("Typed '%' in 'Ime' input field")
        kontakt.type_prezime_1()
        print("Typed '%' in 'Prezime' input field")
        kontakt.type_mobitel_1()
        print("Typed nothing in 'Mobitel' input field")
        kontakt.type_email_3()
        print("Typed '%' in 'E-mail' input field")
        kontakt.type_vasa_poruka_1()
        print("Typed '%' in 'Vaša poruka' input field")
        kontakt.switch_to_hcaptcha_frame()
        kontakt.click_hcaptcha_checkbox()
        time.sleep(25)  # This time.sleep is necessary for manually solving the captcha
        kontakt.switch_to_default_content()
        kontakt.click_posalji_button()
        time.sleep(10)  # This time.sleep is necessary for the method to function: 'wait.until(
        # ec.visibility_of_element_located' doesn't work here
        error_message = "Invalid email"
        assert kontakt.get_text_unhappy_path_actual_message_2() == error_message, "Wrong error message"
        print("Correct error message is displayed")

    @pytest.mark.kontakt
    def test_contact_form_unhappy_path_6(self, driver):
        kontakt = PageKontakt(driver)
        kontakt.open()
        kontakt.close_cookies()
        kontakt.scroll_to_form_fields()
        kontakt.type_ime_1()
        print("Typed '%' in 'Ime' input field")
        kontakt.type_prezime_1()
        print("Typed '%' in 'Prezime' input field")
        kontakt.type_mobitel_1()
        print("Typed nothing in 'Mobitel' input field")
        kontakt.type_email_1()
        print("Typed 'ante@ante.com' in 'E-mail' input field")
        kontakt.type_vasa_poruka_2()
        print("Typed nothing in 'Vaša poruka' input field")
        kontakt.switch_to_hcaptcha_frame()
        kontakt.click_hcaptcha_checkbox()
        time.sleep(25)  # This time.sleep is necessary for manually solving the captcha
        kontakt.switch_to_default_content()
        kontakt.click_posalji_button()
        time.sleep(10)  # This time.sleep is necessary for the method to function: 'wait.until(
        # ec.visibility_of_element_located' doesn't work here
        error_message_1 = "Please, fill in the following fields:"
        error_message_2 = "Vaša poruka"
        assert kontakt.get_text_unhappy_path_actual_message_1() == error_message_1, "Wrong error message"
        assert kontakt.get_text_unhappy_path_actual_message_vasa_poruka() == error_message_2, "Wrong error message"
        print("Correct error message is displayed")
