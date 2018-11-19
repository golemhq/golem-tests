from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'verify_element_checked action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.verify_element_checked('#selected-checkbox')
    actions.verify_element_checked('#unselected-checkbox')
    golem_steps.assert_last_error('element #unselected-checkbox is not checked')
    actions.verify_element_checked('#exampleRadios1')
    actions.verify_element_checked('#exampleRadios2')
    golem_steps.assert_last_error('element #exampleRadios2 is not checked')
