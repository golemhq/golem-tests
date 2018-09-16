from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'assert_alert_text_is_not action'

def test(data):
    actions.navigate(data.env.url+'alert/')
    actions.click('#alert-button')
    actions.assert_alert_text_is_not('incorrect text')
    assert golem_steps.get_last_step_message() == "Assert alert text is not 'incorrect text'"
    try:
        actions.assert_alert_text_is_not('an alert')
    except Exception as e:
        assert "Expected alert text not to be 'an alert'" in e.args[0]
    actions.dismiss_alert()
