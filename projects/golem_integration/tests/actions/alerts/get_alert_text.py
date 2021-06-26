from golem import actions


description = 'Verify get_alert_text action'


def test_get_alert_text(data):
    actions.navigate(data.env.url+'alert/')
    actions.click('#alert-button')
    assert actions.get_alert_text() == 'an alert'
    actions.dismiss_alert()
