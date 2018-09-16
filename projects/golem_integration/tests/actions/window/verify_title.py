from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'verify_title action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.verify_title('Elements')
    golem_steps.assert_last_step_message("Verify page title is 'Elements'")
    actions.verify_title('incorrect title')
    golem_steps.assert_last_error("expected title to be 'incorrect title' but was 'Elements'")
