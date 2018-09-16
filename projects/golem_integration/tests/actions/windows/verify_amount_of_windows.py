from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'verify_amount_of_windows action'

def test(data):
    actions.navigate(data.env.url+'tabs/')
    actions.send_keys('#urlInput', '/elements/')
    actions.click("#goButton")
    actions.wait_for_window_present_by_title('Elements')
    actions.verify_amount_of_windows(2)
    golem_steps.assert_last_step_message('Verify amount of open windows is 2')
    actions.switch_to_window_by_title('Elements')
    actions.close_window()
    actions.verify_amount_of_windows(1)
    actions.verify_amount_of_windows(3)

