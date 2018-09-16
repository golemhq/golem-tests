from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify uncheck_element action'

def test(data):
    actions.navigate(data.env.url + 'elements/')
    checkbox_checked = '#selected-checkbox'
    checkbox_not_checked = '#unselected-checkbox'
    radio_checked = '#exampleRadios1'
    # checkbox not checked
    actions.verify_element_not_checked(checkbox_not_checked)
    actions.uncheck_element(checkbox_not_checked)
    golem_steps.assert_last_step_message('Uncheck checkbox {}'.format(checkbox_not_checked))
    actions.verify_element_not_checked(checkbox_not_checked)
    # checkbox already checked
    actions.verify_element_checked(checkbox_checked)
    actions.uncheck_element(checkbox_checked)
    actions.verify_element_not_checked(checkbox_checked)
    # uncheck a radio button (error)
    actions.verify_element_checked(radio_checked)
    try:
        actions.uncheck_element(radio_checked)
        assert False, 'Expected Exception'
    except Exception as e:
        assert 'Element #exampleRadios1 is not checkbox' in e.args[0]
    # try to uncheck an element not checkbox
    try:
        actions.uncheck_element('#button-one')
        assert False, 'Expected Exception'
    except Exception as e:
        assert 'Element #button-one is not checkbox' in e.args[0]
