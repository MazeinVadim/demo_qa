import time
from pages.alerts import Alerts


def test_timer_alert(browser):
    page = Alerts(browser)
    page.visit()

    assert page.timer_alert_button.exist()
    page.timer_alert_button.click()
    time.sleep(5)

    alert = page.driver.switch_to.alert
    assert alert.text == 'This alert appeared after 5 seconds'
    alert.accept()

