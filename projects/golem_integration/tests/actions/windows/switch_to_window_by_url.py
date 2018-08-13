from golem import actions


description = 'Verify switch_to_window_by_url action'

def test(data):
    tabs_url = data.env.url + 'tabs/'
    elements_url = data.env.url+'elements/'
    nonexistent_url = data.env.url+'nonexistent-url/'
    actions.navigate(tabs_url)
    actions.send_keys('#urlInput', '/elements/')
    actions.click("#goButton")
    actions.switch_to_window_by_url(elements_url)
    actions.verify_title('Elements')
    actions.switch_to_window_by_url(tabs_url)
    actions.verify_title('Tabs')
    try:
        actions.switch_to_window_by_url(nonexistent_url)
        assert False, 'Expected Exception'
    except Exception as e:
        assert 'Window with URL \'{}\' was not found'.format(nonexistent_url) in e.args[0]
