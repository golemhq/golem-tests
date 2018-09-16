from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'assert_alert_not_present action'

def test(data):
    actions.navigate(data.env.url+'alert/')
    actions.assert_alert_not_present()
    assert golem_steps.get_last_step_message() == 'Assert an alert is not present'
    actions.click('#alert-button')
    try:
        actions.assert_alert_not_present()
    except AssertionError as e:
        assert 'an alert was present' in e.args[0]
    actions.dismiss_alert()
    actions.assert_alert_not_present()
