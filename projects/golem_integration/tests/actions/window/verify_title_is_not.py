from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'verify_title_is_not action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.verify_title_is_not('incorrect title')
    golem_steps.assert_last_step_message("Verify page title is not 'incorrect title'")
    actions.verify_title_is_not('Web Playground - Elements')
    golem_steps.assert_last_error("expected title to not be 'Web Playground - Elements'")
