from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'assert_window_present_by_title action'

def test(data):
    url = data.env.url + 'tabs/'
    actions.navigate(url)
    actions.send_keys('#title', 'lorem ipsum')
    actions.click('#goButtonCustom')
    actions.assert_window_present_by_title('Web Playground - Tabs')
    golem_steps.assert_last_step_message("Assert window present by title 'Web Playground - Tabs'")
    actions.assert_window_present_by_title('lorem ipsum')
    expected = "There is no window present with title 'incorrect'".format(url)
    with expected_exception(AssertionError, expected):
        actions.assert_window_present_by_title('incorrect')
