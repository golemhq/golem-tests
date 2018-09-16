from selenium.common.exceptions import TimeoutException
from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify wait_for_alert_present action'

def test(data):
    actions.navigate(data.env.url+'alert/')
    actions.click('#alert-delay-button')
    actions.wait_for_alert_present(10)
    golem_steps.assert_last_step_message('Wait for alert to be present')
    actions.verify_alert_present()
    actions.dismiss_alert()
    actions.click('#alert-delay-button')
    try:
        actions.wait_for_alert_present(3)
        assert False, 'Expected Exception'
    except TimeoutException as e:
        assert "Timeout waiting for alert to be present" in e.args[0]
    actions.dismiss_alert(ignore_not_present=True)
