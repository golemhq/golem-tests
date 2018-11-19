from golem import actions

from projects.golem_integration.utils import expected_exception


description = 'Verify webdriver.wait_for_title_contains method'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    actions.click('#change-title-button')
    actions.assert_title('Web Playground - Dynamic Elements')
    actions.get_browser().wait_for_title_contains('New', 4)
    actions.assert_title('New Title')
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    msg = "Timeout waiting for title to contain 'New'"
    with expected_exception(Exception, msg):
        actions.click('#change-title-button')
        actions.get_browser().wait_for_title_contains('New', 2)
