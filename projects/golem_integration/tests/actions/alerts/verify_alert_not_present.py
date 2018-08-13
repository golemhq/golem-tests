from golem import actions


description = 'Verify_alert_not_present action'

def test(data):
    actions.navigate(data.env.url+'alert/')
    actions.verify_alert_not_present()
    actions.click('#alert-button')
    try:
        actions.verify_alert_not_present()
        assert False, 'Expected Exception'
    except Exception as e:
        assert 'an alert was present' in e.args[0]
    actions.dismiss_alert()
    actions.verify_alert_not_present()
