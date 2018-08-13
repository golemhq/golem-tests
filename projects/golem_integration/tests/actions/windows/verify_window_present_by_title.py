from golem import actions


description = 'verify_window_present_by_title action'

def test(data):
    actions.navigate(data.env.url+'tabs/')
    actions.send_keys('#urlInput', '/elements/')
    actions.click("#goButton")
    actions.verify_window_present_by_title('Elements')
    actions.verify_window_present_by_title('Tabs')
    try:
        actions.verify_window_present_by_title('Title Not Present')
        assert False, 'Expected Exception'
    except Exception as e:
        assert 'There is no window present with title \'Title Not Present\'' in e.args[0]
