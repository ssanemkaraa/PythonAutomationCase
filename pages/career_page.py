import time

from helpers.ui_helper import UiHelper
from utils.json_helper import JsonHelper
from utils.logger import Logger


class CareerPage:
    logger = Logger.log()

    def __init__(self):
        self.__ui_helper = UiHelper()
        self.__config_helper = JsonHelper("config")
        self.__career_page_url = self.__config_helper.get("careerPage")
        self.__careers_quality_assurance_page_url = f"{self.__career_page_url}quality-assurance/"
        self.__open_positions_page_url = f"{self.__career_page_url}open-positions/?department=qualityassurance"

        self.__locator_helper = JsonHelper("locator")
        self.__cookie_locator = self.__locator_helper.get("cookie")
        self.__home_page_locator = self.__locator_helper.get("homePage")
        self.__navigation_page_locator = self.__locator_helper.get("navigation")
        self.__career_page_locator = self.__locator_helper.get("careerPage")
        self.__job_form_page_locator = self.__locator_helper.get("jobFormPage")

    def go_to_careers_quality_assurance_page(self, browser):
        self.__ui_helper.go_to_url(self.__careers_quality_assurance_page_url, browser)
        self.__ui_helper.verify_url(self.__careers_quality_assurance_page_url)

    def check_job_list(self):
        self.__ui_helper.click_element(self.__career_page_locator['seeAllJobs'])
        self.__ui_helper.verify_url(self.__open_positions_page_url)
        self.__ui_helper.click_element(self.__cookie_locator['accept'])
        time.sleep(5)
        self.__ui_helper.click_element(self.__career_page_locator['filterLocation'])
        self.__ui_helper.click_element(self.__career_page_locator['istanbulInFilter'])
        self.__ui_helper.click_element(self.__career_page_locator['filterDepartment'])
        self.__ui_helper.click_element(self.__career_page_locator['qaInFilter'])
        self.__ui_helper.verify_text_in_list(self.__career_page_locator['mainLocatorForFilterResult'],
                                             self.__career_page_locator['subLocatorForFilterResult'],
                                             "Istanbul, Turkey")
        time.sleep(5)
        self.__ui_helper.scroll_to_element(self.__career_page_locator['mainLocatorForFilterResult'])
        time.sleep(5)
        self.__ui_helper.hover_element(self.__career_page_locator['istanbulInJobList'])
        time.sleep(5)
        self.__ui_helper.click_element(self.__career_page_locator['viewRole'])
        self.__ui_helper.switch_to_latest_window()

        self.__ui_helper.is_element_visible(self.__job_form_page_locator['applyButton'])
        time.sleep(10)
