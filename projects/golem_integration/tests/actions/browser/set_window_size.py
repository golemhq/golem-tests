from golem import actions


description = 'Verify set_window_size action'


def test_set_window_size(data):
    actions.open_browser()
    actions.set_window_size(650, 600)
    size = actions.get_window_size()
    assert size['width'] == 650
    assert size['height'] == 600
