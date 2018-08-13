from golem import actions


description = 'verify_amount_of_windows action'

def test(data):
    actions.navigate(data.env.url+'tabs/')
    actions.send_keys('#urlInput', '/elements/')
    actions.click("#goButton")
    actions.wait_for_window_present_by_title('Elements')
    actions.verify_amount_of_windows(2)
    actions.switch_to_window_by_title('Elements')
    actions.close_window()
    actions.verify_amount_of_windows(1)
    try:
        actions.verify_amount_of_windows(3)
        assert False, 'Expected Exception'
    except Exception as e:
        assert 'Expected 3 windows but got 1' in e.args[0]
