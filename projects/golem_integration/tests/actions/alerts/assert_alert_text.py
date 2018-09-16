from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'assert_alert_text action'

def test(data):
    actions.navigate(data.env.url+'alert/')
    actions.click('#alert-button')
    actions.assert_alert_text('an alert')
    assert golem_steps.get_last_step_message() == "Assert alert text is 'an alert'"
    try:
        actions.assert_alert_text('incorrect text')
    except AssertionError as e:
        assert "Expected alert text to be 'incorrect text' but was 'an alert'" in e.args[0]
    actions.dismiss_alert()
