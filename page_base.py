from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class PageBase:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    def _type(self, locator: tuple, text: str, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).send_keys(text)

    def _clear(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).clear()

    def _click(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).click()

    def _cmd_click(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        element = self._find(locator)
        action = ActionChains(self._driver)
        action.key_down(Keys.COMMAND).click(element).key_up(Keys.COMMAND).perform()
        window_handles_count = len(self._driver.window_handles)
        print("Number of open windows:", window_handles_count)
        self._driver.switch_to.window(self._driver.window_handles[1])

    def _hover(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        element = self._find(locator)
        action = ActionChains(self._driver)
        action.move_to_element(element).perform()

    def _wait_until_element_is_visible(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    def _wait_until_element_to_be_clickable(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.element_to_be_clickable(locator))

    @property
    def current_url(self) -> str:
        return self._driver.current_url

    def _is_displayed(self, locator: tuple) -> bool:
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def _open_url(self, url: str):
        self._driver.get(url)

    def _get_text(self, locator: tuple, time: int = 10) -> str:
        self._wait_until_element_is_visible(locator, time)
        return self._find(locator).text

    def _wait_until_element_is_invisible(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.invisibility_of_element_located(locator))

    def _scroll_to(self, locator: tuple):
        element = self._driver.find_element(*locator)
        self._driver.execute_script("arguments[0].scrollIntoView();", element)

    def _switch_to(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        frame_element = self._find(locator)
        self._driver.switch_to.frame(frame_element)

    def _click_and_drag(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        element = self._find(locator)
        action = ActionChains(self._driver)
        action.move_to_element(element).click_and_hold().move_by_offset(-20, 0).pause(1). \
            move_by_offset(40, 0).pause(1).move_by_offset(0, -20).pause(1).move_by_offset(0, 40).release().perform()

    def _check_elements_displayed(self, driver, locator_list):
        # Initialize an empty list to store the web elements
        elements = []
        # Iterate over the locators and find the elements
        for locator in locator_list:
            elements.extend(driver.find_elements(*locator))
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

    def _switch_to_default_content(self):
        self._driver.switch_to.default_content()
