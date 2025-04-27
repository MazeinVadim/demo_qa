from pages.base_page import BasePage
from components.components import WebElement


class KoupAdd(BasePage):
    def __init__(self, driver):
        super().__init__(driver, "https://the-internet.herokuapp.com/add_remove_elements/")

        self.btn_add = WebElement(driver, "#content > div > button", "css")