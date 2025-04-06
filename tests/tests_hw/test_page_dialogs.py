from pages.modal_dialogs import ModalDialogs
from pages.demoqa import DemoQa


def test_modal_elements(browser):

    modal_dialogs_page = ModalDialogs(browser)
    modal_dialogs_page.visit()

    assert not modal_dialogs_page.btns_modal.check_count_elements(5)

def test_navigation_modal(browser):
    modal_dialogs_page = ModalDialogs(browser)
    demoqa_page = DemoQa(browser)

    modal_dialogs_page.visit()

    browser.refresh()

    modal_dialogs_page.icon_home.click()

    browser.back()

    browser.set_window_size(900,400)

    browser.forward()

    assert demoqa_page.equal_url()
    assert "DEMOQA" in browser.title