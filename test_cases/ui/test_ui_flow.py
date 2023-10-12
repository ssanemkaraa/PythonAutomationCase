from pages.career_page import CareerPage
from pages.home_page import HomePage


class TestUiFlow:
    home_page = HomePage()
    career_page = CareerPage()

    def test_check_career(self):
        browser = "Chrome"
        self.home_page.go_to_home_page(browser)
        self.home_page.check_career()

    def test_check_job_list(self):
        browser = "Chrome"
        self.career_page.go_to_careers_quality_assurance_page(browser)
        self.career_page.check_job_list()
