from golem import execution
from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify verify_alert_text_is_not action'


def test_verify_alert_text_is_not(data):
    actions.navigate(data.env.url+'alert/')
    actions.click('#alert-button')
    actions.verify_alert_text_is_not('incorrect text')
    golem_steps.assert_last_step_message("Verify alert text is not 'incorrect text'")
    # Temporarily disable screenshot on error
    # Selenium cannot take screenshots when alert is present
    # TODO
    current = execution.settings['screenshot_on_error']
    execution.settings['screenshot_on_error'] = False
    actions.verify_alert_text_is_not('an alert')
    golem_steps.assert_last_error("Expected alert text not to be 'an alert'")
    actions.dismiss_alert()
    execution.settings['screenshot_on_error'] = current
