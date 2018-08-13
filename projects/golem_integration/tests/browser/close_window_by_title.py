from golem import actions


description = 'Verify webdriver.close_window_by_title method'

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
    # close third window by title
    actions.get_browser().close_window_by_title(third_title)
    actions.verify_amount_of_windows(2)
    actions.verify_title(first_title)
    # close first window by title, from the first window
    actions.get_browser().close_window_by_title(first_title)
    # second window is now active
    actions.verify_amount_of_windows(1)
    actions.verify_title(second_title)
    # try to close a window that is not present
    try:
        actions.get_browser().close_window_by_title('Incorrect Title')
        assert False, 'Expected Exception'
    except Exception as e:
        assert "a window with title 'Incorrect Title' was not found" in e.args[0]
