from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'verify_url_contains action'

def test(data):
    url = data.env.url + 'elements/'
    actions.navigate(url)
    actions.verify_url_contains('elements')
    golem_steps.assert_last_step_message("Verify URL contains 'elements'")
    actions.verify_url_contains('incorrect-partial-url')
    msg = "expected URL '{}' to contain 'incorrect-partial-url'".format(url)
    golem_steps.assert_last_error(msg)
