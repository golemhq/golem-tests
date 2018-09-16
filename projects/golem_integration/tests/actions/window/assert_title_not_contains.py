from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'assert_title_not_contains action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.assert_title_not_contains('incorrect title')
    golem_steps.assert_last_step_message("Assert page title does not contain 'incorrect title'")
    try:
        actions.assert_title_not_contains('Elem')
    except AssertionError as e:
        assert "title contains 'Elem'" in e.args[0]
