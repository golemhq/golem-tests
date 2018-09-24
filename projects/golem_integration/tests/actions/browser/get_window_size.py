from golem import execution
from golem import actions


description = 'Verify get_window_size action'

def test(data):
    actions.open_browser()
    actions.set_window_size(500, 400)
    size = actions.get_window_size()
    assert size['width'] == 500
    assert size['height'] == 400
