from golem import actions


description = 'Verify switch_to_window_by_title action'

def test(data):
    actions.navigate(data.env.url+'tabs/')
    actions.send_keys('#urlInput', '/elements/')
    actions.click("#goButton")
    actions.wait_for_window_present_by_title('Elements', timeout=10)
    actions.switch_to_window_by_title('Elements')
    actions.verify_title('Elements')
    try:
        actions.switch_to_window_by_title('incorrect title')
        assert False, 'Expected Exception'
    except Exception as e:
        assert 'Window with title \'incorrect title\' was not found' in e.args[0]
