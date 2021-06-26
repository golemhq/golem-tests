from golem import actions


description = 'Verify get_window_size action'


def test_get_window_size(data):
    actions.open_browser()
    actions.set_window_size(600, 550)
    size = actions.get_window_size()
    assert size['width'] == 600
    assert size['height'] == 550
