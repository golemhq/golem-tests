from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'assert_element_text_contains action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.assert_element_text_contains('#link1', 'this is a link')
    golem_steps.assert_last_step_message("Assert element #link1 contains text 'this is a link'")
    try:
        actions.assert_element_text_contains('#link1', 'not-contained')
    except AssertionError as e:
        assert "expected element #link1 to contain text 'not-contained'" in e.args[0]
