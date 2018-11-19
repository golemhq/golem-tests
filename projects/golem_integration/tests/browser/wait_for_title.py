from golem import actions

from projects.golem_integration.utils import expected_exception


description = 'Verify webdriver.wait_for_title method'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=2')
    actions.verify_title('Web Playground - Dynamic Elements')
    actions.click('#change-title-button')
    actions.get_browser().wait_for_title('New Title', 4)
    actions.verify_title('New Title')
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    with expected_exception(Exception, "Timeout waiting for title to be 'New Title'"):
        actions.click('#change-title-button')
        actions.get_browser().wait_for_title('New Title', 2)
