from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify double_click action'

def test(data):
    actions.navigate(data.env.url+'special-elements/')
    button = ('id', 'double-click-one')
    actions.double_click(button)
    golem_steps.assert_last_step_message('Double click element double-click-one')
    actions.assert_element_text('#double-click-one-result', 'Double Clicked!')
