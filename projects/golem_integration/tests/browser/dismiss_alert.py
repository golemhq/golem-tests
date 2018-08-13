from golem import actions


description = 'Verify webdriver.dismiss_alert method'

def test(data):
    browser = actions.get_browser()
    browser.navigate(data.env.url + 'alert/')
    actions.click('#alert-button')
    assert browser.alert_is_present() is True
    browser.dismiss_alert()
    assert browser.alert_is_present() is False
    browser.dismiss_alert(ignore_not_present=True)
    try:
        browser.dismiss_alert()
        assert False, 'Expected Exception'
    except Exception as e:
        assert e.__class__.__name__ == 'NoAlertPresentException'