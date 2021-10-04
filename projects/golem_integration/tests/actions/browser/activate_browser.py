from golem import actions
from golem import browser

from projects.golem_integration.pages import golem_steps


description = 'Verify activate_browser enables switching between different opened browser sessions'


def test_activate_browser(data):
    actions.open_browser()
    actions.navigate(data.env.url)
    assert browser.get_browser().current_url == data.env.url
    actions.open_browser('second_browser')
    actions.activate_browser(browser_id='second_browser')
    assert golem_steps.get_last_step_message() == 'Activate browser second_browser'
    actions.navigate(data.env.url + 'elements/')
    assert browser.get_browser().current_url == data.env.url + 'elements/'
    actions.activate_browser('main')
    assert browser.get_browser().current_url == data.env.url


def test_activate_browser_with_invalid_id(data):
    actions.open_browser()
    actions.navigate(data.env.url)
    try:
        actions.activate_browser('second_browser')
    except Exception as e:
        assert 'is not a valid browser id' in e.args[0]
