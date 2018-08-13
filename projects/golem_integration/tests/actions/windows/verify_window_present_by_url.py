from golem import actions


description = 'verify_window_present_by_url action'

def test(data):
    tabs_url = data.env.url+'tabs/'
    elements_url = data.env.url + 'elements/'
    actions.navigate(tabs_url)
    actions.send_keys('#urlInput', '/elements/')
    actions.click("#goButton")
    actions.verify_window_present_by_url(tabs_url)
    actions.verify_window_present_by_url(elements_url)
    try:
        actions.verify_window_present_by_url('/url/not/present')
        assert False, 'Expected Exception'
    except Exception as e:
        assert 'There is no window present with URL \'/url/not/present\'' in e.args[0]
