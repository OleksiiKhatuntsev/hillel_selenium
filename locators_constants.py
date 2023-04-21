class LocatorsConstants:
    ACCEPT_LICENCE_XPATH = "//*[text()='Zaakceptuj wszystko']"
    SEARCH_FIELD_XPATH = "//*[@title='Szukaj']"
    SEARCH_BUTTON_XPATH = "//div[@class='FPdoLc lJ9FBc']//input[@value='Szukaj w Google']"
    GOOGLE_ICO_XPATH = "//div[@class='logo']//img[@class='jfN4p']"

        # driver.find_element(By.XPATH, "//*[@title='Szukaj']").send_keys(123)
        # driver.find_element(By.XPATH, "//div[@class='FPdoLc lJ9FBc']//input[@value='Szukaj w Google']").click()
        # google_ico = driver.find_element(By.XPATH, "//img[@class='jfN4p']")