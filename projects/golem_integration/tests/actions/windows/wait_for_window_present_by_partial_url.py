from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify window_present_by_partial_url action'

def test(data):
    actions.navigate(data.env.url+'tabs/')
    actions.send_keys('#delay', 3)
    actions.send_keys('#title', 'MY_TITLE')
    actions.click("#goButtonCustom")
    partial_url = 'delay=3&title=MY_TITLE'
    actions.wait_for_window_present_by_partial_url(partial_url, timeout=5)
    msg = "Wait for window present by partial url '{}'".format(partial_url)
    golem_steps.assert_last_step_message(msg)
    actions.verify_window_present_by_partial_url(partial_url)
    try:
        actions.wait_for_window_present_by_partial_url('URL_NOT_PRESENT', timeout=3)
        assert False, 'Expected Exception'
    except Exception as e:
        assert "Timeout waiting for window present by partial url 'URL_NOT_PRESENT'" in e.args[0]
