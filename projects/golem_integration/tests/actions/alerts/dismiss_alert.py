from golem import actions


description = 'Verify dismiss_alert action'

def test(data):
    # alert
    actions.navigate(data.env.url+'alert/')
    actions.click('#alert-button')
    actions.verify_alert_present()
    actions.dismiss_alert()
    actions.verify_alert_not_present()
    actions.verify_text_in_element('#result', '1')
    # confirm
    actions.navigate(data.env.url + 'confirm/')
    actions.click('#confirm-button')
    actions.verify_alert_present()
    actions.dismiss_alert()
    actions.verify_alert_not_present()
    actions.verify_text_in_element('#result', 'NOT CONFIRMED')
    # prompt
    actions.navigate(data.env.url + 'prompt/')
    actions.click('#prompt-button')
    actions.verify_alert_present()
    actions.dismiss_alert()
    actions.verify_alert_not_present()
    actions.verify_text_in_element('#result', 'DISMISSED')
