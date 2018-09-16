from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'assert_page_not_contains_text action'

def test(data):
    actions.navigate(data.env.url+'special-elements/')
    actions.assert_page_not_contains_text('THIS TEXT IS NOT PRESENT')
    golem_steps.assert_last_step_message("Assert 'THIS TEXT IS NOT PRESENT' is not present in page")
    try:
        actions.assert_page_not_contains_text('Special Elements')
    except AssertionError as e:
        assert "text 'Special Elements' was found in page" in e.args[0]
