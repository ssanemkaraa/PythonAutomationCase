import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chromeOptions
from selenium.webdriver.firefox.options import Options as firefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from utils.json_helper import JsonHelper
from utils.logger import Logger


class DriverHelper:
    logger = Logger.log()

    def __init__(self):
        self.__config_helper = JsonHelper("config")
        self.__implicit_wait = self.__config_helper.get("implicitWait")
        self.__explicit_wait = self.__config_helper.get("explicitWait")
        self.__driver = None
        self.__browser_name = None
        self.__auto_chrome_driver = None
        self.__auto_firefox_driver = None

    def get_current_driver(self):
        try:
            if self.__driver is None:
                try:
                    self.__driver = self.setup_drivers()
                except Exception as e:
                    self.logger.error("\t Driver - Driver not initialized")
                    self.logger.error(str(e))
                self.logger.info("\t Driver - getCurrentDriver - Driver was None and initialized")
            else:
                self.logger.info("\t Driver - getCurrentDriver - Driver was not None, current driver is used")
                return self.__driver
        except Exception as e:
            self.logger.error("\t Driver - Current driver not initialized")
            raise RuntimeError("Exception : " + self.__browser_name + str(e))
        return self.__driver

    def setup_drivers(self):
        try:
            if self.__browser_name is not None:
                if self.__browser_name == "default":
                    self.__browser_name = self.__config_helper.get("defaultBrowser")
                else:
                    self.__browser_name = self.__browser_name
                self.logger.info("\t Driver - Browser name specified and changed : " + self.__browser_name)
            else:
                self.logger.info("\t Driver - Browser name is not correct ")

            if self.__browser_name == "Chrome":
                ChromeDriverManager().install()
                chrome_options = chromeOptions()
                chrome_options.add_argument("start-maximized")
                chrome_options.add_argument("--incognito")
                chrome_options.add_argument("--disable-blink-features=AutomationControlled")
                prefs = {"profile.default_content_setting_values.notifications": 1}
                chrome_options.add_experimental_option("prefs", prefs)
                self.__driver = webdriver.Chrome(options=chrome_options)
            elif self.__browser_name == "Firefox":
                GeckoDriverManager().install()
                firefox_options = firefoxOptions()
                firefox_options.add_argument("start-maximized")
                firefox_options.add_argument("--incognito")
                firefox_options.add_argument("--disable-blink-features=AutomationControlled")
                prefs = {"profile.default_content_setting_values.notifications": 1}
                self.__driver = webdriver.Firefox(options=firefox_options)

            self.logger.info("\t Driver - " + self.__browser_name + " driver setup done")
            self.general_implicit_wait(self.__driver)
        except Exception as e:
            self.logger.error("\t Driver - " + self.__browser_name + " driver setup failed")
            raise RuntimeError("Exception : " + self.__browser_name + str(e))

        return self.__driver

    def general_implicit_wait(self, driver):
        try:
            assert driver is not None
            driver.implicitly_wait(self.__implicit_wait)
            self.logger.info("\t Driver - Implicit wait done")
        except Exception as e:
            self.logger.error(e)

    def set_browser_name(self, browser_name):
        self.__browser_name = browser_name

    def get_driver(self):
        return self.__driver

    def get_explicit_wait(self):
        return self.__explicit_wait

    def get_implicit_wait(self):
        return self.__implicit_wait
