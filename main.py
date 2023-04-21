from driver import Driver
from main_page import MainPage
from moto_page import MotoPage
from touristic_page import TouristicPage
from moto_details_page import MotoDetailsPage


class TestMotoDetailsTest:

    def setup_class(self):
        self.driver = Driver.get_firefox_driver()
        self.driver.maximize_window()
        self.main_page = MainPage()
        self.moto_page = MotoPage()
        self.moto_details_page = MotoDetailsPage()
        self.touristic_page = TouristicPage()

    def setup_method(self):
        self.driver.get("https://mototek.com.ua/")

    def test_get_moto_certificate(self):
        self.main_page.get_moto_button().click()
        self.moto_page.get_tourist_moto_button().click()
        self.touristic_page.get_benelli_trk_button().click()
        result = self.moto_details_page.get_certification_text()
        assert result == "Euro 3"

    def teardown_method(self):
        pass

    def teardown_class(self):
        self.driver.quit()
