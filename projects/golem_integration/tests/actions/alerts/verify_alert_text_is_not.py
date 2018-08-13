from golem import actions


description = 'Verify verify_alert_text_is_not action'

def test(data):
    actions.navigate(data.env.url+'alert/')
    actions.click('#alert-button')
    actions.verify_alert_text_is_not('incorrect text')
    try:
        actions.verify_alert_text_is_not('an alert')
        assert False, 'Expected Exception'
    except Exception as e:
        assert "Expected alert text not to be 'an alert'" in e.args[0]
    actions.dismiss_alert()
