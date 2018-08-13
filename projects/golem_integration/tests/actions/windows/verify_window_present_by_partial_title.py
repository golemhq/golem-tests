from golem import actions


description = 'verify_window_present_by_partial_title action'

def test(data):
    actions.navigate(data.env.url+'tabs/')
    actions.send_keys('#urlInput', '/elements/')
    actions.click("#goButton")
    actions.verify_window_present_by_partial_title('Elem')  # Elements
    actions.verify_window_present_by_partial_title('Tab')  # Tabs
    try:
        actions.verify_window_present_by_partial_title('Title Not Present')
        assert False, 'Expected Exception'
    except Exception as e:
        assert 'There is no window present with partial title \'Title Not Present\'' in e.args[0]
