from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify_alert_present action'


def test_verify_alert_present(data):
    actions.navigate(data.env.url+'alert/')
    actions.verify_alert_present()
    golem_steps.assert_last_step_message('Verify an alert is present')
    golem_steps.assert_last_error('an alert was not present')
    actions.click('#alert-button')
    actions.verify_alert_present()
    actions.dismiss_alert()
