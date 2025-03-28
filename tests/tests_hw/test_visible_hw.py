from pages.accordian import Accordian
import time

def test_visible_accordian(browser):
    accordian_page = Accordian(browser)
    accordian_page.visit()

    assert accordian_page.section1_content.visible()
    accordian_page.section1_heading.click()
    time.sleep(2)
    assert not accordian_page.section1_content.visible()

def test_visible_accordian_default(browser):
    accordian_page = Accordian(browser)
    accordian_page.visit()

    assert not accordian_page.section2_content_p1.visible()
    assert not accordian_page.section2_content_p2.visible()
    assert not accordian_page.section3_content.visible()