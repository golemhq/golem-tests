from golem import execution
from golem import actions


description = 'Verify get_window_size action'

def test(data):
    actions.open_browser()
    actions.set_window_size(300, 400)
    size = actions.get_window_size()
    assert size['width'] == 300
    assert size['height'] == 400
