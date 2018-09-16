from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'check_element action'

def test(data):
    actions.navigate(data.env.url + 'elements/')
    selected_checkbox = '#selected-checkbox'
    unselected_checkbox = '#unselected-checkbox'
    unselected_radio = '#exampleRadios2'
    # check checkbox
    actions.assert_element_not_checked(unselected_checkbox)
    actions.check_element(unselected_checkbox)
    golem_steps.assert_last_step_message('Check element {}'.format(unselected_checkbox))
    actions.assert_element_checked(unselected_checkbox)
    # check checkbox already checked
    actions.assert_element_checked(selected_checkbox)
    actions.check_element(selected_checkbox)
    actions.assert_element_checked(selected_checkbox)
    # check radio
    actions.assert_element_not_checked(unselected_radio)
    actions.check_element(unselected_radio)
    actions.assert_element_checked(unselected_radio)
    # check radio already checked
    actions.check_element(unselected_radio)
    actions.assert_element_checked(unselected_radio)

