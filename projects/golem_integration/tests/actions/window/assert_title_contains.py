from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'verify_title_contains action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.assert_title_contains('Elem')
    golem_steps.assert_last_step_message("Assert page title contains 'Elem'")
    try:
        actions.assert_title_contains('incorrect')
    except AssertionError as e:
        assert "expected title to contain 'incorrect'" in e.args[0]
