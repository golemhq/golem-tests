from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'close_window action'

def test(data):
    actions.navigate(data.env.url + 'tabs/')
    actions.click('#openTab')
    actions.wait_for_window_present_by_title('Tab', 5)
    actions.assert_amount_of_windows(2)
    actions.switch_to_window_by_title('Tab')
    actions.assert_title('Tab')
    actions.close_window()
    golem_steps.assert_last_step_message('Close current window')
    actions.assert_amount_of_windows(1)
    actions.assert_title('Tabs')
