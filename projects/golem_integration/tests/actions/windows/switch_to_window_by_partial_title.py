from golem import actions


description = 'Verify switch_to_window_by_partial_title action'

def test(data):
    actions.navigate(data.env.url+'tabs/')
    actions.send_keys('#urlInput', '/elements/')
    actions.click("#goButton")
    actions.switch_to_window_by_partial_title('Ele')
    actions.verify_title('Elements')
    try:
        actions.switch_to_window_by_partial_title('incorrect title')
        assert False, 'Expected Exception'
    except Exception as e:
        assert 'Window with partial title \'incorrect title\' was not found' in e.args[0]
