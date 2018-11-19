from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify refresh_page action'

def test(data):
    actions.navigate(data.env.url + 'elements/')
    checkbox = ('id', 'unselected-checkbox')
    actions.click(checkbox)
    actions.assert_element_checked(checkbox)
    actions.refresh_page()
    golem_steps.assert_last_step_message('Refresh page')
    actions.assert_element_not_checked(checkbox)
