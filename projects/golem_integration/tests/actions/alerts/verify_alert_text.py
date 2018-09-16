from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify verify_alert_text action'

def test(data):
    actions.navigate(data.env.url+'alert/')
    actions.click('#alert-button')
    actions.verify_alert_text('an alert')
    golem_steps.assert_last_step_message("Verify alert text is 'an alert'")
    actions.verify_alert_text('incorrect text')
    expected = "Expected alert text to be 'incorrect text' but was 'an alert'"
    golem_steps.assert_last_error(expected)
    actions.dismiss_alert()
