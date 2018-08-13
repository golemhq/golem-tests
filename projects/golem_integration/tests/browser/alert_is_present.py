from golem import actions


description = 'Verify webdriver.alert_is_present method'

def test(data):
    browser = actions.get_browser()
    browser.navigate(data.env.url + 'alert/')
    assert browser.alert_is_present() is False
    actions.click('#alert-button')
    assert browser.alert_is_present() is True
    browser.dismiss_alert()
    assert browser.alert_is_present() is False