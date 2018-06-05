from golem import actions


description = 'Verify accept_alert action when alert is not present'

def test(data):
    actions.navigate(data.env.url+'alert/')
    actions.accept_alert(ignore_not_present=True)
    actions.click('#alert-button')
    try:
        actions.accept_alert()
    except Exception as e:
        assert e.__class__.__name__ == 'NoAlertPresentException'