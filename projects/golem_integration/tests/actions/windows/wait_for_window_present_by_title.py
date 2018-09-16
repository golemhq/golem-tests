from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify window_present_by_title action'

def test(data):
    actions.navigate(data.env.url+'tabs/')
    actions.send_keys('#delay', 3)
    actions.send_keys('#title', 'MY TITLE')
    actions.click("#goButtonCustom")
    actions.wait_for_window_present_by_title('MY TITLE', timeout=5)
    golem_steps.assert_last_step_message("Wait for window present by title 'MY TITLE'")
    actions.verify_window_present_by_title('MY TITLE')
    try:
        actions.wait_for_window_present_by_title('TITLE NOT PRESENT', timeout=3)
        assert False, 'Expected Exception'
    except Exception as e:
        assert "Timeout waiting for window present by title 'TITLE NOT PRESENT'" in e.args[0]
