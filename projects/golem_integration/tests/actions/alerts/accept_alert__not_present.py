from golem import actions


description = 'Verify accept_alert action when alert is not present'

def test(data):
    actions.navigate(data.env.url+'alert/')
    actions.accept_alert(ignore_not_present=True)
    try:
        actions.accept_alert()
        assert False, 'Expected NoAlertPresentException'
    except Exception as e:
        assert e.__class__.__name__ == 'NoAlertPresentException'