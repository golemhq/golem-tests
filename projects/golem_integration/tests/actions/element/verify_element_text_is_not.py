from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'verify_element_text_is_not action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.verify_element_text_is_not('#link1', 'incorrect text')
    golem_steps.assert_last_step_message("Verify element #link1 text is not 'incorrect text'")
    actions.verify_element_text_is_not('#link1', 'this is a link to index')
    golem_steps.assert_last_error("expected element #link1 text to not be 'this is a link to index'")
