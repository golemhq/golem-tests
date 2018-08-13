from golem import actions


description = 'verify_window_present_by_partial_url action'

def test(data):
    actions.navigate(data.env.url + 'tabs/')
    actions.send_keys('#urlInput', '/elements/')
    actions.click("#goButton")
    actions.verify_window_present_by_partial_url('tab')
    actions.verify_window_present_by_partial_url('elem')
    try:
        actions.verify_window_present_by_partial_url('/url/not/present')
        assert False, 'Expected Exception'
    except Exception as e:
        assert 'There is no window present with partial URL \'/url/not/present\'' in e.args[0]
