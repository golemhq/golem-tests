from golem import actions

from projects.golem_integration.utils import expected_exception


description = 'Verify webdriver.wait_for_alert_present method'

def test(data):
    actions.navigate(data.env.url+'alert/')
    actions.click('#alert-delay-button')
    browser = actions.get_browser()
    browser.wait_for_alert_present(5)
    actions.verify_alert_present()
    actions.dismiss_alert()
    actions.click('#alert-delay-button')
    with expected_exception(Exception, "Timeout waiting for alert to be present"):
        browser.wait_for_alert_present(2)
    browser.wait_for_alert_present(5)
    actions.dismiss_alert(ignore_not_present=True)
