from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'verify_element_text_contains action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.verify_element_text_contains('#link1', 'this is a link')
    golem_steps.assert_last_step_message("Verify element #link1 contains text 'this is a link'")
    actions.verify_element_text_contains('#link1', 'not-contained')
    exp = "expected element #link1 text 'this is a link to index' to contain 'not-contained'"
    golem_steps.assert_last_error(exp)
