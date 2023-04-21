from driver import Driver
from label import Label
from selenium.webdriver.common.by import By
from base_page import BasePage


class MotoDetailsPage(BasePage):
    def __init__(self):
        super().__init__()
        self.__certification: Label = None

    def get_certification_text(self):
        self.__certification = Label(
            self._driver.find_element(By.XPATH, "//tr//*[text()='Сертификация']/ancestor::tr//span[text()='Euro 3']"))
        return self.__certification.get_text()
