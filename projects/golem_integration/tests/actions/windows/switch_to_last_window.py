from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify switch_to_last_window action'

def test(data):
    actions.navigate(data.env.url+'tabs/')
    # open two more tabs
    actions.send_keys('#title', 'SECOND TAB')
    actions.click('#goButtonCustom')
    actions.clear_element('#title')
    actions.send_keys('#title', 'THIRD TAB')
    actions.click('#goButtonCustom')
    # wait for the new tabs to load
    actions.wait_for_window_present_by_title('SECOND TAB', timeout=5)
    actions.wait_for_window_present_by_title('THIRD TAB', timeout=5)
    # switch to last tab and navigate to index
    actions.switch_to_window_by_index(2)
    assert actions.get_window_index() == 2
    actions.navigate(data.env.url)
    # switch to first tab
    actions.switch_to_first_window()
    actions.assert_title('Web Playground - Tabs')
    # switch to last tab
    actions.switch_to_last_window()
    golem_steps.assert_last_step_message('Switch to last window')
    assert actions.get_window_index() == 2
    actions.assert_title('Web Playground')
