from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify window_present_by_url action'

def test(data):
    actions.navigate(data.env.url+'tabs/')
    actions.send_keys('#delay', 3)
    actions.send_keys('#title', 'MY_TITLE')
    actions.click("#goButtonCustom")
    url = data.env.url + 'tab/?delay=3&title=MY_TITLE'
    actions.wait_for_window_present_by_url(url, timeout=5)
    golem_steps.assert_last_step_message("Wait for window present by url '{}'".format(url))
    actions.verify_window_present_by_url(url)
    try:
        actions.wait_for_window_present_by_url('URL_NOT_PRESENT', timeout=3)
        assert False, 'Expected Exception'
    except Exception as e:
        assert "Timeout waiting for window present by url 'URL_NOT_PRESENT'" in e.args[0]
