from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'assert_window_present_by_url action'

def test(data):
    url = data.env.url + 'tabs/'
    url_tab = data.env.url + 'tab/'
    actions.navigate(url)
    actions.click('#openTab')
    actions.assert_window_present_by_url(url)
    golem_steps.assert_last_step_message("Assert window present by URL '{}'".format(url))
    actions.assert_window_present_by_url(url_tab)
    expected = "There is no window present with URL 'incorrect'"
    with expected_exception(AssertionError, expected):
        actions.assert_window_present_by_url('incorrect')
