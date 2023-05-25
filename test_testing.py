# This is the place for testing the more complex tests, before moving them to corresponding test pages

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
action = ActionChains(driver)
wait = WebDriverWait(driver, 10)
alert = Alert(driver)


# DONE ✅
def test_rad_s_djecom_individualni_savjetodavni_rad_link():
    # Open page
    driver.get("https://ovdjeisada.hr/")
    time.sleep(2)
    # Hover over 'Usluge' link
    usluge_link = driver.find_element(By.XPATH,
                                      "//ul[@id='menu-navigation']//a[@href='https://ovdjeisada.hr/usluge/']")
    action.move_to_element(usluge_link).perform()
    time.sleep(2)
    # Hover over 'Rad s djecom' link
    rad_s_djecom_link = driver.find_element(By.XPATH,
                                            "//ul[@id='menu-navigation']/li[2]/ul[@class='sub-menu']//a["
                                            "@href='https://ovdjeisada.hr/usluge/rad-s-djecom/']")
    action.move_to_element(rad_s_djecom_link).perform()
    time.sleep(2)
    # Click on 'Individualni savjetodavni rad' link
    individualni_savjetodavni_rad_link = driver.find_element(By.XPATH,
                                                             "//ul[@id='menu-navigation']/li[2]/ul["
                                                             "@class='sub-menu']/li["
                                                             "1]/ul[@class='sub-menu']//a["
                                                             "@href='https://ovdjeisada.hr/usluge/rad-s-djecom/djecji"
                                                             "-psiholog/']")
    action.move_to_element(individualni_savjetodavni_rad_link).perform()
    time.sleep(2)
    individualni_savjetodavni_rad_link.click()
    # Verify that "https://ovdjeisada.hr/usluge/rad-s-djecom/djecji-psiholog/" is opened
    actual_url = driver.current_url
    assert actual_url == "https://ovdjeisada.hr/usluge/rad-s-djecom/djecji-psiholog/", "Expected URL not opened"
    time.sleep(2)
    # Tested with no time.sleep and it functions


# DONE ✅
def test_small_map_widget():
    # Open page
    driver.get("https://ovdjeisada.hr/")
    time.sleep(2)
    # Close cookies pop up by clicking 'Prihvati' button
    cookies_prihvati_button = driver.find_element(By.XPATH, "//button[@class='cmplz-btn cmplz-accept']")
    cookies_prihvati_button.click()
    time.sleep(2)
    # Find small map widget
    small_map_widget = driver.find_element(By.XPATH, "//iframe[@height='165']")
    # Scroll to the small map widget location
    driver.execute_script("arguments[0].scrollIntoView();", small_map_widget)
    time.sleep(2)
    wait.until(ec.visibility_of(small_map_widget))
    # Switch driver to small map widget frame
    driver.switch_to.frame(small_map_widget)
    # Click '-' icon once for zooming out
    zoom_out_button = driver.find_element(By.XPATH, "/html//div[@id='map']/div["
                                                    "@class='leaflet-control-container']/div[1]/div/a[2]")
    zoom_out_button.click()
    time.sleep(2)
    # Click '+' icon once for zooming in
    zoom_in_button = driver.find_element(By.XPATH, "/html//div[@id='map']/div["
                                                   "@class='leaflet-control-container']/div[1]/div/a[1]")
    zoom_in_button.click()
    time.sleep(2)
    # Find small map widget container
    small_map_widget_container = driver.find_element(By.XPATH, "//div[@id='map']")
    # Click & drag somewhere on the map, the travel distance should be 20px to the left, than 20px to the right,
    # than 20px to the top, and then 20px to the bottom
    action.move_to_element(small_map_widget_container).click_and_hold().move_by_offset(-20, 0).pause(1). \
        move_by_offset(40, 0).pause(1).move_by_offset(0, -20).pause(1).move_by_offset(0, 40).release().perform()
    time.sleep(2)
    # Tested with no time.sleep and it functions


# DONE ✅
def test_large_map_widget():
    # Open page
    driver.get("https://ovdjeisada.hr/kontakt/")
    time.sleep(2)
    # Close cookies pop up by clicking 'Prihvati' button
    cookies_prihvati_button = driver.find_element(By.XPATH, "//button[@class='cmplz-btn cmplz-accept']")
    cookies_prihvati_button.click()
    time.sleep(2)
    # Find large map widget
    large_map_widget = driver.find_element(By.XPATH, "//iframe[@height='444']")
    # Scroll to the large map widget location
    driver.execute_script("arguments[0].scrollIntoView();", large_map_widget)
    time.sleep(2)
    wait.until(ec.visibility_of(large_map_widget))
    # Switch driver to large map widget frame
    driver.switch_to.frame(large_map_widget)
    # Click '-' icon once for zooming out
    zoom_out_button = driver.find_element(By.XPATH, "/html//div[@id='map']/div["
                                                    "@class='leaflet-control-container']/div[1]/div/a[2]")
    zoom_out_button.click()
    time.sleep(2)
    # Click '+' icon once for zooming in
    zoom_in_button = driver.find_element(By.XPATH, "/html//div[@id='map']/div["
                                                   "@class='leaflet-control-container']/div[1]/div/a[1]")
    zoom_in_button.click()
    time.sleep(2)
    # Find large map widget container
    large_map_widget_container = driver.find_element(By.XPATH, "//div[@id='map']")
    # Click & drag somewhere on the map, the travel distance should be 20px to the left, than 20px to the right,
    # than 20px to the top, and then 20px to the bottom
    action.move_to_element(large_map_widget_container).click_and_hold().move_by_offset(-20, 0).pause(1). \
        move_by_offset(40, 0).pause(1).move_by_offset(0, -20).pause(1).move_by_offset(0, 40).release().perform()
    time.sleep(2)
    # Tested with no time.sleep and it functions


# DONE ✅
def test_first_carousel():
    # Open page
    driver.get("https://ovdjeisada.hr/usluge/")
    time.sleep(2)
    # Close cookies pop up by clicking 'Prihvati' button
    cookies_prihvati_button = driver.find_element(By.XPATH, "//button[@class='cmplz-btn cmplz-accept']")
    cookies_prihvati_button.click()
    time.sleep(2)
    # Find carousel
    carousel = driver.find_element(By.XPATH, "//div[@class='slick-list']")
    # Scroll to the carousel location
    driver.execute_script("arguments[0].scrollIntoView();", carousel)
    time.sleep(2)
    # Find first carousel element
    first_carousel_element = driver.find_element(By.XPATH, "/html//div[@id='main-content']/article//div["
                                                           "@class='slick-list']/div[@role='listbox']/div[1]/div["
                                                           "@class='et_pb_code_inner']")
    # Get the current position of the first element in the carousel
    current_position_of_first_carousel_element = first_carousel_element.location['x']
    print("Current position of the first carousel element:", current_position_of_first_carousel_element)
    time.sleep(2)  # This time.sleep is necessary for the method to function
    # Loop through the carousel to the left
    for i in range(9):
        # click the left button
        left_button = driver.find_element(By.XPATH, "/html//div[@id='main-content']/article/div["
                                                    "@class='entry-content']//div[@class='et_pb_row "
                                                    "et_pb_row_2']/div/button[1]")
        left_button_aria_disabled = left_button.get_attribute("aria-disabled")
        if "true" not in left_button_aria_disabled:
            left_button.click()
            print("Left button clicked")
            # verify that the carousel has moved to the left
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
    # Loop through the carousel to the right
    for i in range(9):
        # click the right button
        right_button = driver.find_element(By.XPATH, "/html//div[@id='main-content']/article/div["
                                                     "@class='entry-content']//div[@class='et_pb_row "
                                                     "et_pb_row_2']/div/button[2]")
        right_button_aria_disabled = right_button.get_attribute("aria-disabled")
        if "true" not in right_button_aria_disabled:
            right_button.click()
            print("Right button clicked")
            # verify that the carousel has moved to the right
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
    # Find last carousel element
    last_carousel_element = driver.find_element(By.XPATH, "/html//div[@id='main-content']/article//div["
                                                          "@class='slick-list']/div[@role='listbox']/div[9]/div["
                                                          "@class='et_pb_code_inner']")
    # Get the current position of the last element in the carousel
    current_position_of_last_carousel_element = last_carousel_element.location['x']
    print("Current position of the last carousel element:", current_position_of_last_carousel_element)
    time.sleep(2)  # This time.sleep is necessary for the method to function
    # Loop through the carousel to the left
    for i in range(9):
        # click the left button
        left_button = driver.find_element(By.XPATH, "/html//div[@id='main-content']/article/div["
                                                    "@class='entry-content']//div[@class='et_pb_row "
                                                    "et_pb_row_2']/div/button[1]")
        left_button_aria_disabled = left_button.get_attribute("aria-disabled")
        if "true" not in left_button_aria_disabled:
            left_button.click()
            print("Left button clicked")
            # verify that the carousel has moved to the left
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
    # Tested with no time.sleep and it functions


# DONE ✅
def test_first_carousel_seventh_carousel_element():
    # Open page
    driver.get("https://ovdjeisada.hr/usluge/")
    time.sleep(2)
    # Close cookies pop up by clicking 'Prihvati' button
    cookies_prihvati_button = driver.find_element(By.XPATH, "//button[@class='cmplz-btn cmplz-accept']")
    cookies_prihvati_button.click()
    time.sleep(2)
    # Find carousel
    carousel = driver.find_element(By.XPATH, "//div[@class='slick-list']")

    # Scroll to the carousel location
    driver.execute_script("arguments[0].scrollIntoView();", carousel)
    time.sleep(2)
    # Find seventh carousel element
    seventh_carousel_element = driver.find_element(By.XPATH, "/html//div[@id='main-content']/article//div["
                                                             "@class='slick-list']/div[@role='listbox']/div[7]/div["
                                                             "@class='et_pb_code_inner']")

    # Define the list of XPaths of elements inside seventh carousel element
    xpath_list = [
        "/html//div[@id='main-content']/article/div[@class='entry-content']//div[@class='slick-list']/div["
        "@role='listbox']/div[6]//h2[@class='pricing_title']",
        "/html//div[@id='main-content']/article/div[@class='entry-content']/div[@class='et-l et-l--post']//div["
        "@class='slick-list']/div[@role='listbox']/div[7]//ul[@class='pricing']/li[1]/span[1]/img[@alt='Price tag ']",
        "/html//div[@id='main-content']/article/div[@class='entry-content']//div[@class='slick-list']/div["
        "@role='listbox']/div[7]//ul[@class='pricing']//span[.='70€/527,42kn (grupno)']",
        "/html//div[@id='main-content']/article/div[@class='entry-content']/div[@class='et-l et-l--post']//div["
        "@class='slick-list']/div[@role='listbox']/div[7]//ul[@class='pricing']/li[2]/span[1]/img[@alt='Price tag ']",
        "/html//div[@id='main-content']/article/div[@class='entry-content']//div[@class='slick-list']/div["
        "@role='listbox']/div[7]//ul[@class='pricing']//span[.='90€/678,11kn (individualno)']",
        "/html//div[@id='main-content']/article/div[@class='entry-content']/div[@class='et-l et-l--post']//div["
        "@class='slick-list']/div[@role='listbox']/div[7]//ul[@class='pricing']//img[@alt='Clock ']",
        "/html//div[@id='main-content']/article/div[@class='entry-content']/div[@class='et-l et-l--post']//div["
        "@class='slick-list']/div[@role='listbox']/div[7]//ul[@class='pricing']//span[.='60-90 min']",
        "/html//div[@id='main-content']/article/div[@class='entry-content']//div[@class='slick-list']/div["
        "@role='listbox']/div[7]//a[@href='/usluge/rad-s-djecom/kako-nauciti-uciti/']",
        "/html//div[@id='main-content']/article/div[@class='entry-content']//div[@class='slick-list']/div["
        "@role='listbox']/div[7]//a[@href='/usluge/rad-s-mladima/radionice-kako-uciti/']"
    ]
    # Is seventh carousel element displayed?
    if seventh_carousel_element.is_displayed() is True:
        print("Seventh carousel element IS displayed")
        # Check if all the elements inside the seventh carousel are displayed
        check_elements_displayed(driver, xpath_list)
    else:
        # Loop through the carousel with right click until it is displayed
        while not seventh_carousel_element.is_displayed():
            right_button = driver.find_element(By.XPATH,
                                               "/html//div[@id='main-content']/article/div["
                                               "@class='entry-content']//div[@class='et_pb_row "
                                               "et_pb_row_2']/div/button[2]")
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
                # Check if all the elements inside the seventh carousel are displayed
                time.sleep(1)  # This time.sleep is necessary for the method to function
                check_elements_displayed(driver, xpath_list)
                break
    # Tested with no time.sleep and it functions


def check_elements_displayed(driver, xpath_list):
    # Initialize an empty list to store the web elements
    elements = []
    # Iterate over the XPath expressions and find the elements
    for xpath in xpath_list:
        elements.extend(driver.find_elements(By.XPATH, xpath))
    # Print the number of elements
    print("Number of elements:", len(elements))
    # Check if all elements are displayed
    all_displayed = True
    not_displayed_elements = []
    for element in elements:
        if not element.is_displayed():
            all_displayed = False
            not_displayed_elements.append(element)
    # Print the result
    if all_displayed:
        print("All elements are displayed")
    else:
        print("Not all elements are displayed:")
        for element in not_displayed_elements:
            print("- Element:", element)


# DONE ✅
def test_contact_form_happy_path_1():
    # Open page
    driver.get("https://ovdjeisada.hr/kontakt/")
    time.sleep(1)
    # Close cookies pop up by clicking 'Prihvati' button
    cookies_prihvati_button = driver.find_element(By.XPATH, "//button[@class='cmplz-btn cmplz-accept']")
    cookies_prihvati_button.click()
    time.sleep(1)
    # Find form fields
    form_fields = driver.find_element(By.XPATH, "//form[@class='et_pb_contact_form clearfix']")
    # Scroll to the form fields location
    driver.execute_script("arguments[0].scrollIntoView();", form_fields)
    time.sleep(1)
    # Type "%" in 'Ime' input field
    ime = driver.find_element(By.XPATH, "/html//input[@id='et_pb_contact_ime_0']")
    ime.send_keys("%")
    print("Typed '%' in 'Ime' input field")
    time.sleep(1)
    # Type "%" in 'Prezime' input field
    prezime = driver.find_element(By.XPATH, "/html//input[@id='et_pb_contact_prezime_0']")
    prezime.send_keys("%")
    print("Typed '%' in 'Prezime' input field")
    time.sleep(1)
    # Type "" in 'Mobitel' input field
    mobitel = driver.find_element(By.XPATH, "/html//input[@id='et_pb_contact_mobitel_0']")
    mobitel.send_keys("")
    print("Typed nothing in 'Mobitel' input field")
    time.sleep(1)
    # Type "ante@ante.com" in 'E-mail' input field
    email = driver.find_element(By.XPATH, "/html//input[@id='et_pb_contact_e-mail_0']")
    email.send_keys("ante@ante.com")
    print("Typed 'ante@ante.com' in 'E-mail' input field")
    time.sleep(1)
    # Type "%" in 'Vaša poruka' input field
    vasa_poruka = driver.find_element(By.XPATH, "/html//textarea[@id='et_pb_contact_poruka_0']")
    vasa_poruka.send_keys("%")
    print("Typed '%' in 'Vaša poruka' input field")
    time.sleep(1)
    # Switch driver to hcaptcha frame
    hcaptcha_frame = driver.find_element(By.XPATH, "//iframe[@tabindex='0']")
    driver.switch_to.frame(hcaptcha_frame)
    # Click hCaptcha checkbox
    hcaptcha = driver.find_element(By.XPATH, "//div[@id='checkbox']")
    hcaptcha.click()
    # Solve hCaptcha
    time.sleep(25)  # This time.sleep is necessary for manually solving the captcha
    # Switch driver to default content
    driver.switch_to.default_content()
    # Click 'Pošalji' button
    posalji_button = driver.find_element(By.XPATH, "//div[@id='et_pb_contact_form_0']//form["
                                                   "@action='https://ovdjeisada.hr/kontakt/']//button["
                                                   "@name='et_builder_submit_button']")
    posalji_button.click()
    # Verify that "Hvala Vam što ste nam se javili, odgovorit ćemo u najkraćem mogućem roku! 🙂" message is displayed
    time.sleep(5)  # This time.sleep is necessary for the method to function: 'wait.until(
    # ec.visibility_of_element_located' doesn't work here
    actual_message = driver.find_element(By.XPATH, "//div[@id='et_pb_contact_form_0']//p")
    confirmation_message = "Hvala Vam što ste nam se javili, odgovorit ćemo u najkraćem mogućem roku! 🙂"
    assert actual_message.text == confirmation_message, "Wrong confirmation message"
    print("Correct confirmation message is displayed")
    # Tested with no time.sleep and it functions


# DONE ✅
def test_contact_form_happy_path_2():
    # Open page
    driver.get("https://ovdjeisada.hr/kontakt/")
    time.sleep(1)
    # Close cookies pop up by clicking 'Prihvati' button
    cookies_prihvati_button = driver.find_element(By.XPATH, "//button[@class='cmplz-btn cmplz-accept']")
    cookies_prihvati_button.click()
    time.sleep(1)
    # Find form fields
    form_fields = driver.find_element(By.XPATH, "//form[@class='et_pb_contact_form clearfix']")
    # Scroll to the form fields location
    driver.execute_script("arguments[0].scrollIntoView();", form_fields)
    time.sleep(1)
    # Type "%" in 'Ime' input field
    ime = driver.find_element(By.XPATH, "/html//input[@id='et_pb_contact_ime_0']")
    ime.send_keys("%")
    print("Typed '%' in 'Ime' input field")
    time.sleep(1)
    # Type "%" in 'Prezime' input field
    prezime = driver.find_element(By.XPATH, "/html//input[@id='et_pb_contact_prezime_0']")
    prezime.send_keys("%")
    print("Typed '%' in 'Prezime' input field")
    time.sleep(1)
    # Type "12345678" in 'Mobitel' input field
    mobitel = driver.find_element(By.XPATH, "/html//input[@id='et_pb_contact_mobitel_0']")
    mobitel.send_keys("12345678")
    print("Typed '12345678' in 'Mobitel' input field")
    time.sleep(1)
    # Type "ante@ante.com" in 'E-mail' input field
    email = driver.find_element(By.XPATH, "/html//input[@id='et_pb_contact_e-mail_0']")
    email.send_keys("ante@ante.com")
    print("Typed 'ante@ante.com' in 'E-mail' input field")
    time.sleep(1)
    # Type "%" in 'Vaša poruka' input field
    vasa_poruka = driver.find_element(By.XPATH, "/html//textarea[@id='et_pb_contact_poruka_0']")
    vasa_poruka.send_keys("%")
    print("Typed '%' in 'Vaša poruka' input field")
    time.sleep(1)
    # Switch driver to hcaptcha frame
    hcaptcha_frame = driver.find_element(By.XPATH, "//iframe[@tabindex='0']")
    driver.switch_to.frame(hcaptcha_frame)
    # Click hCaptcha checkbox
    hcaptcha = driver.find_element(By.XPATH, "//div[@id='checkbox']")
    hcaptcha.click()
    # Solve hCaptcha
    time.sleep(25)  # This time.sleep is necessary for manually solving the captcha
    # Switch driver to default content
    driver.switch_to.default_content()
    # Click 'Pošalji' button
    posalji_button = driver.find_element(By.XPATH, "//div[@id='et_pb_contact_form_0']//form["
                                                   "@action='https://ovdjeisada.hr/kontakt/']//button["
                                                   "@name='et_builder_submit_button']")
    posalji_button.click()
    # Verify that "Hvala Vam što ste nam se javili, odgovorit ćemo u najkraćem mogućem roku! 🙂" message is displayed
    time.sleep(5)  # This time.sleep is necessary for the method to function: 'wait.until(
    # ec.visibility_of_element_located' doesn't work here
    actual_message = driver.find_element(By.XPATH, "//div[@id='et_pb_contact_form_0']//p")
    confirmation_message = "Hvala Vam što ste nam se javili, odgovorit ćemo u najkraćem mogućem roku! 🙂"
    assert actual_message.text == confirmation_message, "Wrong confirmation message"
    print("Correct confirmation message is displayed")
    # Tested with no time.sleep and it functions


# DONE ✅
def test_contact_form_unhappy_path_1():
    # Open page
    driver.get("https://ovdjeisada.hr/kontakt/")
    time.sleep(1)
    # Close cookies pop up by clicking 'Prihvati' button
    cookies_prihvati_button = driver.find_element(By.XPATH, "//button[@class='cmplz-btn cmplz-accept']")
    cookies_prihvati_button.click()
    time.sleep(1)
    # Find form fields
    form_fields = driver.find_element(By.XPATH, "//form[@class='et_pb_contact_form clearfix']")
    # Scroll to the form fields location
    driver.execute_script("arguments[0].scrollIntoView();", form_fields)
    time.sleep(1)
    # Type "" in 'Ime' input field
    ime = driver.find_element(By.XPATH, "/html//input[@id='et_pb_contact_ime_0']")
    ime.send_keys("")
    print("Typed nothing in 'Ime' input field")
    time.sleep(1)
    # Type "%" in 'Prezime' input field
    prezime = driver.find_element(By.XPATH, "/html//input[@id='et_pb_contact_prezime_0']")
    prezime.send_keys("%")
    print("Typed '%' in 'Prezime' input field")
    time.sleep(1)
    # Type "" in 'Mobitel' input field
    mobitel = driver.find_element(By.XPATH, "/html//input[@id='et_pb_contact_mobitel_0']")
    mobitel.send_keys("")
    print("Typed nothing in 'Mobitel' input field")
    time.sleep(1)
    # Type "ante@ante.com" in 'E-mail' input field
    email = driver.find_element(By.XPATH, "/html//input[@id='et_pb_contact_e-mail_0']")
    email.send_keys("ante@ante.com")
    print("Typed 'ante@ante.com' in 'E-mail' input field")
    time.sleep(1)
    # Type "%" in 'Vaša poruka' input field
    vasa_poruka = driver.find_element(By.XPATH, "/html//textarea[@id='et_pb_contact_poruka_0']")
    vasa_poruka.send_keys("%")
    print("Typed '%' in 'Vaša poruka' input field")
    time.sleep(1)
    # Switch driver to hcaptcha frame
    hcaptcha_frame = driver.find_element(By.XPATH, "//iframe[@tabindex='0']")
    driver.switch_to.frame(hcaptcha_frame)
    # Click hCaptcha checkbox
    hcaptcha = driver.find_element(By.XPATH, "//div[@id='checkbox']")
    hcaptcha.click()
    # Solve hCaptcha
    time.sleep(25)  # This time.sleep is necessary for manually solving the captcha
    # Switch driver to default content
    driver.switch_to.default_content()
    # Click 'Pošalji' button
    posalji_button = driver.find_element(By.XPATH, "//div[@id='et_pb_contact_form_0']//form["
                                                   "@action='https://ovdjeisada.hr/kontakt/']//button["
                                                   "@name='et_builder_submit_button']")
    posalji_button.click()
    # Verify that "Please, fill in the following fields: Ime" error message is displayed
    time.sleep(5)  # This time.sleep is necessary for the method to function: 'wait.until(
    # ec.visibility_of_element_located' doesn't work here
    actual_message1 = driver.find_element(By.XPATH,
                                          "//div[@id='et_pb_contact_form_0']//p[.='Please, fill in the following "
                                          "fields:']")
    actual_message2 = driver.find_element(By.XPATH,
                                          "//div[@id='et_pb_contact_form_0']/div[@class='et-pb-contact-message']/ul["
                                          "1]/li[.='Ime']")
    error_message1 = "Please, fill in the following fields:"
    error_message2 = "Ime"
    assert actual_message1.text == error_message1, "Wrong error message 1"
    assert actual_message2.text == error_message2, "Wrong error message 2"
    print("Correct error message is displayed")
    # Tested with no time.sleep and it functions


# DONE ✅
def test_contact_form_unhappy_path_2():
    # Open page
    driver.get("https://ovdjeisada.hr/kontakt/")
    time.sleep(1)
    # Close cookies pop up by clicking 'Prihvati' button
    cookies_prihvati_button = driver.find_element(By.XPATH, "//button[@class='cmplz-btn cmplz-accept']")
    cookies_prihvati_button.click()
    time.sleep(1)
    # Find form fields
    form_fields = driver.find_element(By.XPATH, "//form[@class='et_pb_contact_form clearfix']")
    # Scroll to the form fields location
    driver.execute_script("arguments[0].scrollIntoView();", form_fields)
    time.sleep(1)
    # Type "%" in 'Ime' input field
    ime = driver.find_element(By.XPATH, "/html//input[@id='et_pb_contact_ime_0']")
    ime.send_keys("%")
    print("Typed '%' in 'Ime' input field")
    time.sleep(1)
    # Type "" in 'Prezime' input field
    prezime = driver.find_element(By.XPATH, "/html//input[@id='et_pb_contact_prezime_0']")
    prezime.send_keys("")
    print("Typed nothing in 'Prezime' input field")
    time.sleep(1)
    # Type "" in 'Mobitel' input field
    mobitel = driver.find_element(By.XPATH, "/html//input[@id='et_pb_contact_mobitel_0']")
    mobitel.send_keys("")
    print("Typed nothing in 'Mobitel' input field")
    time.sleep(1)
    # Type "ante@ante.com" in 'E-mail' input field
    email = driver.find_element(By.XPATH, "/html//input[@id='et_pb_contact_e-mail_0']")
    email.send_keys("ante@ante.com")
    print("Typed 'ante@ante.com' in 'E-mail' input field")
    time.sleep(1)
    # Type "%" in 'Vaša poruka' input field
    vasa_poruka = driver.find_element(By.XPATH, "/html//textarea[@id='et_pb_contact_poruka_0']")
    vasa_poruka.send_keys("%")
    print("Typed '%' in 'Vaša poruka' input field")
    time.sleep(1)
    # Switch driver to hcaptcha frame
    hcaptcha_frame = driver.find_element(By.XPATH, "//iframe[@tabindex='0']")
    driver.switch_to.frame(hcaptcha_frame)
    # Click hCaptcha checkbox
    hcaptcha = driver.find_element(By.XPATH, "//div[@id='checkbox']")
    hcaptcha.click()
    # Solve hCaptcha
    time.sleep(25)  # This time.sleep is necessary for manually solving the captcha
    # Switch driver to default content
    driver.switch_to.default_content()
    # Click 'Pošalji' button
    posalji_button = driver.find_element(By.XPATH, "//div[@id='et_pb_contact_form_0']//form["
                                                   "@action='https://ovdjeisada.hr/kontakt/']//button["
                                                   "@name='et_builder_submit_button']")
    posalji_button.click()
    # Verify that "Please, fill in the following fields: Prezime" error message is displayed
    time.sleep(5)  # This time.sleep is necessary for the method to function: 'wait.until(
    # ec.visibility_of_element_located' doesn't work here
    actual_message1 = driver.find_element(By.XPATH,
                                          "//div[@id='et_pb_contact_form_0']//p[.='Please, fill in the following "
                                          "fields:']")
    actual_message2 = driver.find_element(By.XPATH,
                                          "//div[@id='et_pb_contact_form_0']/div[@class='et-pb-contact-message']/ul["
                                          "1]/li[.='Prezime']")
    error_message1 = "Please, fill in the following fields:"
    error_message2 = "Prezime"
    assert actual_message1.text == error_message1, "Wrong error message 1"
    assert actual_message2.text == error_message2, "Wrong error message 2"
    print("Correct error message is displayed")
    # Tested with no time.sleep and it functions


# ❓INCOMPLETE👇
def test_contact_form_unhappy_path_3():
    # Open page
    driver.get("https://ovdjeisada.hr/kontakt/")
    # time.sleep(1)
    # Close cookies pop up by clicking 'Prihvati' button
    cookies_prihvati_button = driver.find_element(By.XPATH, "//button[@class='cmplz-btn cmplz-accept']")
    cookies_prihvati_button.click()
    # time.sleep(1)
    # Find form fields
    form_fields = driver.find_element(By.XPATH, "//form[@class='et_pb_contact_form clearfix']")
    # Scroll to the form fields location
    driver.execute_script("arguments[0].scrollIntoView();", form_fields)
    # time.sleep(1)
    # Type "%" in 'Ime' input field
    ime = driver.find_element(By.XPATH, "/html//input[@id='et_pb_contact_ime_0']")
    ime.send_keys("%")
    print("Typed '%' in 'Ime' input field")
    # time.sleep(1)
    # Type "%" in 'Prezime' input field
    prezime = driver.find_element(By.XPATH, "/html//input[@id='et_pb_contact_prezime_0']")
    prezime.send_keys("%")
    print("Typed '%' in 'Prezime' input field")
    # time.sleep(1)
    # Type "%" in 'Mobitel' input field
    mobitel = driver.find_element(By.XPATH, "/html//input[@id='et_pb_contact_mobitel_0']")
    mobitel.send_keys("%")
    print("Typed '%' in 'Mobitel' input field")
    # time.sleep(1)
    # Type "ante@ante.com" in 'E-mail' input field
    email = driver.find_element(By.XPATH, "/html//input[@id='et_pb_contact_e-mail_0']")
    email.send_keys("ante@ante.com")
    print("Typed 'ante@ante.com' in 'E-mail' input field")
    # time.sleep(1)
    # Type "%" in 'Vaša poruka' input field
    vasa_poruka = driver.find_element(By.XPATH, "/html//textarea[@id='et_pb_contact_poruka_0']")
    vasa_poruka.send_keys("%")
    print("Typed '%' in 'Vaša poruka' input field")
    # time.sleep(1)
    # Switch driver to hcaptcha frame
    hcaptcha_frame = driver.find_element(By.XPATH, "//iframe[@tabindex='0']")
    driver.switch_to.frame(hcaptcha_frame)
    # Click hCaptcha checkbox
    hcaptcha = driver.find_element(By.XPATH, "//div[@id='checkbox']")
    hcaptcha.click()
    # Solve hCaptcha
    time.sleep(25)  # This time.sleep is necessary for manually solving the captcha
    # Switch driver to default content
    driver.switch_to.default_content()
    # Click 'Pošalji' button
    posalji_button = driver.find_element(By.XPATH, "//div[@id='et_pb_contact_form_0']//form["
                                                   "@action='https://ovdjeisada.hr/kontakt/']//button["
                                                   "@name='et_builder_submit_button']")
    posalji_button.click()
    # Switch driver to the alert dialog
    alert_pop_up = driver.switch_to.alert
    alert_text = alert_pop_up.text
    # Verify that "Please, match the format requested. Only numbers allowed. Minimum length: 8 characters" error
    # message is displayed
    error_message = "Please, match the format requested. Only numbers allowed. Minimum length: 8 characters"
    assert alert_text == error_message, "Wrong error message"
    print("Correct error message is displayed")


# DONE ✅
def test_contact_form_unhappy_path_4():
    # Open page
    driver.get("https://ovdjeisada.hr/kontakt/")
    time.sleep(1)
    # Close cookies pop up by clicking 'Prihvati' button
    cookies_prihvati_button = driver.find_element(By.XPATH, "//button[@class='cmplz-btn cmplz-accept']")
    cookies_prihvati_button.click()
    time.sleep(1)
    # Find form fields
    form_fields = driver.find_element(By.XPATH, "//form[@class='et_pb_contact_form clearfix']")
    # Scroll to the form fields location
    driver.execute_script("arguments[0].scrollIntoView();", form_fields)
    time.sleep(1)
    # Type "%" in 'Ime' input field
    ime = driver.find_element(By.XPATH, "/html//input[@id='et_pb_contact_ime_0']")
    ime.send_keys("%")
    print("Typed '%' in 'Ime' input field")
    time.sleep(1)
    # Type "%" in 'Prezime' input field
    prezime = driver.find_element(By.XPATH, "/html//input[@id='et_pb_contact_prezime_0']")
    prezime.send_keys("%")
    print("Typed '%' in 'Prezime' input field")
    time.sleep(1)
    # Type "" in 'Mobitel' input field
    mobitel = driver.find_element(By.XPATH, "/html//input[@id='et_pb_contact_mobitel_0']")
    mobitel.send_keys("")
    print("Typed nothing in 'Mobitel' input field")
    time.sleep(1)
    # Type "" in 'E-mail' input field
    email = driver.find_element(By.XPATH, "/html//input[@id='et_pb_contact_e-mail_0']")
    email.send_keys("")
    print("Typed nothing in 'E-mail' input field")
    time.sleep(1)
    # Type "%" in 'Vaša poruka' input field
    vasa_poruka = driver.find_element(By.XPATH, "/html//textarea[@id='et_pb_contact_poruka_0']")
    vasa_poruka.send_keys("%")
    print("Typed '%' in 'Vaša poruka' input field")
    time.sleep(1)
    # Switch driver to hcaptcha frame
    hcaptcha_frame = driver.find_element(By.XPATH, "//iframe[@tabindex='0']")
    driver.switch_to.frame(hcaptcha_frame)
    # Click hCaptcha checkbox
    hcaptcha = driver.find_element(By.XPATH, "//div[@id='checkbox']")
    hcaptcha.click()
    # Solve hCaptcha
    time.sleep(25)  # This time.sleep is necessary for manually solving the captcha
    # Switch driver to default content
    driver.switch_to.default_content()
    # Click 'Pošalji' button
    posalji_button = driver.find_element(By.XPATH, "//div[@id='et_pb_contact_form_0']//form["
                                                   "@action='https://ovdjeisada.hr/kontakt/']//button["
                                                   "@name='et_builder_submit_button']")
    posalji_button.click()
    # Verify that "Please, fill in the following fields: E-mail" error message is displayed
    time.sleep(5)  # This time.sleep is necessary for the method to function: 'wait.until(
    # ec.visibility_of_element_located' doesn't work here
    actual_message1 = driver.find_element(By.XPATH,
                                          "//div[@id='et_pb_contact_form_0']//p[.='Please, fill in the following "
                                          "fields:']")
    actual_message2 = driver.find_element(By.XPATH,
                                          "//div[@id='et_pb_contact_form_0']/div[@class='et-pb-contact-message']/ul["
                                          "1]/li[.='E-mail']")
    error_message1 = "Please, fill in the following fields:"
    error_message2 = "E-mail"
    assert actual_message1.text == error_message1, "Wrong error message 1"
    assert actual_message2.text == error_message2, "Wrong error message 2"
    print("Correct error message is displayed")
    # Tested with no time.sleep and it functions


# DONE ✅
def test_contact_form_unhappy_path_5():
    # Open page
    driver.get("https://ovdjeisada.hr/kontakt/")
    time.sleep(1)
    # Close cookies pop up by clicking 'Prihvati' button
    cookies_prihvati_button = driver.find_element(By.XPATH, "//button[@class='cmplz-btn cmplz-accept']")
    cookies_prihvati_button.click()
    time.sleep(1)
    # Find form fields
    form_fields = driver.find_element(By.XPATH, "//form[@class='et_pb_contact_form clearfix']")
    # Scroll to the form fields location
    driver.execute_script("arguments[0].scrollIntoView();", form_fields)
    time.sleep(1)
    # Type "%" in 'Ime' input field
    ime = driver.find_element(By.XPATH, "/html//input[@id='et_pb_contact_ime_0']")
    ime.send_keys("%")
    print("Typed '%' in 'Ime' input field")
    time.sleep(1)
    # Type "%" in 'Prezime' input field
    prezime = driver.find_element(By.XPATH, "/html//input[@id='et_pb_contact_prezime_0']")
    prezime.send_keys("%")
    print("Typed '%' in 'Prezime' input field")
    time.sleep(1)
    # Type "" in 'Mobitel' input field
    mobitel = driver.find_element(By.XPATH, "/html//input[@id='et_pb_contact_mobitel_0']")
    mobitel.send_keys("")
    print("Typed nothing in 'Mobitel' input field")
    time.sleep(1)
    # Type "%" in 'E-mail' input field
    email = driver.find_element(By.XPATH, "/html//input[@id='et_pb_contact_e-mail_0']")
    email.send_keys("%")
    print("Typed '%' in 'E-mail' input field")
    time.sleep(1)
    # Type "%" in 'Vaša poruka' input field
    vasa_poruka = driver.find_element(By.XPATH, "/html//textarea[@id='et_pb_contact_poruka_0']")
    vasa_poruka.send_keys("%")
    print("Typed '%' in 'Vaša poruka' input field")
    time.sleep(1)
    # Switch driver to hcaptcha frame
    hcaptcha_frame = driver.find_element(By.XPATH, "//iframe[@tabindex='0']")
    driver.switch_to.frame(hcaptcha_frame)
    # Click hCaptcha checkbox
    hcaptcha = driver.find_element(By.XPATH, "//div[@id='checkbox']")
    hcaptcha.click()
    # Solve hCaptcha
    time.sleep(25)  # This time.sleep is necessary for manually solving the captcha
    # Switch driver to default content
    driver.switch_to.default_content()
    # Click 'Pošalji' button
    posalji_button = driver.find_element(By.XPATH, "//div[@id='et_pb_contact_form_0']//form["
                                                   "@action='https://ovdjeisada.hr/kontakt/']//button["
                                                   "@name='et_builder_submit_button']")
    posalji_button.click()
    # Verify that "Invalid email" error message is displayed
    time.sleep(5)  # This time.sleep is necessary for the method to function: 'wait.until(
    # ec.visibility_of_element_located' doesn't work here
    actual_message = driver.find_element(By.XPATH, "//div[@id='et_pb_contact_form_0']//ul/li[.='Invalid email']")
    error_message = "Invalid email"
    assert actual_message.text == error_message, "Wrong error message"
    print("Correct error message is displayed")
    # Tested with no time.sleep and it functions


# DONE ✅
def test_contact_form_unhappy_path_6():
    # Open page
    driver.get("https://ovdjeisada.hr/kontakt/")
    time.sleep(1)
    # Close cookies pop up by clicking 'Prihvati' button
    cookies_prihvati_button = driver.find_element(By.XPATH, "//button[@class='cmplz-btn cmplz-accept']")
    cookies_prihvati_button.click()
    time.sleep(1)
    # Find form fields
    form_fields = driver.find_element(By.XPATH, "//form[@class='et_pb_contact_form clearfix']")
    # Scroll to the form fields location
    driver.execute_script("arguments[0].scrollIntoView();", form_fields)
    time.sleep(1)
    # Type "%" in 'Ime' input field
    ime = driver.find_element(By.XPATH, "/html//input[@id='et_pb_contact_ime_0']")
    ime.send_keys("%")
    print("Typed '%' in 'Ime' input field")
    time.sleep(1)
    # Type "%" in 'Prezime' input field
    prezime = driver.find_element(By.XPATH, "/html//input[@id='et_pb_contact_prezime_0']")
    prezime.send_keys("%")
    print("Typed '%' in 'Prezime' input field")
    time.sleep(1)
    # Type "" in 'Mobitel' input field
    mobitel = driver.find_element(By.XPATH, "/html//input[@id='et_pb_contact_mobitel_0']")
    mobitel.send_keys("")
    print("Typed nothing in 'Mobitel' input field")
    time.sleep(1)
    # Type "ante@ante.com" in 'E-mail' input field
    email = driver.find_element(By.XPATH, "/html//input[@id='et_pb_contact_e-mail_0']")
    email.send_keys("ante@ante.com")
    print("Typed 'ante@ante.com' in 'E-mail' input field")
    time.sleep(1)
    # Type "" in 'Vaša poruka' input field
    vasa_poruka = driver.find_element(By.XPATH, "/html//textarea[@id='et_pb_contact_poruka_0']")
    vasa_poruka.send_keys("")
    print("Typed nothing in 'Vaša poruka' input field")
    time.sleep(1)
    # Switch driver to hcaptcha frame
    hcaptcha_frame = driver.find_element(By.XPATH, "//iframe[@tabindex='0']")
    driver.switch_to.frame(hcaptcha_frame)
    # Click hCaptcha checkbox
    hcaptcha = driver.find_element(By.XPATH, "//div[@id='checkbox']")
    hcaptcha.click()
    # Solve hCaptcha
    time.sleep(25)  # This time.sleep is necessary for manually solving the captcha
    # Switch driver to default content
    driver.switch_to.default_content()
    # Click 'Pošalji' button
    posalji_button = driver.find_element(By.XPATH, "//div[@id='et_pb_contact_form_0']//form["
                                                   "@action='https://ovdjeisada.hr/kontakt/']//button["
                                                   "@name='et_builder_submit_button']")
    posalji_button.click()
    # Verify that "Please, fill in the following fields: Vaša poruka" error message is displayed
    time.sleep(5)  # This time.sleep is necessary for the method to function: 'wait.until(
    # ec.visibility_of_element_located' doesn't work here
    actual_message1 = driver.find_element(By.XPATH,
                                          "//div[@id='et_pb_contact_form_0']//p[.='Please, fill in the following "
                                          "fields:']")
    actual_message2 = driver.find_element(By.XPATH,
                                          "//div[@id='et_pb_contact_form_0']/div[@class='et-pb-contact-message']/ul["
                                          "1]/li[.='Vaša poruka']")
    error_message1 = "Please, fill in the following fields:"
    error_message2 = "Vaša poruka"
    assert actual_message1.text == error_message1, "Wrong error message 1"
    assert actual_message2.text == error_message2, "Wrong error message 2"
    print("Correct error message is displayed")
    # Tested with no time.sleep and it functions
