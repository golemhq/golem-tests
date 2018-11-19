from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'assert_window_present_by_partial_url action'

def test(data):
    url = data.env.url + 'tabs/'
    actions.navigate(url)
    actions.click('#openTab')
    actions.assert_window_present_by_partial_url('tabs/')
    golem_steps.assert_last_step_message("Assert window present by partial URL 'tabs/'")
    actions.assert_window_present_by_partial_url('tab/')
    try:
        actions.assert_window_present_by_partial_url('incorrect')
    except AssertionError as e:
        expected = "There is no window present with partial URL 'incorrect'".format(url)
        assert expected in e.args[0]
