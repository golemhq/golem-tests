from golem import actions


description = 'Verify webdriver.switch_to_next_window method'

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
    actions.get_browser().switch_to_next_window()
    actions.verify_title(second_title)
    actions.get_browser().switch_to_next_window()
    actions.verify_title(third_title)
    actions.get_browser().switch_to_next_window()
    actions.verify_title(first_title)