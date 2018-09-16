from golem import actions


description = 'Verify set_window_size action'

def test(data):
    actions.open_browser()
    actions.set_window_size(400, 400)
    size = actions.get_window_size()
    assert size['width'] == 400
    assert size['height'] == 400
