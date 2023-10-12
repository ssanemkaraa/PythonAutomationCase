
from helpers.ui_helper import UiHelper
from utils.json_helper import JsonHelper
from utils.logger import Logger


class HomePage:
    logger = Logger.log()

    def __init__(self):
        self.__ui_helper = UiHelper()

        self.__config_helper = JsonHelper("config")
        self.__home_page_url = self.__config_helper.get("homePage")

        self.__locator_helper = JsonHelper("locator")
        self.__home_page_locator = self.__locator_helper.get("homePage")
        self.__navigation_page_locator = self.__locator_helper.get("navigation")
        self.__career_page_locator = self.__locator_helper.get("careerPage")

    def go_to_home_page(self, browser):
        # Visit https://useinsider.com/ and check Insider home page is opened or not
        self.__ui_helper.go_to_url(self.__home_page_url, browser)
        self.__ui_helper.verify_url(self.__home_page_url)
        self.__ui_helper.is_element_visible(self.__home_page_locator['verifyHomePage'])

    def check_career(self):
        # Select the “Company” menu in the navigation bar
        self.__ui_helper.click_element(self.__navigation_page_locator['companyMenu'])
        # select “Careers”
        self.__ui_helper.click_element(self.__navigation_page_locator['careers'])
        # check Career page, its Locations, Teams, and Life at Insider blocks are open or not
        self.__ui_helper.verify_url(self.__config_helper.get("careerPage"))
        self.__ui_helper.is_element_visible(self.__career_page_locator['findYourDreamJob'])
        self.__ui_helper.is_element_visible(self.__career_page_locator['location'])
        self.__ui_helper.is_element_visible(self.__career_page_locator['lifeAtInsider'])
        self.__ui_helper.is_element_visible(self.__career_page_locator['seeAllTeams'])
