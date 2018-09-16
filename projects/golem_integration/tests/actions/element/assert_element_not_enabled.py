from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'assert_element_not_enabled action'

def test(data):
    actions.navigate(data.env.url+'disabled-elements/')
    actions.assert_element_not_enabled('#text')
    golem_steps.assert_last_step_message('Assert element #text is not enabled')
    actions.navigate(data.env.url+'elements/')
    try:
        actions.assert_element_not_enabled('#input-one')
    except AssertionError as e:
        assert 'element #input-one is enabled' in e.args[0]
