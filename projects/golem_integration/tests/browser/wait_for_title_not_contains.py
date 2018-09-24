from golem import actions

from projects.golem_integration.utils import expected_exception


description = 'Verify webdriver.wait_for_title_not_contains method'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    actions.verify_title('Dynamic Elements')
    actions.click('#change-title-button')
    actions.get_browser().wait_for_title_not_contains('Dynamic', 5)
    actions.verify_title_not_contains('Dynamic')
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    msg = "Timeout waiting for title to not contain 'Dynamic'"
    with expected_exception(Exception, msg):
        actions.click('#change-title-button')
        actions.get_browser().wait_for_title_not_contains('Dynamic', 5)
