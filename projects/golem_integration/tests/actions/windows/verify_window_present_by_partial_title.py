from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'verify_window_present_by_partial_title action'

def test(data):
    actions.navigate(data.env.url+'tabs/')
    actions.send_keys('#urlInput', '/elements/')
    actions.click("#goButton")
    actions.verify_window_present_by_partial_title('Elem')  # Elements
    golem_steps.assert_last_step_message("Verify window present by partial title 'Elem'")
    actions.verify_window_present_by_partial_title('Tab')  # Tabs
