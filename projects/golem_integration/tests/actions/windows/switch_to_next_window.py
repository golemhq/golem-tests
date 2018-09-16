from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify switch_to_next_window action'

def test(data):
    actions.navigate(data.env.url+'tabs/')
    actions.send_keys('#urlInput', '/elements/')
    actions.click("#goButton")
    actions.clear_element('#urlInput')
    actions.send_keys('#urlInput', '/alert/')
    actions.click("#goButton")
    actions.switch_to_window_by_index(0)
    first_title = actions.get_window_title()
    actions.switch_to_window_by_index(1)
    second_title = actions.get_window_title()
    actions.switch_to_window_by_index(2)
    third_title = actions.get_window_title()
    actions.switch_to_window_by_index(0)
    actions.switch_to_next_window()
    golem_steps.assert_last_step_message('Switch to next window')
    actions.verify_title(second_title)
    actions.switch_to_next_window()
    actions.verify_title(third_title)
    actions.switch_to_next_window()
    actions.verify_title(first_title)