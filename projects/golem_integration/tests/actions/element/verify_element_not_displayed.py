from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'verify_element_not_displayed action'

def test(data):
    actions.navigate(data.env.url+'special-elements/')
    actions.verify_element_not_displayed('#hidden-button')
    golem_steps.assert_last_step_message('Verify element #hidden-button is not displayed')
    actions.verify_element_not_displayed('#double-click-one')
    golem_steps.assert_last_error('element #double-click-one is displayed')
