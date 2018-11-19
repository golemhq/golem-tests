from selenium.common.exceptions import TimeoutException
from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'Verify wait_for_alert_present action'

def test(data):
    actions.navigate(data.env.url+'alert/')
    actions.click('#alert-delay-button')
    actions.wait_for_alert_present(5)
    golem_steps.assert_last_step_message('Wait for alert to be present')
    actions.verify_alert_present()
    actions.dismiss_alert()
    actions.click('#alert-delay-button')
    with expected_exception(TimeoutException, "Timeout waiting for alert to be present"):
        actions.wait_for_alert_present(2)
    actions.wait_for_alert_present(5)
    actions.dismiss_alert(ignore_not_present=True)
