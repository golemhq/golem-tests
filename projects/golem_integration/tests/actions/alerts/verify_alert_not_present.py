from golem import actions
from golem import execution

from projects.golem_integration.pages import golem_steps


description = 'Verify_alert_not_present action'


def test_verify_alert_not_present(data):
    actions.navigate(data.env.url+'alert/')
    actions.verify_alert_not_present()
    golem_steps.assert_last_step_message('Verify an alert is not present')
    actions.click('#alert-button')
    # Temporarily disable screenshot on error
    # Selenium cannot take screenshots when alert is present
    # TODO
    current = execution.settings['screenshot_on_error']
    execution.settings['screenshot_on_error'] = False
    actions.verify_alert_not_present()
    golem_steps.assert_last_error('an alert was present')
    actions.dismiss_alert()
    execution.settings['screenshot_on_error'] = current
