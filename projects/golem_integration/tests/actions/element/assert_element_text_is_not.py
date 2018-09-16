from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'assert_element_text_is_not action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.assert_element_text_is_not('#link1', 'incorrect text')
    golem_steps.assert_last_step_message("Assert element #link1 text is not 'incorrect text'")
    try:
        actions.assert_element_text_is_not('#link1', 'this is a link to index')
    except AssertionError as e:
        assert "expected element #link1 text to not be 'this is a link to index'" in e.args[0]
