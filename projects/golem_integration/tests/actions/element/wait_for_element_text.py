from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify webdriver.wait_for_element_text method'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    actions.get_browser().wait_for_element_text('#button-seven', 'New Text', 10)
    golem_steps.assert_last_step_message("Wait for element #button-seven text to be 'New Text'")
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    try:
        actions.get_browser().wait_for_element_text('#button-seven', 'New Text', 3)
        assert False, 'Expected Exception'
    except Exception as e:
        assert "Timeout waiting for element #button-seven text to be 'New Text'" in e.args[0]
