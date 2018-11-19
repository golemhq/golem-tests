from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'verify_element_text_not_contains action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.verify_element_text_not_contains('#link1', 'not-contained')
    golem_steps.assert_last_step_message("Verify element #link1 does not contains text 'not-contained'")
    actions.verify_element_text_not_contains('#link1', 'this is a link')
    msg = "expected element #link1 text 'this is a link to index' to not contain 'this is a link'"
    golem_steps.assert_last_error(msg)
