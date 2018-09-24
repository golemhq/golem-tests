from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'verify_url_not_contains action'

def test(data):
    url = data.env.url + 'elements/'
    actions.navigate(url)
    actions.verify_url_not_contains('incorrect')
    golem_steps.assert_last_step_message("Verify URL does not contain 'incorrect'")
    actions.verify_url_not_contains('elem')
    golem_steps.assert_last_error("expected URL '{}' to not contain 'elem'".format(url))
