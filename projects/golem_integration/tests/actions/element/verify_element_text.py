from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'verify_element_text action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.verify_element_text('#link1', 'this is a link to index')
    golem_steps.assert_last_step_message("Verify element #link1 text is 'this is a link to index'")
    actions.verify_element_text('#link1', 'incorrect text')
    expected = "expected element #link1 text to be 'incorrect text' but was 'this is a link to index'"
    golem_steps.assert_last_error(expected)
