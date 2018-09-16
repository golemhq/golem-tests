from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'assert_window_present_by_title action'

def test(data):
    url = data.env.url + 'tabs/'
    actions.navigate(url)
    actions.send_keys('#title', 'testing')
    actions.click('#goButton')
    actions.assert_window_present_by_title('Tabs')
    golem_steps.assert_last_step_message("Assert window present by title 'Tabs'")
    actions.assert_window_present_by_title('testing')
    try:
        actions.assert_window_present_by_title('incorrect')
    except AssertionError as e:
        expected = "There is no window present with title 'incorrect'".format(url)
        assert expected in e.args[0]
