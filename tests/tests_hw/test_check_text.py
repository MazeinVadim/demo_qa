from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_check_footer_text(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    footer_locator = '#app > footer > span'
    footer_text = demo_qa_page.get_text(footer_locator)  # Use get_text method with locator
    assert footer_text == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'


def test_check_elements_page_text(browser):

    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)

    demo_qa_page.visit()
    demo_qa_page.btn_elements.click()

    center_text_locator = '#app > div > div > div > div.col-12.mt-4.col-md-6'
    center_text = elements_page.get_text(center_text_locator)
    assert center_text == 'Please select an item from left to start practice.'

def test_page_elements(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()

    assert elements_page.text_elements.get_text() == 'Please select an item from left to start practice.'
    assert elements_page.icon.exist()
    assert elements_page.btn_sidbar_first.exist()
    assert elements_page.btn_sidbar_first_textbox.exist()
