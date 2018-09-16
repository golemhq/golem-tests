from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'assert_element_present action'

def test(data):
    actions.navigate(data.env.url+'special-elements/')
    actions.assert_element_present('#double-click-one')
    golem_steps.assert_last_step_message('Assert element is present')
    try:
        actions.assert_element_present('#does-not-exist')
    except AssertionError as e:
        assert 'element #does-not-exist is not present' in e.args[0]
