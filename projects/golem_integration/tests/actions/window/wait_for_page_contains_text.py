from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify wait_for_page_contains_text action'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    text = '<div id="button-five-container">'
    actions.wait_for_page_contains_text(text, timeout=5)
    golem_steps.assert_last_step_message("Wait for page contains text '{}'".format(text))
    # wait times out waiting for text to be present in page
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    try:
        actions.wait_for_page_contains_text('<div id="button-five-container">', timeout=3)
        assert False, 'Expected Exception'
    except Exception as e:
        assert "Timeout waiting for page to contain '<div id=\"button-five-container\">'" in e.args[0]
