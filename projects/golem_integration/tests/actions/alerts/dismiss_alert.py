from golem import actions
from selenium.common.exceptions import NoAlertPresentException

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'Verify dismiss_alert action'


def test_dismiss_alert(data):
    actions.navigate(data.env.url+'alert/')
    actions.click('#alert-button')
    actions.verify_alert_present()
    actions.dismiss_alert()
    golem_steps.assert_last_step_message('Dismiss alert')
    actions.verify_alert_not_present()
    actions.verify_element_text('#result', '1')


def test_dismiss_alert_confirm(data):
    actions.navigate(data.env.url + 'confirm/')
    actions.click('#confirm-button')
    actions.verify_alert_present()
    actions.dismiss_alert()
    actions.verify_alert_not_present()
    actions.verify_element_text('#result', 'NOT CONFIRMED')


def test_dismiss_alert_prompt(data):
    actions.navigate(data.env.url + 'prompt/')
    actions.click('#prompt-button')
    actions.verify_alert_present()
    actions.dismiss_alert()
    actions.verify_alert_not_present()
    actions.verify_element_text('#result', 'DISMISSED')


def test_dismiss_alert__not_present(data):
    actions.navigate(data.env.url+'alert/')
    actions.dismiss_alert(ignore_not_present=True)
    with expected_exception(NoAlertPresentException):
        actions.dismiss_alert()
