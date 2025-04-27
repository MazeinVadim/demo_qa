from pages.base_page import BasePage
from components.components import WebElement


class Koup(BasePage):
    def __init__(self, driver):
        super().__init__(driver, "https://the-internet.herokuapp.com/")

        self.link_add = WebElement(driver, "Add/Remove Elements", "link")