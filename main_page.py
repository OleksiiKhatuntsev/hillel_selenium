from button import Button
from selenium.webdriver.common.by import By
from base_page import BasePage


class MainPage(BasePage):
    def __init__(self):
        super().__init__()
        self.__moto_button: Button = None

    def get_moto_button(self):
        self.__moto_button = Button(self._driver.find_element(By.XPATH,
                                   "//img[@src='https://mototek.com.ua/components/com_jshopping/files/img_categories/ico_moto.png']"))

        return self.__moto_button