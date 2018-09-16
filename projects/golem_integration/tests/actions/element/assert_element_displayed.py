from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'assert_element_displayed action'

def test(data):
    actions.navigate(data.env.url+'special-elements/')
    actions.assert_element_displayed('#double-click-one')
    golem_steps.assert_last_step_message('Assert element #double-click-one is displayed')
    try:
        actions.assert_element_displayed('#hidden-input')
    except AssertionError as e:
        assert 'element #hidden-input is not displayed' in e.args[0]
