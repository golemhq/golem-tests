from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'close_window_by_url action'

def test(data):
    actions.navigate(data.env.url + 'tabs/')
    actions.send_keys('#title', 'foo')
    actions.click('#goButton')
    actions.assert_amount_of_windows(2)
    tab_url = data.env.url + 'tab/'
    actions.close_window_by_partial_url(tab_url)
    golem_steps.assert_last_step_message("Close window by url '{}'".format(tab_url))
    actions.assert_amount_of_windows(1)
