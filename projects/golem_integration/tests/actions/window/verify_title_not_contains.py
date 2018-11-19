from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'verify_title_not_contains action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.verify_title_not_contains('incorrect title')
    golem_steps.assert_last_step_message("Verify page title does not contain 'incorrect title'")
    actions.verify_title_not_contains('Elem')
    golem_steps.assert_last_error("title contains 'Elem'")
