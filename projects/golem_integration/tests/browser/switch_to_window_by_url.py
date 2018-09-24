from golem import actions

from projects.golem_integration.utils import expected_exception


description = 'Verify webdriver.switch_to_window_by_url method'

def test(data):
    tabs_url = data.env.url + 'tabs/'
    elements_url = data.env.url+'elements/'
    nonexistent_url = data.env.url+'nonexistent-url/'
    actions.navigate(tabs_url)
    actions.send_keys('#urlInput', '/elements/')
    actions.click("#goButton")
    actions.get_browser().switch_to_window_by_url(elements_url)
    actions.verify_title('Elements')
    actions.get_browser().switch_to_window_by_url(tabs_url)
    actions.verify_title('Tabs')
    msg = "Window with URL '{}' was not found".format(nonexistent_url)
    with expected_exception(Exception, msg):
        actions.get_browser().switch_to_window_by_url(nonexistent_url)
