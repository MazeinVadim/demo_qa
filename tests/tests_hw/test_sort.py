import time
from pages.tables import Tables


def test_table_sort(browser):
    page = Tables(browser)
    page.visit()

    columns = {
        'first_name': page.header_firstname,
        'last_name': page.header_lastname,
        'age': page.header_age,
        'email': page.header_email,
        'salary': page.header_salary,
        'department': page.header_department
    }

    for col_name, element in columns.items():
        element.click()
        time.sleep(1)
        assert 'sort-asc' in element.get_dom_attribute('class') or \
               'sort-desc' in element.get_dom_attribute('class')