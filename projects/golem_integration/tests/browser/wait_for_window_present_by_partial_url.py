from golem import actions

from projects.golem_integration.utils import expected_exception


description = 'Verify webdriver.window_present_by_partial_url method'

def test(data):
    actions.navigate(data.env.url+'tabs/')
    actions.send_keys('#delay', 3)
    actions.send_keys('#title', 'MY_TITLE')
    actions.click("#goButtonCustom")
    partial_url = 'delay=3&title=MY_TITLE'
    actions.get_browser().wait_for_window_present_by_partial_url(partial_url, timeout=5)
    actions.verify_window_present_by_partial_url(partial_url)
    msg = "Timeout waiting for window present by partial url 'URL_NOT_PRESENT'"
    with expected_exception(Exception, msg):
        actions.get_browser().wait_for_window_present_by_partial_url('URL_NOT_PRESENT', timeout=3)
