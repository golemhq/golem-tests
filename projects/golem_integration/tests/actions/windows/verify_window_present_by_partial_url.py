from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'verify_window_present_by_partial_url action'

def test(data):
    actions.navigate(data.env.url + 'tabs/')
    actions.send_keys('#urlInput', '/elements/')
    actions.click("#goButton")
    actions.verify_window_present_by_partial_url('tab')
    golem_steps.assert_last_step_message("Verify window present by partial URL 'tab'")
    actions.verify_window_present_by_partial_url('elem')
