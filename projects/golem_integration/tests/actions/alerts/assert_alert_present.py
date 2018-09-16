from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'assert_alert_present action'

def test(data):
    actions.navigate(data.env.url+'alert/')
    try:
        actions.assert_alert_present()
    except AssertionError as e:
        assert 'an alert was not present' in e.args[0]
    actions.click('#alert-button')
    actions.assert_alert_present()
    assert golem_steps.get_last_step_message() == 'Assert an alert is present'
    actions.dismiss_alert()