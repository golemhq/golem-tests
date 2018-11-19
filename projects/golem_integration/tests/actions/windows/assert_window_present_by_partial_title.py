from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'assert_window_present_by_partial_title action'

def test(data):
    url = data.env.url + 'tabs/'  # title = 'Web Playground - Tabs'
    actions.navigate(url)
    actions.send_keys('#title', 'lorem ipsum')
    actions.click('#goButtonCustom')
    actions.assert_window_present_by_partial_title('ground - Tabs')
    golem_steps.assert_last_step_message("Assert window present by partial title 'ground - Tabs'")
    actions.wait(1)
    actions.assert_window_present_by_partial_title('lorem')
    try:
        actions.assert_window_present_by_partial_title('incorrect')
    except AssertionError as e:
        expected = "There is no window present with partial title 'incorrect'".format(url)
        assert expected in e.args[0]
