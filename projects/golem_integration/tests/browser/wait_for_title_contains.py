from golem import actions

from projects.golem_integration.utils import expected_exception


description = 'Verify webdriver.wait_for_title_contains method'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    actions.verify_title('Dynamic Elements')
    actions.click('#change-title-button')
    actions.get_browser().wait_for_title_contains('New', 5)
    actions.verify_title_contains('New')
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    msg = "Timeout waiting for title to contain 'New'"
    with expected_exception(Exception, msg):
        actions.click('#change-title-button')
        actions.get_browser().wait_for_title_contains('New', 5)
