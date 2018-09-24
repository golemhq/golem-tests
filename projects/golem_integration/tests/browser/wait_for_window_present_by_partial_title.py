from golem import actions

from projects.golem_integration.utils import expected_exception


description = 'Verify webdriver.window_present_by_partial_title method'

def test(data):
    actions.navigate(data.env.url+'tabs/')
    actions.send_keys('#delay', 3)
    actions.send_keys('#title', 'MY TITLE')
    actions.click("#goButtonCustom")
    actions.get_browser().wait_for_window_present_by_partial_title('MY TI', timeout=5)
    actions.verify_window_present_by_title('MY TITLE')
    msg = "Timeout waiting for window present by partial title 'TITLE NOT PRESENT'"
    with expected_exception(Exception, msg):
        actions.get_browser().wait_for_window_present_by_partial_title('TITLE NOT PRESENT', timeout=3)
