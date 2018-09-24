from golem import actions

from projects.golem_integration.utils import expected_exception


description = 'Verify webdriver.switch_to_window_by_partial_title method'

def test(data):
    actions.navigate(data.env.url+'tabs/')
    actions.send_keys('#urlInput', '/elements/')
    actions.click("#goButton")
    actions.get_browser().switch_to_window_by_partial_title('Ele')
    actions.verify_title('Elements')
    msg = "Window with partial title 'incorrect title' was not found"
    with expected_exception(Exception, msg):
        actions.get_browser().switch_to_window_by_partial_title('incorrect title')
