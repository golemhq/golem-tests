from golem import actions


description = 'Verify wait_for_alert_present action'

def test(data):
    actions.navigate(data.env.url+'alert/')
    actions.click('#alert-delay-button')
    actions.wait_for_alert_present(10)
    actions.verify_alert_present()
    actions.dismiss_alert()
    actions.click('#alert-delay-button')
    try:
        actions.wait_for_alert_present(3)
    except Exception as e:
        assert e.__class__.__name__ == 'TimeoutException'
    actions.dismiss_alert(ignore_not_present=True)
