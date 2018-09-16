from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify switch_to_window_by_index action'

def test(data):
    actions.navigate(data.env.url+'tabs/')
    actions.click('#openTab')
    # firefox does not wait for tabs to load
    actions.wait_for_window_present_by_title('Tab')
    actions.switch_to_window_by_index(1)
    golem_steps.assert_last_step_message('Switch to window of index 1')
    assert actions.get_window_index() == 1
    actions.verify_title('Tab')
    actions.switch_to_window_by_index(0)
    assert actions.get_window_index() == 0
    actions.verify_title('Tabs')