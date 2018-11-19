from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'verify_page_contains_text action'

def test(data):
    actions.navigate(data.env.url+'special-elements/')
    actions.verify_page_contains_text('Special Elements')
    golem_steps.assert_last_step_message("Verify 'Special Elements' is present in the page")
    actions.verify_page_contains_text('THIS TEXT IS NOT PRESENT')
    golem_steps.assert_last_error("text 'THIS TEXT IS NOT PRESENT' not found in the page")
