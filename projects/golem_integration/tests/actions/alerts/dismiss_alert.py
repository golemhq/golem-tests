from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify dismiss_alert action'

def test(data):
    # alert
    actions.navigate(data.env.url+'alert/')
    actions.click('#alert-button')
    actions.verify_alert_present()
    actions.dismiss_alert()
    golem_steps.assert_last_step_message('Dismiss alert')
    actions.verify_alert_not_present()
    actions.verify_element_text('#result', '1')
    # confirm
    actions.navigate(data.env.url + 'confirm/')
    actions.click('#confirm-button')
    actions.verify_alert_present()
    actions.dismiss_alert()
    actions.verify_alert_not_present()
    actions.verify_element_text('#result', 'NOT CONFIRMED')
    # prompt
    actions.navigate(data.env.url + 'prompt/')
    actions.click('#prompt-button')
    actions.verify_alert_present()
    actions.dismiss_alert()
    actions.verify_alert_not_present()
    actions.verify_element_text('#result', 'DISMISSED')
