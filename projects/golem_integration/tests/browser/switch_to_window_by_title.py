from golem import actions

from projects.golem_integration.utils import expected_exception


description = 'Verify webdriver.switch_to_window_by_title method'

def test(data):
    actions.navigate(data.env.url+'tabs/')
    actions.send_keys('#urlInput', '/elements/')
    actions.click("#goButton")
    actions.get_browser().switch_to_window_by_title('Web Playground - Elements')
    actions.verify_title('Web Playground - Elements')
    with expected_exception(Exception,
                            "Window with title 'incorrect title' was not found"):
        actions.get_browser().switch_to_window_by_title('incorrect title')
