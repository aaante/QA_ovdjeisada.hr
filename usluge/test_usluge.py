import time

import pytest

from usluge.page_usluge import PageUsluge


class TestBody:

    @pytest.mark.usluge
    def test_first_carousel(self, driver):
        usluge = PageUsluge(driver)
        usluge.open()
        usluge.close_cookies()
        usluge.scroll_to_first_carousel()
        first_carousel_element = usluge.find_fc_first_carousel_element()
        current_position_of_first_carousel_element = first_carousel_element.location['x']
        print("Current position of the first carousel element:", current_position_of_first_carousel_element)
        time.sleep(2)  # This time.sleep is necessary for the method to function
        for i in range(9):
            left_button = usluge.find_fc_left_button()
            left_button_aria_disabled = left_button.get_attribute("aria-disabled")
            if "true" not in left_button_aria_disabled:
                left_button.click()
                print("Left button clicked")
                new_position_of_first_carousel_element = first_carousel_element.location['x']
                print("New position of the first carousel element:", new_position_of_first_carousel_element)
                if new_position_of_first_carousel_element > current_position_of_first_carousel_element:
                    print("Moved carousel to the left")
                    current_position_of_first_carousel_element = new_position_of_first_carousel_element
                else:
                    print("Carousel did not move to the left")
                    break
                time.sleep(1)  # This time.sleep is necessary for the method to function
            else:
                print("Reached the end of the carousel to the left")
                break
        for i in range(9):
            right_button = usluge.find_fc_right_button()
            right_button_aria_disabled = right_button.get_attribute("aria-disabled")
            if "true" not in right_button_aria_disabled:
                right_button.click()
                print("Right button clicked")
                new_position_of_first_carousel_element = first_carousel_element.location['x']
                print("New position of the first carousel element:", new_position_of_first_carousel_element)
                if new_position_of_first_carousel_element < current_position_of_first_carousel_element:
                    print("Moved carousel to the right")
                    current_position_of_first_carousel_element = new_position_of_first_carousel_element
                else:
                    print("Carousel did not move to the right")
                    break
                time.sleep(1)  # This time.sleep is necessary for the method to function
            else:
                print("Reached the end of the carousel to the right")
                break
        last_carousel_element = usluge.find_fc_last_carousel_element()
        current_position_of_last_carousel_element = last_carousel_element.location['x']
        print("Current position of the last carousel element:", current_position_of_last_carousel_element)
        time.sleep(2)  # This time.sleep is necessary for the method to function
        for i in range(9):
            left_button = usluge.find_fc_left_button()
            left_button_aria_disabled = left_button.get_attribute("aria-disabled")
            if "true" not in left_button_aria_disabled:
                left_button.click()
                print("Left button clicked")
                new_position_of_last_carousel_element = last_carousel_element.location['x']
                print("New position of the last carousel element:", new_position_of_last_carousel_element)
                if new_position_of_last_carousel_element >= current_position_of_last_carousel_element:
                    print("Moved carousel to the left")
                    current_position_of_last_carousel_element = new_position_of_last_carousel_element
                else:
                    print("Carousel did not move to the left")
                    break
                time.sleep(1)  # This time.sleep is necessary for the method to function
            else:
                print("Reached the end of the carousel to the left")
                break

    @pytest.mark.usluge
    def test_first_carousel_seventh_carousel_element(self, driver):
        usluge = PageUsluge(driver)
        usluge.open()
        usluge.close_cookies()
        usluge.scroll_to_first_carousel()
        seventh_carousel_element = usluge.find_fc_seventh_carousel_element()
        if seventh_carousel_element.is_displayed() is True:
            print("Seventh carousel element IS displayed")
            usluge.check_elements_displayed_seventh_carousel_element()
        else:
            while not seventh_carousel_element.is_displayed():
                right_button = usluge.find_fc_right_button()
                right_button_aria_disabled = right_button.get_attribute("aria-disabled")
                if "true" in right_button_aria_disabled:
                    print("Reached the end of the carousel to the right and seventh carousel element is not displayed")
                    break
                right_button.click()
                print("Right button clicked")
                time.sleep(1)  # This time.sleep is necessary for the method to function
                print("Is seventh carousel element displayed?", seventh_carousel_element.is_displayed())
                if seventh_carousel_element.is_displayed() is True:
                    print("Seventh carousel element IS displayed")
                    time.sleep(1)  # This time.sleep is necessary for the method to function
                    usluge.check_elements_displayed_seventh_carousel_element()
                    break
