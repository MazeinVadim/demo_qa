import time
from pages.links import Links


def test_home_link(browser):
    page = Links(browser)
    page.visit()

    assert page.link_home.exist()
    assert page.link_home.get_text() == 'Home'
    assert page.link_home.get_dom_attribute('href') == 'https://demoqa.com'

    original_window = browser.current_window_handle
    page.link_home.click()
    time.sleep(2)

    assert len(browser.window_handles) == 2
    browser.switch_to.window(original_window)