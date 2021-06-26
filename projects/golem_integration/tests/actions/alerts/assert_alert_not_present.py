from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'assert_alert_not_present action'


def test_assert_alert_not_present(data):
    actions.navigate(data.env.url+'alert/')
    actions.assert_alert_not_present()
    assert golem_steps.get_last_step_message() == 'Assert an alert is not present'
    actions.click('#alert-button')
    with expected_exception(AssertionError, 'an alert was present'):
        actions.assert_alert_not_present()
    actions.dismiss_alert()
    actions.assert_alert_not_present()
