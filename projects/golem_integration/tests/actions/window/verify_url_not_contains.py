from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'verify_url_not_contains action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.verify_url_not_contains('incorrect')
    golem_steps.assert_last_step_message("Verify URL does not contain 'incorrect'")
    actions.verify_url_not_contains('elem')
    golem_steps.assert_last_error("URL contains 'elem'")
