from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify click action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.click(('id', 'button-one'))
    golem_steps.assert_last_step_message('Click button-one')
    actions.assert_element_text('#button-one-result', 'Clicked!')
