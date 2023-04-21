from button import Button
from selenium.webdriver.common.by import By
from base_page import BasePage


class TouristicPage(BasePage):
    def __init__(self):
        super().__init__()
        self.__benelli_trk_button: Button = None

    def get_benelli_trk_button(self):
        self.__benelli_trk_button = Button(self._driver.find_element(By.XPATH,
                                                                  "//img[@src='https://mototek.com.ua/components/com_jshopping/files/img_products/thumb_foto_Benelli_TRK_502X_ABS_Off-Road.jpg']"))
        return self.__benelli_trk_button