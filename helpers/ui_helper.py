from selenium.common import NoSuchFrameException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


from helpers.driver_helper import DriverHelper
from utils.logger import Logger


class UiHelper:
    logger = Logger.log()

    def __init__(self):
        self.__driver_helper = DriverHelper()
        self.__driver = self.__driver_helper.get_driver()
        self.__implicit_wait = self.__driver_helper.get_implicit_wait()

    def go_to_url(self, url, browser_name):
        try:
            self.__driver_helper.set_browser_name(browser_name)
            if self.__driver is None:
                self.__driver = self.__driver_helper.setup_drivers()
            else:
                self.__driver = self.__driver_helper.get_driver()
            self.__driver.get(url)
        except Exception as e:
            self.logger.error("\t The method causing the error : go_to_url()")
            raise Exception(e)
        return True

    def click_element(self, locator):
        try:
            wait = WebDriverWait(self.__driver, self.__implicit_wait)
            element = wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
            element.click()
            self.logger.info("UiHelper - Clicked " + str(element))
        except TimeoutException:
            self.logger.error("\t The element with locator " + locator + " is not clickable.")
            return False
        except Exception as e:
            self.logger.error("\t The method causing the error : UiHelper - click_element.")
            raise Exception(e)
        return True

    def force_click_element(self, locator):
        try:
            wait = WebDriverWait(self.__driver, self.__implicit_wait)
            element = wait.until(ec.presence_of_element_located((By.XPATH, locator)))
            self.__driver.execute_script("arguments[0].click();", element)
            self.logger.info("UiHelper - Force Clicked " + str(element))
        except Exception as e:
            self.logger.error("\t The method causing the error : UiHelper - force_click_element.")
            raise Exception(e)
        return True

    def hover_element(self, locator):
        try:
            wait = WebDriverWait(self.__driver, self.__implicit_wait)
            element = wait.until(ec.presence_of_element_located((By.XPATH, locator)))

            action = ActionChains(self.__driver)
            action.move_to_element(element).perform()

            self.logger.info("UiHelper - Hovered over " + str(element))
        except Exception as e:
            self.logger.error("\t The method causing the error : UiHelper - hover_element.")
            raise Exception(e)
        return True

    def scroll_to_element(self, locator):
        try:
            wait = WebDriverWait(self.__driver, self.__implicit_wait)
            element = wait.until(ec.presence_of_element_located((By.XPATH, locator)))

            # Sayfayı belirli bir öğeye kaydır
            self.__driver.execute_script("arguments[0].scrollIntoView(true);", element)

            self.logger.info("UiHelper - Scrolled to " + str(element))
        except Exception as e:
            self.logger.error("\t The method causing the error : UiHelper - scroll_to_element.")
            raise Exception(e)
        return True

    def fill_input_field(self, locator, text):
        try:
            wait = WebDriverWait(self.__driver, self.__implicit_wait)
            input_element = wait.until(ec.presence_of_element_located((By.XPATH, locator)))
            input_element.clear()
            input_element.send_keys(text)
            self.logger.info(f"UiHelper - Filled input field {locator} with text: {text}")
        except Exception as e:
            self.logger.error("\t The method causing the error : UiHelper - fill_input_field.")
            raise Exception(e)

    def get_text(self, locator):
        try:
            wait = WebDriverWait(self.__driver, self.__implicit_wait)
            element = wait.until(ec.presence_of_element_located((By.XPATH, locator)))
            return element.text
        except Exception as e:
            self.logger.error("\t The method causing the error : UiHelper - get_text.")
            raise Exception(e)

    def verify_url(self, expected_url):
        try:
            current_url = self.__driver.current_url
            assert current_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {current_url}"
            self.logger.info(f"UiHelper - Verified URL: {current_url}")
        except Exception as e:
            self.logger.error("\t The method causing the error : UiHelper - verify_url.")
            raise Exception(e)

    def is_element_visible(self, locator):
        try:
            wait = WebDriverWait(self.__driver, self.__implicit_wait)
            element = wait.until(ec.presence_of_element_located((By.XPATH, locator)))
            return element.is_displayed()
        except Exception as e:
            self.logger.error("\t The method causing the error : UiHelper - is_element_visible.")
            raise Exception(e)

    def verify_text_in_list(self, main_locator, sub_locator, verify_text):
        wait = WebDriverWait(self.__driver, self.__implicit_wait)
        elms = wait.until(ec.presence_of_all_elements_located((By.XPATH, main_locator)))

        for elm in elms:
            text = elm.find_element(By.XPATH, sub_locator).text
            self.logger.info(f"verify_text_in_list : {text}")

            if text == verify_text:
                return True
        return False

    def switch_to_frame(self, frame_locator):
        try:
            wait = WebDriverWait(self.__driver, self.__implicit_wait)
            frame = wait.until(ec.presence_of_element_located((By.XPATH, frame_locator)))
            self.__driver.switch_to.frame(frame)
            self.logger.info(f"UiHelper - Switched to frame with locator: {frame_locator}")
        except NoSuchFrameException as e:
            self.logger.error(f"Frame not found with locator: {frame_locator}")
            raise NoSuchFrameException(e)
        except Exception as e:
            self.logger.error("The method causing the error : UiHelper - switch_to_frame.")
            raise Exception(e)

    def switch_to_default_content(self):
        self.__driver.switch_to.default_content()
        self.logger.info("UiHelper - Switched back to default content (out of frames).")

    def switch_to_latest_window(self):
        try:
            # Mevcut pencerenin tanımlandığı kabuk pencereye dön
            self.__driver.switch_to.default_content()

            # Tüm pencere kollarını al
            window_handles = self.__driver.window_handles

            # Son açılan pencereye geçiş yap
            self.__driver.switch_to.window(window_handles[-1])

            self.logger.info("UiHelper - Switched to the latest window.")
        except Exception as e:
            self.logger.error("\t The method causing the error : UiHelper - switch_to_latest_window.")
            raise Exception(e)
        return True
