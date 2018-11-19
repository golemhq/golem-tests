from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'verify_window_present_by_title action'

def test(data):
    actions.navigate(data.env.url+'tabs/')
    actions.click("#openTab")
    actions.wait_for_window_present_by_title('Tab', 5)
    actions.verify_window_present_by_title('Tab')
    golem_steps.assert_last_step_message("Verify window present by title 'Tab'")
    actions.verify_window_present_by_title('Tabs')
