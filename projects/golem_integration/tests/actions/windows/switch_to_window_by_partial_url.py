from golem import actions


description = 'Verify switch_to_window_by_partial_url action'

def test(data):
    actions.navigate(data.env.url + 'tabs/')
    actions.send_keys('#urlInput', '/elements/')
    actions.click("#goButton")
    actions.switch_to_window_by_partial_url('elem')
    actions.verify_title('Elements')
    actions.switch_to_window_by_partial_url('tab')
    actions.verify_title('Tabs')
    try:
        actions.switch_to_window_by_partial_url('xyz')
        assert False, 'Expected Exception'
    except Exception as e:
        assert 'Window with partial URL \'xyz\' was not found' in e.args[0]
