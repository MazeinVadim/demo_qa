from pages.base_page import BasePage
from components.components import WebElement

class Tables(BasePage):

    def __init__(self,driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)
        self.no_date = WebElement(driver, 'div.rt-noData')

    def get_delete_button(self, row_number: int) -> WebElement:
        locator = f'#delete-record-{row_number}'
        return WebElement(self.driver, locator)