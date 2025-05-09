import time
import pytest
from pages.modal_dialogs import ModalDialogs


def test_modal_dialogs(browser):
    page = ModalDialogs(browser)

    # Проверка доступности страницы
    page.visit()
    if not page.equal_url():
        pytest.skip("Страница недоступна")

    # Проверка кнопок
    assert page.btn_small.exist()
    time.sleep(1)
    assert page.btn_large.exist()
    time.sleep(1)

    # Тест Small modal
    page.btn_small.click()
    time.sleep(1)
    assert page.modal_small.visible()
    assert page.btn_close_small.visible()

    page.btn_close_small.click()
    time.sleep(1)

    assert not page.btn_close_small.exist()

    # Тест Large modal
    page.btn_large.click()
    time.sleep(1)
    assert page.modal_large.visible()
    assert page.btn_close_large.visible()

    page.btn_close_large.click()
    time.sleep(1)
    assert not page.btn_close_large.exist()