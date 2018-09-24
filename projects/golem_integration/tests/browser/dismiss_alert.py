from selenium.common.exceptions import NoAlertPresentException
from golem import actions

from projects.golem_integration.utils import expected_exception


description = 'Verify webdriver.dismiss_alert method'

def test(data):
    browser = actions.get_browser()
    browser.navigate(data.env.url + 'alert/')
    actions.click('#alert-button')
    assert browser.alert_is_present() is True
    browser.dismiss_alert()
    assert browser.alert_is_present() is False
    browser.dismiss_alert(ignore_not_present=True)
    with expected_exception(NoAlertPresentException):
        browser.dismiss_alert()
