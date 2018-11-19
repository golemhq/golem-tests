from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'assert_alert_text action'

def test(data):
    actions.navigate(data.env.url+'alert/')
    actions.click('#alert-button')
    actions.assert_alert_text('an alert')
    assert golem_steps.get_last_step_message() == "Assert alert text is 'an alert'"
    msg = "expected alert text to be 'incorrect text' but was 'an alert'"
    with expected_exception(AssertionError, msg):
        actions.assert_alert_text('incorrect text')
    actions.dismiss_alert()
