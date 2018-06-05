from golem import actions


description = 'Verify dismiss_alert action when alert is not present'

def test(data):
    actions.navigate(data.env.url+'alert/')
    actions.dismiss_alert(ignore_not_present=True)
    actions.click('#alert-button')
    try:
        actions.dismiss_alert()
    except Exception as e:
        assert e.__class__.__name__ == 'NoAlertPresentException'