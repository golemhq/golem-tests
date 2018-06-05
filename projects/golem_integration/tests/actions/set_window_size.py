from golem import actions


description = 'Verify set_window_size action'

def test(data):
    actions.open_browser()
    actions.set_window_size(400, 400)
    browser = actions.get_browser()
    width = browser.get_window_size()['width']
    height = browser.get_window_size()['height']
    assert width == 400
    assert height == 400
