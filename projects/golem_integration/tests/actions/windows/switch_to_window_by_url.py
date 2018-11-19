from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'Verify switch_to_window_by_url action'

def test(data):
    tabs_url = data.env.url + 'tabs/'
    elements_url = data.env.url+'elements/'
    nonexistent_url = data.env.url+'nonexistent-url/'
    actions.navigate(tabs_url)
    actions.send_keys('#urlInput', '/elements/')
    actions.click("#goButton")
    actions.switch_to_window_by_url(elements_url)
    golem_steps.assert_last_step_message("Switch to window with URL '{}'".format(elements_url))
    actions.verify_title('Web Playground - Elements')
    actions.switch_to_window_by_url(tabs_url)
    actions.verify_title('Web Playground - Tabs')
    msg = "Window with URL '{}' was not found".format(nonexistent_url)
    with expected_exception(Exception, msg):
        actions.switch_to_window_by_url(nonexistent_url)
