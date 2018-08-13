from golem import actions


description = 'Verify close_window_by_url action'

def test(data):
    actions.navigate(data.env.url+'tabs/')
    actions.send_keys('#urlInput', '/elements/')
    actions.click("#goButton")
    actions.clear_element('#urlInput')
    actions.send_keys('#urlInput', '/alert/')
    actions.click("#goButton")
    actions.switch_to_window_by_index(0)
    first_url = actions.get_current_url()
    first_url_partial = first_url[:-2]
    actions.switch_to_window_by_index(1)
    second_url = actions.get_current_url()
    second_url_partial = second_url[:-2]
    actions.switch_to_window_by_index(2)
    third_url = actions.get_current_url()
    third_url_partial = third_url[:-2]
    actions.switch_to_window_by_index(0)
    # close third window by partial URL
    actions.close_window_by_partial_url(third_url_partial)
    actions.verify_amount_of_windows(2)
    actions.verify_url(first_url)
    # close first window by URL, from the first window
    actions.close_window_by_partial_url(first_url_partial)
    # second window is now active
    actions.verify_amount_of_windows(1)
    actions.verify_url(second_url)
    # try to close a window that is not present
    try:
        actions.close_window_by_partial_url('/incorrect/url')
        assert False, 'Expected Exception'
    except Exception as e:
        assert "a window with partial URL '/incorrect/url' was not found" in e.args[0]
