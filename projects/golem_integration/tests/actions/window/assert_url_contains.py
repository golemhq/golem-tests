from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'assert_url_contains action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.assert_url_contains('elements')
    golem_steps.assert_last_step_message("Assert URL contains 'elements'")
    try:
        actions.assert_url_contains('incorrect')
    except AssertionError as e:
        assert "expected URL to contain 'incorrect'" in e.args[0]
