from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'close_window_by_partial_title action'

def test(data):
    actions.navigate(data.env.url + 'tabs/')
    actions.send_keys('#title', 'lorem ipsum')
    actions.click('#goButtonCustom')
    actions.assert_amount_of_windows(2)
    actions.close_window_by_partial_title('lorem')
    golem_steps.assert_last_step_message("Close window by partial title 'lorem'")
    actions.assert_amount_of_windows(1)

