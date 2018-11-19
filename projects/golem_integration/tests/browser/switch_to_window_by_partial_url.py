from golem import actions

from projects.golem_integration.utils import expected_exception


description = 'Verify webdriver.switch_to_window_by_partial_url method'

def test(data):
    actions.navigate(data.env.url + 'tabs/')
    actions.send_keys('#urlInput', '/elements/')
    actions.click("#goButton")
    actions.get_browser().switch_to_window_by_partial_url('elem')
    actions.verify_title('Web Playground - Elements')
    actions.get_browser().switch_to_window_by_partial_url('tab')
    actions.verify_title('Web Playground - Tabs')
    msg = "Window with partial URL 'xyz' was not found"
    with expected_exception(Exception, msg):
        actions.get_browser().switch_to_window_by_partial_url('xyz')
