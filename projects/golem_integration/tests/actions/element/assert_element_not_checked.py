from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'assert_element_not_checked action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.assert_element_not_checked('#unselected-checkbox')
    golem_steps.assert_last_step_message('element #unselected-checkbox is not checked')
    try:
        actions.assert_element_not_checked('#selected-checkbox')
    except AssertionError as e:
        assert 'element #unselected-checkbox is checked' in e.args[0]
