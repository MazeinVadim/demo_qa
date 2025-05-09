import logging
from components.components import WebElement


class BasePage:

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.viewport = WebElement(driver, 'head > meta')

    def visit(self):
        return self.driver.get(self.base_url)

    def get_url(self):
        return self.driver.current_url

    def equal_url(self):
        if self.get_url() == self.base_url:
            return True
        else:
            return False

    def get_text(self, locator):
        element = WebElement(self.driver, locator)
        return element.get_text()

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def refresh(self):
        self.driver.refresh()

    def get_title(self):
        return self.driver.title

    def alert(self):
        try:
            return self.driver.switch_to.alert
        except Exception as ex:
            logging.log(1, ex)
            return False







