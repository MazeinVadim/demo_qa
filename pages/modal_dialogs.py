from pages.base_page import BasePage
from components.components import WebElement


class ModalDialogs(BasePage):


    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btns_modal = WebElement(driver, 'button[id^="show"]')
        self.icon_home = WebElement(driver, 'header > a > img')
        self.btn_small = WebElement(driver, '#showSmallModal')
        self.btn_large = WebElement(driver, '#showLargeModal')
        self.modal_small = WebElement(driver, '#example-modal-sizes-title-sm')
        self.modal_large = WebElement(driver, '#example-modal-sizes-title-lg')
        self.btn_close_small = WebElement(driver, '#closeSmallModal')
        self.btn_close_large = WebElement(driver, '#closeLargeModal')
