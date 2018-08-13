from golem import actions


description = 'Verify webdriver.wait_for_alert_present method'

def test(data):
    actions.navigate(data.env.url+'alert/')
    actions.click('#alert-delay-button')
    actions.get_browser().wait_for_alert_present(10)
    actions.verify_alert_present()
    actions.dismiss_alert()
    actions.click('#alert-delay-button')
    try:
        actions.get_browser().wait_for_alert_present(3)
        assert False, 'Expected Exception'
    except Exception as e:
        "Timeout waiting for alert to be present" in e.args[0]
    actions.dismiss_alert(ignore_not_present=True)
