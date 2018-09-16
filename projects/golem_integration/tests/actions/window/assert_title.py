from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'assert_title action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.assert_title('Elements')
    golem_steps.assert_last_step_message("Assert page title is 'Elements'")
    try:
        actions.assert_title('incorrect title')
    except AssertionError as e:
        assert "expected title to be 'incorrect title' but was 'Elements'" in e.args[0]
