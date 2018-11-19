from golem import actions
from golem import browser

from projects.golem_integration.pages import golem_steps


description = 'Verify activate_browser enables switching between different opened browser sessions'

def test(data):
    actions.open_browser()
    actions.navigate(data.env.url)
    assert browser.get_browser().current_url == data.env.url
    actions.open_browser('second_browser')
    actions.activate_browser('second_browser')
    assert golem_steps.get_last_step_message() == 'Activate browser second_browser'
    actions.navigate(data.env.url + 'elements/')
    assert browser.get_browser().current_url == data.env.url + 'elements/'
    actions.activate_browser('main')
    assert browser.get_browser().current_url == data.env.url
