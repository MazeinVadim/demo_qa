import time
from pages.text_box import TextBox


def test_text_box(browser):

    text_box_page = TextBox(browser)
    text_box_page.visit()

    full_name = "John Doe"
    current_address = "123 Main St"

    text_box_page.name.send_keys(full_name)
    text_box_page.current_address.send_keys(current_address)
    text_box_page.submit_button.click_force()
    time.sleep(2)

    assert full_name in text_box_page.output_name.get_text()
    assert current_address in text_box_page.output_current_address.get_text()
    time.sleep(5)

