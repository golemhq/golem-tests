from golem import actions


description = 'Verify verify_alert_text action'

def test(data):
    actions.navigate(data.env.url+'alert/')
    actions.click('#alert-button')
    actions.verify_alert_text('an alert')
    try:
        actions.verify_alert_text('incorrect text')
        assert False, 'Expected Exception'
    except Exception as e:
        assert "Expected alert text to be 'incorrect text' but was 'an alert'" in e.args[0]
    actions.dismiss_alert()
