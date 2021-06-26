from golem import actions
from selenium.common.exceptions import NoAlertPresentException

from projects.golem_integration.pages import golem_logger
from projects.golem_integration.utils import expected_exception


description = 'Verify accept_alert action'


def test_accept_alert(data):
    # alert
    actions.navigate(data.env.url+'alert/')
    actions.click('#alert-button')
    actions.verify_alert_present()
    actions.accept_alert()
    assert golem_logger.last_info_log_line_contains('Accept alert')
    actions.verify_alert_not_present()
    actions.verify_element_text('#result', '1')
    # confirm
    actions.navigate(data.env.url + 'confirm/')
    actions.click('#confirm-button')
    actions.verify_alert_present()
    actions.accept_alert()
    actions.verify_alert_not_present()
    actions.verify_element_text('#result', 'CONFIRMED')
    # prompt
    actions.navigate(data.env.url + 'prompt/')
    actions.click('#prompt-button')
    actions.verify_alert_present()
    actions.accept_alert()
    actions.verify_alert_not_present()
    actions.verify_element_text('#result', 'EMPTY')


def test_alert_not_present(data):
    actions.navigate(data.env.url+'alert/')
    actions.accept_alert(ignore_not_present=True)
    with expected_exception(NoAlertPresentException):
        actions.accept_alert()
