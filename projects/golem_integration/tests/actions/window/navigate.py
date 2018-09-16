from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify navigate action'

def test(data):
    actions.navigate(data.env.url)
    golem_steps.assert_last_step_message("Navigate to: '{}'".format(data.env.url))
    assert actions.get_browser().current_url == data.env.url
