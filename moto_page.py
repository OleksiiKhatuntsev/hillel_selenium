from button import Button
from selenium.webdriver.common.by import By
from base_page import BasePage


class MotoPage(BasePage):
    def __init__(self):
        super().__init__()
        self.__tourist_moto_button: Button = None

    def get_tourist_moto_button(self):
        self.__tourist_moto_button = Button(self._driver.find_element(By.XPATH,
                                                            "//img[@src='/components/com_jshopping/files/img_categories/__________________________1.png']"))
        return self.__tourist_moto_button
