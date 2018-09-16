from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'assert_element_not_present action'

def test(data):
    actions.navigate(data.env.url+'special-elements/')
    actions.assert_element_not_present('#does-not-exist')
    golem_steps.assert_last_step_message('Assert element is not present')
    try:
        actions.assert_element_not_present('#double-click-one')
    except AssertionError as e:
        assert 'element #double-click-one is present' in e.args[0]
