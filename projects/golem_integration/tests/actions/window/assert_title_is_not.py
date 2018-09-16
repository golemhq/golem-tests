from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'assert_title_is_not action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.assert_title_is_not('incorrect title')
    golem_steps.assert_last_step_message("Assert page title is not 'incorrect title'")
    try:
        actions.assert_title_is_not('Elements')
    except AssertionError as e:
        assert "expected title to not be 'Elements'" in e.args[0]
