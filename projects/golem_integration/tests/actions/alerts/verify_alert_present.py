from golem import actions


description = 'Verify_alert_present action'

def test(data):
    actions.navigate(data.env.url+'alert/')
    try:
        actions.verify_alert_present()
    except Exception as e:
        assert 'an alert was not present' in e.args[0]
    actions.click('#alert-button')
    actions.verify_alert_present()
    actions.dismiss_alert()