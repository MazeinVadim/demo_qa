import time
from pages.tables import Tables

def test_tables(browser):
    page_tables = Tables(browser)


    page_tables.visit()
    assert not page_tables.no_date.exist()

    row_number = 1
    while True:
        delete_button = page_tables.get_delete_button(row_number)
        if not delete_button.exist():
            break

        delete_button.safe_click()
        time.sleep(0.3)
        row_number += 1

    time.sleep(2)
    assert page_tables.no_date.exist()

