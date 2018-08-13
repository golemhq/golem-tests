from golem import actions


description = 'Verify webdriver.switch_to_window_by_title method'

def test(data):
    actions.navigate(data.env.url+'tabs/')
    actions.send_keys('#urlInput', '/elements/')
    actions.click("#goButton")
    actions.get_browser().switch_to_window_by_title('Elements')
    actions.verify_title('Elements')
    try:
        actions.get_browser().switch_to_window_by_title('incorrect title')
        assert False, 'Expected Exception'
    except Exception as e:
        assert 'Window with title \'incorrect title\' was not found' in e.args[0]
