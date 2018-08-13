from golem import actions


description = 'Verify close_window_by_partial_title action'

def test(data):
    actions.navigate(data.env.url+'tabs/')
    actions.send_keys('#urlInput', '/elements/')
    actions.click("#goButton")
    actions.clear_element('#urlInput')
    actions.send_keys('#urlInput', '/alert/')
    actions.click("#goButton")
    actions.switch_to_window_by_index(0)
    first_title = actions.get_window_title()
    first_title_partial = first_title[:-2]
    actions.switch_to_window_by_index(1)
    second_title = actions.get_window_title()
    second_title_partial = second_title[:-2]
    actions.switch_to_window_by_index(2)
    third_title = actions.get_window_title()
    third_title_partial = third_title[:-2]
    actions.switch_to_window_by_index(0)
    # close third window by partial title
    actions.close_window_by_partial_title(third_title_partial)
    actions.verify_amount_of_windows(2)
    actions.verify_title(first_title)
    # close first window by partial title, from the first window
    actions.close_window_by_partial_title(first_title_partial)
    # second window is now active
    actions.verify_amount_of_windows(1)
    actions.verify_title(second_title)
    # try to close a window that is not present
    try:
        actions.close_window_by_partial_title('Incorrect Title')
        assert False, 'Expected Exception'
    except Exception as e:
        assert "a window with partial title 'Incorrect Title' was not found" in e.args[0]
