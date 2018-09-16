from golem import actions

from projects.golem_integration.pages import golem_steps

description = 'assert_element_checked action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.assert_element_checked('#selected-checkbox')
    golem_steps.assert_last_step_message('element #selected-checkbox is not checked')
    try:
        actions.assert_element_checked('#unselected-checkbox')
    except AssertionError as e:
        assert 'element #unselected-checkbox is not checked' in e.args[0]
    # radio button
    actions.assert_element_checked('#exampleRadios1')
    try:
        actions.assert_element_checked('#exampleRadios2')
    except AssertionError as e:
        assert 'element #exampleRadios2 is not checked' in e.args[0]
