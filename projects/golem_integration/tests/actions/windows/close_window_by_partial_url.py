from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'close_window_by_partial_url action'

def test(data):
    actions.navigate(data.env.url + 'tabs/')
    actions.send_keys('#title', 'foo')
    actions.click('#goButtonCustom')
    actions.assert_amount_of_windows(2)
    actions.close_window_by_partial_url('tab/')
    golem_steps.assert_last_step_message("Close window by partial URL 'tab/'")
    actions.assert_amount_of_windows(1)

