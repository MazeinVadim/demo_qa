from pages.base_page import BasePage
from components.components import WebElement


class Tables(BasePage):

    def __init__(self,driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.modal = WebElement(driver, 'div.modal-content')
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')
        self.btn_submit = WebElement(driver, '#submit')

        # Элементы таблицы
        self.rows = WebElement(driver, 'div.rt-tr-group')
        self.edit_btn = WebElement(driver, 'span[title="Edit"]')
        self.delete_btn = WebElement(driver, 'span[title="Delete"]')

        # Для задачи со звёздочкой
        self.total_pages = WebElement(driver, 'span.-totalPages')
        self.page_info = WebElement(driver, 'input[type="number"]')
        self.btn_next = WebElement(driver, '.pagination-bottom .-next button')
        self.btn_prev = WebElement(driver, '.pagination-bottom .-previous button')
        self.select_rows = WebElement(driver, 'select[aria-label="rows per page"]')

        self.header_firstname = WebElement(driver, 'div.rt-th:nth-child(1)')
        self.header_lastname = WebElement(driver, 'div.rt-th:nth-child(2)')
        self.header_age = WebElement(driver, 'div.rt-th:nth-child(3)')
        self.header_email = WebElement(driver, 'div.rt-th:nth-child(4)')
        self.header_salary = WebElement(driver, 'div.rt-th:nth-child(5)')
        self.header_department = WebElement(driver, 'div.rt-th:nth-child(6)')