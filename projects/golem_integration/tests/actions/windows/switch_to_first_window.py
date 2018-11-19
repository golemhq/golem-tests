from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify switch_to_first_window action'

def test(data):
    actions.navigate(data.env.url+'tabs/')
    actions.click('#openTab')
    actions.wait_for_window_present_by_title('Tab')
    actions.switch_to_window_by_index(1)
    assert actions.get_window_index() == 1
    actions.assert_title('Tab')
    actions.switch_to_first_window()
    golem_steps.assert_last_step_message('Switch to first window')
    assert actions.get_window_index() == 0
    actions.assert_title('Web Playground - Tabs')