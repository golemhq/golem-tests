from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'assert_alert_text_is_not action'


def test_assert_alert_text_is_not(data):
    actions.navigate(data.env.url+'alert/')
    actions.click('#alert-button')
    actions.assert_alert_text_is_not('incorrect text')
    assert golem_steps.get_last_step_message() == "Assert alert text is not 'incorrect text'"
    with expected_exception(AssertionError, "expected alert text not to be 'an alert'"):
        actions.assert_alert_text_is_not('an alert')
    actions.dismiss_alert()
