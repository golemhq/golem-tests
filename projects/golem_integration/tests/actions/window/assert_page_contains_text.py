from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'assert_page_contains_text action'

def test(data):
    actions.navigate(data.env.url+'special-elements/')
    actions.verify_page_contains_text('Special Elements')
    golem_steps.assert_last_step_message("Verify 'Special Elements' is present in page")
    try:
        actions.assert_page_contains_text('THIS TEXT IS NOT PRESENT')
    except AssertionError as e:
        assert "text 'THIS TEXT IS NOT PRESENT' not found in page" in e.args[0]
