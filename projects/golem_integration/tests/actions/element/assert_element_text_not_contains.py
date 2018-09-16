from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'assert_element_text_not_contains action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.assert_element_text_not_contains('#link1', 'not-contained')
    golem_steps.assert_last_step_message("Assert element #link1 does not contain text 'not-contained'")
    try:
        actions.assert_element_text_not_contains('#link1', 'this is a link')
    except AssertionError as e:
        assert "element #link1 contains text 'this is a link'" in e.args[0]
