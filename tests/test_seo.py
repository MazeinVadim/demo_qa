from pages.demoqa import DemoQa
from pages.base_page import BasePage


def test_check_title_demo(browser):

    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    assert browser.title == 'DEMOQA'
