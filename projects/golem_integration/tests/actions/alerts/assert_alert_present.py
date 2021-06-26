from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'assert_alert_present action'


def test_assert_alert_present(data):
    actions.navigate(data.env.url+'alert/')
    with expected_exception(AssertionError, 'an alert was not present'):
        actions.assert_alert_present()
    actions.click('#alert-button')
    actions.assert_alert_present()
    assert golem_steps.get_last_step_message() == 'Assert an alert is present'
    actions.dismiss_alert()
