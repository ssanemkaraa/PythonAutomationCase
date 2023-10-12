from pages.career_page import CareerPage
from pages.home_page import HomePage
import pyautogui

from utils.logger import Logger


class TestUiFlow:
    home_page = HomePage()
    career_page = CareerPage()

    def test_check_career(self):
        browser = "Chrome"
        try:
            self.home_page.go_to_home_page(browser)
            self.home_page.check_career()
        except Exception as e:
            Logger.take_screenshot("test_check_career_error")
            print(f"Error : {str(e)}")

    def test_check_job_list(self):
        browser = "Chrome"
        try:
            self.career_page.go_to_careers_quality_assurance_page(browser)
            self.career_page.check_job_list()
        except Exception as e:
            Logger.take_screenshot("test_check_job_list_error")
            print(f"Error : {str(e)}")
